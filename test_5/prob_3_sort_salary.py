# A list contains sublist with emp information as follows 
# Data = [[101."Seema",45000],[340,"Rajani",13000],[210,"Tannu",14000],[320,'Suresh',35000]]
#write a program to sort the list bansed on the salary

li=[[101,"Seema",45000],[340,"Rajani",13000],[210,"Tannu",14000],[320,'Suresh',35000]]
for i in range(len(li)):
    for j in range(len(li)-i-1):
        if(li[j][2]>li[j+1][2]):
            li[j][2],li[j+1][2]=li[j+1][2],li[j][2]
print(li)            










