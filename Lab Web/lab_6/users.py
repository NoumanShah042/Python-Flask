class User:
    def __init__(self, name, email, gender, password):
        self.name = name
        self.email = email
        self.gender = gender.capitalize()
        self.password = password



usr = User("Nouman", "Nouman@gmail.com", "female", "paasshdhd")
# usr.display()
# print(usr.data_validation()[0])
