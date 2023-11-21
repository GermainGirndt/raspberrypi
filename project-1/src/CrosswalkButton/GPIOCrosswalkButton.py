from queue import SimpleQueue
from gpiozero import Button
from CrosswalkButton.CrosswalkButton import CrosswalkButton

class GPIOCrosswalkButton(CrosswalkButton):
    
    GPIO_BUTTON_PIN = 17
    
    gpio_button: Button = None
    
    def __init__(self, button_pressed_queue: SimpleQueue):
        super().__init__(button_pressed_queue)
    
    def run(self):
        self.gpio_button = Button(self.GPIO_BUTTON_PIN, hold_time=0.15)
        self.gpio_button.when_pressed = self.press
        