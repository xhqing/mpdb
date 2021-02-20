import sys
import os

p = sys.path
os.system("> nohup.out")

for path in p:
    os.system("nohup find {} -name pdb.py".format(path))
    
f = open('nohup.out','r')
string_list = f.readlines()
f.close()

path_list = list(map(lambda x: x[:-1], string_list))
find_pdb = False
for path in path_list:
    if '/pdb.py' in path:
        find_pdb = True
        target_path = path.replace('/pdb.py','/mpdb.py')
        flag = os.system("cp mpdb.py {}".format(target_path))
        if not flag:
            print('mpdb install seccessfully!')
        else:
            print('mpdb install failed.')
        break

if not find_pdb:
    print('mpdb install failed. pdb.py not found.')    



