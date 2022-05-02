import time, pyautogui, keyboard

time.sleep(5)
running = True
while running:
    f = open('spamMessage.txt', 'r')

    for line in f:
        if not keyboard.is_pressed('space'):
            pyautogui.typewrite(line)
            pyautogui.press('enter')
        else:
            running = False

