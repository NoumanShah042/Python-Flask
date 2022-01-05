def filereader(filename):
    file = None
    try:
        file = open(filename)
        lines = file.readlines()
        for line in lines:
            print(line)
    except IOError as e:
        print("File do not exist please provide valid filename", str(e))
    finally:
        if file != None:
            file.close()


def filereader2(filename):
    file = None
    try:
        file = open(filename)
        # print(file.readlines())
        print(file.read())

        # print("next")
        # for f in file:
        #     print(f, end="")
    except IOError as e:
        print("File do not exist please provide valid filename", str(e))
    finally:
        if file != None:
            file.close()


def filewriter(filename):
    file = open(filename, "a")
    file.write("It is appending")
    lines = ["hello\n", "this\n", "gyftdfdf\n", "hfyegfyefg"]
    file.writelines(lines)
    file.close()


def writeStudentRecord(filename, studentDicRec):
    file = open(filename, 'a')
    lst = studentDicRec.values()
    print(lst)  # **********
    convertionList = []
    for item in lst:
        string_ = str(item)
        convertionList.append(string_)
    print(convertionList)
    string = ','.join(convertionList) + '\n'
    print(string)  # ************
    file.write(string)
    file.close()


def writeStudentRecord2(filename, studentDicRec):
    file = open(filename, "a")
    list = [str(studentDicRec[x]) for x in studentDicRec.keys()]
    # string=','.join(list)
    file.write(','.join(list) + '\n')
    file.close()


# filereader("C:\\Users\\Syed Numan Rehman\\Desktop\\std.txt")
# filereader2("C:\\Users\\Syed Numan Rehman\\Desktop\\temp.txt")

# filewriter("C:\\Users\\Syed Numan Rehman\\Desktop\\temp.txt")

student = {"rollno": "BSCSF18M027", "name": "Nouman", "Semmester": 5, "CGPA": 3.9}
writeStudentRecord("C:\\Users\\Syed Numan Rehman\\Desktop\\std.txt", student)

# writeStudentRecord2("C:\\Users\\sanam\\Desktop\\DemoFile\\StudentsData.txt",student)


# ******************************

# def index_(string):
#     idx = -1
#     try:
#         idx = string.index("m")
#     except ValueError as e:
#         idx = -1
#     return idx
#
#
# print(index_("Hello"))
