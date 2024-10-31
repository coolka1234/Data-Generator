import os
user_fk_keys_set=set()
names=['user', 'editor']
def save_set(name):
    with open(f'sets/fk_keys_hash_sets_{name}.txt', 'w') as file:
        for item in user_fk_keys_set:
            file.write("%s\n" % item)

def load_set(name):
    if os.path.exists(f'sets/fk_keys_hash_sets_{name}.txt'):
        with open(f'sets/fk_keys_hash_sets_{name}.txt', 'r') as file:
            for line in file:
                user_fk_keys_set.add(line.strip())
