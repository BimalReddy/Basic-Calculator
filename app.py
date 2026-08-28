from flask import Flask, render_template, request, jsonify
from calculator import evaluate_expression

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/calculate", methods =["POST"])
def calculate():
    data = request.get_json() or {}
    expression = data.get("expression", "")
    current_ans = data.get("ans", 0)

    result, error = evaluate_expression(expression, current_ans)

    if error:
        return jsonify({"error": error}), 400

    return jsonify({"result": error})

if __name__ == "__main__":
    app.run(host= "127.0.0.1", port=5000, debug=True)