import csv 
import random

def load_questions(filename):
    questions = []
    with open (filename, 'r')as file:
        reader = csv.reader(file)
        next (reader)
        for row in reader:
            questions.append(row)
        return questions

print(load_questions("quiz_questions.csv"))

def take_quiz(questions):
    score = 0
    selected_questions = random.sample(questions,10)
    index = 1

    for question in selected_questions:
        print("question #" + str(index) + ": " + question[0])
        print("A" + question[1])
        print("B" + question[2])
        print("C" + question[3])
        print("D" + question[4])

        answer = input("your answer:(A,B,C,D)").strip().upper()
        if answer == question [5]:
            print ("Correct!")
            score += 1
        else:
            print("incorrect")
            print("the correct answer is:" + question[5])

            index += 1 

return score

def display_results(score,total_questions):
    percentage  = (score/total_questions)*100
    if percentage >= 80:
        print("grade: A")
    elif percentage>=60:
        print("grade: B")
    elif percentage >=50:
        print("grade: C")
    else:
        print("grade: D")

questions = load_questions("quiz_questions.csv")
score = take_quiz(questions)
display_results(score,10)