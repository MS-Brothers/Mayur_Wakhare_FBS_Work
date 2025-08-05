#A man goes for shopping. He buys 5 products. Accept the price of all products and display the total bill after adding 18% GST

product_1 = float(input('Enter the price of product 1 : '))
product_2 = float(input('Enter the price of product 2 : '))
product_3 = float(input('Enter the price of product 3 : '))
product_4 = float(input('Enter the price of product 5 : '))
product_5 = float(input('Enter the price of product 6 : '))

total_price = product_1+product_2+product_3+product_4+product_5

gst = total_price * 0.18
total_bill = gst + total_price

print(f'Total Bill with GST is {total_bill}')



