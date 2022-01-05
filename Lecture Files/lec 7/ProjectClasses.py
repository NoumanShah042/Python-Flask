class NegativeBalanceException(Exception):
    pass


class BankAccount:
    bankname = "HBL"

    def __init__(self, accno, acctitle, acctype, accbalance):
        # self.something = None
        print("This is Bank Account Class")
        self.accno = accno
        self.acctitle = acctitle
        self._acctype = acctype
        self.__accbalance = accbalance  # private instance data member

    def deposit(self, amount):
        self.__accbalance = self.__accbalance + amount

    def withdraw(self, amount):
        if self.__accbalance < amount:
            print("Negative Account")
            raise NegativeBalanceException("You account balance is less than described withdraw amount")
        else:
            self.__accbalance = self.__accbalance - amount

    def __some(self):
        print("something to do")

    def printInfo(self):
        # How we can call private member function
        self.__some()
        print("AccountTitle", self.acctitle)
        print("AccountNo", self.accno)
        print("Account Type", self._acctype)
        print("Account Balance", self.__accbalance)


class ExtendedAccount(BankAccount):
    def __init__(self, accno, acctitle, acctype, accbalance, mineAttribute):
        super().__init__(accno, acctitle, acctype, accbalance)
        self.mineAttribute = mineAttribute
        print("This is extented Account Class")
