class Patient:
    def __init__(self,id,age,disease,name,phoneNo):
        self.id=id
        self.name=name
        self.phone=phoneNo
        self.age=age
        self.disease=disease
      
    def __str__(self):
        return f'{self.id}, {self.name}, {self.phone}, {self.age}, {self.disease}' 
    
    
if __name__=='__main__':
    d1=Patient(100,21,'Diarrhea','Sandhya',9359469951)
    print(d1)       