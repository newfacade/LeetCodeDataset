import sys
from io import StringIO
from typing import Any, Dict
import signal
import re
import ast

from data_structure import tree_node, tree_node_to_list, list_node, linked_list_to_list


def parse_input(input_str: str) -> Dict:
    params = {}
    pattern = r"(\w+)\s*=\s*(.+?)(?=,\s*\w+\s*=|$)"
    matches = re.finditer(pattern, input_str)
    
    for match in matches:
        key = match.group(1).strip()
        value_str = match.group(2).strip()
        try:
            params[key] = ast.literal_eval(value_str)
        except (SyntaxError, ValueError) as e:
            continue
    return params


def parse_no_key_input(input_str: str) -> list:
    try:
        obj = ast.literal_eval(input_str.strip())
        return [obj]
    except:
        return []


def get_output_given_entry_point_input(
    code: str, 
    entry_point: str, 
    input_str: str,
    lang_code=''
) -> str:
    namespace = {}
    assertion = ""

    def timeout_handler(signum, frame):
        raise TimeoutError("Function execution timed out")
    
    try:
        exec(code, namespace)
        
        input_str = input_str.replace('null', 'None')
        params = parse_input(input_str=input_str)
        list_params = parse_no_key_input(input_str=input_str) if not params else []

        if 'TreeNode' in lang_code:
            for k, v in params.items():
                if isinstance(v, list):
                    params[k] = tree_node(v)
                    assertion += f"{k} = tree_node({v}),"
                elif isinstance(v, str):
                    assertion += f'{k} = "{v}",'
                else:
                    assertion += f'{k} = {v},'
        elif 'ListNode' in lang_code:
            for k, v in params.items():
                if isinstance(v, list):
                    params[k] = list_node(v)
                    assertion += f"{k} = list_node({v}),"
                elif isinstance(v, str):
                    assertion += f'{k} = "{v}",'
                else:
                    assertion += f"{k} = {v},"
        else:
            for k, v in params.items():
                if isinstance(v, str):
                    assertion += f'{k} = "{v}",'
                else:
                    assertion += f"{k} = {v},"
        assertion = f"candidate({assertion[:-1]})"
            
            
        if '(' in entry_point and ')' in entry_point:
            class_name = entry_point.split('.')[0].replace('(', '').replace(')', '')
            method_name = entry_point.split('.')[1]
            
            instance = namespace[class_name]()
            method = getattr(instance, method_name)
        else:
            method = eval(entry_point, namespace)
            
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        
        try:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(10)

            if params:
                result = method(**params)
            else:
                result = method(*list_params)
            
            if (hasattr(result, 'left') and hasattr(result, 'right')) or result is None:
                result = tree_node_to_list(result)
                assertion = f"    assert is_same_tree({assertion}, tree_node({result}))\n"
            if hasattr(result, 'val') or result is None:
                result = linked_list_to_list(result)
                assertion = f'    assert is_same_list({assertion}, list_node({result}))\n'
            elif '-> str' in lang_code:
                assertion = f'    assert {assertion} == "{result}"\n'
            else:
                assertion = f'    assert {assertion} == {result}\n'
            
            output = str(result)
        except Exception as e:
            output = f"Error: {str(e)}"
        finally:
            sys.stdout = original_stdout
            signal.alarm(0)
        
        return output, assertion
        
    except Exception as e:
        return f"Execution Error: {str(e)}", assertion

