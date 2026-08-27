import math

def evaluate_expression(expr: str, current_ans: float | int=0) -> tuple[float | int | None, str | None]:
    expr = expr.strip()
    if not expr:
        return None, None

    if expr.startswith(('+', '-', '*', '/', '**')):
        expr = f"ans{expr}"

    safe_dict= {
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
        result = eval(expr, safe_dict, {})
        return result, None
    except ZeroDivisionError:
        return None, "Error: division by zero isnt allowed"
    except Exception:
        return None, "Error: check your synatx"

if __name__ == "__main__":
    
    #quick tests
    print(evaluate_expression("sin(radians(90))"))
    print(evaluate_expression("*2", current_ans=65))
    print(evaluate_expression("1/0"))