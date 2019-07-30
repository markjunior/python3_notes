import pickle

blue = '2312'
black = len
with open('./../data/fighters.pickle', 'wb') as f:
    pickle.dump((blue, black), f)

with open('./../data/fighters.pickle', 'rb') as f:
    load_blue, load_black = pickle.load(f)
    print(load_black([2,3,4]), load_blue)


print('-----------------------------------------------')

import jsonpickle


with open('./../data/fighters.json', 'w') as f:
    frozen = jsonpickle.encode(len)
    print(frozen)
    f.write(frozen)

with open('./../data/fighters.json', 'r') as f:
    contents = f.read()
    unfrozen = jsonpickle.decode(contents)
    print(unfrozen)
