from contact import Contact
import os

contact = Contact()


def exact_search_by_mobile_number():
    try:
        f = open('Addressbook.txt', 'r')
        mob_num = contact.input_mobile_number()
        line = " "
        for line in f:
            record_list = line.split(",")
            if record_list[2] == mob_num:
                print(record_list)

    except IOError as e:
        print(e)
    finally:
        f.close()


def special_search_by_mobile_number():
    try:
        f = open('Addressbook.txt', 'r')
        mob_num = contact.input_partianl_mobile_number()
        for line in f:
            record_list = line.split(",")
            if record_list[2].find(mob_num) != -1:
                print(record_list)
    except IOError as e:
        print(e)
    finally:
        f.close()


def exact_search_by_name():
    try:
        f = open('Addressbook.txt', 'r')
        first_nam = input("First Name :").lower()
        last_nam = input("Last Name :").lower()
        line = " "
        for line in f:
            record_list = line.split(",")
            if (record_list[0].lower() == first_nam) and (record_list[1].lower() == last_nam):
                print(record_list)
    except IOError as e:
        print(e)
    finally:
        f.close()


def special_search_by_name():
    try:
        f = open('Addressbook.txt', 'r')
        first_nam = input("First Name :").lower()
        last_nam = input("Last Name :").lower()
        line = " "
        for line in f:
            record_list = line.split(",")
            if (record_list[0].lower().find(first_nam) != -1) and (record_list[1].lower().find(last_nam) != -1):
                print(record_list)
        f.close()
    except IOError as e:
        print(e)
    finally:
        f.close()


def exact_search_by_city():
    f = open('Addressbook.txt', 'r')
    city = input("city:").lower()
    line = " "
    for line in f:
        record_list = line.split(",")
        if record_list[4].lower() == city:
            print(record_list)
    f.close()


def special_search_by_city():
    try:
        f = open('Addressbook.txt', 'r')
        city = input("city:").lower()
        for line in f:
            record_list = line.split(",")
            if record_list[4].lower().find(city) != -1:
                print(record_list)
    except IOError as e:
        print(e)
    finally:
        f.close()


def exact_search_by_email():
    try:
        f = open('Addressbook.txt', 'r')
        email = contact.input_mail()
        line = " "
        for line in f:
            record_list = line.split(",")
            if record_list[5] == email:
                print(record_list)
    except IOError as e:
        print(e)
    finally:
        f.close()


def special_search_by_email():
    try:
        f = open('Addressbook.txt', 'r')
        email = input("Enter Mail:").lower()
        line = " "
        for line in f:
            record_list = line.split(",")
            if record_list[5].lower().find(email) != -1:
                print(record_list)
    except IOError as e:
        print(e)
    finally:
        f.close()


def exact_search_by_website():
    try:
        f = open('Addressbook.txt', 'r')
        web = contact.input_website()
        line = " "
        for line in f:
            record_list = line.split(",")
            if record_list[6][:-1] == web:  # remove \n at the end of line
                print(record_list)
    except IOError as e:
        print(e)
    finally:
        f.close()


def special_search_by_website():
    try:
        f = open('Addressbook.txt', 'r')
        web = input("Website:").lower()
        line = " "
        for line in f:
            record_list = line.split(",")
            if record_list[6][:-1].lower().find(web) != -1:
                print(record_list)
    except IOError as e:
        print(e)
    finally:
        f.close()


def exact_search_by_phone_number():
    try:
        f = open('Addressbook.txt', 'r')
        phone_num = contact.input_phone_number()
        line = " "
        for line in f:
            record_list = line.split(",")
            if record_list[3] == phone_num:
                print(record_list)
    except IOError as e:
        print(e)
    finally:
        f.close()


def special_search_by_phone_number():
    try:
        f = open('Addressbook.txt', 'r')
        phone_num = str(contact.input_partial_phone_number())
        line = " "
        for line in f:
            record_list = line.split(",")
            if record_list[3].find(phone_num) != -1:
                print(record_list)
    except IOError as e:
        print(e)
    finally:
        f.close()


# Delete contact by name , mobile and phone.


def delete_contact_by_name():
    try:
        f = open('Addressbook.txt', 'r')
        temp = open('temp.txt', 'w')
        count = 1
        first_nam = input("First Name :").lower()
        last_nam = input("Last Name :").lower()
        content = f.readlines()
        for line in content:
            record_list = line.split(",")
            if (count == 1) and (record_list[0].lower() == first_nam) and (record_list[1].lower() == last_nam):
                count = count + 1
                print(line)
            else:
                temp.write(line)
    except IOError as e:
        print(e)
    else:
        f.close()
        temp.close()
        os.remove("Addressbook.txt")
        os.rename('temp.txt', "Addressbook.txt")
    finally:
        f.close()
        temp.close()


def delete_contact_by_phone():
    try:
        f = open('Addressbook.txt', 'r')
        temp = open('temp.txt', 'w')
        count = 1
        phone_num = str(contact.input_phone_number())
        content = f.readlines()
        for line in content:
            # print(line)
            record_list = line.split(",")
            if (count == 1) and (record_list[3] == phone_num):
                print(line)
                count = count + 1
            else:
                temp.write(line)
    except IOError as e:
        print(e)
    else:
        f.close()
        temp.close()
        os.remove("Addressbook.txt")
        os.rename('temp.txt', "Addressbook.txt")
    finally:
        f.close()
        temp.close()


def delete_contact_by_mobile():
    try:
        f = open('Addressbook.txt', 'r')
        temp = open('temp.txt', 'w')
        count = 1
        phone_num = contact.input_mobile_number()
        content = f.readlines()
        for line in content:
            # print(line)
            record_list = line.split(",")
            if (count == 1) and (record_list[2] == phone_num):
                print(line)
                count = count + 1
            else:
                temp.write(line)
    except IOError as e:
        print(e)
    else:
        f.close()
        temp.close()
        os.remove("Addressbook.txt")
        os.rename('temp.txt', "Addressbook.txt")
    finally:
        f.close()
        temp.close()


def delete_all_contact_by_name():
    try:
        f = open('Addressbook.txt', 'r')
        temp = open('temp.txt', 'w')
        first_nam = input("First Name :")
        last_nam = input("Last Name :")
        content = f.readlines()
        for line in content:
            record_list = line.split(",")
            if (record_list[0] != first_nam) and (record_list[1] != last_nam):
                # print(line)
                temp.write(line)
            else:
                print(line)
    except IOError as e:
        print(e)
    else:
        f.close()
        temp.close()
        os.remove("Addressbook.txt")
        os.rename('temp.txt', "Addressbook.txt")
    finally:
        f.close()
        temp.close()


def delete_all_contact_by_mobile():
    try:
        f = open('Addressbook.txt', 'r')
        temp = open('temp.txt', 'w')
        mob_num = contact.input_mobile_number()
        content = f.readlines()
        for line in content:
            # print(line)
            record_list = line.split(",")
            if record_list[2] != mob_num:
                temp.write(line)
            else:
                print(line)
    except IOError as e:
        print(e)
    else:
        f.close()
        temp.close()
        os.remove("Addressbook.txt")
        os.rename('temp.txt', "Addressbook.txt")
    finally:
        f.close()
        temp.close()


def delete_all_contact_by_city():
    try:
        f = open('Addressbook.txt', 'r')
        temp = open('temp.txt', 'w')
        city = input("City :").lower()
        content = f.readlines()
        for line in content:
            # print(line)
            record_list = line.split(",")
            if record_list[4].lower() != city:
                temp.write(line)
            else:
                print(line)
    except IOError as e:
        print(e)
    else:
        f.close()
        temp.close()
        os.remove("Addressbook.txt")
        os.rename('temp.txt', "Addressbook.txt")
    finally:
        f.close()
        temp.close()


def update_contact():
    try:
        f = open('Addressbook.txt', 'r')
        temp = open('temp.txt', 'w')
        first_nam = input("First Name :").lower()
        last_nam = input("Last Name :").lower()
        content = f.readlines()
        count = 1
        for line in content:
            record_list = line.split(",")
            if (record_list[0].lower() == first_nam) and (record_list[1].lower() == last_nam) and count==1:
                print("\nEnter Updated Info of contact:")
                count +=1
                contact.input_contact()
                # print("hello")
                temp.write(contact.__str__() + "\n")
            else:
                temp.write(line)
    except IOError as e:
        print(e)
    else:
        f.close()
        temp.close()
        os.remove("Addressbook.txt")
        os.rename('temp.txt', "Addressbook.txt")
    finally:
        f.close()
        temp.close()


def add_contact():
    try:
        f = open('Addressbook.txt', 'a')
        contact.input_contact()
        record1 = contact.__str__()
        f.write('\n' + record1)
    except IOError as e:
        print(e)
    finally:
        f.close()



while True:
    print("========================================================")
    print("1)Add contact")
    print("2)Exact Search")
    print("3)Special Search")
    print("4)Delete contact")
    print("5)Delete all contacts")
    print("6)Update Contact")
    print("7)Exit")
    print("========================================================")
    choice=0
    try:
        choice = int(input("Enter Choice:"))
    except ValueError:
        print("input a Digit")

    if choice == 1:
        add_contact()
        print("Contact Added Successfully")

    elif choice == 2:
        print("Operation Base:")
        print("1)By Name", end="    ")
        print("2)By Mobile", end="    ")
        print("3)By Phone", end="    ")
        print("4)By City", end="    ")
        print("5)By Email", end="    ")
        print("6)By Website")

        choice1 = int(input("Base of Operation:"))
        print("Output:")
        if choice1 == 1:
            exact_search_by_name()
        elif choice1 == 2:
            exact_search_by_mobile_number()
        elif choice1 == 3:
            exact_search_by_phone_number()
        elif choice1 == 4:
            exact_search_by_city()
        elif choice1 == 5:
            exact_search_by_email()
        elif choice1 == 6:
            exact_search_by_website()
    elif choice == 3:
        print("Operation Base:", end="    ")
        print("1)By Name", end="    ")
        print("2)By Mobile", end="    ")
        print("3)By Phone", end="    ")
        print("4)By City", end="    ")
        print("5)By Email", end="    ")
        print("6)By Website")

        choice1 = int(input("Base of Operation:"))
        print("Output:")
        if choice1 == 1:
            special_search_by_name()
        elif choice1 == 2:
            special_search_by_mobile_number()
        elif choice1 == 3:
            special_search_by_phone_number()
        elif choice1 == 4:
            special_search_by_city()
        elif choice1 == 5:
            special_search_by_email()
        elif choice1 == 6:
            special_search_by_website()
    elif choice == 4:
        print("Delete contact :", end="    ")
        print("1)By Name", end="    ")
        print("2)By Mobile Number", end="    ")
        print("3)By Phone")
        choice1 = int(input("Base of Operation:"))
        print("Output:")
        if choice1 == 1:
            delete_contact_by_name()
        elif choice1 == 2:
            delete_contact_by_mobile()
        elif choice1 == 3:
            delete_contact_by_phone()
        print("Deleted Sccessfully")
    elif choice == 5:
        print("Delete contact All :")
        print("1)By Name", end="    ")
        print("2)By City", end="    ")
        print("3)By Mobile")
        choice1 = int(input("Base of Operation:"))

        if choice1 == 1:
            delete_all_contact_by_name()
        elif choice1 == 2:
            delete_all_contact_by_city()
        elif choice1 == 3:
            delete_all_contact_by_mobile()
        print("Deleted Sccessfully")
    elif choice == 6:
        update_contact()
        print("\nUpdated Successfully")
    elif choice == 7:
        break
    else:
        print("input Valid Choice")

# record = Contact()
# record.input_contact()
# print(record.__str__())
