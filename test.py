import keyboard
from os import system

class SelectView:
    def __init__(self):
        self.options = [
            "item 1",
            "item 2",
            "item 3",
            "item 4",
            "item 5"
        ]
        self.pointer = 0
        self.pointer_min = 0
        self.pointer_max = len(self.options) - 1

    def pointer_down(self):
        if self.pointer + 1 <= self.pointer_max:
            self.pointer += 1
            self.print_list()
        
    def pointer_up(self):
        if self.pointer - 1 >= self.pointer_min:
            self.pointer -= 1
            self.print_list()

    def print_list(self):
        system("cls")
        for x in range(0, len(self.options)):
            print(">" if self.pointer == x else " ", self.options[x])

        for x in range(0, 6):
            print(x, end=", ")

    def switch(self):
        keyboard.unhook_all()
        keyboard.add_hotkey("down", self.pointer_down)
        keyboard.add_hotkey("up", self.pointer_up)
        self.print_list()

selectview = SelectView()
selectview.switch()
keyboard.wait()
