import option
import pyautogui
import time

print("rules")
print('~'*1)
print("How it works ==> you need to select a function, then you need to open a text document or something like Telegram, then open someone's contact or chat, then click [Message] and the program will spam, but you need to run the program for work. You must stay there for work!. If you want to exit the program, just go to the console program and put (exit) there.")
print('~'*2)
print("Как это работает ==> вам нужно выбрать функцию, затем вам нужно открыть текстовый документ или что-то вроде Telegram, затем открыть чей-то контакт или чат, затем нажать «Сообщение», и программа будет рассылать спам, но вам нужно запустить программу для работы. Вы должны остаться там для работы!. Если вы хотите выйти из программы, просто зайдите в консольную программу и поместите туда (выход).")
print('~'*2)
time.sleep(10)
print("Hello Admin!")
print('~'*1)
time.sleep(2)
print("Let's troll someone!")
print('~'*1)
time.sleep(2)

def Send_Message1():
    time.sleep(1)
    message1 = "Get link https://github.com/Hol1yyy/Python"
    iterations1 = 300

    for i in range(iterations1):
        pass

    while iterations1 > 0:
        iterations1 -= 1

        pyautogui.typewrite(message1.strip())
        pyautogui.press('enter')
    print("Ты попал в нашу жертву!")

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
    print("Ты попал в нашу жертву!")

print("Started! ^=__=^")
print('~'*1)
print("[1]==>Spam1!")
print('~'*1)

print('~'*1)
print("[2]==>Spam2!")
print('~'*1)

option = input("[Select function]==> ")

if option == "1":
    Send_Message1()
else:
    print('Function Selected!')

if option == "2":
    Send_Message2()
else:
    print('Function Selected!')

i = 1
while True:
    print('Waiting for Start', i)
    if i == 10:
        break
    i += 1
print('Telegram_Spammer ==> Activeted!')

while True:
    a = input()
    if a == 'exit':
        break