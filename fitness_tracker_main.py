# Personal Fitness Tracker System 🏋️‍♂️
import before_starting # The work of the program before the main body (asking for personal information)
import functions # Functions for the choices from the main menu
import file_work # Working with the file functions

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
    global workout_goal, calorie_goal, goals_set
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
            functions.log_workout() # Prompt for workout type and duration
            functions.clear_screen()

        elif choice == '2':
            functions.log_calorie_intake() # Prompt for calories consumed
            functions.clear_screen()

        elif choice == '3':
            functions.view_progress(workout_goal, calorie_goal, goals_set) # Call view_progress function
            functions.clear_screen()

        elif choice == '4':
            functions.reset_progress() # Call reset_progress function
            functions.clear_screen()

        elif choice == '5':
            workout_goal, calorie_goal = functions.set_daily_goals() # Prompt for daily goals
            goals_set = True
            functions.clear_screen()

        elif choice == '6':
            # Print a goodbye message and break the loop
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break
        else:
            print("Invalid choice, please try again.")
            functions.clear_screen()


if __name__ == "__main__":
    # Executing the start of the program and clearing the terminal
    if file_work.is_first_time():
        before_starting.before_starting()
        functions.clear_screen()

    # Executing the main program
    main()