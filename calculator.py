import math
import ast
import operator

ALLOWED_OPERATORS= {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def eval_ast_node(node, context):
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise TypeError("Invalid constant type")

    elif isinstance(node, ast.Name):
        if node.id in context:
            val = context[node.id]
            if isinstance(val, (int, float)):
                return val
        raise NameError(f"Name '{node.id}' is not defined")

    elif isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            operand = eval_ast_node(node.operand, context)
            return ALLOWED_OPERATORS[op_type](operand)
        raise ValueError(f"Unsupported binary operator: {op_type.__name__}")

    elif isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            left = eval_ast_node(node.left, context)
            right = eval_ast_node(node.right, context)
            return ALLOWED_OPERATORS[op_type](operand)
        raise ValueError(f"Unsupported binary operator: {op_type.__name__}")

    elif isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name) and node.func.id in context:
            func = context[node.func.id]
            if callable(func):
                args = [eval_ast_node(arg, context) for arg in node.args]
                return func(*args)
        raise NameError("Invalid function call")
    raise TypeError(f"Unsupported expression node: {type(node).__name__}")

def evaluate_expression(expr: str, current_ans: float | int=0) -> tuple[float | int | None, str | None]:
    expr = expr.strip()
    if not expr:
        return None, None

    if expr.startswith(('+', '-', '*', '/', '**')):
        expr = f"ans{expr}"

    context = {
        "__builtins__": None,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "radians": math.radians,
        "sqrt": math.sqrt,
        "log": math.log,
        "log10": math.log10,
        "factorial": math.factorial,
        "abs":abs,
        "e": math.e,
        "pi": math.pi,
        "ans": 0,
    }

    try:
        parsed_ast = ast.parse(expr, mode='eval')
        result = eval_ast_node(parsed_ast.body, context)
        return result, None

    except ZeroDivisionError:
        return None, "Error: division by zero isn't allowed"
    except (SyntaxError, TypeError, NameError):
        return None, "Error: check your syntax"
    except Exception:
        return None, "Error: calculation"