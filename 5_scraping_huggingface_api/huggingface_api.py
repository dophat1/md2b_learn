import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv


# Load token from .env file
load_dotenv()

HF_TOKEN = os.environ['HF_TOKEN']


# Create the model
client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    token=HF_TOKEN
)

# Separate the .txt file into list of prompts
with open('sample_prompts.txt', 'r') as f:
    prompts = [prompt.strip() for prompt in f]


for prompt in prompts:
    messages = [
        {'role': 'system', 'content':'You are an expert for Machine Learning, NLP and Python coding'},
        {'role': 'user', 'content':prompt}
    ]
    
    response = client.chat_completion(messages=messages, max_tokens=500, top_p=0.2)

    print(response.choices[0].message.content)