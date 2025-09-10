#Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Book:
    def __init__(self,id=1,name='Guest',price=200,author='none'):
        self.bid=id
        self.bname=name
        self.price=price
        self.author=author

    def __del__(self):
        print('Destructor is called')

    def showbook(self):
        print('Book id',self.bid)
        print('name',self.bname)
        print('price',self.price)
        print('author',self.author)

obj1=Book(2,'Meluha',450,"Radha")
obj1.showbook()
