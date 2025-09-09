# A list contains denominationsas follows 
# D=[2000,500,200,100,50,20,10,5]
# Accept amount from user and calculate how many minimum number of notes will be neede for that amount
li=[2000,500,200,100,50,20,10,5]


amt = int(input('Enter the amount : '))
temp = amt
total_notes=0
for i in li:
    count=temp // i
    if count>0:
        print(f'{i} * {count}')
    total_notes += count
    temp = temp % i
print(total_notes)              







# P_2k= temp // 2000
# temp = temp % 2000

# P_500=temp // 500
# temp = temp % 500

# P_200= temp // 200
# temp = temp % 200

# P_100= temp // 100
# temp = temp % 100

# P_50 = temp // 50
# temp = temp % 50

# P_20 = temp // 20
# temp = temp % 20

# P_10=temp // 10
# temp = temp % 10