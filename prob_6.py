#Write a program to calculate profit or loss.
SP = int(input('Enter the Selling price : '))
CP = int(input('Enter the Cost price : '))

if(SP > CP):
    Pro_fit=SP-CP
    print(f'Profit is there and Profit is {Pro_fit}')
else:
    Lo_ss = CP - SP
    print(f'Loss is there and Loss is {Lo_ss}')    