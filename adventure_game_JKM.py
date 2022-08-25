"""
    Justin Maddox
    10/5/2015
    Project 3: Adventure Game
    Has the user start in a house and they have to find their way out to win the game.
"""
# The message that greets the user.
def welcomeMessage():
    print("Welcome to my game!!")
    
# The message that gets displayed when the user wins.
def winnerMessage():
    print ("You entered the living room and used the key on the locked door!"
    +" You're a\nwinner!! Congratulations!!")
    userQuit()
    
# The message that gets displayed when the user quits the game or wins the game.    
def userQuit(): 
    print("Thanks for playing!")
    
# This method has the setting of a living room. The user has the option to go in the bedroom or the kitchen. This is where the user starts off.   
def living_room():
    # If the user has the key and they enter the living room, they win the game.
    if has_key == True:
        winnerMessage()
    else: 
        print ("\nYou are in the living room. The paint from the walls is tearing off."
        +" There is a door near you, but it seems to be locked. To your west is the"
        +" kitchen, where you can eat some tasty snacks and to your south is a bedroom. ")
        direction = input("Which direction would you like to go? (W)est or (S)outh? You also have the option to (Q)uit. ")
        if direction == "W":
            kitchen()
        elif direction == "S":
            bed_room()
        elif direction == "N":
            print("Sorry, you can't go north here.")
            living_room()
        elif direction == "E":
            print ("Sorry, you can't go east here.")
            living_room()
        elif direction == "Q":
            userQuit()
        else:
            print ("Sorry, that's not a valid direction.")
            living_room()
     
# This method has the setting of a kitchen. The user has the option to go in the living room or the dining room.     
def kitchen():
    print ("\nYou are in the kitchen. The water from the sink is slightly running. All of the"
    +" cupboards in the kitchen have been left open, like someone has searched through them."
    +" To your south is the dining room, and to your east is the living room. ")
    direction = input("Which direction would you like to go? (S)outh or (E)ast? You also have the option to (Q)uit. ")
    if direction == "S":
        dining_room()
    elif direction == "E":
        living_room()
    elif direction == "N":
        print("Sorry, you can't go north here.")
        kitchen()
    elif direction == "W":
        print("Sorry, you can't go west here.")
        kitchen()
    elif direction == "Q":
        userQuit()  
    else:
        print("Sorry, that's not a valid direction.")
        kitchen()

# This method has the setting of a bedroom. The user has the option to go in the living room or the dining room.             
def bed_room():
    print ("\nYou are in the bedroom. One of the windows in the room is slightly ajar. The other window"
    +" is shattered with a brick laying on the floor next to it. To your west is the dining room and"
    +" to your north is the living room.")
    direction = input("Which direction would you like to go? (W)est or (N)orth? You also have the option to (Q)uit. ")  
    if direction == "W":
        dining_room()
    elif direction == "N":
        living_room()
    elif direction == "E":
        print("Sorry, you can't go east here.")
        bed_room()
    elif direction == "S":
        print("Sorry, you can't go south here.")
        bed_room()
    elif direction == "Q":
        userQuit()
    else:
        print("Sorry, that's not a valid direction.")
        bed_room()

# This method has the setting of a dining room. The user has the option to go in the kitchen or the bedroom.   
def dining_room():
    print ("\nYou are in the dining room. It is very hard to see in here due to the dim lighting. You notice a staircase is the"
    +" in the center of the room. To your north is the kitchen, and to your east is the bedroom.")
    direction = input("Which direction would you like to go? (N)orth or (E)ast or go (D)own the staircase? You also have the option to (Q)uit. ")
    if direction == "N":
        kitchen()
    elif direction == "E":
        bed_room()
    elif direction == "D":
        # The user can only go downstairs once. Checks to see if the user has the key already.
        if has_key == True:
            print("The door is now locked. You can no longer go downstairs.")
            dining_room()
        else:
            basement()
    elif direction == "S":
        print("Sorry, you can't go south here.")
        dining_room()
    elif direction == "W":
        print("Sorry, you can't go west here.")
        dining_room()
    elif direction == "Q":
        userQuit()
    else:
        print("Sorry, that's not a valid direction.")
        dining_room()

# This method has the setting of a basement. The user retrieves the key while they're down here. They can only go back upstairs.  
def basement():
    global has_key
    print ("\nYou are now in the basement. A cloud of dust passes by you and makes it hard to breath. You move away from the area"
    +" and you notice a key on the floor. You pick up the key and hold onto it. You may use it for later. ")
    direction = input("Press U to go upstairs. You also have the option to (Q)uit. ")
    if direction == "U":
        has_key = True
        dining_room()
    elif direction == "Q":
        userQuit()
    else:
        print("Sorry, the only place you can go is back upstairs.")
        basement()

# Greets the user when the game starts.
welcomeMessage()

# This boolean is set to False because the user needs to retrieve the key first.
has_key = False

# This method is called because this is where the user starts the game.
living_room()



        

