user_age = 0
user_weight = 0
user_height = 0
user_gender = None
daily_calories = 0

def before_starting():
      from time import sleep
      from before_start_functions import get_gender, get_height, get_age, get_weight, check_input, calculate_bmr

      global user_age, user_weight, user_height, user_gender, daily_calories

      print("Welcome to the Personal Fitness Tracker System 🏋️‍♂"
            ""
            "️\n\nWe would like to ask you some questions to get to know you better and improve your experience.")
      sleep(5)
      # Input for age
      user_age = get_age()

      # Input for weight
      user_weight = get_weight()

      # Input for height
      user_height = get_height()

      # Input for gender
      user_gender = get_gender()

      # Asking for physical activity
      print("\nHow would you assess your physical activity?\n"
            "\n1. Sedentary (little to no exercise)"
            "\n2. Lightly active (light exercise or sports 1-3 days/week)"
            "\n3. Moderately active (moderate exercise or sports 3-5 days/week)"
            "\n4. Very active (hard exercise or sports 6-7 days a week)"
            "\n5. Super active (very hard exercise, physical job, or training twice a day)")

      choice = int(input("Enter the number corresponding to your choice: "))
      while not check_input(choice):
            choice = int(input("Enter the number corresponding to your choice: "))
      while choice < 1 or choice > 5:
            print("Invalid choice! Try again.")
            choice = int(input("Enter the number corresponding to your choice: "))

      # Check what the activity factor constant should be equal to according to the level of physical activity
      activity_factor = 0
      if choice == 1:
            activity_factor = 1.2
      elif choice == 2:
            activity_factor = 1.375
      elif choice == 3:
            activity_factor = 1.55
      elif choice == 4:
            activity_factor = 1.725
      elif choice == 5:
            activity_factor = 1.9

      daily_calories = int(calculate_bmr(user_age, user_weight, user_height, user_gender) * activity_factor) # Calculates daily calories goal

      # Asking for user's personal fitness goal
      print("\nWhat is your goal?\n"
            "\n1. Maintaining weight (maintenance)"
            "\n2. Gaining muscle mass (bulking)"
            "\n3. Losing fat (cutting)")

      choice = int(input("Enter the number corresponding to your choice: "))
      while not check_input(choice):
            choice = int(input("Enter the number corresponding to your choice: "))
      while choice < 1 or choice > 3:
            print("Invalid choice! Try again.")
            choice = int(input("Enter the number corresponding to your choice: "))

      # Printing a message of the needed calories according to the choice
      if choice == 1:
            print(f"If you want to maintain your current weight, your caloric intake should match your Total Daily Energy Expenditure (TDEE)."
                  f"\nFor you this is around {daily_calories} calories a day.")
      elif choice == 2:
            print(f"For bulking (gaining muscle mass), you should consume more calories than your Total Daily Energy Expenditure (TDEE) to create a caloric surplus."
                  f"\nA common recommendation for lean bulking (gaining muscle with minimal fat gain) is to start with a 250-500 calorie surplus. "
                  f"\nFor you this is between {daily_calories + 250} and {daily_calories + 500} calories a day.")
      elif choice == 3:
            print(f"For cutting (losing fat), you need to consume fewer calories than your total Daily Energy Expenditure (TDEE) to create a caloric deficit."
                  f"\nA moderate deficit is recommended to avoid losing muscle mass, usually around 300-500 calories below TDEE."
                  f"\nFor you this is between {daily_calories - 500} and {daily_calories - 300} calories a day.")
      print("Remember to always track your calories 😃. You can do that in our app.")
      print("\nThat is all for now. Enjoy the app!")