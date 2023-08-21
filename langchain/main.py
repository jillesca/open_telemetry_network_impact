# Receive information
# review if there is additional informatin stored
# process info received and stored
# notify user original data and analisys
# store original information receive - as emmbedings?

from langchain.llms import OpenAI
import os

LLM_API_KEY = os.environ["LLM_API_KEY"]

llm = OpenAI(openai_api_key=LLM_API_KEY)
