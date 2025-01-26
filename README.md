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

1. We split LeetCodeDataset into train(1570 problems) and test(175 problems) dataset, order problems by `question_id` and use problems with bigger `question_id` for .
2. `meta.query` as query, `meta.response` as response, train LLM using the train split.

## Evaluation

Installation:

```
$ git clone https://github.com/newfacade/LeetCodeDataset
$ pip install -e .
```

Evaluation example:

```
$ eval_lct --version v1 --split test --input_file ./data/LeetCodeDataset-v1-test-problems.jsonl --predict_column meta.response
```

## Data Curation

1. Use [python-leetcode](https://github.com/fspv/python-leetcode) to collect problems and corresponding metadata.
2. Split problem description into two parts: description without examples and examples, concatenate description without examples and `lang_code` to form query, parse examples to get test case.
3. Finally, extract completion from [doocs/leetcode](https://github.com/doocs/leetcode), test cases and completion are cross verified.

## 🙏 Acknowledgement

- [HumanEval](https://github.com/openai/human-eval)
- [EvalPlus](https://github.com/evalplus/evalplus)
