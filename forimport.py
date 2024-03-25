import pyautogui
import script.modules.anotherimport as anotherimport

class ForImport:
    def __init__(self, flag=False):
        self.flag = flag
        anotherimport.print_hello()
        pass

    def print_positions(self):
        while True:
            print(pyautogui.position())
            pyautogui.sleep(1)
            if self.flag:
                exit()