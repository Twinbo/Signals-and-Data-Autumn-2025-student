import numpy as np
from caesarcipher import CaesarCipher
from itertools import chain
import pickle
import inflect

def load_glove_vectors(glove_file):
    glove_dict = {}
    with open(glove_file, 'r', encoding='utf-8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            vector = np.array(values[1:], dtype='float32')
            glove_dict[word] = vector
    return glove_dict

def main(dry_run=True):
    print("Loading GloVe vectors...")
    glove_file = 'assignment_3/SignDat-Assign4/glove.42B.300d.txt'
    glove_dict = load_glove_vectors(glove_file)

    # Create text and encode it using Caesar cipher and ascii
    text = "What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo"
    text_encoded = [CaesarCipher(i, offset=69).encoded for i in text.split()]
    text_ascii_encoded = [[ord(char) for char in i] + [ord(" ")] for i in text_encoded]
    text_ascii_encoded = list(chain.from_iterable(text_ascii_encoded))

    # Generate GloVe vectors from it
    full_list = []
    inflector = inflect.engine()
    for number in text_ascii_encoded:
        sublist = []
        for subnumber in str(number):
            subnumber = inflector.number_to_words(str(subnumber))
            sublist.append(glove_dict[subnumber])
        full_list.append(np.array(sublist))

    # Dump with Pickle
    if not dry_run:
        with open('importanter_stuff.pkl', 'wb') as f:
            pickle.dump(full_list, f)


if __name__ == '__main__':
    main(dry_run=False)
