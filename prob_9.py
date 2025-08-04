#Input 5 subject marks from user and display grade(eg.First class,Second class ..)
JS=int(input('Enter your JavaScript Subject Marks : '))
py=int(input('Enter your Python Subject Marks : '))
C=int(input('Enter your C Subject Marks : '))
Java=int(input('Enter your Java Subject Marks : '))
Net=int(input('Enter your Net Subject Marks : '))

if(90 <= JS<= 100):
    print(f'JavaScript -> {JS} Marks -> A Grade -> Pass with First Class')
elif(70 <= JS <= 89):
    print(f'JavaScript -> {JS} Marks -> B Grade -> Pass with Second Class')  
elif(35<= JS <= 69):
    print(f'JavaScript -> {JS} Marks -> C Grade -> Pass with Third Class')
else:
    print(f'JavaScript Fail!!')  

if(90 <= py<= 100):
    print(f'Python -> {py} Marks -> A Grade -> Pass With First Class')
elif(70 <= py <= 89):
    print(f'Python -> {py} Marks -> B Grade -> Pass With second Class')  
elif(35<= py <= 69):
    print(f'Python -> {py} Marks -> C Grade -> Pass With Third Class')
else:
    print(f'Python Fail!!') 

if(90 <= C<= 100):
    print(f'C -> {C} Marks -> A Grade -> Pass with First Class')
elif(70 <= C <= 89):
    print(f'C -> {C} Marks -> B Grade -> Pass with Second Class')  
elif(35<= C <= 69):
    print(f'C -> {C} Marks -> C Grade -> Pass with Third Class')
else:
    print(f'C Fail!!')  

if(90 <=Java<= 100):
    print(f'Java -> {Java} Marks -> A Grade -> Pass with First Class')
elif(70 <= Java <= 89):
    print(f'Java -> {Java} Marks -> B Grade -> Pass with Second Class')  
elif(35<= Java <= 69):
    print(f'Java -> {Java} Marks -> C Grade -> Pass with Third Class')
else:
    print(f' Java Fail!!')  

if(90 <= Net<= 100):
    print(f'.Net -> {Net} Marks -> A Grade -> Pass with First Class')
elif(70 <= Net <= 89):
    print(f'Net -> {Net} Marks -> B Grade -> Pass with Second Class')  
elif(35<= Net <= 69):
    print(f'Net -> {Net} Marks -> C Grade -> Pass with Third Class')
else:
    print(f'.Net Fail!!')              
    
               