# Script for inversing the stupid funciton generating 'encrypted' stuff

import pickle
import numpy as np
import inflect
from tqdm import tqdm
from caesarcipher import CaesarCipher
from word2number import w2n

def load_glove_vectors(glove_file):
    glove_dict = {}
    with open(glove_file, 'r', encoding='utf-8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            vector = np.array(values[1:], dtype='float32')
            glove_dict[word] = vector
    return glove_dict

def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

def find_closest_word(target_vector, glove_lookup):
    max_similarity = -1
    closest_word = None
    for word, vector in glove_lookup.items():
        similarity = cosine_similarity(target_vector, vector)
        if similarity > max_similarity:
            max_similarity = similarity
            closest_word = word

    return closest_word

def get_number_vectors(glove_dict, true_numbers=False):
    # Define the list of numbers as strings
    if true_numbers:
        numbers = [str(i) for i in range(1, 11)]
    
    else:
        inflector = inflect.engine()
        numbers = [inflector.number_to_words(str(i)) for i in range(1, 11)] + [str(i) for i in range(1, 11)]

    # Create a sub-dictionary with only the vectors for the numbers 1-10
    number_vectors = {num: glove_dict[num] for num in numbers if num in glove_dict}

    return number_vectors

def main(encrypted):

    print("Loading GloVe vectors...")
    glove_file = 'assignment_3/SignDat-Assign4/glove.42B.300d.txt'
    glove_dict = load_glove_vectors(glove_file)
    number_vectors = get_number_vectors(glove_dict)

    print("Decrypting...")
    all_numbers = []
    for i in tqdm(encrypted):
        current_number = []
        for vector in i:
            target_vector = vector
            current_number.append(str(w2n.word_to_num(find_closest_word(target_vector, glove_lookup=number_vectors))))
        all_numbers.append(current_number)

    print(all_numbers)
    print([chr(int("".join(i))) for i in all_numbers])
    print("".join([chr(int("".join(i))) for i in all_numbers]))
    print(CaesarCipher("".join([chr(int("".join(i))) for i in all_numbers]), offset=69).decoded)



if __name__ == "__main__":
    with open("assignment_3/SignDat-Assign4/importanter_stuff.pkl", "rb") as fp:
        encrypted = pickle.load(fp)

    main(encrypted)
    