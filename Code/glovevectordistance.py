import numpy as np


def calculate_distance(word1, word2, embeddings_file):
    embeddings = {}
    with open(embeddings_file, 'r', encoding='utf-8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            vector = np.array([float(val) for val in values[1:]])
            embeddings[word] = vector
    
    if word1 not in embeddings or word2 not in embeddings:
        return "Word not found in embeddings"
    
    distance = np.linalg.norm(embeddings[word1] - embeddings[word2])
    return distance

embeddings_file = '../GloVe/glove.6B/glove.6B.50d.txt'
word1 = 'king'
word2 = 'queen'
distance = calculate_distance(word1, word2, embeddings_file)
print(f"Distance between '{word1}' and '{word2}': {distance}")