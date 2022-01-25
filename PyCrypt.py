import time
import random
import os
import logging
import json
import array
import sys
import colorama
from colorama import Fore, Style

const_char = [
    "A", "B",
    "C", "D",
    "E", "F",
    "G", "H",
    "I", "J",
    "K", "L",
    "M", "N",
    "O", "P",
    "Q", "R",
    "S", "T",
    "U", "V",
    "W", "X",
    "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
]

const_int = [
    4, 5,
    6, 8,
    10, 16
]

setPass = input("Please set encryption password: ")
if setPass == "":
    logging.log(setPass)
    pass
else:
    pass

askForEncryption = input("Type your string to be encrypted: ")
if askForEncryption == "":
    logging.log(askForEncryption)
    pass
else:
    pass

encryption = ''.join(random.choice(const_char) for i in range(random.choice(const_int)))

def reverseEncryption():
    print("Reversed string: " + askForEncryption)

time.sleep(3)

print("Your encrypted string:\n" + encryption)

askForReverse = input("\nWould you like to show original text? If yes, enter your password: ")
if askForReverse == setPass:
    reverseEncryption()
    pass
else:
    print("Password failed, exiting...")
    sys.exit()

print("\nThank you for using PyCrypt!")
