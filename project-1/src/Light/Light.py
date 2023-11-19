from Light.LightState import LightState

class Light:    
    state: LightState = None
    
    def set_state(self, state: LightState):
        if not state or not isinstance(state, LightState):
            raise ValueError("state must be of type Light")
    
        self.state = state
    
    def get_state(self):        
        if not self.state:
            raise ValueError("state must be set before calling get_state")

        return self.state
