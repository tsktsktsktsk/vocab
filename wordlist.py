import os
import json
from random import shuffle
dir_path = './audio'
words = [filename[:-4] for filename in os.listdir(dir_path)]
shuffle(words)
word_dict = {
    "words": words
}
with open('wordlist.json', 'w') as fout:
    json.dump(word_dict, fout)