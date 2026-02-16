from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Home page (HTML UI)
@app.route('/')
def home():
    return render_template("calu.html")


# Calculator API
@app.route('/cal', methods=["POST"])
def math_operator():
    data = request.get_json()

    operation = data["operation"]
    number1 = float(data["number1"])
    number2 = float(data["number2"])

    if operation == "add":
        result = number1 + number2
    elif operation == "multiply":
        result = number1 * number2
    elif operation == "division":
        result = number1 / number2
    else:
        result = number1 - number2

    return jsonify({
        "operation": operation,
        "result": result
    })


if __name__ == '__main__':
    app.run(debug=True)
