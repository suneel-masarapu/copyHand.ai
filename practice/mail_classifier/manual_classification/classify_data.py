import os
import sys
root = "C:/Users/sunee/OneDrive - IIT Delhi/projects/deep learning/copyHand.ai/practice/mail_classifier/manual_classification"
index_file = os.path.join(root,'index.txt')
source = os.path.join(root,'path_to_samples.txt')
true_val_path = "C:/Users/sunee/OneDrive - IIT Delhi/projects/deep learning/testcases/emails/classification/tru.txt"
false_val_path = "C:/Users/sunee/OneDrive - IIT Delhi/projects/deep learning/testcases/emails/classification/flse.txt"

need_to_check = []
index = 0
with open(source,'r') as file :
    paths = file.read()
    need_to_check = paths.split('\n')

with open(index_file,'r') as file :
    index = int(file.read())

while index < len(need_to_check) :
    filepath = need_to_check[index]
    with open(filepath,'r') as file :
        print(file.read())
    jury = input("\n\n\ngood(1) : bad(0) : stop(s) ? :: ")
    if(jury == 's') :
        sys.exit("BYe,good day")
    if(jury == '1') :
        with open(true_val_path,'a') as temp :
            temp.write(filepath + '\n')
    else :
        with open(false_val_path,'a') as temp :
            temp.write(filepath + '\n')
    index +=  1 
    with open(index_file,'w') as temp :
        temp.write(str(index) + '\n')
    os.system("cls")







