# Personal Fitness Tracker System 🏋️‍♂️
from os import system # For pausing and clearing terminal
from time import sleep
import before_starting # The work of the program before the main body (asking for personal information)
import functions # Functions for the choices from the main menu


# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily goals
workout_goal = calorie_goal = 0  # Daily workout goal in minutes and calorie intake goal
goals_set = False # Check if goals for the day are set

# Assign values for user's personal data
age = before_starting.user_age
weight = before_starting.user_weight
height = before_starting.user_height
gender = before_starting.user_gender

def main():
    """
    Main function to interact with the user.
    """
    print("Welcome to the Personal Fitness Tracker System 🏋️‍♂️\n")

    while True:
        # Display menu options
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("\nEnter your choice: ")

        if choice == '1':
            functions.log_workout() # Prompt for workout type and duration

        elif choice == '2':
            functions.log_calorie_intake() # Prompt for calories consumed

        elif choice == '3':
            functions.view_progress() # Call view_progress function

        elif choice == '4':
            functions.reset_progress() # Call reset_progress function

        elif choice == '5':
            global workout_goal, calorie_goal
            workout_goal, calorie_goal = functions.set_daily_goals() # Prompt for daily goals

        elif choice == '6':
            # Print a goodbye message and break the loop
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break
        else:
            print("Invalid choice, please try again.")
            sleep(2)


if __name__ == "__main__":
    # Executing the start of the program and clearing the terminal
    before_starting.before_starting()
    system("pause")
    system("cls")

    # Executing the main program
    main()