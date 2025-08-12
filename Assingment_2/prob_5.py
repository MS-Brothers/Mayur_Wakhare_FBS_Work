#WAP to calculate selling price of book based on cost price and discount.
cost_price = int(input('Enter the Cost Price : '))
Discount = int(input('Enter the Discount : '))
sell_price = cost_price + (Discount/100)
print(f'Selling Price is : {sell_price}')