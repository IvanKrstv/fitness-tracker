import os.path
from fitness_tracker_main import user_age, user_weight, user_height, user_gender, workout_goal, calorie_goal, workouts, calories

data_file = "user_data.txt"

def file_write():
    with open(data_file, "w") as file:
        file.write(f"Age: {user_age}"
                   f"\nWeight: {user_weight}"
                   f"\nHeight: {user_height}"
                   f"\nGender: {user_gender}"
                   f"\nDaily workout goal: {workout_goal}"
                   f"\nDaily calorie intake goal: {calorie_goal}"
                   f"\nWorkouts list: {workouts}"
                   f"\nCalories list: {calories}")

def file_read():
    with open(data_file, "r") as file:
        for line_num, line in enumerate(file):
            line_list = line.split(": ")
            if line_num == 0:
                age = int(line_list[1])
            elif line_num == 1:
                weight = float(line_list[1])
            elif line_num == 2:
                height = float(line_list[1])
            elif line_num == 3:
                gender = line_list[1].strip()
            elif line_num == 4:
                work_goal = int(line_list[1])
            elif line_num == 5:
                cal_goal = int(line_list[1]) if line_list[1].isdigit() else float(line_list[1])
            elif line_num == 6:
                line_list = line_list[1].replace('[', '').replace(']', '').replace('"', '')
                workouts_list = line_list.split(", ")
                for element in range(1, len(workouts_list), 2):
                    workouts_list[element] = float(workouts_list[element])
            elif line_num == 7:
                line_list = line_list[1].replace('[', '').replace(']', '').replace('"', '')
                calories_list = line_list.split(", ")
                for element in range(len(calories_list)):
                    calories_list[element] = float(calories_list[element])
    return age, weight, height, gender, work_goal, cal_goal, workouts_list, calories_list

def is_first_time(file_name ="app_first_time.txt"):
    if os.path.exists(file_name):
        return False
    else:
        with open(file_name, "w") as file:
            file.write("Already opened")
        return True

