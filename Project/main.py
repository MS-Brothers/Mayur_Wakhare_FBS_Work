from admin_menu import Admin
from User_Part.usermanagement import patient_menu

ch = 0
while ch != '3':
    print('''
🏥 Welcome to Hospital Management System
Please select your choice:
1️⃣  Admin 
2️⃣  User/Patient
3️⃣  Exit''')
    ch = input('Enter your choice: ')
    
    if ch == '1':
        ad = Admin()
    elif ch == '2':
        ad1=patient_menu()
    elif ch == '3':
        print('Exit Successfully.')
    else:
        print('Invalid Choice...')
