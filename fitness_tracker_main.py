# Personal Fitness Tracker System 🏋️‍♂️
from os import system # For pausing and clearing terminal
import before_starting # The work of the program before the main body (asking for personal information)
import functions # Functions for the choices from the main menu

# Executing the start of the program and clearing the terminal
before_starting.before_starting()
system("pause")
system("cls")

# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily goals
workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal

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
            # Prompt for workout type and duration
            pass
        elif choice == '2':
            # Prompt for calories consumed
            pass
        elif choice == '3':
            # Call view_progress function
            pass
        elif choice == '4':
            # Call reset_progress function
            pass
        elif choice == '5':
            # Prompt for daily goals
            pass
        elif choice == '6':
            # Print a goodbye message and break the loop
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()