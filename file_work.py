import os.path

data_file = "user_data.txt"

def file_write(user_age: int, user_weight: float, user_height: float, user_gender: str, workout_goal: int, calorie_goal: int, workouts: list, calories: list) -> None:
    with open(data_file, "w") as file: # Open the file for writing
        # Write the whole user information
        file.write(f"Age: {user_age}"
                   f"\nWeight: {user_weight}"
                   f"\nHeight: {user_height}"
                   f"\nGender: {user_gender}"
                   f"\nDaily workout goal: {workout_goal}"
                   f"\nDaily calorie intake goal: {calorie_goal}"
                   f"\nWorkouts list: {", ".join(workouts)}"
                   f"\nCalories list: {", ".join(calories)}")

def file_read() -> int and float and float and str and int and int and list and list:
    with open(data_file, "r") as file: # Open the file for reading
        for line_num, line in enumerate(file): # Goes through the file's lines
            line_list = line.split(": ") # Split the line
            element = line_list[1] # Define the value we are working with
            if line_num == 0:
                age = int(element )
            elif line_num == 1:
                weight = float(element)
            elif line_num == 2:
                height = float(element)
            elif line_num == 3:
                gender = element.strip()
            elif line_num == 4:
                work_goal = int(element)
            elif line_num == 5:
                cal_goal = int(element)
            elif line_num == 6:
                #line_list = line_list[1].replace('[', '').replace(']', '').replace("'", '').replace('"', '')
                workouts_list = element.split(", ")
                workouts_list = [int(el) if el.isdigit() else el for el in workouts_list]

            elif line_num == 7:
                #line_list = line_list[1].replace('[', '').replace(']', '').replace("'", '').replace('"', '')
                calories_list = element.split(", ")
                calories_list = list(map(int, calories_list))

    return age, weight, height, gender, work_goal, cal_goal, workouts_list, calories_list

def is_first_time(file_name ="app_first_time.txt"):
    if os.path.exists(file_name): # if the file exists
        return False
    else:
        with open(file_name, "w") as file: # Creates the file
            file.write("Already opened")
        return True

