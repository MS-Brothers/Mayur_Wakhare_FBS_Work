import csv
import os
import bcrypt
from datetime import datetime
from prettytable import PrettyTable

DATA_PATH = "core_python/Project/data"
PATIENT_FILE = os.path.join(DATA_PATH, "patients.csv")
DOCTOR_FILE = os.path.join(DATA_PATH, "doctors.csv")
APPOINTMENT_FILE = os.path.join(DATA_PATH, "appointments.csv")
BILL_FILE = os.path.join(DATA_PATH, "bills.csv")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Patient:
    def __init__(self):
        self.pid = None
        self.pname = None

    # REGISTER 
    def register(self):
        print("\n🩺 Register as New Patient 🩺")

        pid = input("Enter Patient ID: ").strip()
        pname = input("Enter Full Name: ").strip()
        age = input("Enter Age: ").strip()
        disease=input('Enter the Disease:').strip()
        gender = input("Enter Gender (M/F/O): ").strip().upper()
        phone = input("Enter Phone Number: ").strip()
        password = input("Create Password: ").strip()
        

        # Check if patient ID already exists
        if os.path.exists(PATIENT_FILE):
            with open(PATIENT_FILE, "r", newline='') as f:
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    if row and row[0] == pid:
                        print("❌ Patient ID already exists. Please login.")
                        return

        # Encrypt password before saving
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Save data permanently in CSV
        file_exists = os.path.exists(PATIENT_FILE)
        with open(PATIENT_FILE, "a", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["ID", "Name", "Phone", "Age", "Disease", "Password"])
            # writer.writerow([pid, pname, age, gender, phone, hashed_password])
            writer.writerow([pid, pname, phone, age, disease, hashed_password])
            

        print(f"✅ Registration successful! Welcome {pname}. You can now log in securely.")

    #LOGIN
    def login(self):
        print("\n🔐 Patient Login 🔐")
        pid = input("Enter Patient ID: ").strip()
        password = input("Enter Password: ").strip()

        if not os.path.exists(PATIENT_FILE):
            print("❌ No patient data found. Please register first.")
            return False

        with open(PATIENT_FILE, "r", newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                if row and row[0] == pid:
                    stored_hash = row[5]  # Encrypted password column
                    #Verify password using bcrypt
                    if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
                        self.pid = pid
                        self.pname = row[1]
                        print(f"✅ Welcome back, {self.pname}!")
                        return True
                    else:
                        print("❌ Invalid password.")
                        return False

        print("❌ Patient ID not found.")
        return False

    def viewDoctors(self):
        print("\n👨‍⚕️ Available Doctors 👩‍⚕️")

        if not os.path.exists(DOCTOR_FILE):
            print("❌ Doctors data not found.")
            return

        with open(DOCTOR_FILE, "r", newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            table = PrettyTable(["Doctor ID", "Name", "Specialization", "Phone", "Consultation Fee"])
            for row in reader:
                table.add_row([row["ID"], row["Name"], row["Specialization"], row["Phone"], row["Fee"]])
        print(table)

    # BOOK APPOINTMENT 
    def bookAppointment(self):
        print("\n📅 Book Appointment 📅")

        # Ensure patient logged in
        if not self.pid:
            print("❌ Please login first to book an appointment.")
            return

        # Show available doctors
        self.viewDoctors()

        doctor_id = input("\nEnter Doctor ID to book appointment: ").strip()
        appointment_date = input("Enter Appointment Date (DD-MM-YYYY): ").strip()
        appointment_time = input("Enter Appointment Time (Example: 10:30 AM): ").strip()

        # Validate date format
        try:
            appt_date = datetime.strptime(appointment_date, "%d-%m-%Y")
            if appt_date.date() < datetime.now().date():
                print("❌ Appointment date must be today or in the future.")
                return
        except ValueError:
            print("❌ Invalid date format. Use DD-MM-YYYY.")
            return

        # Check if doctor exists
        doctor_found = None
        with open(DOCTOR_FILE, "r", newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader, None)
            for row in reader:
                if row and row[0].strip() == doctor_id:
                    doctor_found = row
                    break

        if not doctor_found:
            print(f"❌ Doctor ID '{doctor_id}' not found.")
            return

        doctor_name = doctor_found[1]
        try:
            consultation_fee = float(doctor_found[4])
        except (IndexError, ValueError):
            consultation_fee = 250.0  # Default fallback

        print(f"\nConsultation Fee: ₹{consultation_fee}")
        confirm = input("\nDo you want to book this appointment? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("❌ Appointment not booked.")
            return

        # Prevent duplicate booking for same doctor, date, and time
        if os.path.exists(APPOINTMENT_FILE):
            with open(APPOINTMENT_FILE, "r", newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    if (row and row[0] == self.pid and row[2] == doctor_id and
                        row[4] == appointment_date and row[5] == appointment_time):
                        print("⚠️ You already have this appointment booked.")
                        return

        # Append to appointment.csv with status = Pending
        file_exists = os.path.exists(APPOINTMENT_FILE)
        with open(APPOINTMENT_FILE, "a", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Patient_ID", "Patient_Name", "Doctor_ID", "Doctor_Name", "Date", "Time", "Status"])
            writer.writerow([self.pid, self.pname, doctor_id, doctor_name, appointment_date, appointment_time, "Pending"])

        print(f"\n✅ Appointment booked successfully with {doctor_name} on {appointment_date} at {appointment_time}.")
        print("🕓 Waiting for admin confirmation...")

    # VIEW APPOINTMENTS 
    def viewAppointments(self):
        print("\n📋 Your Appointments 📋")
        if not os.path.exists(APPOINTMENT_FILE):
            print("❌ No appointments found.")
            return

        with open(APPOINTMENT_FILE, "r", newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            table = PrettyTable(["Patient ID", "Patient Name", "Doctor ID", "Doctor Name", "Date", "Time", "Status"])
            found = False
            for row in reader:
                if row and row[0] == self.pid:
                    table.add_row(row)
                    found = True

        if found:
            print(table)
        else:
            print("❌ No appointments found for your ID.")


# ------------------ PATIENT MENU ------------------
def patient_menu():
    patient = Patient()
    clear_screen()
    while True:
        print('''
🧍‍♀️  PATIENT SECTION 🧍‍♂️
1️⃣  Login
2️⃣  Register as New Patient
3️⃣  Back to Main Menu
''')
        ch = input("Enter your choice: ").strip()
        clear_screen()
        if ch == '1':
            if patient.login():
                while True:
                    print(f'''
Welcome {patient.pname}! Please select an option:
1️⃣  View Doctors
2️⃣  Book Appointment
3️⃣  View Appointments
4️⃣  Logout
''')
                    opt = input("Enter your choice: ").strip()

                    if opt == '1':
                        patient.viewDoctors()
                    elif opt == '2':
                        patient.bookAppointment()
                    elif opt == '3':
                        patient.viewAppointments()
                    elif opt == '4':
                        print("👋 Logged out successfully.")
                        break
                    else:
                        print("❌ Invalid choice. Please try again.")

        elif ch == '2':
            patient.register()

        elif ch == '3':
            print("⬅️ Returning to Main Menu...")
            break

        else:
            print("❌ Invalid choice. Please try again.")


# ------------------ MAIN ------------------
if __name__ == "__main__":
    patient_menu()
