import os
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationSummaryBufferMemory


LLM_API_KEY = os.environ["LLM_API_KEY"]
SYSTEM_PROMPT = """
    You are chatbot who receives alerts based on telemetry data from network devices. 
    Your job is to make sense of the alert received and process for an engineer. 
    Provide as much help as possible, but don't invent. reply in markdown format.
    If you receive new information that differs from previous conversation review if the events could be related
    """


class LLM_Chatbot:
    def __init__(self) -> None:
        self._start_llm()

    def _start_llm(self):
        llm = ChatOpenAI(openai_api_key=LLM_API_KEY, temperature=0)
        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessagePromptTemplate.from_template(
                    " ".join(SYSTEM_PROMPT.split())
                ),
                MessagesPlaceholder(variable_name="history"),
                HumanMessagePromptTemplate.from_template("{input}"),
            ]
        )
        memory = ConversationSummaryBufferMemory(
            llm=llm, max_token_limit=3000, return_messages=True
        )
        self.conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)

    def conversations(self, data: str):
        return self.conversation({"input": data})


if __name__ == "__main__":
    chatbot = LLM_Chatbot()
    chatbot.conversations("tell me a joke about developers")
    print(chatbot.__dict__)
    chatbot.conversations("now about lawyers")
    print(chatbot.__dict__)
    chatbot.conversations("now make a one, but consider the previous answer")
    print(chatbot.__dict__)
    chatbot.conversations("can you do a summary of what we talked about?")
    print(chatbot.__dict__)
