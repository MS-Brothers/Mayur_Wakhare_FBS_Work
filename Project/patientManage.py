import csv
import os
from colorama import Fore, Style, init
from patient_1 import Patient_1

init(autoreset=True)

class PatientManagement:
    def __init__(self):
        pass

    def clear(self):
        '''Clear the terminal screen'''
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):
        ch = ''
        d1 = Patient_1()   # ✅ Initialize once outside the loop
        while ch != '5':
            self.clear()
            print(Fore.CYAN + '''
===============================
   🏥 Patient Management Menu
===============================
1] Add Patient
2] Update Patient
3] Delete Patient
4] Show All Patient
5] Back to Main Menu
''')
            ch = input(Fore.YELLOW + "👉 Enter your choice: ")

            if ch == '1':
                d1.addPatient()
            elif ch == '2':
                d1.updatePatient()
            elif ch == '3':
                d1.deletePatient()
            elif ch == '4':
                d1.showallPatient()  # ✅ Now output will stay until you press Enter
            elif ch == '5':
                print(Fore.RED + "🔙 Returning to Main Menu...")
            else:
                print(Fore.RED + "❌ Invalid Choice!")
                input("Press Enter to continue...")

if __name__ == '__main__':
    d2 = PatientManagement()
    d2.menu()
                    