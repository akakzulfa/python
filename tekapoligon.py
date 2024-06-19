#!/usr/bin/env python

import random

def main():
    """Sila teka poligon"""
    print("Teka poligon")
    
    poligon = [
        "segitiga",
        "sisi empat",
        "pentagon",
        "heksagon",
        "heptagon",
        "oktagon",
        "nonagon",
        "dekagon"
        ]

    x =random.choice(poligon)
    max_trials= 3
    trial=0
    guess = None
    #print(x)
    while trial<max_trials:
        guess = str(input("Poligon apa dalam fikiran saya? "))
        
        if x == guess:
            print(f"Tahniah! Tekaan anda betul!".format(guess))
            break
        else:
            print(f"Maaf, tekaan anda salah. Sila cuba lagi.".format(guess))
            print(f"Anda ada {max_trials} kali percubaan.")
            max_trials -= 1
        if max_trials == 0:
            print(f"Cubaan tamat. Poligon itu ialah {x}.".format(guess))
        
main()