def check_gender( gender):
    gender = gender.lower()
    if gender != "male" and gender != "female":
        return False
    else:
        return True

print(check_gender("male"))
print(check_gender("female"))
print(check_gender("femggale"))
