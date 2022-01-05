class Contact:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.mobile = None
        self.phone = None
        self.city = None
        self.email = None
        self.website = None

    def __str__(self):
        return self.first_name + "," + self.last_name + "," + self.mobile \
               + "," + str(self.phone) + "," + self.city + "," + self.email + "," + self.website

    def input_website(self):
        website1 = input("Website as xxxxxxxx.com:")
        while website1[-4:] != ".com":
            website1 = input("Input Valid Website:")
        return website1

    def input_mail(self):
        email1 = input("Email as xxxxx@xxxx.com :")
        while (email1.find('@') == -1) or (email1[-4:] != ".com"):
            email1 = input("input Valid email:")
        return email1



    def input_phone_number(self):
        flag = True
        phone1 = None
        while flag:
            phone1 = input("Input Phone as XXXXXXXXXX (all digits):")
            if phone1.isdigit():
                if len(phone1) == 10:
                    flag = False
        phone1 = int(phone1)
        return phone1


    def input_partial_phone_number(self):
        flag1 = True
        phone1 = None
        while flag:
            phone1 = input("Input Phone as XXXXXXXXXX (all digits):")
            # print(len(phone))
            if phone1.isdigit():
                flag = False
        phone1 = int(phone1)
        return phone1

    def input_mobile_number(self):
        flag = True
        while flag:
            mobile = input("Enter Mobile as XXXX-XXXXXXX:")
            if len(mobile) == 12:
                if mobile[4] == '-':
                    if mobile[:4].isdigit():
                        if mobile[5:].isdigit():
                            flag = False
        return mobile


    def input_partianl_mobile_number(self):
        flag = True
        while flag:
            mobile1 = input("Enter Mobile as XXXX-XXXXXXX:")
            if mobile1.isdigit():
                flag = False

        return mobile1

    def input_contact(self):
        self.first_name = input("First Name :")
        self.last_name = input("Last Name :")

        self.mobile = self.input_mobile_number()
        self.phone = self.input_phone_number()

        self.city = input("City :")

        self.email = self.input_mail()

        self.website = self.input_website()
