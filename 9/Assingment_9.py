with open("assingment9.txt", mode="r", encoding="utf8") as rfile, open("assingment9result.txt", mode="w", encoding="utf8") as wfile:
    wordlist = rfile.read().split()
    title = ["Dr.", "Mr.", "Dr.", "Jr."]
    forexample = ["e.g","i.e."]
    website = ".com"
    realdot = []
    script = []
    def cavemanfilter():
        for word in wordlist:
            if "." in word or "?" in word:
                if word in title or word in forexample:
                    pass
                else:
                    if any(cha.isdigit() for cha in word) or word.find(website) != -1:
                        pass
                    else:
                        realdot.append(word)
                        # print(realdot)
        return realdot
    def newline():
        for word in wordlist:
            if word not in realdot:
                notdotword = (word + " ")
                wfile.write(notdotword)
            else:
                dotword = (word + "\n")
                wfile.write(dotword)
    cavemanfilter()
    newline()
    

                
            

                