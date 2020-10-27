
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
#making new dictionary and adding the new dictionary to the inventory dictionary
inventory1 = {'pocket':['seashell','strange berry','lint']}
inventory.update(inventory1)

#print
for a, b in inventory.items():
    print(a," : ", b)

#just a border between prints
for a in range(60):
    print("-", end="")
print("")

#returning backpack value and sorting the value
sorter = (inventory.get(("backpack")))
sorter.sort()

#print
for a, b in inventory.items():
    print(a," : ", b)

