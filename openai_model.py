"""
Use to get completions from an OpenAI completions endpoint. This version
of the script only works with Azure OpenAI service, since OpenAI no longer
hosts their code completion models.
"""
import time
import os
from typing import List
from multipl_e.completions import partial_arg_parser, make_main
import json
import openai
from openai import OpenAI

client = OpenAI(base_url=os.getenv("OPENAI_API_BASE"),
                api_key=os.getenv("OPENAI_API_KEY"))
# import openai.error

global engine, model


def completions(
    prompts: List[str], max_tokens: int, temperature: float, top_p, stop
) -> List[str]:
    results = []
    for prompt in prompts:
        kwargs = {
            "prompt": prompt,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_p": top_p,
            "stop": stop
        }

        if engine is not None:
            kwargs["engine"] = engine
        elif model is not None:
            if model == "deepseek_chat":
                kwargs["model"] = "deepseek-chat"
            elif model == "silconflow_deepseekv3":
                kwargs["model"] = "Pro/deepseek-ai/DeepSeek-V3"
            elif model == "silconflow_qwen2.5_coder:7b":
                kwargs["model"] = "Qwen/Qwen2.5-Coder-7B-Instruct"
            else:
                # 把model里面的'_'替换为'-'
                m = model.replace('_', '-')
                kwargs["model"] = m

        failed_attempts = 5
        while failed_attempts > 0:
            try:
                result = client.completions.create(**kwargs)
                result = result.choices[0].text  # Access attributes directly
                break
            except openai.RateLimitError:
                print("Rate limited...")
                time.sleep(5)
            except Exception as e:
                print(f"Error: {e}")
                failed_attempts -= 1
        if failed_attempts == 0:
            print("Failed to get completion after 5 attempts.")
            result = ""  # Return an empty string or handle the error as needed.
        results.append(result)
        time.sleep(0.1)
    return results


def main():
    global engine, model
    args = partial_arg_parser()
    args.add_argument("--model", type=str)
    args.add_argument("--engine", type=str)
    args.add_argument("--name-override", type=str)
    args.add_argument("--azure", action="store_true")
    args = args.parse_args()

    if args.engine is None and args.model is None:
        raise ValueError("Must specify either engine or model.")
    elif args.engine is not None and args.model is not None:
        raise ValueError("Must specify either engine or model, not both.")

    engine = args.engine
    model = args.model
    if args.name_override:
        name = args.name_override
    else:
        if args.engine is not None:
            name = args.engine
        else:
            name = args.model

    make_main(args, name, completions)


if __name__ == "__main__":
    main()
