prices = {
            "banana": 4,
            "apple": 2,
            "orange": 1.5,
            "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
def thingamajig():
    for item in prices:
        print (item)
        print ("Price: " + str(prices[item]))
        print ("Stock: " + str(stock[item]) +"\n")
thingamajig()
def thingamabob():
    total = 0
    for key in prices:
        print (prices[key] * stock[key])
        subtotal = prices[key] * stock[key]
        total += subtotal
    return total
total = thingamabob()
print("Total :",total)
