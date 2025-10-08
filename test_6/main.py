class Vehicles():
    def __init__(self,basic,extra):
        self.basic=basic
        self.extra=extra



class TwoWheelers(Vehicles):
    def __init__(self, basic, extra=0):
        super().__init__(basic, extra)
    def calculate(self):
        
        person=int(input("Enter the number of persons: "))
        if person>2:
            Total_toll=self.basic+(person*(self.extra))
            
        else:
            Total_toll=self.basic

        return Total_toll
class ThreeWheelers(Vehicles):
    def __init__(self, basic, extra):
        super().__init__(basic, extra)
    def calculate(self):
        person=int(input('Enter the number of person : '))
        if person>3:
            Total_toll=self.basic+(person*(self.extra))
        else:
            Total_toll=self.basic
        return Total_toll 
class FourWheelers(Vehicles):
    def __init__(self, basic, extra):
        super().__init__(basic, extra)
    def calculate(self):
        person=int(input('Enter the number of person : '))
        if person>4:
            Total_toll=self.basic+(person*(self.extra))
        else:
            Total_toll=self.basic
        return Total_toll 
class Heavy(Vehicles):
    def __init__(self, basic, extra):
        super().__init__(basic, extra)
    def calculate(self):
        person=int(input('Enter the number of person : '))
        if person>6:
            Total_toll=self.basic+(person*(self.extra))
        else:
            Total_toll=self.basic
        return Total_toll 
print(''' 
         Which type of Vehicles you have : 
         1]Two Wheelers
         2]Three Wheelers
         3]Four Wheelers
         4]Heavy Veheicle
         5]Exit''')    
choice=input('Enter the Choice :')

while choice>'0':
 
    if choice=='1':
        print('Two Wheelers :')
        t1=TwoWheelers(20,10)    
        print(t1.calculate())
        break 
    elif choice=='2':
        print('Three Wheelers :')
        th1=ThreeWheelers(30,20)
        print(th1.calculate()) 
        break 
    elif choice=='3':
        print('Four Wheelers:')
        f1=FourWheelers(40,40)
        print(f1.calculate()) 
        break  
    elif choice=='4':
        print('Heavy Veheicle :')
        h1=Heavy(60,100)
        print(h1.calculate())  
        break 
    elif choice=='5':
        break    



            

  

        
        