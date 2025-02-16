#####################################################################################
# Program: Temperature Sensor
# Author: Jayce Baxter
# Date: January 28th, 2025
# Description: Calculates minimum, maximum and average temperature based on
#              user input
#####################################################################################

# Initializing list
temp = []

# Using booleans for validation
validation = False

numeric_value = False
valid_range = False
list_populated = False
user_exit = False

# Once all validation criteria are met, sets validation to True
if list_populated == True and valid_range == True and numeric_value == True and user_exit == True:
    validation = True

# Loops as long as the user hasn't pressed 3 to exit
while user_exit == False:

    menu_option = input("Enter 1 to add a temperature, 2 to calculate, or 3 to exit: ")

    # Ensures the menu option is numeric
    try:
        menu_option = int(menu_option)

    except ValueError:
        print("Please enter a number.")
        continue

    # If user presses 1, gives them the option to add temperatures to the list
    if menu_option == 1:

        while validation == False:

            user_temp = input("\nPlease enter a temperature, or enter q to return to menu: ")

            # Handles null values
            if user_temp == "":
                print("Input cannot be blank.")
                continue

            # Handles non-numeric values
            try:
                user_temp = float(user_temp)
                numeric_value = True

            # Takes user back to main menu if they enter q
            except ValueError:
                if user_temp == "q":
                    break
                else:
                    print("Please enter a valid number.")
                    continue

            # Handles values outside of acceptable range
            if user_temp < -50 or user_temp > 150:
                print("Temperature must be between -50 and 150 degrees Celsius.")
                continue

            # If all validation passes, appends to list
            else:
                temp.append(user_temp)
                valid_range = True

                # If user enters 2, calculates based on their input
    elif menu_option == 2:

        # Handles empty list
        if not temp:
            print("List is blank. Unable to calculate.")

        # Prints min, max, and average
        else:
            temp_sum = sum(temp)
            temp_length = len(temp)
            average_temp = int(temp_sum) / int(temp_length)
            min_temp = min(temp)
            max_temp = max(temp)
            print(f"The average temperature is {round(average_temp, 2)}°C.")
            print(f"The minimum temperature is {round(min_temp, 2)}°C.")
            print(f"The maximum temperature is {round(max_temp, 2)}°C.")

            # Resets list so that values from previous calculations aren't reused
            temp = []

    # Exits if user inputs 3
    elif menu_option == 3:
        user_exit = True

    else:
        print("\nInvalid input. Please enter a number from 1-3.")