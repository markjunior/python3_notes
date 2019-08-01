import pickle

cur_str = '2312'
cur_fn = len
with open('./../data/fighters.pickle', 'wb') as f:
    pickle.dump((cur_str, cur_fn), f)

with open('./../data/fighters.pickle', 'rb') as f:
    load_str, load_fn = pickle.load(f)
    print(load_fn([2,3,4]), load_str)


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
