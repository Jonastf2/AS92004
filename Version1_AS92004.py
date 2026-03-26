#Version 9 Reworded a small amount of questions
#Comment: Add detection for not answering a,b,c or d
import os
import random
import time

AGE_MAX = 18 #Max age
AGE_MIN = 11 #Min age

amt_needed = 20 #Amount needed to finish quiz
amt_answered = 0 #How many questions you answered
scr_total = 0.0 #Your total score
qs_answered = [] #Which questions you answered
questions = { #The list of questions and the choices
    1:"What is the maximum amount of players in a single team? \n a. 6 | b. 10 \n-------------- \n c. 5 | d. 12",
    2:"How many playable characters are there in TF2? \n a. 10 | b. 9 \n-------------- \n c. 14 | d. 5",
    3:"In what year was TF2 released for free? \n a. 2010 | b. 2011 \n------------------- \n c. 2012 | d. 2009",
    4:"What corperation made TF2? \n a. Valve | b. Ubisoft \n------------------------ \n c. Facepunch | d. Sega",
    5:"How many players are allowed in a single team of competitive TF2 \n a. 8 | b. 6 \n-------------- \n c. 4 | d. 10",
    6:"What class has the most mobility options? \n a. Scout | b. Pyro \n---------------------- \n c. Heavy |d. Soldier",
    7:"How many stages/sections are the in the Control Point map 'Dustbowl'? \n a. 2 | b. 1 \n------------- \n c. 5 | d. 3",
    8:"In the gamemode Capture the Flag, how many times do you have to capture the other team's intellegence to win? \n a. 1 | b. 2 \n------------- \n c. 3 | d. 4",
    9:"What is TF2 based off of? \n a. A Quake mod | b. A Gmod mod \n------------------------------------ \n c. A CS-GO mod | d. It is original",
    10:"How many buildings can Engineer build in total? \n a. 1 | b. 4 \n------------- \n c. 3 | d. 5",
    11:"What class is the best at single target damage? \n a. Medic | b. Demoman \n----------------------- \n c. Sniper | d. Spy",
    12:"What type of class is Spy? \n a. Support | b. Defense \n----------------------------------- \n c. Offense | d. None of the Above",
    13:"Which weapon displays a special kill message? \n a. Knife | b. Fish \n--------------------- \n c. Sign | d. Pistol",
    14:"How many buttons does the Gunslinger have in total? \n a. 4 | b. 10 \n--------------- \n c. 15 | d. 20",
    15:"What is the health decay of the Conniver's Kunai? \n a. ~2.33hp/s | b. ~4.66hp/s \n----------------------------- \n c. ~6.99hp/s | d. ~5hp/s",
    16:"What country is Sniper from? \n a. Australia | b. America \n---------------------------- \n c. Britan | d. New Zealand",
    17:"How many cosmetics that makes noise are there? \n a. 11 | b. 14 \n--------------- \n c. 17 | d. 20",
    18:"Who does the weapon 'Neon Annihilator' belong to? \n a. Demoman | b. Sniper \n------------------------ \n c. Pyro | d. Scout",
    19:"Which finger is Merasmus missing? \n a. Pinky | b. Middle \n---------------------- \n c. Index | d. Thumb",
    20:"How much does a medium med kit heal a Scout using the Sandman? \n a. 45 | b. 55 \n--------------- \n c. 63 | d. 50",
    21:"The achievement 'I Spy' is awarded for igniting [x] spies. \n a. 10 | b. 33 \n---------------- \n c. 66 | d. 100",
    22:"When carrying the bomb, robots lose [x] of their speed. \n a. 100% | b. 75% \n------------------ \n c. 50% | d. 25%",
    23:"How many Scream Fortress war paint collections exist? \n a. 5 | b. 6 \n------------- \n c. 7 | d. 8",
    24:"What is the chance of the Batsaber's alternate death effect? \n a. 1% | b. 5% \n----------------- \n c. 10% | d. 25%",
    25:"What is the number present on the Postal Pummeler? \n a. 333 | b. 777 \n----------------- \n c. 666 | d. 606",
    26:"According to the Mannsylvania's Blood Bag, since when was scout missing? \n a. 1972 | b. 1984 \n------------------- \n c. 1998 | d. 2001",
    27:"What year's Scream-Fortress event added no new maps? \n a. 2010 | b. 2012 \n------------------- \n c. 2015 | d. 2017",
    28:"What is the character cap for a name tag? \n a. 36 | b. 40 \n--------------- \n c. 46 | d. 50",
    29:"Each Eyelander decapitation makes Demoman [x%] faster. \n a. 8% | b. 7% \n--------------- \n c. 6% | d. 5%",
    30:"How many diffrent spellbooks are there in TF2? \n a. 1 | b. 2 \n------------- \n c. 3 | d. 4",
    31:"What is the max amount of items per Mann Co. cart? \n a. 128 | b. 225 \n----------------- \n c. 347 | d. 512",
    32:"How many turbines are there in the map 'Turbine'? \n a. 3 | b. 4 \n------------- \n c. 5 | d. 6",
    33:"A 100% charged Baby Face's Blaster' gives Scout a [x%] boost. \n a. 25% | b. 30% \n----------------- \n c. 35% | d. 40%",
    34:"How much self-damage does the grenade taunt do? \n a. 320 | b. 420 \n----------------- \n c. 520 | d. 620",
    35:"How many bullets per minute can the SMG shoot? \n a. 120 | b. 750 \n----------------- \n c. 600 | d. 340",
    36:"In what year was the Rocket Jumper's design changed? \n a. 2016 | b. 2012 \n------------------- \n c. 2014 | d. 2018",
    37:"How many seconds will an enemy be marked-for-death for after being hit by a Fan O'War? \n a. 8 | b. 12 \n--------------- \n c. 10 | d. 15",
    38:"The Iron Bomber's fuse time is [x%] shorter. \n a. 20% | b. 30% \n----------------- \n c. 40% | d, 50%",
    39:"The Ambassador is made of [xkg] of steel. \n a. 2.4kg | b. 3.6kg \n--------------------- \n c. 4.8kg | d. 6kg",
    40:"The Beggar's Bazooka has a [x%] reduced explosion radius. \n a. -20% | b. -30% \n------------------- \n c. -40% | d. -50%"
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
    20:"b",
    21:"a",
    22:"c",
    23:"a",
    24:"d",
    25:"d",
    26:"a",
    27:"d",
    28:"b",
    29:"a",
    30:"c",
    31:"b",
    32:"a",
    33:"d",
    34:"a",
    35:"c",
    36:"b",
    37:"d",
    38:"b",
    39:"b",
    40:"a"
}

def clear_text(): #Easy clear text
      os.system('cls' if os.name == 'nt' else 'clear')

def game_intro(): #All of the intro compiled into one function
    age_check()
    difficulty()
    time.sleep(2)
    clear_text()
    welcome_text()
    rules()
    continue_ask()
    clear_text()

def difficulty(): #Difficulty choosing
    global amt_needed
    difficulty = int(input("Type 1 for Easy mode, Type 2 for Normal mode or Type 3 for Hard mode! \n:"))
    while difficulty != 1 or 2 or 3:
        if difficulty == 1:
            amt_needed -= 10
            print("Easy mode! 10 questions.")
            return
        elif difficulty == 2:
            amt_needed -= 5
            print("Normal mode! 15 questions.")
            return
        elif difficulty == 3:
            print("Hard mode! 20 questions.")
            return
        else:
            difficulty = input("Type 1 for Easy mode, Type 2 for Normal mode or Type 3 for Hard mode! \n:")

def rules(): #The rules
    print("Welcome to the TF2 quiz, this is a quiz about the 2007 class shooter 'Team Fortress 2' made by valve")
    print("Here are the rules: \n 1. This is a multi choice quiz, so please answer by using a, b, c or d.")
    print("2. I reccomend not searching any of the questions up but if you're stuck, please do.")
    print("3. correct answers adds 1 to your score and wrong answers takes away 1 from your score.")
    print("4. For questions with [x], you will need to answer what [x] is.")
       
def continue_ask(): #Ask if ready for the next question
    ready = input("Type yes to continue:").lower().strip()
    if ready == "yes":
        return
    else:
        while ready != "yes":
            clear_text()
            ready = input("Type yes to continue:").lower().strip()
    
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

def drumroll(timer): #Drumroll and duration
    while timer != 0: #Drumroll please
        time.sleep(1)
        print("...") #For suspense!
        timer -= 1

def score_change(change_amount): #just to change the score
    global scr_total
    scr_total += change_amount

def random_question(): #Generates a random question and lets you answer
    global amt_answered
    qnum = random.randint(a= 1, b= 40) #Generates a random question with a random number 
    while qnum in qs_answered: #This makes it so that if the question generated is in the list ,aka already answered it will roll for another one
        qnum = random.randint(a= 1, b= 40) #Re generate
    print(f"Question {amt_answered + 1}:")
    print(questions[qnum])
    playerans = input("Enter your answer!:").lower().strip() #user answer
    if playerans == answers[qnum]: #Correct answer
        print("You are correct!!!")
        score_change(1)
    else: #Wrong answer
        print("You are wrong, \n The correct answer is actually:")
        drumroll(4)
        print(f"{answers[qnum]}!!")
        score_change(-1)
    amt_answered += 1
    qs_answered.append(qnum) #This adds the answered question into the list of answered questions 
    continue_ask()
    clear_text()

def main(): #Main gameplay loop 
    global amt_answered
    global amt_needed
    global scr_total
    #game_intro()
    while amt_answered != amt_needed:
        random_question()
    print("You have answered every question! \n Your score is:")
    drumroll(5)
    print(f"{scr_total}!!!") #FINAL SCORE!!!!
    
main()