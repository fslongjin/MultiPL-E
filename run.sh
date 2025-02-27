# export OPENAI_API_BASE="http://localhost:11434/v1"
export OPENAI_API_BASE="https://api.siliconflow.cn/v1"
# export OPENAI_API_BASE="https://api.deepseek.com/beta"
export OPENAI_API_KEY="123"
# MODEL="qwen2.5_coder:7b"
MODEL="silconflow_qwen2.5_coder:7b"

# rs / cpp
LANG="rs"
DATASET="humaneval"
BATCH_SIZE=1
COMPLETIONS_LIMIT=20
TEMPERATURE=0.2
MAX_TOKENS=1024
OUTPUT_DIR_PREFIX="tutorial"

python3 openai_model.py --azure --model $MODEL --lang $LANG --root-dataset $DATASET \
        --batch-size $BATCH_SIZE --temperature $TEMPERATURE \
        --completion-limit $COMPLETIONS_LIMIT --max-tokens $MAX_TOKENS \
        --output-dir-prefix $OUTPUT_DIR_PREFIX
