import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.environ['HF_TOKEN']

client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    token=HF_TOKEN
)


messages = [
    {'role': 'system', 'content':'You are an expert for Machine Learning, NLP and Python coding'},
    {'role': 'user', 'content':'Explain to me what an API is.'}
]


response = client.chat_completion(messages=messages, max_tokens=500, top_p=0.2)

print(response.choices[0].message.content)