f = open("thebook.txt", mode="r", encoding="utf8")
biglist = [line.rstrip('\n') for line in f]
f.close()
print(biglist)
def bigchunggus():
    for word in biglist:
        counts = biglist
        if word in counts:
            counts[word] += 1
        else:
            counts[word] == 1
    return counts
counts = bigchunggus(biglist)
print(counts)
print(content_list)
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count(biglist))

