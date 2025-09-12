#Python Program to Check if a Given Key Exists in a Dictionary or Not
def di(key,dict):
    for i in dict:
        if key in dict:
            return "Key Exists in a Dictionary"
        else:
            return "Key not exixts not in Dictionary"
dict={1:'BMW',2:'Mustang GT',3:'Mercedes',4:'Audi'}
key=int(input('Enter the Key : '))
res=di(key,dict)
print(res)        