import math
import re

def calculator():
    print("Interactive Calculator")
    print("Arithmetic: +, -, *, /, **(power), ()")
    print("Trigonometry: sin(x), cos(x), radians(x), pi")
    print("- Type an operator first to continue with your last result")
    print("- Use 'ans' inside an equation to insert your last result")
    print("- Type a number to start a fresh calculation")
    print("- Type 'c' to clear memory or 'q' to quit")

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

    while True:
        user_input= input("Calculate: ").strip()
        if user_input.lower() == 'q':
            print("Closing the calculator, Bye!")
            break
        if user_input.lower() == 'c':
            safe_dict["ans"]=0
            print("Memory cleared")
            continue
        if not user_input:
            continue
        if user_input.startswith(('+', '-', '*', '/', '**')):
            user_input =f"ans{user_input}"
        try:
            result = eval(user_input, safe_dict, {})
            print(f"Result: {result}")
            safe_dict["ans"]= result
        except ZeroDivisionError:
            print("Error: division by zero isn't allowed")
        except Exception:
            print("Error: check your syntax")

if __name__ == "__main__":
    calculator()
