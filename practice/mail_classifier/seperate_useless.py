import shutil
import os

source = "C:/Users/sunee/OneDrive - IIT Delhi/projects/deep learning/testcases/emails/raw"

with open(source + "/useless.txt",'r') as file :
    data = file.read()

useless_files = data.split()
os.makedirs(source + '/useless/',exist_ok=1)
destination = os.path.join(source,'useless')

count_moved = 0
count_not_found = 0

for filename in useless_files :
    filename += '.txt'
    dest = os.path.join(destination,filename)
    sor = os.path.join(source,filename)
    try :
        shutil.move(sor,dest)
        count_moved += 1
    except FileNotFoundError :
        count_not_found += 1
        continue
    
print("moved : ",count_moved)
print("not found : ",count_not_found)
print("total : ",len(useless_files))

