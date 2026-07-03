import numpy as np 
import math
from sentence_transformers import SentenceTransformer 

dictionary = {}

def dict_build(sentences):
    words = sentences.lower().split(" ")
    for word in words:
        if word not in dictionary:
            dictionary[word] = len(dictionary)
    return dictionary

def vector_embedding(sentences):
    lowercase = sentences.lower()
    words = lowercase.split(" ")
    word_embedding = np.zeros(len(dictionary))
    for word in words:
        if word in dictionary:
            idx = dictionary[word]
            word_embedding[idx] += 1
    return word_embedding

def dot(a,b):
    if len(a) == len(b):
        n = len(a)
        sum = 0
        for i in range(n):
            sum += a[i] * b[i] 
        return sum
    else:
        return False
    
def norm(a):
    sum = 0 
    for i in range(len(a)):
        sum += a[i]**2
    normalized = math.sqrt(sum)
    return normalized
    
def cosine_similarity(a, b):
    return dot(a,b)/(norm(a) * norm(b))

sentence_1 = "A golden retriever playing in the park"
sentence_2 = "A dog running through grass"

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
a = model.encode(sentence_1)
b = model.encode(sentence_2)



print(cosine_similarity(a, b))