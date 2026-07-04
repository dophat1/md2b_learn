import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import pandas as pd 

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


answers = {}
total = len(prompts)

for i, prompt in enumerate(prompts, start=1):
    print(f"----- Processing {i}/{total} -----")
    print(f"Prompt: {prompt}")
    messages = [
        {'role': 'system', 'content':'You are an expert for Machine Learning, NLP and Python coding'},
        {'role': 'user', 'content': prompt}
    ]
    
    response = client.chat_completion(messages=messages, max_tokens=200, top_p=0.2)
    print(f"Response: {response.choices[0].message.content}")
    answers[prompt] = response.choices[0].message.content
    



df = pd.DataFrame(list(answers.items()), columns=['prompt', 'answer'])
df.to_csv("prompts_answers.csv")
print("Saved successfully")
