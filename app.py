from flask import Flask, render_template, request, jsonify, session
import os
from calculator import evaluate_expression

app= Flask(__name__)
app.secret_key = os.urandom(24).hex()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/calculate", methods =["POST"])
def calculate():
    data = request.get_json() or {}
    expression = data.get("expression", "")
    current_ans = session.get("ans", 0)

    result, error = evaluate_expression(expression, current_ans)

    if error:
        return jsonify({"error": error}), 400

    if result is not None:
        session["ans"] = result

    return jsonify({"result": error, "ans": session.get("ans")})

@app.route("/api/clear", methods=["POST"])
def clear_memory():
    session["ans"] = 0
    return jsonify({"message": "Memory cleared", "ans":0})

if __name__ == "__main__":
    app.run(host= "127.0.0.1", port=5000, debug=True)