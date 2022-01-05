class BankAccount:
    bankname = "HBL"

    def __init__(self, accno, acctitle, acctype, accbalance):
        self.accno = accno
        self.acctitle = acctitle
        self.acctype = acctype
        self.__accbalance = accbalance  # private instance data member

    def deposit(self, amount):
        self.__accbalance = self.accbalance + amount

    def withdraw(self, amount):
        if self.__accbalance < amount:
            print("Negative Account")
        else:
            self.__accbalance = self.accbalance - amount

    def printInfo(self):
        print("AccountTitle", self.acctitle)
        print("AccountNo", self.accno)
        print("Account Type", self.acctype)
        print("Account Balance", self.__accbalance)
