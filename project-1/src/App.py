import threading
from queue import SimpleQueue
from Light.GPIOTrafficLight import GPIOTrafficLight
from CrosswalkButton.GPIOCrosswalkButton import GPIOCrosswalkButton
from Light.Light import Light
from CrosswalkButton.KeyboardCrosswalkButton import KeyboardCrosswalkButton
from TrafficLightController.TrafficLightControllerForStreetSegment import TrafficLightControllerForStreetSegment

# Set to True if running on Raspberry Pi
# Set to False if running on local machine
SHOULD_USE_RASPBERRY_PI = False

# Create a thread-safe queue
button_pressed_queue = SimpleQueue()

if SHOULD_USE_RASPBERRY_PI:
    traffic_light = GPIOTrafficLight()
    crosswalk_button = GPIOCrosswalkButton(button_pressed_queue)
else:
    traffic_light = Light()
    crosswalk_button = KeyboardCrosswalkButton(button_pressed_queue)
    
pedestrian_light = Light()
traffic_light_controller = TrafficLightControllerForStreetSegment(traffic_lights=[traffic_light], pedestrian_lights=[pedestrian_light], button_pressed_queue=button_pressed_queue)


    
def main(): 
    producer_thread = threading.Thread(target=crosswalk_button.run)
    
    consumer_thread_one = threading.Thread(target=traffic_light_controller.run)
    consumer_thread_two = threading.Thread(target=traffic_light_controller.run)
    consumer_thread_three = threading.Thread(target=traffic_light_controller.run)
    
    producer_thread.start()
    consumer_thread_one.start()
    consumer_thread_two.start()
    consumer_thread_three.start()


main()