import os
user_fk_keys_set=set()
vehicles_numbers_set=set()
licenses_fk_keys_set=set()
inspector_fk_keys_set=set()
passenger_fk_keys_set=set()
line_numbers_set=set()
path_fk_keys_set=set()
names=['users', 'editors', 'licenses', 'vehicles', 'inspectors', 'passengers', 'paths', 'line_numbers']
def save_set(name):
    with open(f'sets/fk_keys_hash_sets_{name}.txt', 'w') as file:
        for item in user_fk_keys_set:
            file.write("%s\n" % item)

def load_set(name):
    if os.path.exists(f'sets/fk_keys_hash_sets_{name}.txt'):
        with open(f'sets/fk_keys_hash_sets_{name}.txt', 'r') as file:
            for line in file:
                if name=='vehicles':
                    vehicles_numbers_set.add(line.strip())
                elif name=='licenses':
                    licenses_fk_keys_set.add(line.strip())
                elif name=='user':        
                    user_fk_keys_set.add(line.strip())
                elif name=='inspector':
                    inspector_fk_keys_set.add(line.strip())
                elif name=='passenger':
                    passenger_fk_keys_set.add(line.strip())
                elif name=='path':
                    path_fk_keys_set.add(line.strip())
                elif name=='line_numbers':
                    line_numbers_set.add(line.strip())
