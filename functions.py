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

def view_progress():
    """
    Display a summary of the user's progress for the day.
    - Calculate the total workout time and total calories.
    - Print motivational feedback.
    """
    pass


def reset_progress():
    """
    Clear all data from the workouts and calories lists.
    - Print a confirmation message.
    """
    pass


def set_daily_goals(workout_minutes, calorie_limit):
    """
    Set daily goals for workout time and calorie intake.
    - Update the global variables workout_goal and calorie_goal.
    - Print a confirmation message.
    """
    pass


def encouragement_system():
    """
    Provide motivational feedback based on progress and goals.
    - Compare current totals to the daily goals.
    - Print encouragement messages.
    """
    pass

