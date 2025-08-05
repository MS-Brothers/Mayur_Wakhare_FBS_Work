#Write a program to calculate the total cost of painting. The interior of building with four equal sized walls.

Height = float(input('Enter the height of wall : '))
Width = float(input('Enter the width of wall : '))

cost = float(input('Enter the cost of wall per square meter : '))

area = 4 * Height * Width
total_cost = area * cost

print(f'You have this area {area} and your Total cost is {total_cost}')