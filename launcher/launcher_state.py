"""State definitions for the startup launcher."""

from enum import Enum, auto


class LauncherState(Enum):
    STARTUP = auto()
    LOADING = auto()
    PAUSED = auto()
    ACTIVE = auto()
    CLOSED = auto()
    

current_state = LauncherState.STARTUP

def set_state(new_state: LauncherState):
    
    global current_state
    current_state = new_state
    return current_state

def get_state():
    return current_state
    
    
    