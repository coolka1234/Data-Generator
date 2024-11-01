import os

user_fk_keys_set=set()
vehicles_numbers_set=set()
licenses_fk_keys_set=set()
inspector_fk_keys_set=set()
passenger_fk_keys_set=set()
line_numbers_set=set()
path_fk_keys_set=set()
path_stops_fk_keys_set=set()
names=['users', 'editors', 'licenses', 'vehicles', 'inspectors', 'passengers', 'paths', 'line_numbers']
def save_set(name):
    with open(f'sets/fk_keys_hash_sets_{name}.txt', 'w') as file:
        if name=='vehicles':
            for item in vehicles_numbers_set:
                file.write("%s\n" % item)
        elif name=='licenses':
            for item in licenses_fk_keys_set:
                file.write("%s\n" % item)
        elif name=='user':
            for item in user_fk_keys_set:
                file.write("%s\n" % item)
        elif name=='inspector':
            for item in inspector_fk_keys_set:
                file.write("%s\n" % item)
        elif name=='passenger':
            for item in passenger_fk_keys_set:
                file.write("%s\n" % item)
        elif name=='paths':
            for item in path_fk_keys_set:
                file.write("%s\n" % item)
        elif name=='line_numbers':
            for item in line_numbers_set:
                file.write("%s\n" % item)
        elif name=='users':
            for item in user_fk_keys_set:
                file.write("%s\n" % item)
        elif name=='path_stops':
            for item in path_stops_fk_keys_set:
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
                elif name=='path_stops':
                    path_stops_fk_keys_set.add(line.strip())
                elif name=='users':
                    user_fk_keys_set.add(line.strip())
