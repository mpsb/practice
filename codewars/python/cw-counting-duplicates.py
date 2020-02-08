from collections import Counter 

def duplicate_count(text):
    count = Counter(text.lower())
    return len([count[i] for i in count if count[i] > 1])
     