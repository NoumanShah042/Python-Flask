def check_name(name):
    if len(name) <= 0 or len(name) > 20:
        return False
    else:
        return True


# print(check_name(input("name:")))

def check_phone(phone):
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


# phone = input("Enter Phone :")
# print(check_phone(phone))

# print(len(phone) != 12)
# print(phone[:2] != '03')
# print(not phone[:4].isnumeric())
# print(not phone[5:].isnumeric())
# print(phone[4] != '-')

# print("03424556029".isnumeric())

def check_bg(bg):
    if bg not in ['A+', 'O+', 'B+', 'AB+', 'A-', 'O-', 'B-', 'AB-']:
        return False
    else:
        return True


# blood_group = input("Enter blood_group :")
# print(check_bg(blood_group))


def check_city(city):
    if len(city) <= 0 or len(city) > 50:
        return False
    else:
        return True


# print(check_city(input("city:")))


def check_cnic(cnic):
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


# print(check_cnic(input("cnic:")))
# check_cnic(cnic)

def input_record():
    name = input("Enter Name :")
    blood_group = input("Enter blood_group :")
    phone = input("Enter Phone :")
    cnic = input("Enter CNIC :")
    city = input("Enter City :")
    print(name, blood_group, phone, cnic, city)

input_record()