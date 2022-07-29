import random

def roll_a_dice(min,max):
    while True:
        print("Rolling the dice...")
        num = random.randint(min,max)
        if num==1:
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
        elif num==2:
            print("[-----]")
            print("[0    ]")
            print("[     ]")
            print("[    0]")
            print("[-----]")
        elif num==3:
            print("[-----]")
            print("[0    ]")
            print("[  0  ]")
            print("[    0]")
            print("[-----]")
        elif num==4:
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[-----]")
        elif num==5:    
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
        else :
            print("[-----]")
            print("[0   0]")
            print("[0   0]")
            print("[0   0]")
            print("[-----]")

        choice = input("Press y to roll the dice again or n to exit :(y/n) ")
        if choice.lower()=='n':
            break
roll_a_dice(1,6)