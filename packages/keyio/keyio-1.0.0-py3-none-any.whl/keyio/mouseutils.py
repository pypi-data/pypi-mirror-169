from typing import Callable, Union, Tuple, List, Type
import threading, datetime, ctypes, time, os

class MouseUtils:
    
    library_name  = os.path.join(os.path.join(os.path.dirname(__file__), "lib"), "mouseutils.dll")
    
    LEFT_BUTTON   = 0
    
    MIDDLE_BUTTON = 1
    
    RIGHT_BUTTON  = 2
    
    MOUSE_MOVE    = 3
    
    NUM_KEYS      = 3
    
    NUM_DIFFS     = NUM_KEYS + 1
    
    QUANTUM       = 0.001
    
    PREEMPTIVE    = False 
    
    @classmethod 
    def configure_quantum(class_, quantum : Union[ float, int ], preemptive : bool = False) -> Type[ "MouseUtils" ]:
       class_.QUANTUM    = quantum 
       class_.PREEMPTIVE = preemptive 
       return class_ 
   
    def __init__(self) -> None:
        self.library = ctypes.cdll.LoadLibrary(self.library_name)
        self.library.get_mouse_coord.argtypes             = [  ctypes.c_void_p, ctypes.c_void_p  ]
        self.library.set_mouse_coord.argtypes             = [  ctypes.c_size_t, ctypes.c_size_t  ]
        self.library.press_button.argtypes                = [  ctypes.c_size_t  ]
        self.library.release_button.argtypes              = [  ctypes.c_size_t  ]
        self.library.vertical_scroll.argtypes             = [  ctypes.c_int32  ]
        self.library.button_pressed.argtypes              = [  ctypes.c_size_t  ]
        self.library.button_pressed.restype               =    ctypes.c_bool 
        self.library.get_mouse_state_differences.argtypes = [  ctypes.c_void_p  ]
        self.library.get_mouse_state_differences.restype  =    ctypes.c_size_t 
        
        self.button_indices                               = list(range(self.NUM_DIFFS))
        
        self.__monitor_key_indices                        = []
                
        self.funct_list                                   = [ None ] * self.NUM_DIFFS 
        
        self.use_monitor                                  = False 
        
        self.monitor_thread                               = None
        
    @classmethod 
    def sleep(class_, sleep_duration : Union[ float, int ]) -> Type[ "MouseUtils" ]:
        if (class_.PREEMPTIVE):
            SOT = datetime.datetime.now()
            while ((datetime.datetime.now() <= SOT)):
                pass 
        else:
            time.sleep(sleep_duration)
        return class_
        
    def get_mouse_coord(self) -> Tuple[ int ]:
        __x = (ctypes.c_size_t * 1)()
        __y = (ctypes.c_size_t * 1)()
        self.library.get_mouse_coord(__x, __y)
        return (
            int(__x[0]),
            int(__y[0])
        )
    
    def preset_mouse_states(self) -> "MouseUtils":
        self.library.preset_mouse_states()
        return self 
    
    def set_mouse_coord(self, x : int, y : int) -> "MouseUtils":
        if not (isinstance(x, int)):
            x = int(x)
        if not (isinstance(y, int)):
            y = int(y)
        self.library.set_mouse_coord(x, y)
        return self 
    
    def press_button(self, mouse_button : int) -> "MouseUtils":
        self.library.press_button(mouse_button)
        return self 
    
    def release_button(self, mouse_button : int) -> "MouseUtils":
        self.library.release_button(mouse_button)
        return self 
    
    def scroll(self, dy : int) -> "MouseUtils":
        self.library.vertical_scroll(dy)
        return self 
    
    def set_latest_mouse_states(self) -> "MouseUtils":
        self.library.set_latest_mouse_states()
        return self 
    
    def set_previous_mouse_states(self) -> "MouseUtils":
        self.library.set_previous_mouse_states()
        return self 
    
    def set_mouse_state_differences(self) -> "MouseUtils":
        self.library.set_mouse_state_differences()
        return self 
    
    def get_mouse_state_differences(self) -> List[ bool ]:
        __state_diffs = (ctypes.c_bool * self.NUM_DIFFS)()
        self.library.get_mouse_state_differences(__state_diffs)
        return list(__state_diffs)
    
    def button_pressed(self, mouse_key : int) -> bool:
        return self.library.button_pressed(mouse_key)
    
    def monitor(self, key_code : Union[ int, List[ int ] ]) -> Callable:           
        if (isinstance(key_code, list)):
            self.__monitor_key_indices.append(key_code)
        else:
            self.__monitor_key_indices.append([ key_code ])
            
        def monitor_code(function : Callable) -> Callable:
            for kc in self.__monitor_key_indices[-1]:
                self.funct_list[kc] = function
            return function
        return monitor_code 
    
    def initialize_monitors(self) -> "MouseUtils":
        if (self.funct_list.__len__()):
            self.use_monitor = True
        return self 
    
    def stop_thread(self) -> "MouseUtils":
        if ((self.use_monitor) and (self.monitor_thread is not None)):
            self.terminate()
            self.monitor_thread.join()
        return self 
        
    def start_thread(self) -> "MouseUtils":
        if (self.use_monitor):
            self.monitor_thread = threading.Thread(target = self.run)
            self.monitor_thread.start()
        return self
    
    def terminate(self) -> "MouseUtils":
        self.use_monitor = False 
        return self         
    
    def run(self) -> "MouseUtils":
        self.preset_mouse_states()
        while (self.use_monitor):
            self.set_latest_mouse_states()
            self.set_mouse_state_differences()
            diffs = self.get_mouse_state_differences()
            for index, diff in enumerate(diffs):
                function = self.funct_list[index]
                if ((diff) and (function is not None)):
                    if (index < self.NUM_KEYS):
                        function(index, self.button_pressed(index))
                    else:
                        function(index, self.get_mouse_coord())
            self.set_previous_mouse_states()
            if (self.QUANTUM != 0):
                self.sleep(self.QUANTUM)
        return self 
    