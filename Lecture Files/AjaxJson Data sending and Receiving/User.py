class User:
    def __init__(self,fname,lname,email,password):
        self.fname=fname
        self.lname=lname
        self.email = email
        self.password =password

    def display(self):
        print("Fname"+self.fname+"Lname:"+self.lname+"Email:"+self.email+"Password:"+self.email)



def Test():
    u = User("Aisha","Khan","aisha@yahoo.com","123")
    u.display()
if __name__ == '__main__':
    Test()
