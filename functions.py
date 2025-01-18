def log_workout(workouts):
    """
    Log a workout.
    - Append the workout type and duration to the workouts list.
    - Print a confirmation message.
    """
    workout_type = input("What type of workout did you do?\nType of workout: ")
    duration = float(input("Duration: "))
    workouts.append(workout_type)
    workouts.append(duration)

    hours = int(duration)
    minutes = duration - hours

    if hours > 0:
        final_message = f"Your workout: {workout_type} for {hours} hours and {minutes} minutes has been successfully saved."
    else:
        final_message = f"Your workout: {workout_type} for {minutes} minutes has been successfully saved."
    print(final_message)

def log_calorie_intake(calories):
    """
    Log calorie intake for a meal.
    - Append the calorie amount to the calories list.
    - Print a confirmation message.
    """
    calories_consumed = float(input("How many calories did you have in your meal?\nCalories: "))
    calories.append(calories_consumed)
    final_message = f"You consumed {calories_consumed} in this meal and they have been successfully saved."
    print(final_message)

def calculate_duration(workouts):
    total_hours = 0
    total_minutes = 0
    for element in range(len(workouts)):
        if element % 2 != 0:
            total_hours += int(workouts[element])
            total_minutes += workouts[element] - int(workouts[element])
    total_duration = total_hours * 60 + total_minutes
    return total_duration
def calculate_calories(calories):
    total_calories = 0
    for element in calories:
        total_calories += element
    return total_calories
def view_progress(workouts, calories):
    """
    Display a summary of the user's progress for the day.
    - Calculate the total workout time and total calories.
    - Print motivational feedback.
    """
    total_duration = calculate_duration(workouts)
    total_calories = calculate_calories(calories)
    if total_duration >= 60:
        duration_message = f"Your workout time today was: {total_duration // 60} hours and {total_duration - total_duration // 60 * 60} minutes."
    else:
        duration_message = f"Your workout time today was: {total_duration} minutes."
    calories_message = f"You consumed {total_calories} calories today."
    print(duration_message)
    print(calories_message)
    print("You are doing great! Keep going 💪!")

def reset_progress(workouts, calories):
    """
    Clear all data from the workouts and calories lists.
    - Print a confirmation message.
    """
    workouts.clear()
    calories.clear()
    print("Your progress has been reset.")

def set_daily_goals(workout_time, calorie_limit):
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

def encouragement_system():
    """
    Provide motivational feedback based on progress and goals.
    - Compare current totals to the daily goals.
    - Print encouragement messages.
    """
    pass

