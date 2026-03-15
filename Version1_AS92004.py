#version 3 Finishing every question and answer
#comment: 
import os
import random
import time
import math

AGE_MAX = 18
AGE_MIN = 11

q_answered = []
questions = {
    1:"Whats the maximum amount of players in one team? \n a. 6 | b. 10 \n ------------- \n c. 5 | d. 12",
    2:"How many classes are there in TF2? \n a. 10 | b. 9 \n ------------- \n c. 14 | d. 5",
    3:"In what year was TF2 released for free? \n a. 2010 | b. 2011 \n ----------------- \n c. 2012 | d. 2009",
    4:"What corperation made TF2? \n a. Valve | b. Ubisoft \n ---------------------- \n c. Facepunch | d. Sega",
    5:"How many players are allowed in each team of competitive TF2 \n a. 8 | b. 6 \n ------------- \n c. 4 | d. 10",
    6:"What class has the most mobility? \n a. Scout | b. Pyro \n -------------------- \n c. Heavy |d. Soldier",
    7:"How many stages/sections are the in the Control Point map 'Dustbowl'? \n a. 1 | b. 2 \n ----------- \n c. 3 | d. 4",
    8:"In the gamemode Capture the Flag, how many times do you have to capture the other team's intellegence to win? \n a. 1 | b. 2 \n ----------- \n c. 3 | d. 4",
    9:"What is TF2 based off of? \n a. A Quake mod | b. A Gmod mod \n ---------------------------------- \n c. A CS-GO mod | d. It is original",
    10:"How many buildings can Engineer build? \n a. 1 | b. 4 \n ----------- \n c. 3 | d. 5",
    11:"What class is the best at single target damage? \n a. Medic | b. Demoman \n --------------------- \n c. Sniper | d. Spy",
    12:"What type of class is Spy? \n a. Support | b. Defense \n --------------------------------- \n c. Offense | d. None of the Above",
    13:"What weapon displays a special kill message? \n a. Knife | b. Fish \n ------------------- \n c. Sign | d. Pistol",
    14:"How much does a key cost in TF2? \n a. $4 | b. $3 \n ------------- \n c. $5 | d. $9",
    15:"What gender is Pyro? \n a. Male | b. Female \n -------------------------- \n c. Non-Binary | d. Unknown",
    16:"Where is Sniper from? \n a. Australia | b. America \n -------------------------- \n c. Britan | d. New Zealand",
    17:"What race is Demoman? \n a. Scottish | b. African american \n --------------------------------- \n c. African | d. Asian",
    18:"Who does the weapon 'Neon Annihilator' belong to? \n a. Demoman | b. Sniper \n ---------------------- \n c. Pyro | d. Scout",
    19:"19",
    20:"20",
}
answers = {
    1:"d",
    2:"b",
    3:"b",
    4:"a",
    5:"b",
    6:"d",
    7:"c",
    8:"c",
    9:"a",
    10:"b",
    11:"c",
    12:"a",
    13:"b",
    14:"a",
    15:"d",
    16:"d",
    17:"a",
    18:"c",
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
    print("Here are the rules: \n 1. This is a multi choice quiz, so please answer by using a, b, c or d. \n 2. I reccomend not searching any of the questions up but if you're stuck, sure. ")
    print("this screen will be cleared in 10 seconds.......")
    time.sleep(10)
    clear_text()

def clear_text(): #easy clear text
      os.system('cls' if os.name == 'nt' else 'clear')

def random_question(): # generates a random question and lets you answer
    qnum = random.randint(a= 15, b= 15)
    while qnum in q_answered: #this makes it so that if the question generated is in the list aka. already answered it will roll for another one
        qnum = random.randint(a= 15, b= 15)
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
    random_question()
    random_question()
    random_question()
    random_question()
    random_question()
main()