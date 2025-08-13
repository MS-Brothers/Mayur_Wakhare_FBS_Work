# Write a program to accept basic salary of n emp. if basic salary is below 20000 da=10% ta=12% hra = 15% otherwise da=15% ta=18% hra=20% based on this calculate the total salary of each emp and also total salary for all emp


emp=int(input('Enter the employee count : '))
a=0
sum=0
for i in range(1,emp+1):
    sal=float(input(f'Enter the basic salary of Employee {i}  : '))
    if(sal<20000):
        da=sal*0.10
        ta=sal*0.12
        hra=sal*0.15
        print(f'Total Salary of {i} Employee is {da+ta+hra+sal}')
        a=da+ta+hra+sal
        sum+=a
    else:
        da=sal*0.15
        ta=sal*0.18
        hra=sal*0.20
        print(f'Total Salary of {i} Employee is {da+ta+hra+sal}')
        a=da+ta+hra+sal
        sum+=a
print(f'Total salary of all employee is {sum}')        