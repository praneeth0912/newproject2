import ast
import math
import operator

# Supported math operators
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def _eval_tree(node):
    if isinstance(node, ast.Expression):
        return _eval_tree(node.body)

    elif isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Invalid number format")

    elif isinstance(node, ast.BinOp):
        left = _eval_tree(node.left)
        right = _eval_tree(node.right)
        op_type = type(node.op)

        if op_type in OPERATORS:
            if op_type == ast.Div and right == 0:
                raise ValueError("Cannot divide by zero")
            return OPERATORS[op_type](left, right)
        raise ValueError("Unsupported operation")

    elif isinstance(node, ast.UnaryOp):
        operand = _eval_tree(node.operand)
        op_type = type(node.op)

        if op_type in OPERATORS:
            return OPERATORS[op_type](operand)
        raise ValueError("Unsupported operation")

    else:
        raise ValueError("Invalid Expression")


def calculate(expression):
    if not expression or not str(expression).strip():
        return 0

    try:
        # Sanitize common user formatting input
        clean_expr = str(expression).strip()
        parsed_ast = ast.parse(clean_expr, mode='eval')
        return _eval_tree(parsed_ast)
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")
    except ValueError as ve:
        raise ve
    except Exception:
        raise ValueError("Invalid Expression")


# Scientific functions
def square(expression):
    val = calculate(expression)
    return float(val) ** 2

def square_root(expression):
    val = calculate(expression)
    if val < 0:
        raise ValueError("Square root of a negative number is not supported")
    return math.sqrt(val)

def percentage(expression):
    val = calculate(expression)
    return float(val) / 100