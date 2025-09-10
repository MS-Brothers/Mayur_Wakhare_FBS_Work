
# Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook
class Product:
    def __init__(self,pid=1,pname='guest',price=90,quantity=1):
        self.id=pid
        self.name=pname
        self.price=price
        self.qua  = quantity
    def __del__(self):
        print('Destructor is Called')
    def Showproduct(self):
        print("Product id",self.id)        
        print("Product Name",self.name)
        print("Product Price",self.price)
        print("Quantity of product",self.qua)
obj1=Product(12,'Headset',2000,1)        
obj1.Showproduct()
