#Write a program to create three lists of numbers, their squares and cubes
li=[2,3,4,5,6,7,8,9]
squ=[]
cube=[]
for i in li:
    squ.append(i*i)
    cube.append(i**3)
print("Number : ",li)
print("Squares : ",squ)
print("Cubes : ",cube)    