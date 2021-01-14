import requests
import json
import pprint
import random
import html

#needs internet connection to run

######################################
#Quiz application without GUI
#The application allows to select from a list of possible answers without typing the answer in full but by just the letter choice
######################################

def quizzer():
    print("Welcome to some IT Quiz!!! *clap-clap-clap*")
    print("Getting questions")
    print("Use a, b, c or d if provided to answer questions with the exception of true or false questions")
    
    #Questions are got from the link below
    r = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=medium")
    
    #Text with questions is changed from json format for Python to understand
    question = json.loads(r.text)
    quizq = [] #stores quiz questions
    quizans = [] #stores right answer
    quizincor = [] #stores incorrect answers
    quizpans = [] #stores possible answers
    for i in range(0, 10): #range ends at 10 because there are 10 questions
        quizq.append(question['results'][i]['question']) #appends the questions
        quizans.append(question['results'][i]['correct_answer']) #appends the correct answer to the question
        quizincor.append(question['results'][i]['incorrect_answers']) #appends the incorrect answers to the question
        question['results'][i]['incorrect_answers'].append(question['results'][i]['correct_answer']) #puts all correct and incorrect answers to the specific question together
        quizpans.append(question['results'][i]['incorrect_answers']) #appends all possible answers
        
    qcounter = 0 #checks number of questions tackled
    score = 0
    x = 0
    
    
    while qcounter != len(quizq): #checks if total number of questions answered is equal to number of questions
        random.shuffle(quizpans[x]) #shuffles list of possible answers
        anscho = ['a' , 'b', 'c', 'd']
        print(html.unescape(quizq[x])) #prints question with qoutes or apostrophes in displayed question instead of #&quot;
        
        #For True or False questions
        if quizans[x] == 'True' or quizans[x] == 'False': 
            print('True or False')
            
        #For questions with four possible answers
        else:
            #prints answer choices
            for i in range(len(quizpans[x])):
                print(anscho[i] + '. ' + html.unescape(quizpans[x][i]), end=" ")
            print()
            
        ########
        #Selecting the answer
        ########
        ans = input("What's the answer?\n")
        if ans == 'a':
            ans = quizpans[x][0]
        elif ans == 'b':
            ans = quizpans[x][1]
        elif ans == 'c':
            ans = quizpans[x][2]
        elif ans == 'd':
            ans = quizpans[x][3]
            
        ##################################
        #Checks if the answer is correct
        ##################################
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

###################
#To play again
###################
response = input("Would you like to play again?\n").lower()
while response == "yes":
    quizzer()
else:
    print("Thank you for playing")
        
    


