import re
def hapax(filepath):
    file = open(filepath, encoding="utf8") 
    words = re.findall('\w+', file.read().lower())
    count = {key: 0 for key in words} #var store count
    for word in words:  #iterate if word is already in the sequence datatype
        count[word] += 1
    for word in count:  #add new sequence datatype for new word
        if count[word] == 1:
            print (word)    
hapax('thebook.txt')