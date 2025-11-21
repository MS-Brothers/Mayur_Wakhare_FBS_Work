from doctormanagement import DoctorManagement
from patientManage import PatientManagement
from billingmanagement import BillingSystem
from colorama import Fore, Style, init
import os
import getpass

# Initialize colorama
init(autoreset=True)

class HospitalManage:

    def __init__(self):
        self.doctor = DoctorManagement()
        self.patient=PatientManagement()
        self.billing=BillingSystem()

    def clear(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):
        ch = ''
        while ch != '4':
            self.clear()
            print(Fore.CYAN + '''
🏥 Welcome Admin!

1️⃣  Doctor Management
2️⃣  Patient Management
3️⃣  Billing System
4️⃣  Exit
''')
            ch = input(Fore.YELLOW + "👉 Enter your choice: ")

            if ch == '1':
                print(Fore.GREEN + "🩺 Welcome to Doctor Management Section.")
                self.doctor.menu()

            elif ch == '2':
                print(Fore.BLUE + "👨‍⚕️ Welcome to Patient Management Section.")
                # input(Fore.MAGENTA + "Press Enter to continue...")
                self.patient.menu()

            elif ch == '3':
                print(Fore.LIGHTYELLOW_EX + "💰 Billing System under development...")
                self.billing.menu()
                input(Fore.MAGENTA + "Press Enter to continue...")

            elif ch == '4':
                # print(Fore.LIGHTCYAN_EX + "📊 Reports Module coming soon...")
                # input(Fore.MAGENTA + "Press Enter to continue...")
                print(Fore.RED + "🚪 Exiting from 🏥 Hospital Management System...")
                break

            # elif ch == '5':
            #     print(Fore.RED + "🚪 Exiting from 🏥 Hospital Management System...")
            #     break

            else:
                print(Fore.RED + "❌ Invalid choice! Please try again.")
                input("Press Enter to continue...")

if __name__ == "__main__":
    h1 = HospitalManage()
    password = getpass.getpass("🔑 Enter Admin Password: ")
    if password == "1234":
        h1.menu()
    else:
        print(Fore.RED + "❌ Incorrect password. Access Denied!")
