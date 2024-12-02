import os
source = "C:/Users/sunee/OneDrive - IIT Delhi/projects/deep learning/testcases/emails/raw"
target = "C:/Users/sunee/OneDrive - IIT Delhi/projects/deep learning/copyHand.ai/practice/mail_classifier/manual_classification/path_to_samples.txt"


for filename in os.listdir(source) :
    filepath = os.path.join(source,filename)
    if os.path.isfile(filepath) :
        with open(target,'a') as file :
            file.write(source+'/'+filename+'\n')