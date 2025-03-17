import re


def parse_classes_and_methods(code: str) -> dict:
    class_pattern = re.compile(r'^\s*class\s+(\w+)\b')
    method_pattern = re.compile(r'^(\s*)def\s+(\w+)\(')
    
    result = {}
    current_class = None
    class_indent = 0
    method_indent = 0
    
    for line in code.split('\n'):
        stripped_line = line.lstrip()
        if not stripped_line:
            continue
        
        # Check for class definition
        class_match = class_pattern.match(line)
        if class_match:
            if current_class:
                current_class = None
                class_indent = 0
                method_indent = 0
            class_name = class_match.group(1)
            class_indent = len(line) - len(stripped_line)
            current_class = class_name
            method_indent = 0
            result[class_name] = []
            continue
        
        # Check for methods if inside a class
        if current_class:
            current_line_indent = len(line) - len(stripped_line)
            if method_indent == 0:
                if current_line_indent > class_indent:
                    method_match = method_pattern.match(line)
                    if method_match:
                        method_indent = current_line_indent
                        method_name = method_match.group(2)
                        result[current_class].append(method_name)
                else:
                    current_class = None
                    class_indent = 0
                    method_indent = 0
            else:
                if current_line_indent == method_indent:
                    method_match = method_pattern.match(line)
                    if method_match:
                        method_name = method_match.group(2)
                        result[current_class].append(method_name)
                elif current_line_indent < method_indent:
                    if current_line_indent <= class_indent:
                        current_class = None
                        class_indent = 0
                        method_indent = 0
    return result
