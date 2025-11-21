class Doctor:
    def __init__(self,id,name,degree,specialization,phoneNo,consultation_fee):
        self.id=id
        self.name=name
        self.degree=degree
        self.spec=specialization
        self.phone=phoneNo
        self.fee=consultation_fee
      
    def __str__(self):
        return f'{self.id}, {self.name},{self.degree}, {self.spec}, {self.phone}, {self.fee}' 
    
    
if __name__=='__main__':
    d1=Doctor(101,'Dr.Meheta','MBBS','Cardiologist',9359469958,500)
    print(d1)       