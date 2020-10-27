with open("file.txt",mode="r",encoding="utf8") as rfile, open("2ndtext", mode="w", encoding="utf8") as wfile:
    longlist = []
    for lines in rfile:
        longlist.append(lines.split())
    # print(longlist)
    for list1 in longlist:
        # print(list1)
        str1 = " "   
        dud = (str1.join(list1))
        wfile.write(dud+"\n")
        print(dud)
