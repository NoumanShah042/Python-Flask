from  ProjectClasses import BankAccount

acc= BankAccount("001378699","Aisha","Current",500)
acc.printInfo()
print(acc.acctitle)
acc.deposit(1000)
acc.printInfo()
print(acc.bankname)
acc.bankname="UBL"
print(acc.bankname)
acc2= BankAccount("001378700","Muhammad","Current",10000)
acc2.printInfo()
print(acc2.bankname)
acc2.bankname="MCB"
print(acc2.bankname)
print(acc.bankname)
print(BankAccount.bankname)
#print(acc.accbalance)







'''
try:
    list=[1,2]
    print(list[3])
except IndexError:
    print("Index Error")


file = None
try:
    file = open("Test.txt","w")
    file.write("Hello")
    var=10
    print("Hello"+var)
except TypeError as e:
    print("Type mismatch")
    #raise IndexError
    # raising it as instance by passing some custome message
    raise IndexError("You did something wrong")
finally:
    if file!=None:
        file.close()
    print("I can be printed")

print("I can be printed fsjfhjfh")
'''