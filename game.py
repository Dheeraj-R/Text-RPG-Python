#GH potions in shop /DONE/
#Main Page   edit little bit
#mini quests/something to earn coins /TASKS GIVEN/
#Monster Class - Parent Class:::Derived classes for species
#different attacks /DONE/
#web


import sys
import os
import pickle
import random
import time
#import ascii_magic

Mini_Games_List = [""]

Weapons_in_Shop = {"Steel Sword": 40, "Silver Sword":80} #Weapons shop category
Potions_in_Shop = {"Potion":5, "Greater Healing Potion":20} #health potions shop category


class Player:  #player overlay
    def __init__(self, name):
        self.name = name
        self.MaxHealth = 100
        self.health = self.MaxHealth
        self.MaxMana = 20
        self.mana = self.MaxMana
        self.coins = 100
        self.potions = {"Potion": 3, "Greater Healing Potion": 0}
        self.base_attack = 10
        self.weapons = ["Wooden Sword"]
        self.currentWeapon = ["Wooden Sword"]

    @property
    def attack(self):
        attack = self.base_attack
        if self.currentWeapon == "Wooden Sword":
            attack+= 5
        if self.currentWeapon == "Steel Sword":
            attack += 15
        if self.currentWeapon == "Silver Sword":
            attack += 30
        
        return attack

class Goblin:
    def __init__(self, name):
        self.name = name
        self.MaxHealth = 50
        self.health = self.MaxHealth
        self.attack = 5
        self.GainCoins = 10
        #self.level = 1
Goblin1 = Goblin("Goblin 1")

class Wolf: 
    def __init__(self, name):
        self.name = name
        self.MaxHealth = 70
        self.health = self.MaxHealth
        self.attack = 7
        self.GainCoins = 20
Wolf1 = Wolf("Wolf 1")

def main():
    ####MAIN TITLE EDIT

    os.system('cls')
    
    print("     **       ** ******** **         ******    *******   ****     **** ********  ")
    print("    /**      /**/**///// /**        **////**  **/////** /**/**   **/**/**/////   ")
    print("    /**   *  /**/**      /**       **    //  **     //**/**//** ** /**/**        ")
    print("    /**  *** /**/******* /**      /**       /**      /**/** //***  /**/*******   ")
    print("    /** **/**/**/**////  /**      /**       /**      /**/**  //*   /**/**////    ")
    print("**** //****/**      /**      //**    **//**     ** /**   /    /**/**             ")
    print("**/   ///**/********/******** //******  //*******  /**        /**/********       ")
    print("/       // //////// ////////   //////    ///////   //         // ////////        ")

    time.sleep(3)
    
    os.system('cls')
    print("Welcome to Solo Leveling\n")
    print("1.Start\n2.Load\n3.Exit")

    option = input(">>>> ")
    if option == "1":
        start()
    elif option == "2":
        if os.path.exists("savefile") == True:
            os.system('cls')
            with open('savefile', 'rb') as file: 
                global PlayerA
                PlayerA = pickle.load(file)
            print("Loading Save state...")
            option = input(' ')
            start1()
        else: 
            print("You have no savefile.\n")
            option = input(' ')
            main()
    elif option == "3":
        sys.exit()
    else:
        main()


def start():   #new game
    os.system('cls')
    print("------------------")
    print("Enter your name: ")
    option = input(">>>> ")
    global PlayerA
    PlayerA = Player(option)
    start1()

def start1():  #main menu for game
    os.system('cls')
    i = 1
    print("----------------------------------------")
    print("Name: %s" % PlayerA.name)
    print("Attack: %i 🗡️" % PlayerA.attack)
    print("Coins: %i 🪙" % PlayerA.coins)
    print("Mana: %i 🔥 "% PlayerA.mana)
    print("Health: %i/%i ♥️" % (PlayerA.health, PlayerA.MaxHealth))

    for key,value in PlayerA.potions.items():
        print(str(i)+ ") " + key + ": 🧪 " + str(value))
        i += 1
    #print("Potions: %i ➕\nGreater Healing Potions: %i 🧪" % (PlayerA.potions[], PlayerA.potions[2]))

    #print("Potions: %i ➕" % PlayerA.potions) 
    print("Weapons: %s\n" % PlayerA.weapons)
    print("Current Weapon: %s" % PlayerA.currentWeapon)
    print("----------------------------------------")
    print(" ")
    print("1.Fight\n2.Shop\n3.Inventory\n4.Mini-Games\n5.Save\n6.Exit\n")
    print("----------------------------------------")
    option = input(">>>> ")
    if option == "1":
        prepare_to_fight()
    elif option == "2":
        shop()
    elif option == "3":
        inventory()
    elif option == "4":
        minigame() 
    elif option == "5":
        os.system('cls')
        with open('savefile', 'wb') as file:
            pickle.dump(PlayerA, file)
            print("Save State Loaded")
            option = input(' ')
            start1()            
    elif option == "6":
        sys.exit()
    else:
        start1()

def prepare_to_fight():
    global enemy
    enemychoice = random.randint(1,2)
    if enemychoice == 1:
        enemy = Goblin1
    else:
        enemy = Wolf1
    fight()

def fight():

    if PlayerA.mana < 0:
        PlayerA.mana = 0

    os.system('cls')
    print("    %s        vs        %s" % (PlayerA.name, enemy.name))
    print("-------------------------------------")
    print("%s's Health: %i/%i  %s's Health: %i/%i" % (PlayerA.name, PlayerA.health, PlayerA.MaxHealth, enemy.name, enemy.health, enemy.MaxHealth))
    print("Potions: %s" % PlayerA.potions)
    print("-------------------------------------")
    print("1.Attack\n2.Drink Potion\n3.Run\n")
    option = input(">>>> ")
    if option == "1":
        pre_attack()                                         
    if option == "2":
        potion()
    if option == "3":
        run()
        
    else:
        fight()
        
def pre_attack():
    print("-----------------------------------")
    print("1.Basic Attack\n2.Special Attack")
    print("-----------------------------------")
    attack_input = int(input(">>>> "))
    if attack_input == 1:
        attack()
    elif attack_input == 2:
        special_attack()
    else: 
        print("That move doesn't exist!!!")
        time.sleep(2)
        
        fight()    

    
def special_attack():
    # player SAttack
    SPA = random.randint(15, 25)  #special player attack damage
    
    if PlayerA.mana >= 10:
        PlayerA.mana -= 10
        enemy.health -= SPA
        print("You have used Fire Strike!")
        print("You have dealt %i damage" % SPA)
        time.sleep(2)

        if enemy.health <= 0:
            victory()
        else:
            fight()
            
    else: 
        print("You don't have enough mana!")
        time.sleep(1)
        fight()
    

    # enemy SAttack   #so enemy can either attack or dodge the spcial attack
    SEA = 0
    Enemy_SA = ""
    if enemy == Goblin1:
        SEA = random.randint(7,15)
       # Enemy_name = enemy.name
        Enemy_SA = "Spear Throw"
    if enemy == Wolf1:
        SEA = random.randint(10,20)
       # Enemy_name = enemy.name
        Enemy_SA = "X - Slash"


    if SEA > 13:
        PlayerA.health -= SEA
        print("%s has used %s" % (enemy.name, Enemy_SA))
        print("%s has dealt %i damage to you" % (enemy.name, SEA))
        time.sleep(2)

        if PlayerA.health <= 0:
            defeat()
        else:
            fight()

    else:
        EDamage = random.randint(int(enemy.attack/3), enemy.attack)     #if p/3, then enemy miss  the atteck  
        if EDamage == int(enemy.attack/3):
            print("%s's Attack Missed!" % enemy.name)
            time.sleep(2)
        else: 
            PlayerA.health -= EDamage
            print("%s has dealt %i damage to you" % (enemy.name, EDamage))
            time.sleep(2)

        if PlayerA.health <= 0:
            defeat()

        else:                                       #check it later
            fight()

    #else:                
        #enemy.health += SPA
    #    print("Enemy dodged your attack!")
    #    time.sleep(2)


def attack():
    
    PDamage = random.randint(int(PlayerA.attack/3), PlayerA.attack) #if p/3, player miss the chance
    EDamage = random.randint(int(enemy.attack/3), enemy.attack)     #if p/3, then enemy miss  the atteck  
    
    if PDamage == int(PlayerA.attack/3):
        print("Your Attack Missed!")
        time.sleep(1)
    else: 
        enemy.health -= PDamage
        print("You have dealt %i damage" % PDamage)
        time.sleep(1)
    
    if enemy.health <= 0:
        victory()
    
    if EDamage == int(enemy.attack/3):
        print("%s's Attack Missed!" % enemy.name)
        time.sleep(2)
    else: 
        PlayerA.health -= EDamage
        print("%s has dealt %i damage to you" % (enemy.name, EDamage))
        time.sleep(2)
    
    if PlayerA.health <= 0:
        defeat()

    else:                                       #check it later
        fight()
   
def potion():
    potion1()
    fight()
    
def potion1():    #INCREASES HEALTH 
    i = 1
    print("------------------------------------")
    print("Which potion do you want?")
    print("[Type the name of the potion you want to drink.]")
    for key,value in PlayerA.potions.items():
        print(str(i) + ") " + key + ": " + str(value))
        i += 1
    print("------------------------------------")
    option = input(">>>> ")

    if option in PlayerA.potions:
    
        if option == "Potion":                       #potion = +30 health
            if PlayerA.potions[option] > 0:
                PlayerA.health += 20 
                if PlayerA.health > PlayerA.MaxHealth:
                    PlayerA.health = PlayerA.MaxHealth
                    PlayerA.potions[option] -= 1
                    print("You drank a Potion!")
                    time.sleep(2)
            else:
                print("You don't have any Potions!")
                time.sleep(2)
        elif option == "Greater Healing Potion":
                if PlayerA.potions[option] > 0:
                    PlayerA.health += 50               #ghpotion increases 50 health   
                    if PlayerA.health > PlayerA.MaxHealth:
                        PlayerA.health = PlayerA.MaxHealth
                        PlayerA.potions[option] -= 1
                        print("You drank a Greater Healing Potion!")
                        time.sleep(2)
                else:
                    print("You don't have any Greater Healing Potions!")
                    time.sleep(2)
    else:
        print("That %s does not exist!" % option)
        #os.system('cls')
        potion1()


def run():                 # decrease coins if want to run, else fight
    if PlayerA.coins > 5:
          PlayerA.coins -=5
          print("You ran away \n")
          time.sleep(2)
          start1()
    else:
        print("You Don't have enough 🪙 to run away!")
        time.sleep(2)
        fight()

def victory():
    #os.system('cls')
    PlayerA.coins += enemy.GainCoins
    enemy.health = enemy.MaxHealth            #resets enemy health
    PlayerA.mana = PlayerA.MaxMana            #resets player mana
    print("You have defeated the enemy %s" % enemy.name)
    time.sleep(2)
    print("You have obtained %i 🪙  gold coins!" %enemy.GainCoins)
    time.sleep(2)
    start1()



def defeat():
    #os.system('cls')
    PlayerA.coins -= 10
    print("YOU HAVE BEEN DEFEATED")
    time.sleep(2)
    PlayerA.health = PlayerA.MaxHealth     #resets player health
    PlayerA.mana = PlayerA.MaxMana         #resets player mana
    start1()
    

    
def inventory():
    os.system('cls')
    i = 1
    print("-----------------------------")
    print("Weapons: ")
    for weap in PlayerA.weapons:
        print(str(i) + ') ' + weap)
        i += 1
    print("-----------------------------")
    i = 1
    print("Potions: ")
    for key,value in PlayerA.potions.items():
        print(str(i) + ") " + key + ": " + str(value))
        i += 1
    #print("Potions: %i" % PlayerA.potions)
    #print("Greater Healing Potions: %i" % PlayerA.potions)
    print("-----------------------------")

    time.sleep(2)
    print('What do you want to do?\n')
    print("1.Choose Weapon\n2.Close Inventory\n")
    print("-----------------------------")
    option = input(">>>> ")
    if option == "1":
        equip()
    elif option == "2":
        start1()


def equip():
    os.system('cls')
    i = 1
    print("-----------------------------")
    print("Choose Weapon to equip: ")
    for weap in PlayerA.weapons:
        print(str(i) + ") " + weap)
        i += 1
    print("Type 'Back' to go back\nType Weapon Name to choose: ")
    print("-----------------------------")
    option = input(">>>> ")

    if option in PlayerA.currentWeapon:
        print("Already equipped %s" % option)
        time.sleep(2)
        equip()
    
    elif option == 'Back':
        start1()

    elif option in PlayerA.weapons:
        PlayerA.currentWeapon = option
        print("You have equipped %s" % PlayerA.currentWeapon)
        time.sleep(2)
        start1()
    else:
        print("That item %s does not exist in your inventory" % option)
        time.sleep(2)
        equip()


def shop():
    os.system('cls')

    print("-----------------------------")
    print("\nWelcome to shop!\nWhat would you like to buy?\n")
    print("1.Weapons\n2.Potions\n3.Back\n")
    print("-----------------------------")

    option = input(">>>> ")

    if option == "1":
        i = 1
        for key,value in Weapons_in_Shop.items():
            print(str(i) + ') ' + key + ': ' + str(value) + " 🪙")
            i += 1
        print("Which weapon do you want to buy?")
        time.sleep(2)
        option = input(">>>> ")
        
        if option in Weapons_in_Shop:
            print("That will cost %i 🪙" % Weapons_in_Shop[option])
            time.sleep(2)
            if PlayerA.coins >= Weapons_in_Shop[option]:
                PlayerA.coins -= Weapons_in_Shop[option]
                PlayerA.weapons.append(option)
                print("You have bought %s!" % option)    
                time.sleep(2)
                shop()
            else:
                print ("You don't have enough 🪙 Coins!".capitalize())
                time.sleep(2)
                shop()
        else:
            print("That weapon does not exist!")
            time.sleep(2)
            shop()



    elif option == "2":
        i = 1
        for key,value in Potions_in_Shop.items():
            print(str(i) + ') ' + key + ': ' + str(value) + " 🪙")
            i += 1

        print("which one you want?")
        print("--------------------------------------")

        option = input(">>>> ")   
        if option == "Potion":
            print("How many potions do you want to buy?\n")
            print("--------------------------------------")
            time.sleep(2)
            count = int(input(">>>> "))
            cost = Potions_in_Shop[option]*count
            if PlayerA.coins >= cost:
                PlayerA.coins -= cost
                PlayerA.potions[option] += count
            else:
                print("You don't have enough 🪙!")
                time.sleep(2)
        elif option == "Greater Healing Potion":
            print("How many Greater Healing Potions you want to buy? ")
            print("--------------------------------------")    
            count = int(input(">>>> "))
            cost = Potions_in_Shop[option]*count   
            if PlayerA.coins >= cost:
                PlayerA.coins -= cost
                PlayerA.potions[option] += count
            else:
                print("You don't have enough 🪙!")
                time.sleep(2)
        else:
            print("THat potion does not exist!")
            time.sleep(2)
            shop()
    
    elif option == "3":
        start1()
    else:
        print("That option does not exist. Try Again.")
        time.sleep(2)
        shop()

def minigame():
    os.system('cls')
    i = 1
    print("which game do you want to play?")
    for x in Mini_Games_List:
        print(str(i) + ") " + x)
        i += 1
    option = int(input(">>>> "))
    if option == 1:
        sanidhya()
    elif option == 2:
        bhargav()
    elif option == 3:
        jatin()
    else: 
        print("That game does not exist!")
        time.sleep(2)
        minigame()

def sanidhya():   #increase PlayerA.coin acc to game
    pass

def bhargav():
    def intro():
        print("                It is impossible to win in this still you can try you best XD ")
        print("                       Enter board number in you turn to play your move           ")
        print("                     +_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")
        time.sleep(5)
        os.system('cls')

    board = {1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}
    pp = 'O'
    computer = 'X'
    #we impliment minimac algo....
    #reference from https://levelup.gitconnected.com/mastering-tic-tac-toe-with-minimax-algorithm-3394d65fa88f
    #Mastering Tic-Tac-Toe with Minimax Algorithm in Python
    intro()
    def printBoard(board):
        os.system('cls')
        print(board[1] + " |" + board[2] + " |" + board[3])
        print("-+-+-+-+-")
        print(board[4] + " |" + board[5] + " |" + board[6])
        print("-+-+-+-+-")
        print(board[7] + " |" + board[8] + " |" + board[9])
        print("\n")
       

    def spaceIsFree(position):
        if board[position] == ' ':
            return True 
        return False 

    def insertLetter(letter, position):
        if spaceIsFree(position):
            board[position] = letter 
            printBoard(board)
            if checkDraw():
                print("Draw!")
                time.sleep(2)
                start1()
                
            if checkWin():
                if letter == 'X':
                    print("Bot wins!")
                    time.sleep(2)
                    start1()
                    
                else:
                    print("player wins!")
                    PlayerA.coins += 10
                    time.sleep(2)
                    start1()
            return 
        else:
            print("Invalid position")
            position = int(input("Please enter a new position: "))
            insertLetter(letter, position)
            return    

    def checkWin():
        if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
            return True
        elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
            return True
        elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
            return True
        elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
            return True
        elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
            return True
        elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
            return True
        elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
            return True
        elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
            return True
        else:
            return False

    def checkWhichMarkWon(mark):
        if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
            return True
        elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
            return True
        elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
            return True
        elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
            return True
        elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
            return True
        elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
            return True
        elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
            return True
        elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
            return True
        else:
            return False

    def checkDraw():
        for key in board.keys():
            if board[key] == ' ':
                return False 
        return True 

    def ppMove():
        position = int(input("Enter a position for 'O': "))
        insertLetter(pp, position)
        return 

    def compMove():
        bestScore = -800
        bestMove = 0
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer
                score = minimax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score 
                    bestMove = key
        insertLetter(computer, bestMove)
        return 
    def minimax(board, isMaximizing):
        if checkWhichMarkWon(computer):
            return 1 
        elif checkWhichMarkWon(pp):
            return -1 
        elif checkDraw():
            return 0
            
        if isMaximizing:
            bestScore = -800 
            for key in board.keys():
                if board[key] == ' ':
                    board[key] = computer 
                    score = minimax(board, False)
                    board[key] = ' '
                    if score > bestScore:
                        bestScore = score
            return bestScore 
        else:
            bestScore = 800 
            for key in board.keys():
                if board[key] == ' ':
                    board[key] = pp 
                    score = minimax(board, True)
                    board[key] = ' '
                    if score < bestScore:
                        bestScore = score 
            return bestScore


    while not checkWin():
        compMove()
        ppMove()

def jatin():
  
    from random import randint

    print("      .----------------.  .----------------.  .----------------.  .----------------.     ")
    print("     | .--------------. || .--------------. || .--------------. || .--------------. |         ")
    print("     | | ____    ____ | || |      __      | || |   ________   | || |  _________   | |")
    print("     | ||_   \  /   _|| || |     /  \     | || |  |  __   _|  | || | |_   ___  |  | |")
    print("     | |  |   \/   |  | || |    / /\ \    | || |  |_/  / /    | || |   | |_  \_|  | |")
    print("     | |  | |\  /| |  | || |   / ____ \   | || |     .'.' _   | || |   |  _|  _   | |")
    print("     | | _| |_\/_| |_ | || | _/ /    \ \_ | || |   _/ /__/ |  | || |  _| |___/ |  | |")
    print("     | ||_____||_____|| || ||____|  |____|| || |  |________|  | || | |_________|  | |")
    print("     | |              | || |              | || |              | || |              | |")
    print("     | '--------------' || '--------------' || '--------------' || '--------------' |")
    print("     ' ----------------'  '----------------'  '----------------'  '----------------' ")

    time.sleep(1)
    os.system('cls')
    print("        You get traped in a maze there are monster at randon location you need to         ")          
    print("         find a way to go to the exit of the maze without encount the enemy            ")
    print("                  10 gold coins are waitng for you at the exit gate                        ")
    time.sleep(1)
    os.system('cls')
    charX = 0
    charY = 0
    mazeX = 5
    mazeY = 5
    enemy_number = 6
    board = [["| |" for a in range(mazeX)] for b in range(mazeY)]
    currentposition = "|&|" 
    board[charX][charY] = currentposition
    ls = []
    for m in range(enemy_number):
        enemyX = randint(1,5)
        enemyY = randint(1,5)
        ele = (enemyX,enemyY)
        ls.append(ele)

    while True:
        def check():
            for i in range(4):
        
                    if ls[i][0] == charX and ls[i][1] == charY:
                    
                        print("YOU ATTACKED BY MONSTER GAME OVER")
                        board[charX][charY] = "|X|"
                        time.sleep(2)
                        start1()
                    if charX == mazeX-1 and charY == mazeY-1:
                        
                        print("You win the game")
                        print("You get 10 gold coins")
                        PlayerA.coins += 10
                        time.sleep(2)
                        start1()


        #print(ls)
        for i in board:
            print("--- --- --- --- ---")
            print(" ".join(i))
            print("--- --- --- --- ---")
        print("                   -🥇-")

        print("Instruction :")
        print("Up: W  ||  Down: S  || Left: A  || Right: D")
        
        option = input("Enter you option:>>> ")
        
        if option == "W":
            os.system('cls')
            board[charX][charY] = "| |"
            charX -= 1
            if mazeX > charX:
                board[charX][charY] = "|&|"
            else:
                print("You hit the wall")
                charX = 0
                charY = 0
                board[charX][charY] = "|&|"
            check()
            
        elif option == "S":
            os.system('cls')
            board[charX][charY] = "| |"
            charX += 1
            if mazeX > charX:
                board[charX][charY] = "|&|"
            else:
                print("You hit the wall")
                time.sleep(1)
                charX = 0
                charY = 0
                board[charX][charY] = "|&|"
            check()
        elif option == "A":
            os.system('cls')
            board[charX][charY] = "| |"
            charY -= 1
            if mazeY > charY:
                board[charX][charY] = "|&|"
            else:
                print("You hit the wall")
                charX = 0
                charY = 0
                board[charX][charY] = "|&|"
            check()
        elif option == "D":
            os.system('cls')
            board[charX][charY] = "| |"
            charY += 1
            if mazeY > charY:
                board[charX][charY] = "|&|"
            else:
                print("You hit the wall")
                charX = 0
                charY = 0
                board[charX][charY] = "|&|"
            check()



main()