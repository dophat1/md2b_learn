import numpy as np 
import math

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


print(dict_build("Happy birthday"))
print(dict_build("I wish you a wonderful anniversary"))
a = vector_embedding("Happy birthday")
b = vector_embedding("I wish you a wonderful anniversary")
print(cosine_similarity(a, b))