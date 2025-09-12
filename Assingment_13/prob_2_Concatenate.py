#Python Program to Concatenate Two Dictionaries Into One
# dict1 = {"name": "Mayur"}
# dict2 = {"age": 22, "city": "Pune"}

# result = {**dict1, **dict2}
# print(result)

dict1={1:'Mayur'}
dict2={2:'Wakhare'}
result=dict1
for i in dict2:
    result[i]=dict2[i]
print(result)    