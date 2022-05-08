# -*- coding: cp1251 -*-

# -*- coding: utf-8 -*-

# -*- coding: windows-1251 -*-

######################################################
#  -------                                           #
# |       \            |     |          |  |         #
# |       /            |     |          |  |         #
# |-------   \ _ /     |-----|  / _ \   |  |  \ _ /  #
# |       \   \ /      |     | | (_) |  |  |   \ /   #
# |       /    /       |     |  \___/   |  |    /    #
#  -------    /                                /     #
######################################################

import pyautogui, time, option, pyfiglet

print("rules")
print('~' * 1)
print("How it works ==> you need to select a function, then you need to open a text document or something like Telegram, then open someone's contact or chat, then click [Message] and the program will spam, but you need to run the program for work. You must stay there for work!. If you want to exit the program, just go to the console program and put (exit) there.")
print('~' * 1)
time.sleep(5)
print("Hello Admin!")
print('~' * 1)
time.sleep(2)
print("Let's troll someone!")
print('~' * 1)
time.sleep(2)

def Send_Message1():
    time.sleep(1)
    message1 = "Get link https://github.com/Hol1yyy/Python"
    iterations1 = 300

    for i in range(iterations1):
        pass

    while iterations1 > 0:
        iterations1 -= 1

        pyautogui.typewrite (message1.strip ())
        pyautogui.press('enter')
    print("You got them!")

def Send_Message2():
    time.sleep(1)
    message2 = "Hello fucking bitch!"
    iterations2 = 300

    for i in range(iterations2):
        pass

    while iterations2 > 0:
        iterations2 -= 1

        pyautogui.typewrite(message2.strip())
        pyautogui.press('enter')
    print("You got them")

print("Started! ^=__=^")
print('~' * 1)
print("[1]==>Spam1!")
print('~' * 1)

print('~' * 1)
print("[2]==>Spam2!")
print('~' * 1)

option = input("[Select function]==> ")

print('*' * 5)
print("Waiting for Start")
print('*' * 30)
time.sleep (2)
print("Telegram_Spammer ==> Activeted! :)")
print('*' * 30)

if option == "1":
    Send_Message1()

if option == "2":
    Send_Message2()