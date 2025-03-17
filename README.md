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
- `query`: The query including problem description and starter code.
- `response`: The correct response.
- `input_output`: Test cases.
- `meta`:
  - `question_id`: The LeetCode problem's question ID.
  - `difficulty`: The problem's difficulty level (Easy, Medium, or Hard).
  - `lang_code`: The format of the completion.
  - `question_title`: The problem description.
  - `tags`: E.g. ['Array', 'Hash Table']
  - `estimated_date`: Estimated release date

## Training

LeetCodeDataset can be used for training as follows:

1. The dataset is split into training and test sets. Problems are ordered by `question_id`, with those having larger `question_id` values used for the test set.
2. Use `query` as the query and `response` as the response to train the LLM using the training split.

The number of problems in each version and split is as follows:

| Version | Train | Test |
| ------- | ----- | ---- |
| v0.1.0      | 1570  | 175  |
| v0.2.0      | 1890  | 200  |
| v0.3.0      | 2386  | 386  |

## Evaluation

### Installation

```bash
git clone https://github.com/newfacade/LeetCodeDataset
pip install -e .
```

### LeetCodeDataset Evaluation Example

```bash
eval_lcd --version v0.3.0 \
         --split test \
         --input_file ./data/LeetCodeDataset-v0.3.0-test.jsonl \
         --predict_column completion
```

### Explanation of Parameters

- `version`: v0.1.0 or v0.2.0 or v0.3.0.
- `split`: test or train.
- `input_file`: A JSONL file containing the problems and predictions for the specified LeetCodeDataset, with `task_id` and prediction.
- `predict_column`: The column name of the prediction in `input_file`, e.g., `{'task_id': 'two_sum', 'output': 'To solve the problem of finding two indices ...'}` uses `--predict_column output`.

You can also perform custom evaluations using the `evaluate_functional_correctness` command, which is consistent with human-eval.

## Data Curation

1. Metadata Acquisition, including:
    – question id: unique numeric identifier
    – question: url-related string (serves as primary task id)
    – problem description
    – starter code
2. Canonical Solution Verification
   - Retrieved reference solutions from GitHub open-source datasets
   - Validated solution correctness through LeetCode’s official execution environment
3. Entry Point Identification: Implemented text pattern matching to detect target functions
4. Test Case Generation
5. Automated Evaluation Framework
   - Developed sandboxed execution environment for safe code evaluation
   - Implemented trial-and-error mechanism to Execute canonical solutions against generated inputs

## Paper/blog/projects Using LeetCodeDataset

- [Pre-SFT: Let Models Decide on Supervisory Data for Fine-Tuning](https://www.notion.so/swtheking/150d3429a80780c394dfea632713c1b7?v=150d3429a8078171a969000c3ec41f2a)
- [Preference Modeling: Binary Discrimination Versus Imitation Learning](https://swtheking.notion.site/?v=182d3429a807812fb1e1000c2557a107)
- [POLICY FILTRATION IN RLHF TO FINE-TUNE LLM FOR CODE GENERATION](https://arxiv.org/pdf/2409.06957)
- [AdaptiveStep: Automatically Dividing Reasoning Step through Model Confidence](https://arxiv.org/pdf/2502.13943)
- [Breaking the Attention Trap in Code LLMs: A Rejection Sampling Approach to Enhance Code Execution Prediction](https://openreview.net/pdf?id=4l2hCRYHuo)
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
