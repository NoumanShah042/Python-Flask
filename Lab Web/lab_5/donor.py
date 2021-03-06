class Donor:
    def __init__(self, name, blood_group, phone, cnic, city):
        self.name = name
        self.blood_group = blood_group
        self.phone = phone
        self.cnic = cnic
        self.city = city

    def check_name(self, name):
        if len(name) <= 0 or len(name) > 20:
            return False
        else:
            return True

    def check_phone(self, phone):
        if len(phone) != 12:
            return False
        elif phone[:2] != '03':
            return False
        elif not phone[:4].isnumeric():
            return False
        elif not phone[5:].isnumeric():
            return False
        elif phone[4] != '-':
            return False
        else:
            return True

    def check_bg(self, bg):
        if bg not in ['A+', 'O+', 'B+', 'AB+', 'A-', 'O-', 'B-', 'AB-']:
            return False
        else:
            return True

    def check_city(self, city):
        if len(city) <= 0 or len(city) > 50:
            return False
        else:
            return True

    def check_cnic(self, cnic):
        if len(cnic) != 15:
            return False
        elif not cnic[:5].isnumeric():
            return False
        elif not cnic[6:13].isnumeric():
            return False
        elif not cnic[-1].isnumeric():
            return False
        elif cnic[5] != '-' or cnic[-2] != '-':
            return False
        else:
            return True

    def data_validation(self):
        if not self.check_name(self.name):
            return False
        if not self.check_bg(self.blood_group):
            return False
        if not self.check_phone(self.phone):
            return False
        if not self.check_cnic(self.cnic):
            return False
        if not self.check_city(self.city):
            return False
        else:
            return True



    def input_record(self):
        name = input("Enter Name :")
        blood_group = input("Enter blood_group :")
        phone = input("Enter Phone :")
        cnic = input("Enter CNIC :")
        city = input("Enter City :")
        print(name, blood_group, phone, cnic, city)

    def search(self):
        print(self.name, self.blood_group, self.phone, self.cnic, self.city)
        return "pass"

# dnr = Donor("Nouman", "AB+", "0342-4556029", "35201-6731026-3", "LHR")
# print(dnr.data_validation())