
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minute":
        return f"{num_of_days} days are {num_of_days * 24*60} minutes"
    else:
        return "Unsupported Units"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_num = int(days_and_unit_dictionary["days"])
        if user_input_num > 0:
            num_of_units = days_to_units(user_input_num, days_and_unit_dictionary["unit"])
            print(num_of_units)
        elif user_input_num == 0:
            print("You enter 0")
        else:
            print("You entered negative number")

    except ValueError:
        print("Your input is not a valida number!")


user_input_message = "User, enter number of days and conversion unit\n"