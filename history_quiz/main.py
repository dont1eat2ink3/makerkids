import json
import random


with open("ages.json","r") as file:
    ages = json.load(file)

print("welcome to your history quiz!")
print("You will be quizzed on inventions, daily life, and major events.")
print("try to guess the correct time period for each. type exit to quit")

score = 0

while True:
    print("what would you like to be quizzed on?")
    print("options:  inventions, daily life, major events")
    category = input("enter your choice").strip().lower()

    if category == "exit":
        print("thanks for playing!")
        print(f"your final score:"{score})
        break

    if category not in ["inventions","major events","daily life"]
    print("invalid choice. please choose from the options above.")
    continue

quiz_items = []

for age, details in ages.items():
    quiz_items.appened((random.choice(details[category.capitalize()]),age))

quiz_item, correct_age = random.choice(quiz_items)
print("which time period do you think this belongs to?")
print(quiz_item)
user_answer = input("your answer: ").strip()

if user_answer.lower() == correct_age.lower():
    print("correct!")
    score = +1
    print(f"score: {score}")
else:
    print(f"incorrect!the correct answer is: {correct_age}")
    print(f"score: "{score})