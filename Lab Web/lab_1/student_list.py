students_list = []


def input_dic():
    print("Enter Student Info:\n")
    dic = {}
    name = input("Name:")
    roll_no = input("Roll No:")
    cgpa = float(input("CGPA:"))
    sem = int(input("Semester:"))
    dic.update({"Name": name})
    dic.update({"CGPA": cgpa})
    dic.update({"Roll No.": roll_no})
    dic.update({"Semester": sem})
    return dic


def display_list():
    for i in students_list:
        for key, value in i.items():
            print(key, ":", value, end="    ")
        print("")


choice = 'y'
while choice == 'y':
    d = input_dic()
    students_list.append(d)
    choice = input("\nEnter Another Record: y/n :").lower()

display_list()

