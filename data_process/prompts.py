import json
import random
from typing import List, Optional

SYSTEM_PROMPT_GEN_INPUTS = "You are an expert Python programmer. You will be given a question (including a problem specification and starter code) along with a few sample inputs. Your task is to generate additional inputs that are consistent with the question and the provided sample inputs.\n\n"

SAMPLE_INPUTS = "#### Sample inputs (json format):\n"

GEN_INPUTS = "#### Generate some additional inputs that are more complex than the sample inputs (you should specify argument name in the inputs, using json format):\n"

SYSTEM_PROMPT_GEN_INPUTS_EXAMPLE = "You are an expert Python programmer. You will be given a question (including a problem specification and starter code). Your task is to generate inputs that are consistent with the problem specification and starter code. An example will be provided for illustration.\n\n"

SAMPLE_INPUTS_EXAMPLE = "#### Some valid inputs of the starter code (json format):\n"

GEN_INPUTS_EXAMPLE = "#### Some valid inputs (you should specify argument name in the inputs) of the starter code (json format, only output a json block! no explain, no comment, no multiple json block):\n"


def _gen_json_inputs(inputs: List[str]):
    return "```json\n" + json.dumps(inputs, ensure_ascii=False, indent=4) + "\n```\n\n"


def prompt_gen_inputs(problem_desc: str, sample_inputs: List[str]) -> str:
    prompt = SYSTEM_PROMPT_GEN_INPUTS
    prompt +=  "#### Question:\n" + problem_desc + "\n\n"
    prompt += SAMPLE_INPUTS + _gen_json_inputs(inputs=sample_inputs)
    prompt += GEN_INPUTS
    return prompt


def prompt_gen_inputs_using_example(problem_desc: str, example_desc: str, example_inputs: List[str]) -> str:
    prompt = SYSTEM_PROMPT_GEN_INPUTS_EXAMPLE
    
    prompt += "**** Example ****\n\n"
    prompt += "#### Question:\n" + example_desc + "\n\n"
    prompt += SAMPLE_INPUTS_EXAMPLE + _gen_json_inputs(inputs=example_inputs)
    
    prompt += "**** Now Your Task ****\n\n"
    prompt += "#### Question:\n" + problem_desc + "\n\n"
    prompt += GEN_INPUTS_EXAMPLE
    return prompt


SYSTEM_MESSAGE_GENERIC = "You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests.\n\n"

FORMATTING_MESSAGE_WITH_STARTER_CODE = "You will use the following starter code to write the solution to the problem and enclose your code within delimiters."


def lcb_style_leetcode_prompt(question_title: str, lang_code):
    prompt = SYSTEM_MESSAGE_GENERIC
    prompt += f"### Question:\n{question_title}\n\n"
    prompt += f"### Format: {FORMATTING_MESSAGE_WITH_STARTER_CODE}\n"
    prompt += f"```python\n{lang_code}\n```\n\n"
    prompt += "### Answer: (use the provided format with backticks)\n\n"
    return prompt


LEETCODE_PROMPT = """Given the description of an algorithm problem and its starter code, please integrate these two parts into a complete problem statement without providing the solution to the algorithm problem.


===== Exemplar 1 =====

===== Problem description:
You are given a 0-indexed string s that consists of digits from 0 to 9.
A string t is called a semi-repetitive if there is at most one consecutive pair of the same digits inside t. For example, 0010, 002020, 0123, 2002, and 54944 are semi-repetitive while 00101022, and 1101234883 are not.
Return the length of the longest semi-repetitive substring inside s.
A substring is a contiguous non-empty sequence of characters within a string.
 
Example 1:

Input: s = "52233"
Output: 4
Explanation: The longest semi-repetitive substring is "5223", which starts at i = 0 and ends at j = 3. 

Example 2:

Input: s = "5494"
Output: 4
Explanation: s is a semi-reptitive string, so the answer is 4.

Example 3:

Input: s = "1111111"
Output: 2
Explanation: The longest semi-repetitive substring is "11", which starts at i = 0 and ends at j = 1.

 
Constraints:

1 <= s.length <= 50
'0' <= s[i] <= '9'

===== Starter code:
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:

===== Complete problem statement:
You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests. You will NOT return anything except for the program.
### Question:
You are given a 0-indexed string s that consists of digits from 0 to 9.
A string t is called a semi-repetitive if there is at most one consecutive pair of the same digits inside t. For example, 0010, 002020, 0123, 2002, and 54944 are semi-repetitive while 00101022, and 1101234883 are not.
Return the length of the longest semi-repetitive substring inside s.
A substring is a contiguous non-empty sequence of characters within a string.
 
Example 1:

Input: s = "52233"
Output: 4
Explanation: The longest semi-repetitive substring is "5223", which starts at i = 0 and ends at j = 3. 

Example 2:

Input: s = "5494"
Output: 4
Explanation: s is a semi-reptitive string, so the answer is 4.

Example 3:

Input: s = "1111111"
Output: 2
Explanation: The longest semi-repetitive substring is "11", which starts at i = 0 and ends at j = 1.

 
Constraints:

1 <= s.length <= 50
'0' <= s[i] <= '9'

### Format: You will use the following starter code to write the solution to the problem and enclose your code within delimiters.
```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        
```

### Answer: (use the provided format with backticks)


===== Exemplar 2 =====

===== Problem description:
Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.
The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  
 
Example 1:

Input: n = 4
Output: "pppz"
Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".

Example 2:

Input: n = 2
Output: "xy"
Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".

Example 3:

Input: n = 7
Output: "holasss"

 
Constraints:

1 <= n <= 500

===== Starter code:
class Solution:
    def generateTheString(self, n: int) -> str:

===== Complete problem statement:
Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.
The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  
 
Example 1:

Input: n = 4
Output: "pppz"
Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".

Example 2:

Input: n = 2
Output: "xy"
Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".

Example 3:

Input: n = 7
Output: "holasss"

 
Constraints:

1 <= n <= 500

Please complete the following python code to solve the problem:
```python
class Solution:
    def generateTheString(self, n: int) -> str:
```


===== Attention =====
1. Do not confine yourself to the format of the example above; feel free to express it creatively.
2. The complete problem should include both the problem description and the starter code.
3. Avoid using terms like "Problem description," "Starter code," or "Complete problem statement" in the final complete problem statement.
4. No explain, no format characters, only output the complete problem statement!


===== Now Your Task =====

===== Problem description:
{question_title}

===== Starter code:
{lang_code}

===== Complete problem statement:
"""
