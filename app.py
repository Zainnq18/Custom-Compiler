from flask import Flask, request, jsonify
from main import compile_source

app = Flask(__name__)

@app.route('/')
def home():
    return "Compiler is running!"

@app.route('/compile', methods=['POST'])
def compile_code():
    data = request.json
    source_code = data.get("code", "")

    listing, target, errors = compile_source(source_code)

    return jsonify({
        "listing": listing,
        "target": target,
        "errors": errors
    })

if __name__ == '__main__':
    app.run()
