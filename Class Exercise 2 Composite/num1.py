class Author():
    def __init__(self, auAuthor, email, gender):
        self.__name = auAuthor
        self.__email = email
        self.__gender = gender
        if self.__gender not in ['M', 'F']:
            raise ValueError(gender)
        if "@gmail.com" not in self.__email:
            raise ValueError(email) 

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getGender(self):
        return self.__gender

    def __str__(self):
        return(f"Author[name= {self.__name},email= {self.__email},gender= {self.__gender}]")
    
class Book(Author):
    def __init__(self, aBook, price, qty=0, author=[] ):
        self.__name = aBook
        self.__price = price
        self.__qty = qty
        self.__author = Author

    def getName(self):
        return self.__name

    def getAuthor(self):
        return self.__author

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price

    def getQty(self):
        return self.__qty

    def setQty(self, qty):
        self.__qty = qty

    def __str__(self,):
        return(f"Book[name={self.__name},Authors={self.getAuthorNames()},price={self.getPrice()},qty={self.getQty()}]")
    def getAuthorNames(self):
        return [author1.__str__(),author2.__str__()]

author1 = Author("Au","@gmail.com","M")
author2 = Author("Ae","B@gmail.com","M")
TestBook = Book("Bookname", 2000, 10, [author1,author2])
print(TestBook.__str__())