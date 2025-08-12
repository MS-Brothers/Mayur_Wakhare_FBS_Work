# Calculate the total salary of emp according to da(10%) ta(12%) hra(15%) of basic salary
basic_sal = int(input('Enter your basic salary :'))
da_sal=basic_sal *(10/100)
ta_sal=basic_sal*(12/100)
hra_sal=basic_sal*(15/100)

print(f'The total salary of the employee is {basic_sal+da_sal+ta_sal+hra_sal}')

