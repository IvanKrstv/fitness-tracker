def get_age():
    while True:
        try:
            age = int(input("Your age: "))
            if 1 <= age <= 150:
                break
            else:
                print("Are you sure this is your real age? Try again.")
                continue
        except ValueError:
            print("Invalid age! Please enter a number.")
    return age

def get_weight():
    while True:
        try:
            weight = float(input("Your weight (in kilograms): "))
            if 10 <= weight <= 500:
                break
            else:
                print("Are you sure this is your real weight? Try again.")
                continue
        except ValueError:
            print("Invalid weight! Please enter a number.")
    return weight

def get_height():
    while True:
        try:
            height = float(input("Your height (in centimeters): "))
            if 50 <= height <= 300:
                break
            else:
                print("Are you sure this is your real height? Try again.")
                continue
        except ValueError:
            print("Invalid height! Please enter a number.")
    return height

def get_gender():
    gender = input("Your gender (Male or Female): ").lower()
    while gender not in ["male", "female"]:
        print("No such gender! Try again.")
        gender = input("Your gender (Male or Female): ").lower()
    return gender

def calculate_bmr(age, weight, height, gender):
    bmr = None
    if gender == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == "female":
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return bmr

def check_input(variable, a, b):
    try:
        variable = int(variable)
    except ValueError:
        print("Invalid input! Please enter a number.")
        return False
    if variable not in range(a, b + 1):
        print(f"The number is not in the given range. Please enter a number in the range between {a} and {b}")
        return False
    return True