import os
import json
import logging
from flask import Flask, request, jsonify
from llm_bot import LLM_Chatbot


try:
    LLM_HTTP_LISTEN_PORT = os.environ["LLM_HTTP_LISTEN_PORT"]
except:
    LLM_HTTP_LISTEN_PORT = 8080

logging.basicConfig(filename="flask.log", level=logging.INFO)


app = Flask(__name__)

chatbot = LLM_Chatbot()


def chat_to_ai(data: str) -> str:
    return chatbot.chat(data)


def process_webhook(data: dict) -> None:
    analyse = ""
    analyse += json.dumps(data.get("commonLabels", ""))
    analyse += json.dumps(data.get("title", ""))
    analyse += json.dumps(data.get("state", ""))
    analyse += json.dumps(data.get("message", ""))
    analyse += json.dumps(data.get("commonAnnotations", ""))
    logging.debug(analyse)
    answer = chat_to_ai(json.dumps(analyse))
    msg = f"LLM answered: {answer}"
    logging.info(msg)
    print(msg, flush=True)


@app.route("/", methods=["POST"])
def receive_webhook():
    if request.method == "POST":
        data = request.json
        logging.debug(data)

        # Grafana sends empty post to validate the webhook.
        if "firing" in data["status"]:
            process_webhook(data)

        return jsonify(success=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=LLM_HTTP_LISTEN_PORT, debug=False)
