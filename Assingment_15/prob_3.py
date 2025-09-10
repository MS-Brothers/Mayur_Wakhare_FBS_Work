# Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

# Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook
class Shirt:
    def __init__(self,sid=1,sname='guest',type='casual',price=200,size='small'):
        self.id=sid
        self.name=sname
        self.type=type
        self.price=price
        self.size  = size

    def __del__(self):
        print('Destructor is Called')
    def ShowShirts(self):
        print("Shirt id",self.id)        
        print("Shirt Name",self.name)
        print('Shirt type', self.type)
        print("Shirt Price",self.price)
        print("Size of shirt",self.size)
obj1=Shirt(2,'Jacket','Casual',2000,'Medium')        
obj1.ShowShirts()
print('########################################')
obj2=Shirt()
obj2.ShowShirts()
