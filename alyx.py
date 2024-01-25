import math
import time
import random


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
    game_over()
    
    
    
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


    
def game_over():          
  print('''
   _________    __  _________   ____ _    ____________
  / ____/   |  /  |/  / ____/  / __ \ |  / / ____/ __ \
 / / __/ /| | / /|_/ / __/    / / / / | / / __/ / /_/ /
/ /_/ / ___ |/ /  / / /___   / /_/ /| |/ / /___/ _, _/ 
\____/_/  |_/_/  /_/_____/   \____/ |___/_____/_/ |_|    
''')   
    
Alyx_Start()