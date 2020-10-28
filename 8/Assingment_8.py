# words = ("audino bagon baltoy banette bidoof braviary bronzor carracosta "
#          "charmeleon cresselia croagunk darmanitan deino emboar emolga "
#          "exeggcute gabite girafarig gulpin haxorus")
# words = (words.split())

trylist = ["ab","bc","cd","ef","ba","ad","de","def"]
seqcollection = {}
longestcomb = []
def listmaker():
    for pokemon in trylist:
        if pokemon[0] != pokemon[-1]:
            seqcollection[pokemon[0]] = [pokemon]
        else:
            seqcollection[pokemon[0]].append(pokemon)
        
print(seqcollection)

def combining(current_chain):
    if len(longestcomb) < len(current_chain):
        longestcomb = current_chain

    
