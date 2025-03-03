# LeetCodeDataset

LeetCodeDataset is a dataset consists of Python leetcode problems that can be used for LLM training and evaluation.

<p align="center">
    <a href="https://huggingface.co/datasets/newfacade/LeetCodeDataset">💻 Hugging Face Datasets</a>
</p>

## Data Fields

Consistent with [human-eval](https://github.com/openai/human-eval) problem file format.

- `task_id`: corresponding leetcode problem question title slug, relates to problem url
- `prompt`: prefix of completion, e.g basic import
- `entry_point`: function name for evaluation
- `test`: check function using test cases
- `completion`: completion only without the prompt
- `examples`: test cases
- `meta`:
    - `question_id`: leetcode problem question id
    - `difficulty`: Easy, Medium or Hard
    - `lang_code`: completion format
    - `question_title`: problem description
    - `query`: query
    - `response`: correct response
    - `split`: e.g train/test

## Training

LeetCodeDataset can be used for training:

1. We split LeetCodeDataset into train and test dataset, order problems by `question_id` and use problems with bigger `question_id` as the test set.
2. `meta.query` as query, `meta.response` as response, train LLM using the train split.

Number of problems with respect to each version and split:

| version       | train | test |
|---------------|-------|------|
| v1            | 1570  | 175  |
| v2            | 1890  | 200  |

## Evaluation

Installation:

```
$ git clone https://github.com/newfacade/LeetCodeDataset
$ pip install -e .
```

LeetCodeDataset Evaluation example:

```
$ eval_lct --version v1 \
           --split test \
           --input_file ./data/LeetCodeDataset-v1-test-problems.jsonl \
           --predict_column meta.response
```

explain params:

* `version`: v1 or v2
* `split`: test or train
* `input_file`: a jsonl file to be evaluated, contains `task_id` and prediction for the specified LeetCodeDataset
* `predict_column`: column name of prediction in `input_file`, e.g. `{'task_id': 'two_sum', 'output': 'To solve the problem of finding two indices ...'}` uses `--predict_column output`

You can also run custom evaluation using the command `evaluate_functional_correctness` (consistent with human-eval).

## Data Curation

1. Use [python-leetcode](https://github.com/fspv/python-leetcode) to collect problems and corresponding metadata.
2. Split problem description into two parts: description without examples and examples, concatenate description without examples and `lang_code` to form query, parse examples to get test case.
3. Finally, extract completion from [doocs/leetcode](https://github.com/doocs/leetcode), test cases and completion are cross verified.

## Blog/papers using LeetCodeDataset

* [Pre-SFT: Let Models Decide on Supervisory Data for Fine-Tuning](https://www.notion.so/swtheking/150d3429a80780c394dfea632713c1b7?v=150d3429a8078171a969000c3ec41f2a)
* [Preference Modeling: Binary Discrimination Versus Imitation Learning](https://swtheking.notion.site/?v=182d3429a807812fb1e1000c2557a107)

## Citation

```bibtex
@software{xia2025leetcodedataset,
  author = {Yunhui Xia, Wei Shen, Renbiao Liu, Yan Wang, Xiaonan He, Chuheng Zhang, Bruce},
  title = {LeetCodeDataset: A Dataset of Algorithmic Problems Suitable for LLM Training and Evaluation},
  year = {2025},
  url = {https://github.com/newfacade/LeetCodeDataset},
  version = {1.0},
}
```

## 🙏 Acknowledgement

- [HumanEval](https://github.com/openai/human-eval)
- [EvalPlus](https://github.com/evalplus/evalplus)
