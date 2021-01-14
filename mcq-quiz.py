import requests
import json
import pprint
import random
import html

#needs internet connection to run

def quizzer():
    print("Welcome to some IT Quiz!!! *clap-clap-clap*")
    print("Getting questions")
    print("Use a, b, c or d if provided to answer questions with the exception of true or false questions")
    r = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=medium")
    question = json.loads(r.text)
    quizq = [] #stores quiz questions
    quizans = [] #stores right answer
    quizincor = [] #stores incorrect answers
    quizpans = [] #stores possible answers
    for i in range(0, 10):
        quizq.append(question['results'][i]['question'])
        quizans.append(question['results'][i]['correct_answer'])
        quizincor.append(question['results'][i]['incorrect_answers'])
        question['results'][i]['incorrect_answers'].append(question['results'][i]['correct_answer'])
        quizpans.append(question['results'][i]['incorrect_answers'])
    qcounter = 0
    score = 0
    x = 0
    while qcounter != len(quizq):
        random.shuffle(quizpans[x]) #shuffles list
        anscho = ['a' , 'b', 'c', 'd']
        print(html.unescape(quizq[x])) #prints question with qoutes instead of #&quot;
        if quizans[x] == 'True' or quizans[x] == 'False':
            print('True or False')
        else:
            for i in range(len(quizpans[x])):
                print(anscho[i] + '. ' + html.unescape(quizpans[x][i]), end=" ")
            print()
        ans = input("What's the answer?\n")
        if ans == 'a':
            ans = quizpans[x][0]
        elif ans == 'b':
            ans = quizpans[x][1]
        elif ans == 'c':
            ans = quizpans[x][2]
        elif ans == 'd':
            ans = quizpans[x][3]
            
        if ans == quizans[x]:
            print("Correct")
            score += 1
        else:
            print("Incorrect")
            print("The correct answer is", quizans[x])
        x += 1
        qcounter += 1
        print("Next question")
    print("Your score for this quiz:", score)

quizzer()

response = input("Would you like to play again?\n").lower()
while response == "yes":
    quizzer()
else:
    print("Thank you for playing")
        
    


