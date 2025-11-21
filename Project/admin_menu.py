import getpass
from hospitalManage import HospitalManage
class Admin:
    def __init__(self):
        h1=HospitalManage()
        ch=0
        while ch!='2':
            print('''Please select choice :
                1️⃣  Login
                2️⃣  Exit''')
            ch=input('Enter your choice:')
            if ch=='1':
                un = input("👤 Enter Username: ")
                passw = getpass.getpass("🔑 Enter Password: ")
                if un=='admin' and passw=='1234':
                    print('Logged in successful.')
                    h1.menu()
                else:
                    print('Invalid Credentials...')    
            elif ch=='2':
                print('Thank u for visiting us!!! ')
            else:
                print('Invalid Choice...')

if __name__=='__main__':
    a=Admin()