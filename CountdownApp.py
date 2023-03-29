import datetime

user_input = input("Enter your goal with deadline separated by colon\n")
input_list = user_input.split(":")  # Python:20.06.2023

# Access input list using index
goal = input_list[0]
deadline = input_list[1]

# Convert/Parse date string into date time
deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")

# Get Today date
today_date = datetime.datetime.today()

# Calculation to get deadline : Time remaining for the goal
time_till = deadline_date - today_date
print(time_till)

# convert deadline into hours
hours_till = int(time_till.total_seconds() / 60 / 60)

print(f"Dear user! Time remaining for your goal  :{goal} is {hours_till} hours")
