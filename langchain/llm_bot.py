import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


LLM_API_KEY = os.environ["LLM_API_KEY"]
SYSTEM_PROMPT = "You are chatbot who receives alerts based on telemetry data from network devices. Your job is to make sense of the alert received and process for an engineer. Provide as  much help as possible, but don't invent. reply in markdown format"


class LLM_Chatbot:
    def __init__(self) -> None:
        self._start_llm()

    def _start_llm(self):
        self.llm = ChatOpenAI(openai_api_key=LLM_API_KEY)
        self.prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(SYSTEM_PROMPT),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{question}"),
            ]
        )

        self.memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        self.conversation = LLMChain(
            llm=self.llm, prompt=self.prompt, verbose=True, memory=self.memory
        )

    def conversations(self, data: str) -> LLMChain:
        return self.conversation({"question": data})
