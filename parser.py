import ast

code_to_analyze = """
def calculate_area(radius):
    \"\"\"Calculates the area of a circle.\"\"\"
    return 3.14 * radius * radius
"""

tree = ast.parse(code_to_analyze)

for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        print(f"Found function: {node.name}")
        print(f"Arguments: {[arg.arg for arg in node.args.args]}")