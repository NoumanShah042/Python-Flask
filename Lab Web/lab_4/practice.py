# def input_roll( ):
#     deg = ['cs', 'se', 'it']
#     sec = ['m', 'a']
#     while True:
#         roll = input("Input Roll:").lower()
#         if len(roll) != 10 or roll[0] != "b":
#             print("10 and b invalid")
#             continue
#         if roll[1:3] not in deg or roll[6] not in sec:
#             print("hell  sec and deg")
#             continue
#         if roll[3] != "f":
#             print("f")
#             continue
#         if not roll[4:6].isnumeric():
#             continue
#         if not roll[-3:].isnumeric():
#             continue
#         return roll
#
#
# print(input_roll())


def input_email( ):
    email1 = input("Email as xxxxx@xxxx.xxx :")
    while (email1.find('@') == -1) or (email1.find('.') == -1) or len(email1[email1.find('.') + 1:])>3:
        email1 = input("input Valid email:")
    return email1


print(input_email())
