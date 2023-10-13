"""
# -*- coding: utf-8 -*-

Created on Oct 2023
@author: Prateek Yadav

"""
import warnings
warnings.filterwarnings('ignore')


from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain import HuggingFaceHub

# Using OpenAI LLM
llm = OpenAI()
chat_model = ChatOpenAI()

prompt = "Alice has a parrot. What animal is Alice's pet?"

print(llm.predict(prompt))
print('-'*100)
print(chat_model.predict(prompt))


# Using OS LM
# llm = HuggingFaceHub(repo_id="google/flan-t5-xl", huggingfacehub_api_token='pass')
# print('-' * 100)
# completion = llm(prompt)
