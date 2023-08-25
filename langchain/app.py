import os
import json
import logging
from flask import Flask, request, jsonify, g
from llm_bot import LLM_Chatbot


try:
    LLM_HTTP_LISTEN_PORT = os.environ["LLM_HTTP_LISTEN_PORT"]
except:
    LLM_HTTP_LISTEN_PORT = 8080

logging.basicConfig(filename="flask.log", level=logging.DEBUG)

app = Flask(__name__)

chatbot = LLM_Chatbot()


def talk_to_chat(data: str) -> dict:
    return chatbot.conversations(data)


def process_webhook(data: dict) -> None:
    analyse = ""
    analyse += json.dumps(data["commonLabels"])
    analyse += json.dumps(data["title"])
    analyse += json.dumps(data["state"])
    analyse += json.dumps(data["message"])
    analyse += json.dumps(data["commonAnnotations"])
    print(f"{analyse}=")
    answer = talk_to_chat(analyse)
    print(f"LLM answered: {answer['text']}", flush=True)


@app.route("/", methods=["POST"])
def receive_webhook():
    if request.method == "POST":
        print(f"{request.json=}")
        data = request.json

        # Grafana sends empty request to validate the webhook.
        if "firing" in data["status"]:
            process_webhook(data)

        return jsonify(success=False)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=LLM_HTTP_LISTEN_PORT, debug=True)
