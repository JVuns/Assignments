with open("file.txt",mode="r",encoding="utf8") as rfile, open("2ndtext", mode="w", encoding="utf8") as wfile:
    longlist = []
    for lines in rfile:
        longlist.append(lines.split())
    # print(longlist)
        linecount = 0
    for list1 in longlist:
        # print(list1)
        linecount += 1
        acceptablecount = str(linecount)
        str1 = " "   
        dud = (str1.join(list1))
        wfile.write(str(linecount)+" "+dud+"\n")

