#version 1 imported stuff, dictionary made, generated questions
#comment: gotta finish adding all the questions.
import os
import random
import time



questions = {
    1:"Whats the maximum amount of players in one team? \n a. 6 | b. 10 \n ------------- \n c. 5 | d. 12",
    2:"2",
    3:"3",
    4:"4",
    5:"5",
    6:"6",
    7:"7",
    8:"8",
    9:"9",
    10:"10",
    11:"11",
    12:"12",
    13:"13",
    14:"14",
    15:"15",
    16:"16",
    17:"17",
    18:"18",
    19:"19",
    20:"20",
}
answers = {
    1:"d",
    2:"2",
    3:"3",
    4:"4",
    5:"5",
    6:"6",
    7:"7",
    8:"8",
    9:"9",
    10:"10",
    11:"11",
    12:"12",
    13:"13",
    14:"14",
    15:"15",
    16:"16",
    17:"17",
    18:"18",
    19:"19",
    20:"20"
}

def clear_text():
      os.system('cls' if os.name == 'nt' else 'clear')

def randomquestion(): # generates a random question and lets you answer
    qnum = random.randint(a= 1, b= 1)
    print(questions[qnum])
    playerans = input("Enter your answer!:").lower().strip()
    if playerans == answers[qnum]:
          print("You are correct!!!")
    else:
        print("You are wrong, \n The correct answer is actually:")
        time.sleep(1)
        print(answers[qnum])
    time.sleep(5)
    clear_text()

def main(): # main code
        randomquestion()

main()