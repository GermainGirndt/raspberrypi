import sys
import threading
from queue import SimpleQueue
import time
from termcolor import colored
from Light.Light import Light
from Light.LightState import LightState
from utils import validate_not_empty_array_of_instance

class TrafficLightControllerForStreetSegment:
    
    traffic_lights: list[Light]= None
    pedestrian_lights: list[Light]= None
    lock = None
    
    def __init__(self, traffic_lights: list[Light], pedestrian_lights: list[Light], button_pressed_queue: SimpleQueue):
        
        validate_not_empty_array_of_instance(pedestrian_lights, Light, "pedestrian lights")
        validate_not_empty_array_of_instance(traffic_lights, Light, "traffic lights")
        
        if not button_pressed_queue or not isinstance(button_pressed_queue, SimpleQueue):
            raise TypeError("button_pressed_queue must be of type SimpleQueue")
        
        self.traffic_lights = traffic_lights
        self.pedestrian_lights = pedestrian_lights
        
        for traffic_light in self.traffic_lights:
            traffic_light.set_state(LightState.GREEN)
        
        for pedestrian_light in self.pedestrian_lights:
            pedestrian_light.set_state(LightState.RED)
            
        self.button_pressed_queue = button_pressed_queue
        
        self.lock = threading.Lock()
        
    def run(self):
    
        while True:
            sys.stdout.flush()
            timestamp = self.button_pressed_queue.get()
            print(colored(f"TrafficLightControllerForStreetSegment->run: Request to cross the street received at {timestamp}", "blue"))
            
            can_lock_be_acquired = self.lock.acquire(blocking=False)
            
            if not can_lock_be_acquired:
                print(colored(f"TrafficLightControllerForStreetSegment->run: Ignoring the request, since pedestrian are already passing\n", "red"))
                continue
            print(colored(f"TrafficLightControllerForStreetSegment->run: Accepting the request, since no pedestrian is crossing\n", "green"))
            
            self.let_pedestrian_cross()
            print(colored("TrafficLightControllerForStreetSegment->run: Pedestrian pass through completed\n", "green"))
            
            self.lock.release()
    
    
    def let_pedestrian_cross(self):            
        # by doing so, we prevent the 'ressource starvation' (cars can never pass through, because pedestrians are always pressing the button)
        print("TrafficLightControllerForStreetSegment->let_pedestrian_cross: Waiting 6 seconds for cars to pass through")
        time.sleep(6)
        
        print("TrafficLightControllerForStreetSegment->let_pedestrian_cross: Transitioning to the pedestrian phase")
        self.transition_to_the_pedestrian_phase()
        
        print("TrafficLightControllerForStreetSegment->let_pedestrian_cross: Waiting 6 seconds for pedestrians to cross the street")
        time.sleep(6)
        
        print("TrafficLightControllerForStreetSegment->let_pedestrian_cross: Transitioning back to the cars phase")
        self.transition_to_the_cars_phase()
        
    
    def transition_to_the_pedestrian_phase(self):
        for traffic_light in self.traffic_lights:
            traffic_light.set_state(LightState.YELLOW)
            
        print("TrafficLightControllerForStreetSegment->transition_to_the_pedestrian_phase: Waiting 3 seconds for the last cars to stop/pass through, preventing accidents")
        time.sleep(3)
        
        for traffic_light in self.traffic_lights:
            traffic_light.set_state(LightState.RED)
        
        for pedestrian_light in self.pedestrian_lights:
            pedestrian_light.set_state(LightState.GREEN)
            
                    
    def transition_to_the_cars_phase(self):
        for pedestrian_light in self.pedestrian_lights:
            pedestrian_light.set_state(LightState.YELLOW) # corresponds to the flashing/blinking pedestrian signal

        print("TrafficLightControllerForStreetSegment->transition_to_the_cars_phase: Waiting 3 seconds for the last pedestrian to stop/pass through, preventing accidents")
        time.sleep(3)
        
        for traffic_light in self.traffic_lights:
            traffic_light.set_state(LightState.GREEN)
        
        for pedestrian_light in self.pedestrian_lights:
            pedestrian_light.set_state(LightState.RED)