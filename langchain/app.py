import os
import json
import logging
from flask import Flask, request, jsonify, g
from llm_bot import LLM_Chatbot
from langchain.chains import LLMChain


try:
    LLM_HTTP_LISTEN_PORT = os.environ["LLM_HTTP_LISTEN_PORT"]
except:
    LLM_HTTP_LISTEN_PORT = 8080

logging.basicConfig(filename="flask.log", level=logging.DEBUG)

app = Flask(__name__)


def talk_to_chat(chatbot: LLMChain, data: str) -> dict:
    return chatbot.conversations(data)


@app.route("/webhook", methods=["POST"])
def alerts():
    if request.method == "POST":
        print("data sent to /webhook")
        data = json.loads(request.args.get("data"))
        analyse = ""
        analyse += json.dumps(data["commonLabels"])
        analyse += json.dumps(data["title"])
        analyse += json.dumps(data["state"])
        analyse += json.dumps(data["message"])
        analyse += json.dumps(data["commonAnnotations"])
        chatbot = LLM_Chatbot()
        answer = talk_to_chat(chatbot, analyse)
        print(f"LLM answered: {answer['text']}", flush=True)
        return jsonify(answer["text"])


@app.route("/", methods=["POST"])
def alert2():
    if request.method == "POST":
        print("data sent to /")
        print(request.__dict__)

        data = json.loads(request.args.get())
        analyse = ""
        analyse += json.dumps(data["commonLabels"])
        analyse += json.dumps(data["title"])
        analyse += json.dumps(data["state"])
        analyse += json.dumps(data["message"])
        analyse += json.dumps(data["commonAnnotations"])
        chatbot = LLM_Chatbot()
        answer = talk_to_chat(chatbot, analyse)
        print(f"LLM answered: {answer['text']}", flush=True)
        return jsonify(answer["text"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=LLM_HTTP_LISTEN_PORT, debug=True)
