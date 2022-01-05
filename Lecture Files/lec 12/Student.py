class Student:
    def __init__(self ,name, rollno ,semmester ,cgpa):
        self.name=name
        self.rollno= rollno
        self.semmester= semmester
        self.cgpa=cgpa

    def display(self):
        print(self.name ,self.rollno,  self.semmester, self.cgpa  )