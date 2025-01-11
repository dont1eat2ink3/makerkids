import random
import csv 

def display_clue(word, x ):
    clue = " "

    for i in range(len(word)):
        if i < x :
            clue += word[i]
        else:
            clue += "_"
        
        clue += " "

    print("Name of the country: " + clue.upper())

#display_clue("Canada",4)

def save_leaderboard(name,score,file_name= "leaderboard.csv"):
    with open(file_name,"a", newline="") as file:
        writer= csv.writer(file)
        writer.writerow([name, score])

#save_leaderboards("Maliha", 15)

def display_leaderboard(file_name= "leaderboard.csv"):
    try:
        with open(file_name,"r") as file:
            reader= csv.reader(file)
            scores=list(reader)

            scores.sort(key=lambda x : int(x[1]), reverse=True)
            print("leaderboard(top 10):")
            for i in range(10):
                if i < len (scores):
                    print(f"{i+1}. {scores[i][0]} - {scores[i][1]} points")
    except FileNotFoundError:
        print("No Leaderboard data found")

display_leaderboard()

countries = [
    "Australia", "Brazil", "Canada", "Denmark", "Egypt", "France", "Ghana", "Haiti",
    "India", "Japan", "Kenya", "Lebanon", "Madagascar", "Nepal", "Oman", "Poland",
    "Qatar", "Rwanda", "Singapore", "Turkey", "Uganda", "Venezuela", "Yemen", "Zambia"
]

player_score = 0

random.shuffle(countries)

used_countries = countries[:10]

print("welcome to the 'Name the Country quiz'!")

for round_num in range(len(used_countries)):
    country = used_countries[round_num]
    print(f"Round{ round_num+1}: ")
    clue_length = 1

    while clue_length <= len(country):
        display_clue(country, clue_length)
        guess = input ("your guess? ").title()