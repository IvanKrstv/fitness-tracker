# Personal Fitness Tracker System 🏋️‍♂️
import before_starting # The work of the program before the main body (asking for personal information)
import functions # Functions for the choices from the main menu
import file_work # Working with the file functions

user_age = 0
user_weight = 0
user_height = 0
user_gender = None

# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily workout goal in minutes and calorie intake goal
workout_goal = 0
calorie_goal = 0
goals_set = False # Check if goals for the day are set

def main():
    """
    Main function to interact with the user.
    """
    global workouts, calories, workout_goal, calorie_goal, goals_set
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
        print()

        if choice == '1':
            functions.log_workout(workouts) # Prompt for workout type and duration
            print(workouts)

        elif choice == '2':
            functions.log_calorie_intake(calories) # Prompt for calories consumed
            print(calories)

        elif choice == '3':
            functions.view_progress(workouts, calories, workout_goal, calorie_goal, goals_set) # Call view_progress function

        elif choice == '4':
            functions.reset_progress(calories_list=calories, workouts_list=workouts) # Call reset_progress function

        elif choice == '5':
            workout_goal, calorie_goal = functions.set_daily_goals() # Prompt for daily goals
            goals_set = True

        elif choice == '6':
            # Print a goodbye message and break the loop
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break
        else:
            print("Invalid choice, please try again.")

        functions.clear_screen()


if __name__ == "__main__":
    try:
        # Executing the start of the program and clearing the terminal
        if file_work.is_first_time():
            before_starting.before_starting() # Function for the first time menu

            # Assigning user's data
            user_age = before_starting.user_age
            user_weight = before_starting.user_weight
            user_height = before_starting.user_height
            user_gender = before_starting.user_gender

            functions.clear_screen() # Clearing the screen to continue with the main program
        else:
            user_age, user_weight, user_height, user_gender, workout_goal, calorie_goal, goals_set = file_work.file_read() # If the program is not opened for a first time, read user's data from a file
        # Executing the main program
        main()

    finally:
        file_work.file_write(user_age, user_weight, user_height, user_gender, workout_goal, calorie_goal, workouts, calories) # Saving the data to a file when the file is closed