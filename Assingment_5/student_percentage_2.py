#Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and average percentage of students
n=int(input('Enter the number of student : '))
total_per=0
for i in range(1,n+1):
    total=0
    for j in range(1,6):
        marks=float(input(f'Enter the {j} subject marks : '))
        total+=marks
    per=total/5   #use for 1 subject percentage
    total_per+=per
    print(f'Percentage of student {i} : {per}%')
    
    
average=total_per/n
print(f'Average percentage of all students : {average}%')    


    
