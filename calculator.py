import math
import ast
import operator
import re

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

    elif hasattr(ast, 'Num') and isinstance(node, ast.Num):
        return node.n

    elif isinstance(node, ast.Name):
        if node.id in context:
            val = context[node.id]
            if isinstance(val, (int, float)):
                return val
        raise NameError(f"Name '{node.id}' is not defined")

    elif isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            left = eval_ast_node(node.left, context)
            right = eval_ast_node(node.right, context)
            return ALLOWED_OPERATORS[op_type](left, right)
        raise ValueError(f"Unsupported binary operator: {op_type.__name__}")
    
    elif isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            operand = eval_ast_node(node.operand, context)
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

def preprocess_expression(expr: str) -> str:
    expr = re.sub(r'\)\s*([0-9a-zA-Z\(])', r')*\1', expr)
    expr = re.sub(r'(?<![a-zA-Z])(\d+(?:\.\d+)?)\s*(\(\b[a-zA-Z])', r'\1*\2', expr)
    expr = re.sub(r'\b(ans|pi|e)\s*\(', r'\1*(', expr)
    return expr

def evaluate_expression(expr: str, current_ans: float | int=0) -> tuple[float | int | None, str | None]:
    expr = expr.strip()
    if not expr:
        return None, None

    if expr.startswith(('+', '-', '*', '/', '**')):
        expr = f"ans{expr}"

    expr = preprocess_expression(expr)

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
        "ans": current_ans,
    }

    try:
        parsed_ast = ast.parse(expr, mode='eval')
        result = eval_ast_node(parsed_ast.body, context)
        return result, None

    except ZeroDivisionError:
        return None, "Error: division by zero isn't allowed"
    except (SyntaxError, TypeError, ValueError, NameError) as e:
        print(f"DEBUG AST/Preprocess Error: {e}")
        return None, f"Error: check your syntax ({e})"
    except Exception as e:
        import traceback
        traceback.print_exc()
        return None, f"Error: {e}"