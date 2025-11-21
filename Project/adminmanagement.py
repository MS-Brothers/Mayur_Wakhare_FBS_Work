import csv
import os
from prettytable import PrettyTable

DATA_PATH = "core_python/Project/data"
APPOINTMENT_FILE = os.path.join(DATA_PATH, "appointments.csv")

class Admin:
    def viewAppointments(self):
        if not os.path.exists(APPOINTMENT_FILE):
            print("❌ No appointments found.")
            return

        print("\n📋 All Appointments 📋")
        with open(APPOINTMENT_FILE, "r") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            table = PrettyTable(header)
            rows = list(reader)
            for row in rows:
                table.add_row(row)
        print(table)

    def confirmAppointment(self):
        if not os.path.exists(APPOINTMENT_FILE):
            print("❌ No appointments file found.")
            return

        pid = input("Enter Patient ID to confirm: ").strip()
        did = input("Enter Doctor ID: ").strip()
        date = input("Enter Appointment Date (DD-MM-YYYY): ").strip()

        rows = []
        updated = False

        with open(APPOINTMENT_FILE, "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if row[0] == pid and row[2] == did and row[4] == date:
                    row[6] = "Confirmed"
                    updated = True
                rows.append(row)

        if updated:
            with open(APPOINTMENT_FILE, "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerows(rows)
            print("✅ Appointment confirmed successfully!")
        else:
            print("❌ Appointment not found.")

def admin_menu():
    admin = Admin()
    while True:
        print('''
🧑‍💼 ADMIN MENU 🧑‍💼
1️⃣  View All Appointments
2️⃣  Confirm Appointment
3️⃣  Exit
''')
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            admin.viewAppointments()
        elif choice == '2':
            admin.confirmAppointment()
        elif choice == '3':
            print("👋 Exiting admin panel...")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    admin_menu()
