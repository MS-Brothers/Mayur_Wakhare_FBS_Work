
import csv
import os
from colorama import Fore, Style, init
from doctor_1 import Doctor_1

init(autoreset=True)

class DoctorManagement:
    def __init__(self):
        pass

    def clear(self):
        '''Clear the terminal screen'''
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):
        ch = ''
        d1 = Doctor_1()   # ✅ Initialize once outside the loop
        while ch != '5':
            self.clear()
            print(Fore.CYAN + '''
===============================
   🏥 Doctor Management Menu
===============================
1] Add Doctor
2] Update Doctor
3] Delete Doctor
4] Show All Doctors
5] Back to Main Menu
''')
            ch = input(Fore.YELLOW + "👉 Enter your choice: ")

            if ch == '1':
                d1.addDoctor()
            elif ch == '2':
                d1.updateDoctors()
            elif ch == '3':
                d1.deleteDoctor()
            elif ch == '4':
                d1.showallDoctor()  # ✅ Now output will stay until you press Enter
            elif ch == '5':
                print(Fore.RED + "🔙 Returning to Main Menu...")
            else:
                print(Fore.RED + "❌ Invalid Choice!")
                input("Press Enter to continue...")

if __name__ == '__main__':
    d2 = DoctorManagement()
    d2.menu()
                    