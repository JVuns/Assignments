words = ("audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask")
# words = (words.split())

listmaker = words.split(" ")
pokemondict = {}
for pokemon in listmaker:
    if pokemon[0] not in pokemondict:
        pokemondict[pokemon[0]] = [pokemon]
    else:
        pokemondict[pokemon[0]].append(pokemon)
print(pokemondict)
# length = 0
# longest = []

# def braincell(currentchain):
#     global length
#     global longest

#     if len(currentchain) > length:
#         length = len(currentchain)
#         longest = currentchain
#         # print(longest)
#     if currentchain[-1][-1] in pokemondict:
#         for name in pokemondict[currentchain[-1][-1]]:
#             if name not in currentchain: 
#                 braincell(currentchain + [name])
            
# for names in listmaker:
#     braincell([names])

# # Print all the stuff
# print(longest)
