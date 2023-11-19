from pynput.keyboard import Key, Listener
from termcolor import colored
from CrosswalkButton.CrosswalkButton import CrosswalkButton

class KeyboardCrosswalkButton(CrosswalkButton):
    
    def __init__(self, button_pressed_queue):
        super().__init__(button_pressed_queue)
    
    def run(self):            
        listener = Listener(on_press=self.__handle_keyboard_input)
        listener.start()
    
    def __handle_keyboard_input(self, key):    
            
        if key in [Key.space]:
            print(colored("KeypressEvent: Space was pressed", "yellow"))
            self.press()