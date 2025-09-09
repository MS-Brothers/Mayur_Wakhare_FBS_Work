# There is list with some numbers. Create a new dictionary using the list in such way that key is number and value is frequency of occurances of that number in list
#[1,3,4,1,12,3,6,7,1,2,4]
#{1:3,3:2,2:2,
li=[1,3,4,1,12,3,6,7,1,2,4]
freq={}
for i in li:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)            


