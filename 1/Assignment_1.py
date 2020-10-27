def ez2look():
    for a, b in inventory.items():
        print(a," : ", b)
    for a in range(60):
        print("-", end="")
    print("")

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
#making new dictionary and adding the new dictionary to the inventory dictionary
inventory1 = {'pocket':['seashell','strange berry','lint']}
inventory.update(inventory1)
ez2look()
#returning values of keys
backpackitem = (inventory.get("backpack"))
#sort, remove, and add value
backpackitem.sort()
ez2look()
backpackitem.remove("dagger")
ez2look()
inventory["gold"] += 50
ez2look()
