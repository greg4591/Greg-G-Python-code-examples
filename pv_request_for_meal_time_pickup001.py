# This program collects information about a resident's name, address, and meal choice,
# and prints the formatted information.

def name(fn, ln):   # Function to format the residents First and Last name
    return f"{fn} {ln}" # Returns the formatted name

def address(house_no,street): # Function to format the residents address within Plymouth Village
    """Function to format the residents address within Plymouth Village."""
    return f"{house_no} {street}" # Returns the formatted address

def meal_time(meal): # Function to format the meal time
    """Function to format the meal time."""
    return f"Meal: {meal}" # Returns the formatted meal time

def main(): # Main function to collect user input and display formatted information
    """Main function to collect user input and display formatted information."""
    residents_name = input("Enter residents name (fn ln): ") # Collects the residents name
    if not residents_name.strip(): # Check if the input is empty
        print("Residents name cannot be empty.")
        return
    fn, ln = residents_name.split(maxsplit=1) # Splits the name into first and last name
    if not fn or not ln: # Check if both first and last names are provided
        print("Please provide both first and last names.")
        return
    print(f'Name: {name(fn, ln)}') # Prints the formatted name
    print(f'residents_name: {residents_name}') # Prints the original residents name input
    # Collects the residents address
    residents_address = input("Enter residents address (house_no street): ")    # Check if the input is empty
    if not residents_address.strip():  # Check if the input is empty
        print("Residents address cannot be empty.") 
        return
    house_no, street = residents_address.split(maxsplit=1) # Splits the address into house number and street
    print(f'Address: {address(house_no, street)}')
    print(f'residents_address: {residents_address}')
    meal = input("Enter meal (breakfast, lunch, or dinner): ").strip().lower() # Collects the meal choice
    # Check if the meal choice is valid
    if meal not in ("breakfast", "lunch", "dinner"): # Check if the meal choice is valid
        print("Invalid meal choice. Please enter breakfast, lunch, or dinner.") # Prints an error message if the meal choice is invalid
    else:
        print(f'Meal: {meal_time(meal)}') # Prints the formatted meal time
    print(f'residents_meal: {meal}') # Prints the original meal choice input
    print(f'meal: {meal}')

main()