import json
import random
with open ("ages.json","r") as file:
    ages = json.load(file)

print("welcome to the time machine")
print(" travel through time and learn about the history, or the future!")
print(" type the name of a time period that you would like to go to, or type Exit to leave")
print("available time periods:")
for time_period in ages.keys():
    print(f"- {time_period}")

while True:
    user_choice = input("where would you like to go?")

    if user_choice == "exit":
        print("Exiting the machine, thanks for visiting!")
        break

    elif user_choice in ages:
        print(f"you have traveled to the {user_choice}!")

        selected_age = ages[user_choice]
        invention = random.choice(selected_age["Inventions"])
        major_event = random.choice(selected_age["Major Events"])
        daily_life = random.choice(selected_age["Daily Life"])

        print(f"- a notable invention: {invention}")
        print(f"- a major historical event: {major_event}")
        print(f"- what a daily life was like: {daily_life}")
        print("_------------------------------------------")
    else:
        print("Invalid period, we havent explored that far yet!, please choose something available.")