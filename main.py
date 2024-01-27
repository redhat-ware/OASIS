import math
import time
import random

def start():
    x =""
    while x != "yes" and x != "no":
        x = input("Begin Oasis Startup Procedure? (Yes, No) >")
        if x == "yes":
            print("User Input Accepted. Initionalizing Startup Procedure")
            time.sleep(2)
            print("Startup Procedure Complete. Booting Up Oasis Program")
            time.sleep(2)
            logo()
        elif x == "no":
            print("Goodbye")
            quit()
        else:
            print("ERROR. INCORRECT COMAND")
            x = start()
            
def logo():
    print('''
 ______     ______     ______     __     ______       
/\  __ \   /\  __ \   /\  ___\   /\ \   /\  ___\      
\ \ \/\ \  \ \  __ \  \ \___  \  \ \ \  \ \___  \     
 \ \_____\  \ \_\ \_\  \/\_____\  \ \_\  \/\_____\    
  \/_____/   \/_/\/_/   \/_____/   \/_/   \/_____/    
        2024 OASIS TECH LAB   
    ''')
    time.sleep(3)
    opening()
def opening():
    print("You open your eyes....")
    time.sleep(3)
    
    # Ask for the player's name
    
    player_name = input("What is your name? ")
    time.sleep(3)
    
    # Display a welcome message with the player's name
    
    print(f"You see a map in front of you, {player_name}.")
    time.sleep(3)
    
    destination = input("Where do you want to go? ")
    
    print("In front of you, is a journey, a quest if you would.")
    time.sleep(3)
    print("The Nine Regions of Vastora have at least one or more tribute, waiting to have their desires of love and lust be fullfiled.")
    time.sleep(3)
    print("...At least by the only human who is up to the task.")
    time.sleep(3)
    prologue()

def prologue():
    print("You are standing in front of a map. This is where you can travel.")
    time.sleep(2)
    print("you can go in nine different directions")
    time.sleep(2)
    print("To the north is the Volcanic Region, filled with the most scaled dragons of Vastora.")
    time.sleep(2)
    print("To the northeast is the Desert Dunes Region, nothing but sands, ancient cities and snakes of all kinds.")
    time.sleep(2)
    print("To the east is the Lush Rainforest Region, serene and tranqil but hiding feathers in the covered skies.")
    time.sleep(2)
    print("To the southeast is the Vast Ocean Region, blue seas hiding a luxury treasure and a sparkling treasure.")
    time.sleep(2)
    print("To the south is the Frozen Tundra Region, cold and frigid but warmth can be found within.")
    time.sleep(2)
    print("To the southwest is the Rocky Mesa Region, hot, barren and nothing much, perfect for unique characters.")
    time.sleep(2)
    print("To the west is the Grass Plain Region, may look empty but a pasture of love lies within.")
    time.sleep(2)
    print("To the northwest is the Glassstone Cave Region, wonder what's hidding in here?")
    time.sleep(2)
    print("Make your selection and begin you quest")
    location()

def location():
    x =""    
    while x != "north" and x != "south" and x != "east" and x != "west" and x != "northwest" and x != "northeast" and x != "southwest" and x != "southeast":
        x = input("Where would you like to travel? (north, south, east, west, northwest, northeast, southwest, southeast) >")
        if x == "north":
            locked_L()
        elif x == "south":
            locked_L()
        elif x == "east":
            locked_L()
        elif x == "west":
            locked_L()
        elif x == "northeast":
            northeast()
        elif x == "northwest":
            locked_L()
        elif x == "southwest":
            locked_L()
        elif x == "southeast":
            locked_L()
        else:
            print("I guess I'll repeat your options then.")
            x = location()





"Northeast - Desert Dune Region"

def northeast():
    print('''
    The travel across the hot desert sand seems very detremental.
    Almost if there is nothing out there.
    ''')
    time.sleep(3)
    print('''
    After some time, you come across an etched stone, partially covered in sand.
    The stone reads;
    1 MILE NORTHEAST - DURSRIN TOWN
    ''')
    time.sleep(3)
    print('''
    As you continue forward, Dursrin Town comes into view and before you know it, you're at the town's gate.
    In the town, there are numerous amount of vendors.
    The buildings are mostly sandstone, but some are furnished with marble and covers of silk or satin.
    Key shops have massive signs and some that lead through alleyways, for something hidden, possibly lustful.
    ''')
    time.sleep(3)
    print('''
    Its the middle of the day. As you walk on the suprisingly cool limestone paths, you get a closer look at some of the key vendors.
    Fruits, exotic meats, potions? You can't wrap your head around that one. You also understand that you're wearing a somewhat revealing desert atire for men.
    You decide to stop yourself and begin to focus on why you have come here. You take a quick look around at the somewhat crowded plaza. But then you see them.
    ''')
    time.sleep(1)
    dursrin_town_shop_choice()



def dursrin_town_shop_choice():
    x =""
    while x != "Alyx" and x != "Cadren" and x != "Zaphyr":
        x = input("Three different snakes are wearing an orange arm band. They are the tributes of the Desert Dune Region. Choose a store to engage in contact with a tribute. (Jewelery, Potions, Fruits) >")
        if x == "Jewelery":
            Alyxintro()
        elif x == "Potions":
            current_end()
        elif x=="Fruits":
            current_end()
        else:
            print("Choose 1 | Hint: Case Sensitive")
            dursrin_town_shop_choice()




"Desert Dune Region Alyx"
def Alyxintro():
    print('''
    ===------:-:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::    
    =--------::::::::::::::::::::::::::::::::=++**++-::::::::::::--====***=::::::::::::.::::::::::    
    -------:::::::::::::::::::::::::::::::-+===+*++--=**+===+++++=+--==::-:=::::::::::::::::::::::    
    -------::::::::::::::::::::::::::::::-++=-==++=++++**+==+===--+=-=-=::..:+:::::::.::::::::::::    
    ------:-:::::::::::::::::::::::::::::--:::--==++-:==-+=:-===+-===--:::::::-::::::::.::::::::::    
    -------::::::::::::::::::::::::::::::---::::::=:::::::::-=:-====+--::.::::=:.::::::::.:::..:::    
    ----::-:::::::::::::::::::::::::::::::=::+-::=:::::::=-=:-==::=----:::..::::..........::.::.::    
    -----:::::::::::::::::::::::::::::::::--:::==*:::::::-=***=.:=:::==::::::::......:..:..::..:::    
    ----:-:::::::::::::::::::::::::::::::::-+:::::-::::::-***=:::-+:::::-:::....:..::.:......:....    
    ----:::::::::::::::::::::::::::::::::::::==-::=::::::::::::::-=:::::::-:....:::::.........::::    
    ---::-::::::::::::::::::::::::::::::::::::::::==-:::::::::---=:::::::::::...:.........:..:..:.    
    ---:::::::::::::::::::::::::::::::::::::::::=::::=-:::::::::::::::::.::-:.........::...:..:..:    
    ---:-:::::::::::::::::::::::::::::::::::::::::++--=::---:::::::::--===::........:......::...:.    
    --:::::::::::::::::::::::::::::::::::::::::::::+==--=::-::-===-::::-::...:.:...:..............    
    ---:::::::::::::::::::::::::::::::::::::::::::::*-::----=---*:-:-:-:-:..:..::.................    
    ----::::::::::::::::::::::::::::::::::::::::::::+=:::=::-:::+-:.:::-=-:.......................    
    --:::::::::::::::::::::::::::::::::::::::::::::::=::--::::-=-+-::-:::..:..:...:::...:.......:.    
    ----::::::::::::::::::::::::::::::::::::::::::::+=:--::::::--==---=-:::::::::::..:.:.:::::.:::    
    -:-:--::::::::::::::::::::::::::::::::::::::::::-+=--=:::-:::----::::--:::::::::.:::..:::.::::    
    ---:---:::::::::::::::::::::::::::::::::::::::+---::===::=--=:::-::::-::-:::::::..::::.:::::.:    
    -------::::-::::::::::::::::::::::::::::::::+-:---:---::::=++:::::+*+-:++**-:::::::::.::::::::    
    -----:-----:--::::::::::::::::::::::::::::-=--:---=:::--:::::-:::********+++**::::::::::::::::    
    ----------:-:---::::::::::::::::::::::::::+-::-:-=:--::::::::::-::-+************::::::::::::::    
    ----------:----::::::::::::::::::::::::::-=-----=+::::::::::::::-::::***+++**+****::::::::::::    
    ---------------::-::-::::::::::::::::::::+---===*:*:::::::-=----+-:=-:--+**+++*+***+::::::::::    
    -----------:-----::-::::::::::::::::::::-=--===+-=+::::::+------=-=-:::--:::+********-::::::::    
    -------------------::-::::::::::::::::::=*#*****::+=-:::-=----=+=:=-::+=::::::=*******::::::::    
    --------------------::--::::::::::::::::%%%%***-::-**+===*==*++====++-::::::::::::=++-::::::::    
    --------------------------:-:::::::::::-%#%#**=-:--=**------:::---==-:::::::::::::::::::::::::    
    ----------------------------:--:-:-:-:-**#*%%*---::=*+*==--::-::-:-==:::::::::::::::::::::::::    
    -----------------------:----------:::--#%###%=-::---*+*=+==+=--:-:-==:::::::::::::::::::::::::    
    --------------------------------:-----+######-------*++--===-====--=-:::::::::::::::::::::::::    
    =--=----------------------------------##%###*------=*++-----=======*::::::::::::::::::::::::::    
    -=-----------------------------------+#%%###+------*+*+-----------+-::::::::::::::::::::::::::    
    -==----------------------------------*%%***#------=*+********++=--=----:::::::::::::::==::::::    
    ==-==--------------------------------###%%#=-----**+*------=*++*+==------------::---::--:---:-    
    ===--=-=----------------------------+%%%##*----=*++*===----=+--=-*-----------:----------------    
    ========-=-=-=-==-------------------*##%#*----=*++*+*+++++++=----+----------------------------    
    ==============-==-=--=------------==*#%%%=----*++*=++***+++===--==----------------------------    
    ====================-==-=--===---==+#%%%+----=*++*========+===+++-----------------------------    
    ==================-==--==-=--======%#%@*==--=-*****+++*+++#==-=-==----+**##*+=-------=--------    
    =+==+===================-====-====*@%@@*====-=*+**=+***+*****+***------*********==-===--=-----    
    +++++++===========================%%@%%*===--=*+*+=====**%%*==-=+-------=*#*#++++**===-====-=-    
    +++++++++=+=======================%@@#==-=====**#++++=***%##++=++----------=**==+++**+==-=====    
    +++++++++++=+++=+=================++++========**#=====+*###*====+-==--=------=**++++*#*+======    
    =+=++++++++++++++++=++=======================+***==+**+*##******+===============**++++**#=====    
    +++=======++++++++++++++++=+=+===============#*******+++*+=====++================*++++*##*+===    
    ++++++++=========++++++++++++++++++++=+++=+=*#*#++====++*++++*+*+================+****+*****==    
    ****++++++++++=========+++++++++++++++++++++***#+******#+++++=+*==================****+**++**=    
    *******+++++++++++==+++==+++++=++++++++++++##*##*+++++++++++++**+==+==============+#**+**+++*+    
    **********+*++++++++++++++++++===+++++++*#****#*++++*****++++++++++++==+========++=#**+******+    
    *********+****+*+++++++++++++++++++++******#********++++++++***++=+=+++=+==++==++=+#**+**+++*+    
    ********************++*+++++++++*#***********#*++++++******++*+++==+==+=+==+=+++=+*#****+++*#+    
    ***************************#%#************#*#++++****+++++++**++++++++=+=++=+==++*#******+++*+    
    ********************%@@%#****************#*#**#**+++++****++*#*+++++++++++=++++********++***++    
    **************###***************************+++++***#**++++*#****###********##***********+**++    
    *******###******************************#*#***#***+*++*****#***********************#*+++***+++    
    ****##*********************************###***+*****#***++*************************++*****+++++    
    **%###********************************###**********+*****#***********************#****#+++++++    
    *#**********************************#*#************#*+********************#@#*#*****#*++++++++    
    ##*********************************%##****************#**#**#*###*#%%%*****#***#*#%**+++++++++    
    *%#******************************%##**##***#****#****#**#**#***************#***%******+***+**+    
    ***%%#*************************##%***#***#***#*******#%#******#**%********##**************+**+    
    *******#%%%%%%@@@@@@%%%%######%##******************+********%%%%%%#####***********************    
    **********************************************************************************************
    ''')
    time.sleep(3)
    print('''
    Alyx , Lamia , Female , Twenty Three
    
    Colors: Light Tan , Medium Tan , Dark Tan  Markings: Lilac-Pink  Eyes: Ocean Blue
    
    Turn-ons: Latex, Coil, Light Bondage, Spiral/Voice Hypnosis, Having a Good Pet, Being a Dominatng Mistress
    
    Current Mood: Not as Horny/Very Dry
    ''')
    time.sleep(3)
    print('''
    On the outside, Alyx is soft, kind, and caring for the people around her. 
    She works with alot of jewelery and peircings for her day job, but has a keen intrest in "certain" types of clothings.
    But by nightfall, you'll soon understand that she's in control. Hypnotized, you'll find youself as her good little pet, willing to obey any comands.
    ''')
    Alyxtrigger()



def Alyxtrigger():
    x =""
    while x != "yes" and x != "no":
        x = input("Would you like to engage with Alyx? (Yes, No) >")
        if x == "yes":
            Alyx_Start()
        elif x == "no":
            northeast()
        else:
            print("ERROR.INCORRECT INPUT")
            Alyxtrigger()


def Alyx_Start():
    print('''
     ______     __  __     __         __  __    
    /\  __ \   /\ \_\ \   /\ \       /\_\_\_\   
    \ \  __ \  \ \____ \  \ \ \____  \/_/\_\/_  
     \ \_\ \_\  \/\_____\  \ \_____\   /\_\/\_\ 
      \/_/\/_/   \/_____/   \/_____/   \/_/\/_/ 
    ''')
    time.sleep(3)
    print('''
    You duck inside the Jewelery Store, following the tan snake, and to avoid the sun that came out from behind the clouds.
    You're about to make a first impression when something catches you by suprise.
    This snake is obviously a female, but her height, tail length, and the way her head is shaped may suggest that she's a lamia.
    Her outfit is quite intriguing as well. A dark grey woman's office skirt, a white silk scarf over a light grey sleeveless shirt, and white silk gloves that extend past her elbows.
    She's inspecting a set of ocean teal teardrop-shaped earings with gold fasteners.
    You move closer to inspect the set yourself. She then realizes you're there as her head turns to reveal lilac-pink markings and ocean blue eyes.
    ''')
    time.sleep(8)
    Alyx_Dialogue_1()
    
def Alyx_Dialogue_1():
    print('''
    Options:
    A> Sorry, I didn't mean to scare you like that!
    B> My bad.
    ''')
    x =""
    while x != "A" and x != "B":
        x = input("???: Ahh! Please say something if your behind me! >")
        if x == "A":
            print("Sorry, I didn't mean to scare you like that!")
            time.sleep(2)
            Alyx_Dialogue_1a()
        elif x == "B":
            print("My bad.")
            time.sleep(2)
            Alyx_Dialogue_1b()
        else:
            print("You gonna say something? Or.....")
            Alyx_Dialogue_1()
            
def Alyx_Dialogue_1a():
    print("???: Well I'm sorry for reacting like that.")
    time.sleep(3)
    Alyx_Dialogue_2()
    
    
    
def Alyx_Dialogue_1b():
    print("???: Go home. If you're going to be rude, then leave")
    time.sleep(2)
    print("Alyx walks away. She dumps the bright orange arm band on the limestone path as she leaves. Tough luck.")
    time.sleep(2)
    game_over()


def Alyx_Dialogue_2():
    print("???: Name's Alyx, by the way.")
    time.sleep(2)
    print('''
    Options:
    A> I guess you could say that.
    B> You bet!
    ''')
    time.sleep(2)
    x =""
    while x != "A" and x != "B":
        x = input("Alyx: The multicolored band you're wearing indicates you're here to see someone. Someone important.>")
        if x == "A":
            print("I guess you could say that.")
            time.sleep(2)
            Alyx_Dialogue_2a()
        elif x == "B":
            print("You bet!")
            time.sleep(2)
            Alyx_Dialogue_2b()
        else:
            print("You gonna say something? Or.....")
            Alyx_Dialogue_2()

def Alyx_Dialogue_2a():
    print('''
    Alyx:
    Heh. I like you, little guy.
    Since I'm the tribute and you're the guy goin' around trying to.... please us.
    Tomorrow night at my place. 
    See ya then.
    ''')
    time.sleep(3)
    print("Alyx hands you an orange slip of fabric. A tribute has now been marked.")
    time.sleep(3)
    current_end()





def tryagain():
    x =""
    while x != "yes" and x != "no":
        x = input("Do you want to play again? (Yes, No) >")
        if x == "yes":
            print("Well then.... Alright")
            prologue()
        elif x == "no":
            print("System: Session Ending. Goodbye")
            game_over()
            time.sleep(4)
            quit()
        else:
            print("ERROR.INCORRECT INPUT")
            x = tryagain()


def game_over():          
  print('''
   _________    __  _________   ____ _    ____________
  / ____/   |  /  |/  / ____/  / __ \ |  / / ____/ __ \
 / / __/ /| | / /|_/ / __/    / / / / | / / __/ / /_/ /
/ /_/ / ___ |/ /  / / /___   / /_/ /| |/ / /___/ _, _/ 
\____/_/  |_/_/  /_/_____/   \____/ |___/_____/_/ |_|

''')

def locked():
    print('''In this version of the game, this is not made/avilible. Look at our itch page for update!''')
    location()

def locked_L():
    print('''You see a bit sight that says: ERROR, NOT AVAILBE. Maybe try somewhere else?''')
    location()

def current_end():
    print('''
    This the current active end of our development. Thank you for your support so far!
    ''')
    time.sleep(4)
    print("System: Session Ending. Goodbye")
    time.sleep(4)
    quit()




start()
