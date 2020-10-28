import re
def howmanynumber(filepath):
    file = open(filepath, encoding="utf8") 
    words = re.findall('\w+', file.read())
    wordcount = 0
    dalength = 0
    for word in words: 
        wordcount += 1 #the number of word
        dalength += len(word) #the number of character
    avg = dalength/wordcount 
    return avg
print(howmanynumber('thebook.txt'))
