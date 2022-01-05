import math


def add():
    a = float(input("Enter 1st Operand:"))
    b = float(input("Enter 1st Operand:"))
    return a + b


def sub():
    a = float(input("Enter 1st Operand:"))
    b = float(input("Enter 1st Operand:"))
    return a - b


def mul():
    a = float(input("Enter 1st Operand:"))
    b = float(input("Enter 1st Operand:"))
    return a * b


def divide():
    a = float(input("Enter 1st Operand:"))
    b = float(input("Enter 1st Operand:"))
    return a / b


def square():
    a = float(input("Enter Operand:"))
    return a * a


def squareRoot():
    a = float(input("Enter Operand:"))
    return math.sqrt(a)


def factorial():
    a = int(input("Enter Operand:"))
    if a < 0:
        print("Enter Positive Number")
    else:
        return math.factorial(a)


def power_of_10():
    x = float(input("Enter Operand:"))
    return math.pow(10, x)


def x_pow_y():
    x1 = float(input("Enter x:"))
    y = float(input("Enter y:"))
    return math.pow(x1, y)


def log_base_10():
    x = float(input("Enter x:"))
    return math.log10(x)


def natural_log():
    x = float(input("Enter x:"))
    return math.log2(x)


def exponential_constant():
    x = float(input("Enter x to multiply with exponential_constant:"))
    return math.e * x


def pi_constant():
    x = float(input("Enter x to multiply with pi_constant:"))
    return math.pi * x


def degree_to_radian(deg):
    radian = deg * (math.pi / 180)
    return radian


def sin():
    x = float(input("Enter x:"))
    return degree_to_radian(math.sin(x))


def cos():
    x = float(input("Enter x:"))
    return degree_to_radian(math.cos(x))


def tan():
    x = float(input("Enter x:"))
    return degree_to_radian(math.tan(x))


def arc_sin():
    x = float(input("Enter number in the range -1 to 1 :"))
    if (x >= -1) and (x <= 1):
        # return degree_to_radian(math.asin(x))
        return math.asin(x)
    else:
        print("Enter in range -1 to 1")


def arc_cos():
    x = float(input("Enter number in the range -1 to 1 :"))
    if (x >= -1) and (x <= 1):
        # return degree_to_radian(math.asin(x))
        return math.acos(x)
    else:
        print("Enter in range -1 to 1")


def arc_tan():
    x = float(input("Enter x:"))
    return degree_to_radian(math.atan(x))


pr = 1


def calculator():
    global pr
    if pr == 1:
        print("============== Menu ===============")
        print("1. Add", end="            ")
        print("2. Subtract", end="           ")
        print("3. Multiply", end="           ")
        print("4. Divide")
        print("5. Factorial", end="      ")
        print("6. Square", end="             ")
        print("7. Square Root", end="        ")
        print("8. 10^x")
        print("9. x^y", end="            ")
        print("10. log10", end="             ")
        print("11. log2", end="              ")
        print("12. Sin")
        print("13. Cos", end="           ")
        print("14. Tan", end="               ")
        print("15. Arc Sin", end="           ")
        print("16. Arc Cos")
        print("17. Arc Tan", end="       ")
        print("18. e", end="                 ")
        print("19. pi", end="            ")
        pr = pr + 1

    x = int(input("\nSelect Operation:"))
    print("")
    if x == 1:
        print(add())
    elif x == 2:
        print(sub())
    elif x == 3:
        print(mul())
    elif x == 4:
        print(divide())
    elif x == 5:
        print(factorial())
    elif x == 6:
        print(square())
    elif x == 7:
        print(squareRoot())
    elif x == 8:
        print(power_of_10())
    elif x == 9:
        print(x_pow_y())
    elif x == 10:
        print(log_base_10())
    elif x == 11:
        print(natural_log())
    elif x == 12:
        print(sin())
    elif x == 13:
        print(cos())
    elif x == 14:
        print(tan())
    elif x == 15:
        print(arc_sin())
    elif x == 16:
        print(arc_cos())
    elif x == 17:
        print(arc_tan())
    elif x == 18:
        print(exponential_constant())
    elif x == 19:
        print(pi_constant())


choice = 'y'
while choice == 'y':
    calculator()
    choice = input("\nEnter Another Record: y/n :")
    choice = choice.lower()

