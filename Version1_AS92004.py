#Version 6 added score system and refined the looping of random questions into amount of questions you answered instead of the sum of the questions you answered and added the scoring system with a reveal to your final score
#Comment: 
#Code that are hashtagged are for testing purposes
import os
import random
import time

AGE_MAX = 18
AGE_MIN = 11

amt_answered = 0 #How many questions you answered
scr_total = 0 #Your score
qs_answered = [] #Which questions you answered
questions = { #The list of questions and the choices
    1:"Whats the maximum amount of players in one team? \n a. 6 | b. 10 \n-------------- \n c. 5 | d. 12",
    2:"How many classes are there in TF2? \n a. 10 | b. 9 \n-------------- \n c. 14 | d. 5",
    3:"In what year was TF2 released for free? \n a. 2010 | b. 2011 \n------------------- \n c. 2012 | d. 2009",
    4:"What corperation made TF2? \n a. Valve | b. Ubisoft \n------------------------ \n c. Facepunch | d. Sega",
    5:"How many players are allowed in each team of competitive TF2 \n a. 8 | b. 6 \n-------------- \n c. 4 | d. 10",
    6:"What class has the most mobility? \n a. Scout | b. Pyro \n---------------------- \n c. Heavy |d. Soldier",
    7:"How many stages/sections are the in the Control Point map 'Dustbowl'? \n a. 2 | b. 1 \n------------- \n c. 5 | d. 3",
    8:"In the gamemode Capture the Flag, how many times do you have to capture the other team's intellegence to win? \n a. 1 | b. 2 \n------------- \n c. 3 | d. 4",
    9:"What is TF2 based off of? \n a. A Quake mod | b. A Gmod mod \n------------------------------------ \n c. A CS-GO mod | d. It is original",
    10:"How many buildings can Engineer build? \n a. 1 | b. 4 \n------------- \n c. 3 | d. 5",
    11:"What class is the best at single target damage? \n a. Medic | b. Demoman \n----------------------- \n c. Sniper | d. Spy",
    12:"What type of class is Spy? \n a. Support | b. Defense \n----------------------------------- \n c. Offense | d. None of the Above",
    13:"What weapon displays a special kill message? \n a. Knife | b. Fish \n--------------------- \n c. Sign | d. Pistol",
    14:"How many buttons does the Gunslinger have in total? \n a. 4 | b. 10 \n--------------- \n c. 15 | d. 20",
    15:"What is the health decay of the Conniver's Kunai? \n a. ~2.33hp/s | b. ~4.66hp/s \n----------------------------- \n c. ~6.99hp/s | d. ~5hp/s",
    16:"Where is Sniper from? \n a. Australia | b. America \n---------------------------- \n c. Britan | d. New Zealand",
    17:"How many cosmetics that makes noise are there? \n a. 11 | b. 14 \n--------------- \n c. 17 | d. 20",
    18:"Who does the weapon 'Neon Annihilator' belong to? \n a. Demoman | b. Sniper \n------------------------ \n c. Pyro | d. Scout",
    19:"What finger is Merasmus missing? \n a. Pinky | b. Middle \n---------------------- \n c. Index | d. Thumb",
    20:"How much does a medium med kit heal a Scout using the Sandman?\n a. 45 | b. 55 \n--------------- \n c. 63 | d. 50",
}
answers = { #The answers 
    1:"d",
    2:"b",
    3:"b",
    4:"a",
    5:"b",
    6:"d",
    7:"d",
    8:"c",
    9:"a",
    10:"b",
    11:"c",
    12:"a",
    13:"b",
    14:"c",
    15:"a",
    16:"d",
    17:"b",
    18:"c",
    19:"a",
    20:"b"
}

#def difficulty():
    
def clear_text(): #Easy clear text
      os.system('cls' if os.name == 'nt' else 'clear')

def game_intro(): #All of the intro compiled into one
    age_check()
    welcome_text()
    continue_ask()
    clear_text()

def rules(): #The rules
    print("Welcome to the TF2 quiz, this is a quiz about the 2007 class shooter 'Team Fortress 2' made by valve")
    print("Here are the rules: \n 1. This is a multi choice quiz, so please answer by using a, b, c or d.")
    print("2. I reccomend not searching any of the questions up but if you're stuck, please do.")
    print("3. correct answers add 1 to your score and wrong answers minus 1 from your score.")
       
def continue_ask(): #Ask if ready for the next question
    ready = input("Type yes to continue:").lower().strip()
    if ready == "yes":
        return
    else:
        while ready != "yes":
            clear_text()
            ready = input("Type yes when you're ready!:").lower().strip()
    
def welcome_text(): #Welcome text
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

def age_check(): #In order to see if they're applicable to play
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

def score_change(change_amount): #just to change the score
    global scr_total
    scr_total += change_amount

def random_question(): #Generates a random question and lets you answer
    global amt_answered
    qnum = random.randint(a= 1, b= 20) #Generates a random question with a random number 
    while qnum in qs_answered: #This makes it so that if the question generated is in the list ,aka already answered it will roll for another one
        qnum = random.randint(a= 1, b= 20)
    print(questions[qnum])
    playerans = input("Enter your answer!:").lower().strip() #user answer

    if playerans == answers[qnum]: #Correct
        print("You are correct!!!")
        score_change(1)
    else: #Wrong
        print(f"You are wrong, \n The correct answer is actually:{list(answers[qnum])}")
        score_change(-1)
    amt_answered += 1
    qs_answered.append(qnum) #This adds the answered question into the list of answered questions 
    print(scr_total)
    continue_ask()
    clear_text()

def main(): #Main code
    drumroll_timer = 3 #how long drumroll is
    game_intro()
    global amt_answered
    while amt_answered != 20:
        random_question()
    print("You have answered every question! \n Your score is:")
    while drumroll_timer != 0: #drumroll please
        time.sleep(1)
        print("...") #For suspense
        drumroll_timer -= 1
    print(f"{scr_total}!!!")
    
main()
