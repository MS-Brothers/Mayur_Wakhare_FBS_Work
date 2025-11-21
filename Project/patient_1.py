import csv
import bcrypt
import os
from colorama import Fore, Style, init
from prettytable import PrettyTable

# init(autoreset=True)

class Patient_1:
    def __init__(self):
        # Store all patient data inside data/patients.csv
        self.filename = os.path.join("core_python", "Project", "data", "patients.csv")

        # Create file with header if not exists
        if not os.path.exists(self.filename):
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Phone", "Age", "Disease", "Password"])

    def is_id_unique(self, patient_id):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # skip header
                for row in reader:
                    if row and row[0] == patient_id:
                        return False
        except FileNotFoundError:
            pass
        return True

    def addPatient(self):
        print(Fore.CYAN + "\n🧾 Add New Patient Details\n")
        try:
            while True:
                patient_id = input("Enter Patient ID: ").strip()
                if self.is_id_unique(patient_id):
                    break
                else:
                    print(Fore.RED + f"❌ Patient ID {patient_id} already exists. Please enter a different ID.")

            name = input("Enter Patient Name: ").strip()

            # Phone validation
            while True:
                phone = input("Enter Phone Number (+91 allowed): ").strip()
                if phone.startswith("+91"):
                    if len(phone) == 13 and phone[1:].isdigit():
                        break
                    else:
                        print(Fore.RED + "❌ Invalid '+91' number. It must have 10 digits after +91.")
                elif phone.isdigit() and len(phone) == 10:
                    break
                else:
                    print(Fore.RED + "❌ Invalid phone number. Please enter a 10-digit number.")

            # Age validation
            while True:
                try:
                    age = int(input("Enter Patient Age: "))
                    if 0 < age < 150:
                        break
                    else:
                        print(Fore.RED + "❌ Invalid age. Please enter a valid age (1–149).")
                except ValueError:
                    print(Fore.RED + "❌ Please enter a numeric value for age.")

            disease = input("Enter Disease: ").strip()

            # ✅ Encrypt default password using bcrypt
            default_password = "1234"
            hashed_password = bcrypt.hashpw(default_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            # Save to CSV
            with open(self.filename, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([patient_id, name, phone, age, disease, hashed_password])

            print(Fore.GREEN + f"\n✅ Patient '{name}' added successfully!")
            print(Fore.YELLOW + f"🔐 Default password (encrypted) stored in CSV.")

        except Exception as e:
            print(Fore.RED + f"❌ Error adding patient: {e}")

        input(Fore.YELLOW + "\nPress Enter to return to menu...")
    def updatePatient(self):
        print(Fore.CYAN + '\n🩹 Update Patient Details')
        try:
            pati_id = input('Enter the Patient ID to update: ').strip()
            updated = False
            patients = []

            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    if row[0] == pati_id:  # If ID matches
                        updated = True
                        print(Fore.YELLOW + f'\nCurrent Details:\nID: {row[0]} | Name: {row[1]} | Phone: {row[2]} | Age: {row[3]} | Disease: {row[4]}')

                        print(Fore.CYAN + '\nEnter New Details (Press Enter to keep old values):')

                        new_name = input(f'New Name [{row[1]}]: ').strip() or row[1]

                        # Phone validation
                        while True:
                            new_phone = input(f'New Phone [{row[2]}]: ').strip()
                            if new_phone == "":
                                new_phone = row[2]
                                break
                            if new_phone.startswith("+91"):
                                if len(new_phone) == 13 and new_phone[1:].isdigit():
                                    break
                                else:
                                    print(Fore.RED + 'Invalid "+91" format. Must have "+91" followed by 10 digits.')
                            elif new_phone.isdigit() and len(new_phone) == 10:
                                break
                            else:
                                print(Fore.RED + 'Invalid phone number. Try again.')

                        # Age validation
                        while True:
                            new_age = input(f'New Age [{row[3]}]: ').strip()
                            if new_age == "":
                                new_age = row[3]
                                break
                            if new_age.isdigit() and 0 < int(new_age) <= 150:
                                break
                            else:
                                print(Fore.RED + 'Invalid age. Please enter a valid age.')

                        new_disease = input(f'New Disease [{row[4]}]: ').strip() or row[4]

                        # Keep same password (index 5)
                        new_password = row[5] if len(row) > 5 else "1234"

                        row = [row[0], new_name, new_phone, new_age, new_disease, new_password]

                    patients.append(row)

            if updated:
                with open(self.filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["ID", "Name", "Phone", "Age", "Disease", "Password"])
                    writer.writerows(patients)
                print(Fore.GREEN + f'\n✅ Patient ID {pati_id} updated successfully!')
            else:
                print(Fore.RED + f'❌ No patient found with ID {pati_id}')

        except Exception as e:
            print(Fore.RED + f'❌ Error while updating patient: {e}')
            input('Press Enter to continue...')

    def deletePatient(self):
        print(Fore.RED + '\n🗑️  Delete Patient Record')
        try:
            patient_id = input('Enter the Patient ID: ').strip()
            deleted = False
            patients = []

            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    if row[0] == patient_id:
                        deleted = True
                        print(Fore.YELLOW + f'\nAre you sure you want to delete "{row[1]}"?')
                        confirm = input(Fore.GREEN + 'Type "yes" to confirm: ').lower()
                        if confirm == 'yes':
                            print(Fore.RED + f'🗑️  Patient "{row[1]}" deleted successfully.')
                            continue
                        else:
                            print(Fore.YELLOW + "Deletion cancelled.")
                            patients.append(row)
                    else:
                        patients.append(row)

            if deleted:
                with open(self.filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["ID", "Name", "Phone", "Age", "Disease", "Password"])
                    writer.writerows(patients)
            else:
                print(Fore.RED + f'❌ Patient with ID {patient_id} not found.')

            input(Fore.YELLOW + 'Press Enter to continue...')

        except Exception as e:
            print(Fore.RED + f'❌ Error while deleting patient: {e}')
            input('Press Enter to continue...')

    def showallPatient(self):
        print(Fore.YELLOW + "\n📋 All Registered Patients:\n")
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                header = next(reader, None)
                data = list(reader)

                if data:
                    table = PrettyTable(["ID", "Name", "Phone", "Age", "Disease", "Password"])
                    for row in data:
                        table.add_row(row)
                    print(Fore.CYAN + str(table))
                else:
                    print(Fore.RED + "⚠️ No patient records found yet.")

        except FileNotFoundError:
            print(Fore.RED + "⚠️ Patient file not found.")

        input(Fore.YELLOW + "\nPress Enter to return to menu...")
