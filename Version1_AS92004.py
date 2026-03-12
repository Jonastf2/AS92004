#version 2 added prevention to repeating questions, welcome text and more
#comment: 
import os
import random
import time

AGE_MAX = 18
AGE_MIN = 11

q_answered = []
questions = {
    1:"Whats the maximum amount of players in one team? \n a. 6 | b. 10 \n ------------- \n c. 5 | d. 12",
    2:"How many classes are there in the game? \n a. 10 | b. 9 \n ------------- \n c. 14 | d. 5",
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
    2:"b",
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

def welcome_text(): #yeah
      print("""  
  _______ ______ ___                _     
 |__   __|  ____|__ \              (_)    
    | |  | |__     ) |   __ _ _   _ _ ____
    | |  |  __|   / /   / _` | | | | |_  /
    | |  | |     / /_  | (_| | |_| | |/ / 
    |_|  |_|    |____|  \__, |\__,_|_/___|
                           | |            
                           |_|            
                      
                      """)

def age_check(): #in order to see if they're applicable to play
    user_age = int(input("How old are you? \n :"))
    if user_age > AGE_MAX or user_age < AGE_MIN:
        print("Sorry, you are too old/young to play. \n You can play if you're between 11 and 18 years old.")
        time.sleep(1)
        exit()
    else:
        print("On you go!")
        time.sleep(1)
        clear_text()
        return

def game_intro(): #rules and stuff
    print("Welcome to the TF2 quiz, this is a quiz about the 2007 class shooter 'Team Fortress 2' made by valve")
    print("Here are the rules: \n 1.This is a multi choice quiz, so please answer by using a, b, c or d.")
    time.sleep(5)
    clear_text()

def clear_text(): #easy clear text
      os.system('cls' if os.name == 'nt' else 'clear')

def random_question(): # generates a random question and lets you answer
    qnum = random.randint(a= 1, b= 4)
    while qnum in q_answered: #this makes it so that if the question generated is in the list aka. already answered it will roll for another one
        qnum = random.randint(a= 1, b= 4)
    print(questions[qnum])
    playerans = input("Enter your answer!:").lower().strip()

    if playerans == answers[qnum]:
          print("You are correct!!!")
    else:
        print("You are wrong, \n The correct answer is actually:")
        print(answers[qnum])
    
    q_answered.append(qnum) #this adds the answered question into the list 
    print(q_answered) #this is just for testing
    time.sleep(3)
    clear_text()

def main(): # main code
    welcome_text()
    age_check()
    game_intro()
    random_question()
    random_question()
    random_question()
    random_question()
    random_question()
main()