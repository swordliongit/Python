import pyautogui
import time


def run_poc():
    # Open Notepad
    pyautogui.hotkey('win', 'r')
    pyautogui.write('notepad')
    pyautogui.press('enter')

    # Wait for Notepad to open
    time.sleep(2)

    # Type some text
    pyautogui.write('Hello, this is a POC using PyAutoGUI!')

    # Save the file
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.write('POC_File.txt')
    pyautogui.press('enter')


if __name__ == "__main__":
    run_poc()
