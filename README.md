# LeetCodeDataset

LeetCodeDataset is a dataset comprising Python LeetCode problems designed for training and evaluating Large Language Models (LLMs).

<p align="center">
    <a href="https://huggingface.co/datasets/newfacade/LeetCodeDataset">💻 Hugging Face Datasets</a>
</p>

## Data Fields

The dataset adheres to the [human-eval](https://github.com/openai/human-eval) problem file format.

- `task_id`: The LeetCode problem's question title slug, which corresponds to the problem URL.
- `prompt`: The prefix for the completion, such as basic imports.
- `entry_point`: The function name used for evaluation.
- `test`: A function to check test cases.
- `completion`: The completion without the prompt.
- `examples`: Test cases.
- `meta`:
  - `question_id`: The LeetCode problem's question ID.
  - `difficulty`: The problem's difficulty level (Easy, Medium, or Hard).
  - `lang_code`: The format of the completion.
  - `question_title`: The problem description.
  - `query`: The query.
  - `response`: The correct response.
  - `split`: The dataset split (e.g., train/test).

## Training

LeetCodeDataset can be used for training as follows:

1. The dataset is split into training and test sets. Problems are ordered by `question_id`, with those having larger `question_id` values used for the test set.
2. Use `meta.query` as the query and `meta.response` as the response to train the LLM using the training split.

The number of problems in each version and split is as follows:

| Version | Train | Test |
| ------- | ----- | ---- |
| v1      | 1570  | 175  |
| v2      | 1890  | 200  |

## Evaluation

### Installation

```bash
git clone https://github.com/newfacade/LeetCodeDataset
pip install -e .
```

### LeetCodeDataset Evaluation Example

```bash
eval_lcd --version v1 \
         --split test \
         --input_file ./data/LeetCodeDataset-v1-test-problems.jsonl \
         --predict_column meta.response
```

### Explanation of Parameters

- `version`: v1 or v2.
- `split`: test or train.
- `input_file`: A JSONL file containing the problems and predictions for the specified LeetCodeDataset, with `task_id` and prediction.
- `predict_column`: The column name of the prediction in `input_file`, e.g., `{'task_id': 'two_sum', 'output': 'To solve the problem of finding two indices ...'}` uses `--predict_column output`.

You can also perform custom evaluations using the `evaluate_functional_correctness` command, which is consistent with human-eval.

## Data Curation

1. Use [python-leetcode](https://github.com/fspv/python-leetcode) to collect problems and their metadata.
2. Split the problem description into two parts: the description without examples and the examples. Concatenate the description without examples and `lang_code` to form the query, and parse the examples to extract test cases.
3. Finally, extract the completion from [doocs/leetcode](https://github.com/doocs/leetcode). Test cases and completion are cross-verified.

## Paper/blog/projects Using LeetCodeDataset

- [Pre-SFT: Let Models Decide on Supervisory Data for Fine-Tuning](https://www.notion.so/swtheking/150d3429a80780c394dfea632713c1b7?v=150d3429a8078171a969000c3ec41f2a)
- [Preference Modeling: Binary Discrimination Versus Imitation Learning](https://swtheking.notion.site/?v=182d3429a807812fb1e1000c2557a107)
- [POLICY FILTRATION IN RLHF TO FINE-TUNE LLM FOR CODE GENERATION](https://arxiv.org/pdf/2409.06957)
- [AdaptiveStep: Automatically Dividing Reasoning Step through Model Confidence](https://arxiv.org/pdf/2502.13943)
- [code-r1](https://github.com/ganler/code-r1)

## Citation

```bibtex
@software{xia2025leetcodedataset,
  author = {Yunhui Xia, Wei Shen, Renbiao Liu, Yan Wang, Siyue Wu, Xiaonan He},
  title = {LeetCodeDataset: A Dataset of Algorithmic Problems Suitable for LLM Training and Evaluation},
  year = {2025},
  url = {https://github.com/newfacade/LeetCodeDataset},
  version = {0.1.0},
}
```

## 🙏 Acknowledgment

- [HumanEval](https://github.com/openai/human-eval)
- [OpenCodeEval](https://github.com/richardodliu/OpenCodeEval)
- [EvalPlus](https://github.com/evalplus/evalplus)
