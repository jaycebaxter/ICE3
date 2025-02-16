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

# Function for menu option 3, calculations
def calculate():

    global temp

    # Handles empty list
    if not temp:
        return "List is blank. Unable to calculate."

    # Prints min, max, and average
    else:
        temp_sum = sum(temp)
        temp_length = len(temp)
        average_temp = int(temp_sum) / int(temp_length)
        min_temp = min(temp)
        max_temp = max(temp)
        return (f"The average temperature is {round(average_temp, 2)}°C.\n"
                f"The minimum temperature is {round(min_temp, 2)}°C.\n"
                f"The maximum temperature is {round(max_temp, 2)}°C.")

        # Resets list so that values from previous calculations aren't reused
        temp = []

def add_temp(user_temp):

    global valid_range
    global numeric_value
    global validation

    # Handles null values
    if user_temp == "":
        return "Input cannot be blank."

    # Handles non-numeric values
    try:
       user_temp = float(user_temp)
       numeric_value = True

    # Takes user back to main menu if they enter q
    except ValueError:
        if user_temp == "q":
            return None
        else:
           return "Please enter a valid number."

    # Handles values outside of acceptable range
    if user_temp < -50 or user_temp > 150:
        return "Temperature must be between -50 and 150 degrees Celsius."

    # If all validation passes, appends to list
    else:
        temp.append(user_temp)
        valid_range = True
        return "Added to list."

def clear_list():
    global temp
    temp = []

def menu_options():

    global user_exit
    global list_populated

    # Loops as long as the user hasn't pressed 3 to exit
    while user_exit == False:
        menu_option = input("1. Add temperature\n2. Calculate\n3. Clear list\n4. Exit\n")

        # If user presses 1, gives them the option to add temperatures to the list
        if menu_option == "1":
            user_temp = input("Please enter a temperature, or enter q to return to menu: ")
            user_output = add_temp(user_temp)
            print(user_output)

        elif menu_option == "2":
            if temp:
                list_populated = True
            print(calculate())

        elif menu_option == "3":
            clear_list()

        # Exits if user inputs 4
        elif menu_option == "4":
            user_exit = True
            return "Exiting"

        else:
            print("Invalid input. Please enter a number from 1-3.")

if __name__ == "__main__":
    menu_options()