# Authored by Arjun Guha and Abhinav Jangda
# Copyright (c) 2022, Roblox Inc, Northeastern University, and University of Massachusetts Amherst
#
# This is a helper script for translating problems from the OpenAI HumanEval
# problems to Language L.
import ast
from glob import glob
import re
from pathlib import Path
import argparse
from models import MODELS


def translate_expr(translator, py_expr: ast.AST):
    """
    Translates a Python expression to Language L.
    """

    match py_expr:
        case ast.Constant(value=s):
            return translator.gen_literal(s)
        case ast.UnaryOp(op=ast.USub(), operand=ast.Constant(value=n)) if type(3) in [int, float]:
            return translator.gen_literal(-n)
        case ast.Name(id):
            return translator.gen_var(id)
        case ast.List(elts=elts):
            return translator.gen_list([translate_expr(translator, e) for e in elts])
        case ast.Tuple(elts=elts):
            return translator.gen_tuple([translate_expr(translator, e) for e in elts])
        case ast.Dict(keys=keys, values=values):
            return translator.gen_dict(
                [translate_expr(translator, e) for e in keys],
                [translate_expr(translator, e) for e in values],
            )
        case ast.Call(func, args):
            return translator.gen_call(
                translate_expr(translator, func),
                [translate_expr(translator, a) for a in args],
            )
        case _other:
            print("OMFG" + py_expr)
            raise Exception(f"Unhandled expression: {py_expr}")


class PromptVisitor(ast.NodeVisitor):
    """Helper for translate_prompt"""

    def __init__(self, translator):
        super().__init__()
        self.state = "start"
        self.translator = translator

    def visit_FunctionDef(self, node: ast.FunctionDef):
        if self.state != "start":
            self.state = "error"
            return

        self.name = node.name
        self.args = node.args.args
        self.returns = node.returns

        match node.body:
            case [ast.Expr(value=ast.Constant(s)), ast.Pass()] if type(s) == str:
                self.description = s
                self.state = "complete"
            case _other:
                self.state = "error"

    def translate_func_decl(self, doctest_transformation: str) -> str | None:
        if self.state != "complete":
            return None
        # TODO(arjun): Use doctest_transformation
        match doctest_transformation:
            case "keep":
                description = self.description
            case "remove":
                # TODO(arjun): Remove all doctests
                description = self.description 
            case "transform":
                # Steps:
                # Find the Python expression and result in each doctest
                # py_ast = ast.parse("PYTHON EXPRESSION", "bogus filename")
                # translate_expr(py_ast, self.translator) to get the string for that expression in the target language
                description = self.description # TODO(arjun): Transform doctests
            case _other:
                raise Exception(f"bad doctest_transformation")
        return self.translator.translate_prompt(self.name, self.args, self.returns, description)


def translate_prompt(translator, doctest_transformation: str, py_prompt: str, filename: str) -> str:
    """
    Reads in a prompt from the HumanEval dataset with "    pass" appended. Translates the prompt to
    Language L. Ignores type annotations and imports. Fails if the prompt has auxiliary functions.
    """
    prompt_ast = ast.parse(py_prompt + "    pass", filename)
    prompt_visitor = PromptVisitor(translator)
    prompt_visitor.visit(prompt_ast)
    return prompt_visitor.translate_func_decl(doctest_transformation)


def translate_tests(translator, py_tests: str, entry_point: str, filename: str) -> str:
    """
    Translates a suite of tests from the HumanEval dataset to Language L. Expects the code to look like:

    METADATA = ... <-- optional

    def check():
        assert(LHS == RHS)
        ...
    """
    tests_ast = ast.parse(py_tests, filename)
    test_cases = translator.test_suite_prefix_lines(entry_point)
    match tests_ast:
        case ast.Module(body=[ast.FunctionDef(body=body)]):
            body_ast = body
        case ast.Module(body=[ast.Assign(), ast.FunctionDef(body=body)]):
            body_ast = body
        case _other:
            return None  # TODO(arjun): Should this blow up?
    for item_ast in body_ast:
        match item_ast:
            case ast.Assert(
                test=ast.Compare(left=left, ops=[ast.Eq()], comparators=[right])
            ):
                try:
                    left = translate_expr(translator, left)
                    right = translate_expr(translator, right)
                    test_cases.append(translator.deep_equality(left, right))
                except Exception as e:
                    print(f"Exception translating expressions for {filename}: {e}")
                    return None
            case ast.Expr(value=ast.Name(id="print")):
                pass
            case _other:
                print("Failed to translate tests for " + filename)
                return None
    for line in translator.test_suite_suffix_lines():
        test_cases.append(line)
    return "\n".join(test_cases)


def translate_file(args, translator, file):
    file = Path(file).resolve()
    cleaned_task_id = re.search("HumanEval_\d+", file.name).group(0)
    entry_point = re.search("(HumanEval_\d+)_(.+).py", file.name).group(2)

    reading_prompt = True
    reading_tests = False
    prompt_buffer = []
    tests_buffer = []
    with open(file) as f:
        for line in f:
            if "### Canonical solution below ###" in line:
                reading_prompt = False
            if "### Unit tests below ###" in line:
                reading_tests = True
                continue
            if "def test_check():" in line:
                break

            if reading_prompt:
                prompt_buffer.append(line)
            if reading_tests:
                tests_buffer.append(line)

    prompt = "".join(prompt_buffer)
    translated_prompt = translate_prompt(translator, args.doctests, prompt, f"{cleaned_task_id}.py")

    tests = "".join(tests_buffer)
    translated_tests = translate_tests(
        translator, tests, entry_point, f"{cleaned_task_id}.py"
    )

    if translated_prompt is None:
        print(f"Failed to translate prompt for {file}")
        return
    if translated_tests is None:
        print(f"Failed to translate tests for {file}")
        return
    response = MODELS[args.model](args, translated_prompt, translator.stop, 1)[0]

    filename = Path(
        file.parent,
        "..",
        f"{translator.file_ext}-{args.doctests}-{args.model}",
        f"{cleaned_task_id}_{entry_point}.{translator.file_ext}",
    ).resolve()
    filename.parent.mkdir(parents=True, exist_ok=True)

    with open(filename, "w") as f:
        f.write(translated_prompt)
        f.write(response)
        f.write("\n\n")
        f.write(translated_tests)
        print(f'Wrote {filename}')


def main(translator):
    if len(translator.stop) <= 0 or len(translator.stop) > 4:
        raise Exception("Translator must have 0 < n <= 4 stop words!")

    # Commandline arguments: --port 
    args = argparse.ArgumentParser()
    args.add_argument("--port", type=int, default=9000, help="Port to use for OpenAI Caching Proxy")

    # argument --doctests with options "keep", "remove", and "transform"
    args.add_argument(
        "--doctests",
        type=str,
        default="keep",
        help="What to do with doctests: keep, remove, or transform",
    )

    args.add_argument(
        "--model",
        type=str,
        default="code_davinci_001_temp_0.2",
        help="Code generation model to use")

    args.add_argument(
        "--files",
        type=int,
        nargs="*",
        default=[],
        help="Specify the files to translate by their number, e.g. --files 0 1 2"
    )

    args = args.parse_args()

    if args.doctests not in [ "keep", "remove", "transform" ]:
        raise Exception("Invalid value for --doctests")


    directory = Path(Path(__file__).parent, "..", "datasets").resolve()
    files_unsorted = directory.glob(f"originals/*.py") 
    files_sorted = sorted(files_unsorted, key=(lambda s: int(str(s).split("_")[1])))
    files_index = []
    if len(args.files) > 0:
        files_index = args.files
    else:
        files_index = range(len(files_sorted)) 
    for i in files_index:
        filepath = files_sorted[i]
        translate_file(args, translator, filepath)
