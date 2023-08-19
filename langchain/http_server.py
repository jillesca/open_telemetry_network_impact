import os
import json
import logging
from flask import Flask, request, jsonify

LLM_API_KEY = os.environ["LLM_API_KEY"]
LLM_HTTP_LISTEN_PORT = os.environ["LLM_HTTP_LISTEN_PORT"]

logging.basicConfig(filename="flask.log", level=logging.DEBUG)

app = Flask(__name__)


@app.route("/alerts", methods=["POST"])
def alerts():
    if request.method == "POST":
        data = json.loads(request.args.get("data"))
        print(data, flush=True)
        return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=LLM_HTTP_LISTEN_PORT, debug=True)
