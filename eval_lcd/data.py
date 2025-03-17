import json
import os
import re
import ast
import gzip

import tempdir
import wget
from appdirs import user_cache_dir

CACHE_DIR = user_cache_dir("leetcodedataset")


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


def decompress_gz(input_file: str):
    output_file = input_file[:-3]
    with gzip.open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            f_out.write(f_in.read())


def get_problem_file(version: str, split: str):
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    problem_file = os.path.join(ROOT, 'data', f'LeetCodeDataset-{version}-{split}.jsonl')
    if not os.path.exists(problem_file):
        decompress_gz(problem_file + '.gz')
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


def get_dataset_metadata(version: str, split: str):
    assert split in {'train', 'test'}
    url = f"https://github.com/newfacade/leetcode_release/raw/refs/tags/{version}/LeetCodeDataset-{version}-{split}.jsonl.gz"
    cache_path = os.path.join(CACHE_DIR, f"LeetCodeDataset-{version}-{split}.jsonl")
    return url, cache_path


def make_cache(gzip_url: str, cache_path: str):
    if not os.path.exists(cache_path):
        print(f"Downloading dataset from {gzip_url}")

        with tempdir.TempDir() as tmpdir:
            tmp_gz_path = os.path.join(tmpdir, f"data.jsonl.gz")
            wget.download(gzip_url, tmp_gz_path)

            with gzip.open(tmp_gz_path, "rb") as f:
                data = f.read().decode("utf-8")

        # create CACHE_DIR if not exists
        if not os.path.exists(CACHE_DIR):
            os.makedirs(CACHE_DIR)

        # Write the original data file to CACHE_DIR
        with open(cache_path, "w") as f:
            f.write(data)
