from queue import SimpleQueue
from datetime import datetime
from termcolor import colored
        
class CrosswalkButton(object):
    button_pressed_queue: SimpleQueue = None
    
    def __init__(self, button_pressed_queue: SimpleQueue):
        
        if not button_pressed_queue or not isinstance(button_pressed_queue, SimpleQueue):
            raise TypeError(f"button_pressed_queue must be of type SimpleQueue. Found {type(button_pressed_queue)}")
        
        self.button_pressed_queue = button_pressed_queue
        
    def press(self):
        # schedulle the tasks concurrently
        print(colored("CrosswalkButton: Pedestrian pressed the Button", "blue"))
        self.button_pressed_queue.put(datetime.now())
        

        