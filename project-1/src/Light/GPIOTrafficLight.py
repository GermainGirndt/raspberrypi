from gpiozero import LED
from Light.Light import Light
from Light.LightState import LightState


class GPIOTrafficLight(Light):
    
    GPIO_RED_LED_PIN = 2
    GPIO_YELLOW_LED_PIN = 3
    GPIO_GREEN_LED_PIN = 4
    
    gpio_red_led: LED = None
    gpio_yellow_led: LED = None
    gpio_green_led: LED = None
    
    gpio_current_led: LED = None
    
    def __init__(self):
        super().__init__()
        self.gpio_red_led = LED(self.GPIO_RED_LED_PIN)
        self.gpio_yellow_led = LED(self.GPIO_YELLOW_LED_PIN)
        self.gpio_green_led = LED(self.GPIO_GREEN_LED_PIN)
        self.gpio_current_led = None
    
    def set_state(self, state: LightState):
        super().set_state(state)
        
        if (self.gpio_current_led):
            self.gpio_current_led.off()
            
        if (state == LightState.RED):
            self.gpio_current_led = self.gpio_red_led
        elif (state == LightState.YELLOW):
            self.gpio_current_led = self.gpio_yellow_led
        elif (state == LightState.GREEN):
            self.gpio_current_led = self.gpio_green_led
        else:
            raise ValueError("state must be of type Light")
        
        self.gpio_current_led.on()
        