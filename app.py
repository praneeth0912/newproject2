from flask import Flask, render_template, request, jsonify
import operations
import text_utils

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/text-analyzer")
def text_analyzer():
    return render_template("text_analyzer.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid request payload"}), 400

    expression = str(data.get("expression", "")).strip()
    operation = data.get("operation")

    if not expression and operation != "C":
        return jsonify({"result": ""})

    try:
        if operation == "=":
            result = operations.calculate(expression)

        elif operation == "√":
            result = operations.square_root(expression)

        elif operation == "x²":
            result = operations.square(expression)

        elif operation == "%":
            result = operations.percentage(expression)

        else:
            return jsonify({"error": "Invalid Operation"}), 400

        # Clean float formatting (5.0 -> 5)
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        return jsonify({"result": result})

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception:
        return jsonify({"error": "Server error processing calculation"}), 500

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    text = data.get("text", "")
    operation = data.get("operation")

    data = request.get_json()

    text = data.get("text", "").strip()
    operation = data.get("operation")

# Validate input
    if not text:
        return jsonify({
        "error": "Please enter some text."
    }), 400

    if any(char.isdigit() for char in text):
        return jsonify({
        "error": "Numbers are not allowed. Please enter text only."
    }), 400

    if operation == "reverse":

        result = text_utils.reverse_text(text)

    elif operation == "character_count":

        result = text_utils.character_count(text)

    elif operation == "vowel_count":

        result = text_utils.vowel_count(text)

    else:

        return jsonify({
            "error": "Invalid Operation"
        }), 400

    return jsonify({
        "result": result
    })



if __name__ == "__main__":
    app.run(debug=True)