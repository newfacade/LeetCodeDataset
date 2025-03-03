import json
import os
import re
import ast


def read_jsonl(filename: str):
    """
    Read a jsonl file (or a txt file), parse each line, and return a list.
    """
    with open(filename, "r", encoding="utf-8") as fp:
        for line in fp:
            yield json.loads(line)


def write_jsonl(filename: str, data: list):
    """
    Write iterable data to a jsonl file.
    """
    with open(filename, "w", encoding="utf-8") as fp:
        for x in data:
            fp.write(json.dumps(x, ensure_ascii=False) + "\n")


def read_problems(problem_file: str):
    return {task['task_id']: task for task in read_jsonl(problem_file)}


def get_problem_file(version: str, split: str):
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    problem_file = os.path.join(ROOT, 'data', f'LeetCodeDataset-{version}-{split}-problems.jsonl')
    print(problem_file)
    assert os.path.exists(problem_file), f'{problem_file} does not exist'
    return problem_file


def get_nested(item: dict, path: str):
    current = item
    for key in path.split('.'):
        current = current[key]
    return current


def extract_completion(text: str) -> str:
    """
    Extract completion from text.
    """
    pattern = r"```python\n(.*?)```"
    code_blocks =re.findall(pattern, text, re.S)
    code_blocks.sort(key=lambda x: len(x.split('\n')))
    if code_blocks:
        # longest code block
        return code_blocks[-1]
    else:
        return text


def syntax_check(code: str) -> bool:
    try:
        ast.parse(code)
        return True
    except (SyntaxError, MemoryError):
        return False


def code_extract(text: str) -> str:
    lines = text.split("\n")
    longest_line_pair = (0, 0)
    longest_so_far = 0

    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            current_lines = "\n".join(lines[i : j + 1])
            if syntax_check(current_lines):
                current_length = sum(1 for line in lines[i : j + 1] if line.strip())
                if current_length > longest_so_far:
                    longest_so_far = current_length
                    longest_line_pair = (i, j)

    return "\n".join(lines[longest_line_pair[0] : longest_line_pair[1] + 1])
