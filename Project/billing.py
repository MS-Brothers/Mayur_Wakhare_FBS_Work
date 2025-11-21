# billing.py
class Billing:
    def __init__(self, bill_id, patient_id, patient_name, doctor_name, room_charge, medicine_charge, test_charge):
        self.bill_id = bill_id
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.room_charge = float(room_charge)
        self.medicine_charge = float(medicine_charge)
        self.test_charge = float(test_charge)
        self.total = self.room_charge + self.medicine_charge + self.test_charge
