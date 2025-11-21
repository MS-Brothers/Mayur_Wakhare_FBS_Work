import csv
import os
from doctor import Doctor
from colorama import Fore, Style, init
from prettytable import PrettyTable

class Doctor_1:
    def __init__(self):
        self.filename = os.path.join(os.path.dirname(__file__), "data", "doctors.csv")

        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Degree", "Specialization", "Phone", "Fee"])

    def is_id_unique(self, doctor_id):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if row[0] == doctor_id:
                        return False
        except FileNotFoundError:
            pass
        return True

    def addDoctor(self):
        print(Fore.CYAN + "\n🩺 Add New Doctor Details")
        try:
            # ---- ID Validation ----
            while True:
                id = input("Enter the Doctor ID: ").strip()
                if self.is_id_unique(id):
                    break
                else:
                    print(Fore.RED + f"Doctor ID {id} already exists. Please use a different ID.")

            # ---- Name Validation ----
            while True:
                name = input("Enter the Doctor Name: ").strip()
                valid = True
                for ch in name:
                    if not (ch.isalpha() or ch == ' ' or ch == '.'):
                        valid = False
                        break
                if valid:
                    break
                else:
                    print(Fore.RED + "Invalid Name. Only alphabets, spaces, and '.' allowed.")

            # ---- NEW FIELD: Degree ----
            degree = input("Enter Degree (MBBS / MD / MS / etc.): ").strip()

            # ---- Specialization ----
            spec = input("Enter Specialization: ").strip()

            # ---- Phone Validation ----
            while True:
                phone = input("Enter Phone Number: ").strip()
                if phone.startswith("+91"):
                    if len(phone) == 13 and phone[1:].isdigit():
                        break
                    else:
                        print(Fore.RED + "Invalid '+91' format! Must have +91 + 10 digits.")
                elif phone.isdigit() and len(phone) == 10:
                    break
                else:
                    print(Fore.RED + "Invalid phone number! Enter 10-digit number.")

            # ---- Fee ----
            while True:
                fee = input("Enter Consultation Fee: ").strip()
                if fee.isdigit():
                    break
                else:
                    print(Fore.RED + "Invalid fee. Enter numeric value only.")

            # Doctor object
            doctor = Doctor(id, name, degree, spec, phone, fee)

            # Write to CSV
            with open(self.filename, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([doctor.id, doctor.name, doctor.degree, doctor.spec, doctor.phone, doctor.fee])

            print(Fore.GREEN + f"\n✅ Doctor '{name}' added successfully!")
            input(Fore.YELLOW + "Press Enter to continue...")

        except Exception as e:
            print(Fore.RED + f"❌ Error while adding doctor: {e}")
            input("Press Enter to continue...")

    def updateDoctors(self):
        print(Fore.CYAN + "\n🛠 Update Doctor Details")

        try:
            doc_id = input("Enter Doctor ID to update: ").strip()
            updated = False
            doctors = []

            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    if row[0] == doc_id:
                        updated = True

                        print(Fore.YELLOW + f"\n📋 Current Details:")
                        print(f"ID: {row[0]} | Name: {row[1]} | Degree: {row[2]} | Spec: {row[3]} | Phone: {row[4]} | Fee: {row[5]}")

                        print(Fore.CYAN + "\nEnter new details (press Enter to keep old value):")

                        new_name = input(f"New Name [{row[1]}]: ").strip() or row[1]
                        new_degree = input(f"New Degree [{row[2]}]: ").strip() or row[2]
                        new_spec = input(f"New Specialization [{row[3]}]: ").strip() or row[3]

                        # Phone validation
                        while True:
                            new_phone = input(f"New Phone [{row[4]}]: ").strip()
                            if new_phone == "":
                                new_phone = row[4]
                                break
                            if new_phone.startswith("+91"):
                                if len(new_phone) == 13 and new_phone[1:].isdigit():
                                    break
                                else:
                                    print(Fore.RED + "⚠️ Invalid '+91' format!")
                            elif new_phone.isdigit() and len(new_phone) == 10:
                                break
                            else:
                                print(Fore.RED + "⚠️ Invalid phone number!")

                        new_fee = input(f"New Fee [{row[5]}]: ").strip() or row[5]

                        doctors.append([row[0], new_name, new_degree, new_spec, new_phone, new_fee])
                        print(Fore.GREEN + "\n✅ Doctor details updated successfully!\n")

                    else:
                        doctors.append(row)

            if updated:
                with open(self.filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["ID", "Name", "Degree", "Specialization", "Phone", "Fee"])
                    writer.writerows(doctors)
            else:
                print(Fore.RED + f"⚠️ Doctor with ID {doc_id} not found!")

            input(Fore.YELLOW + "Press Enter to continue...")

        except Exception as e:
            print(Fore.RED + f"❌ Error while updating doctor: {e}")
            input("Press Enter to continue...")

    def deleteDoctor(self):
        print(Fore.RED + "\n🗑 Delete Doctor Record")

        try:
            doc_id = input("Enter the Doctor ID: ").strip()
            deleted = False
            doctors = []

            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                header = next(reader)

                for row in reader:
                    if row[0] == doc_id:
                        deleted = True
                        print(Fore.YELLOW + f'\nAre you sure you want to delete "{row[1]}"?')
                        confirm = input(Fore.GREEN + 'Type "yes" to confirm: ').lower()

                        if confirm == 'yes':
                            print(Fore.RED + f'Doctor "{row[1]}" deleted successfully.')
                            continue
                        else:
                            print(Fore.YELLOW + "Deletion cancelled.")
                            doctors.append(row)
                    else:
                        doctors.append(row)

            if deleted:
                with open(self.filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["ID", "Name", "Degree", "Specialization", "Phone", "Fee"])
                    writer.writerows(doctors)
            else:
                print(Fore.RED + f"Doctor with ID {doc_id} not found!")

            input(Fore.YELLOW + "Press Enter to continue...")

        except Exception as e:
            print(Fore.RED + f"Error while deleting doctor: {e}")
            input("Press Enter to continue...")

    def showallDoctor(self):
        print(Fore.YELLOW + "\n📋 All Registered Doctors:\n")

        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                data = list(reader)

                if data:
                    table = PrettyTable(["ID", "Name", "Degree", "Specialization", "Phone", "Fee"])
                    for row in data:
                        table.add_row(row)
                    print(Fore.CYAN + str(table))
                else:
                    print(Fore.RED + "⚠️ No doctor records found yet.")

        except FileNotFoundError:
            print(Fore.RED + "⚠️ Doctor file not found!")

        input(Fore.YELLOW + "\nPress Enter to return to menu...")
