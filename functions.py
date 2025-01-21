from fitness_tracker_main import workouts, calories
from os import system

def log_workout():
    """
    Log a workout.
    - Append the workout type and duration to the workouts list.
    - Print a confirmation message.
    """
    workout_type = input("What type of workout did you do?\nType of workout: ")
    duration = float(input("Duration (in minutes): "))
    workouts.append(workout_type)
    workouts.append(duration)

    if duration >= 60:
        final_message = f"Your workout: {workout_type} for {duration // 60} hours and {duration - duration // 60 * 60} minutes has been successfully saved."
    else:
        final_message = f"Your workout: {workout_type} for {duration} minutes has been successfully saved."
    print(final_message)

def log_calorie_intake():
    """
    Log calorie intake for a meal.
    - Append the calorie amount to the calories list.
    - Print a confirmation message.
    """
    calories_consumed = float(input("How many calories did you have in your meal?\nCalories: "))
    calories.append(calories_consumed)
    final_message = f"You consumed {calories_consumed} in this meal and they have been successfully saved."
    print(final_message)

def calculate_duration():
    total_duration = 0
    for element in range(len(workouts)):
        if element % 2 != 0:
            total_duration += workouts[element]
    return total_duration
def calculate_calories():
    total_calories = 0
    for element in calories:
        total_calories += element
    return total_calories
def view_progress(workout_goal, calorie_goal, goals_set):
    """
    Display a summary of the user's progress for the day.
    - Calculate the total workout time and total calories.
    - Print motivational feedback.
    """
    total_duration = calculate_duration()
    total_calories = calculate_calories()
    if total_duration >= 60:
        duration_message = f"\nYour total workout time today is: {total_duration // 60} hours and {total_duration - total_duration // 60 * 60} minutes."
    else:
        duration_message = f"Your total workout time today is: {total_duration} minutes."
    calories_message = f"\nYou have consumed {total_calories} calories today."
    print(duration_message)
    if goals_set:
        print(encouragement_system_workouts(workout_goal))
    print(calories_message)
    if goals_set:
        print(encouragement_system_calories(calorie_goal))

def reset_progress():
    """
    Clear all data from the workouts and calories lists.
    - Print a confirmation message.
    """
    workouts.clear()
    calories.clear()
    print("Your progress has been reset.")

def set_daily_goals():
    """
    Set daily goals for workout time and calorie intake.
    - Update the global variables workout_goal and calorie_goal.
    - Print a confirmation message.
    """
    workout_time = float(input("How many minutes would you like to train today? Minutes: "))
    calorie_limit = float(input("How many calories would you like to consume today? Calories: "))
    print(f"You have set a goal to workout {workout_time} minutes "
          f"and consume {calorie_limit} calories today. We believe you can do it! 💪")
    return workout_time, calorie_limit

def encouragement_system_workouts(workout_goal):
    """
    Provide motivational feedback based on progress and goals.
    - Compare current totals to the daily goals.
    - Print encouragement messages.
    """
    is_workout_met = False # Variable for checking if workout goal is met

    # Check if workout goal was met
    if workout_goal <= calculate_duration():
        is_workout_met = True

    # Writing the message
    if is_workout_met:
        workout_message = (f"Good job!💪 You have met your workout time goal of {workout_goal} minutes as"
                            f"you have trained for {calculate_duration()} minutes today.")
    else:
        workout_message = (f"You still have {workout_goal - calculate_duration()} minutes until "
                           f"you meet your goal of {workout_goal} minutes. Get back to work! 💪")
    print(workout_message)

def encouragement_system_calories(calorie_goal):
    """
    Provide motivational feedback based on progress and goals.
    - Compare current totals to the daily goals.
    - Print encouragement messages.
    """
    is_calorie_met = False # Variable for checking if calorie intake goal is met

    # Check if calorie intake goal was met
    if calorie_goal <= calculate_calories():
        is_calorie_met = True

    # Writing the message
    if is_calorie_met:
        calorie_message = (f"Good job!💪 You have met your calorie intake goal of {calorie_goal} calories as"
                            f"you have consumed {calculate_calories()} calories today.")
    else:
        calorie_message = (f"You still have {calorie_goal - calculate_calories()} calories until "
                           f"you meet your goal of {calorie_goal} calories. It is time to eat more! 😁")

    print(calorie_message)

def clear_screen():
    system("pause")
    system("cls")

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