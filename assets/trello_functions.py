import pyperclip
import pyautogui
import time

def goToTrello():
    pyautogui.hotkey('ctrl', 't')
    pyautogui.write('https://trello.com/b/OEq8HWra/lead-controller')
    pyautogui.press('enter')
    time.sleep(1)

def createFirstCard(name):
    pyautogui.moveTo(184, 433)
    pyautogui.click()
    pyperclip.copy(name)
    pyautogui.hotkey('ctrl', 'v')

def createNextCard(name):
    pyautogui.hotkey('enter')
    pyperclip.copy(name)
    pyautogui.hotkey('ctrl', 'v')