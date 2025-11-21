import csv
import os
from colorama import Fore, init
from prettytable import PrettyTable
from billing import Billing

init(autoreset=True)

class BillingSystem:
    def __init__(self):
        # Store all bills in core_python\Project\data\bills.csv
        self.filename = os.path.join("core_python", "Project", "data", "bills.csv")

        # Create file if not exists
        if not os.path.exists(self.filename):
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Bill_ID", "Patient_ID", "Patient_Name", "Doctor_Name",
                    "Room_Charge", "Medicine_Charge", "Test_Charge", "Total"
                ])

    def addBill(self):
        print(Fore.CYAN + "\n🧾 Generate New Bill\n")

        bill_id = input("Enter Bill ID: ").strip()
        patient_id = input("Enter Patient ID: ").strip()
        doctor_id = input("Enter Doctor ID: ").strip()

        # Validate Patient ID from patients.csv
        patient_file = os.path.join("core_python", "Project", "data", "patients.csv")
        patient_found = False
        patient_name = ""

        try:
            with open(patient_file, "r", newline="") as file:
                reader = csv.reader(file)
                next(reader)  # skip header
                for row in reader:
                    # CSV Format: ID,Name,Phone,Age,Disease,Password
                    if row and row[0] == patient_id:
                        patient_found = True
                        patient_name = row[1]  # Name column
                        break
        except FileNotFoundError:
            print(Fore.RED + "❌ ERROR: patients.csv not found!")
            return

        if not patient_found:
            print(Fore.RED + f"❌ Patient ID {patient_id} does NOT exist!")
            input(Fore.YELLOW + "Press Enter to return...")
            return

        # Validate Doctor ID from doctors.csv
        doctor_file = os.path.join("core_python", "Project", "data", "doctors.csv")
        doctor_found = False
        doctor_name = ""

        try:
            with open(doctor_file, "r", newline="") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    # CSV Format: ID,Name,Specialization,Phone,Fee
                    if row and row[0] == doctor_id:
                        doctor_found = True
                        doctor_name = row[1]  # Name column
                        break
        except FileNotFoundError:
            print(Fore.RED + "❌ ERROR: doctors.csv not found!")
            return

        if not doctor_found:
            print(Fore.RED + f"❌ Doctor ID {doctor_id} does NOT exist!")
            input(Fore.YELLOW + "Press Enter to return...")
            return
        
        print(Fore.GREEN + f"\n✔ Patient Found: {patient_name}")
        print(Fore.GREEN + f"✔ Doctor Found:  {doctor_name}")

        try:
            room_charge = float(input("Enter Room Charge: "))
            medicine_charge = float(input("Enter Medicine Charge: "))
            test_charge = float(input("Enter Test Charge: "))

            bill = Billing(
                bill_id, patient_id, patient_name,
                doctor_name, room_charge, medicine_charge, test_charge
            )

            # Write bill to bills.csv
            with open(self.filename, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    bill.bill_id, bill.patient_id, bill.patient_name,
                    bill.doctor_name, bill.room_charge, bill.medicine_charge,
                    bill.test_charge, bill.total
                ])

            print(Fore.GREEN + f"\n✅ Bill generated successfully for {bill.patient_name}!")
            print(Fore.YELLOW + f"💰 Total Amount: ₹{bill.total:.2f}")

        except ValueError:
            print(Fore.RED + "❌ ERROR: Enter only numeric values for charges!")

        input(Fore.YELLOW + "\nPress Enter to return to menu...")


    def showAllBills(self):
        print(Fore.CYAN + "\n📋 All Billing Records\n")
        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.reader(file)
                header = next(reader, None)
                data = list(reader)

                if data:
                    table = PrettyTable(header)
                    for row in data:
                        if not row or len(row) != len(header):
                            continue
                        table.add_row(row)
                    print(table)
                else:
                    print(Fore.RED + "⚠️ No bills found.")
        except FileNotFoundError:
            print(Fore.RED + "⚠️ Billing file not found.")

        input(Fore.YELLOW + "\nPress Enter to return to menu...")

    def menu(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(Fore.MAGENTA + "\n💰 HOSPITAL BILLING SYSTEM MENU 💰")
            print(Fore.YELLOW + """
1. Generate New Bill
2. Show All Bills
3. Exit
""")
            choice = input(Fore.CYAN + "Enter your choice: ").strip()

            if choice == "1":
                self.addBill()
            elif choice == "2":
                self.showAllBills()
            elif choice == "3":
                print(Fore.GREEN + "✅ Exiting Billing System... Goodbye!")
                break
            else:
                print(Fore.RED + "⚠️ Invalid choice, please try again.")
                input("Press Enter...")
               
if __name__ == "__main__":
    from colorama import Fore, init
    init(autoreset=True)

    b1 = BillingSystem()
    b1.menu()
                
                
