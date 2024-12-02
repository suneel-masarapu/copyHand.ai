import re
from collections import defaultdict
import os

stop_words = set([
    "a", "about", "above", "after", "again", "against", "all", "am", "an", 
    "and", "any", "are", "arent", "as", "at", "be", "because", "been", 
    "before", "being", "below", "between", "both", "but", "by", "cant", 
    "cannot", "could", "couldnt", "did", "didnt", "do", "does", "doesnt", 
    "doing", "dont", "down", "during", "each", "few", "for", "from", "further", 
    "had", "hadnt", "has", "hasnt", "have", "havent", "having", "he", 
    "hed", "hell", "hes", "her", "here", "heres", "hers", "herself", "him", 
    "himself", "his", "how", "hows", "i", "id", "ill", "im", "ive", 
    "if", "in", "into", "is", "isnt", "it", "its", "itself", 
    "lets", "me", "more", "most", "mustnt", "my", "myself", "no", "nor", 
    "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", 
    "ours", "ourselves", "out", "over", "own", "same", "shant", "she", 
    "shed", "shell", "shes", "should", "shouldnt", "so", "some", "such", 
    "than", "that", "the", "their", "theirs", "them", "themselves", 
    "then", "there", "theres", "these", "they", "theyd", "thell", "theyre", 
    "theyve", "this", "those", "through", "to", "too", "under", "until", 
    "up", "very", "was", "wasnt", "we", "wed", "well", "were", "weve", 
    "were", "werent", "what", "whats", "when", "whens", "where", "wheres", 
    "which", "while", "who", "whos", "whom", "why", "whys", "with", "wont", 
    "would", "wouldnt", "you", "youd", "youll", "youre", "youve", "your", 
    "yours", "yourself", "yourselves"
])

def parse(filepath, target):
    # Open the file with utf-8 encoding and ignore decoding errors
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()

    # Initialize the word frequency map
    word_count = defaultdict(int)
    
    with open(target, 'w', encoding='utf-8') as tar:
        count = 0
        for line in lines:
            if count < 3:
                count += 1
                continue

            # Process each line, removing unwanted characters
            temp = ""
            words = re.findall(r'\b[A-Za-z]+\b', line)  # Extract words consisting only of alphabets
            for word in words:
                word = modify(word.lower())  # Modify the word
                if word not in stop_words:
                    temp += word + " "
                    word_count[word] += 1
            tar.write(temp.strip() + "\n")  # Write processed line to target file

    return word_count


def modify(word):
    # Remove common suffixes from words
    if len(word) == 1:
        return word
    if word.endswith('s') and len(word) > 1 and word[-2] != 's':
        return word[:-1]
    elif word.endswith('ed') and len(word) > 2:
        return word[:-2]
    elif word.endswith('ly') and len(word) > 2:
        return word[:-2]
    elif word.endswith('ing') and len(word) > 3:
        return word[:-3]
    return word

# Create directories if they don't exist
os.makedirs("C:/Users/sunee/OneDrive - IIT Delhi/projects/deep learning/testcases/emails/parsed", exist_ok=True)
path = "C:/Users/sunee/OneDrive - IIT Delhi/projects/deep learning/testcases/emails/raw"
dest = "C:/Users/sunee/OneDrive - IIT Delhi/projects/deep learning/testcases/emails/parsed"
word_path = "C:/Users/sunee/OneDrive - IIT Delhi/projects/deep learning/testcases/emails/word_count.txt"
word_count = defaultdict(int)

# Process each file in the directory
for filename in os.listdir(path):
    filepath = os.path.join(path, filename)
    destination = os.path.join(dest, filename)
    temp = parse(filepath, destination)
    for word, count in temp.items():
        word_count[word] += count

# Write the word counts to the output file
with open(word_path, 'w') as file:
    for word, count in word_count.items():
        file.write(f"{word},{count}\n")
