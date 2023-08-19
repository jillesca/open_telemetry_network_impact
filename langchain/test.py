from flask import Flask, request, jsonify
import os
import json


app = Flask(__name__)
LLM_API_KEY = os.environ["LLM_API_KEY"]


@app.route("/alerts", methods=["POST"])
def alerts():
    if request.method == "POST":
        data = json.loads(request.args.get("data"))
        print(data, flush=True)
        return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
