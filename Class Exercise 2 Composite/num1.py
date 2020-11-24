class Author():
    def __init__(self, auAuthor, email, gender):
        self.__name = auAuthor
        self.__email = email
        self.__gender = gender

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getGender(self):
        return self.__gender

    def __str__(self):
        return(f"Author[name{self.__name},email={self.__email},gender={self.__gender}]")
    
class Book(Author):
    def __init__(self, aBook, price, auAuthor, email, gender, qty=0, author=[]):
        self.__name = aBook
        self.__price = price
        self.__obj_Author = Author(auAuthor, email, gender)
        self.__qty = qty
        self.__author = author
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
        return(f"Book[name={self.__name},Author[name={self.__obj_Author.getName()},email={self.__obj_Author.getEmail()},gender={self.__obj_Author.getGender()}],price={self.getPrice()},qty={self.getQty()}]")
    def getAuthorNames(self):
        return self.__author
TestBook = Book("Bookname", 2000, ["Charles","Bonnie"], "Charles@gmail.com", "M", 10)
print(TestBook.__str__())