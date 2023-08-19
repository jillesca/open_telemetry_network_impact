from flask import Flask, request, jsonify
import os


app = Flask(__name__)
LLM_API_KEY = os.environ["LLM_API_KEY"]


@app.route("/")
def index():
    return "it works again one more time, testing!!!!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
