from typing import Callable, Union, Tuple, List, Type 
import threading, datetime, ctypes, time, os

class KeyUtils:
    
    library_name = os.path.join(os.path.join(os.path.dirname(__file__), "lib"), "keyutils.dll")
    
    NUM_KEYS     = 256
    
    QUANTUM      = 0.001
    
    PREEMPTIVE   = False 
    
    class KeyCode:
                
        CHAR_0 = 48
        CHAR_1 = 49
        CHAR_2 = 50
        CHAR_3 = 51
        CHAR_4 = 52
        CHAR_5 = 53
        CHAR_6 = 54
        CHAR_7 = 55
        CHAR_8 = 56
        CHAR_9 = 57
        
        CHAR_A = CHAR_a = 65
        CHAR_B = CHAR_b = 66
        CHAR_C = CHAR_c = 67
        CHAR_D = CHAR_d = 68
        
        CHAR_E = CHAR_e = 69
        CHAR_F = CHAR_f = 70
        CHAR_G = CHAR_g = 71
        CHAR_H = CHAR_h = 72 
        
        CHAR_I = CHAR_i = 73
        CHAR_J = CHAR_j = 74
        CHAR_K = CHAR_k = 75
        CHAR_L = CHAR_l = 76
        
        CHAR_M = CHAR_m = 77
        CHAR_N = CHAR_n = 78
        CHAR_O = CHAR_o = 79
        CHAR_P = CHAR_p = 80 
        
        CHAR_Q = CHAR_q = 81
        CHAR_R = CHAR_r = 82
        CHAR_S = CHAR_s = 83
        CHAR_T = CHAR_t = 84 
        
        CHAR_U = CHAR_u = 85
        CHAR_V = CHAR_v = 86
        CHAR_W = CHAR_w = 87
        CHAR_X = CHAR_x = 88 
        
        CHAR_Y = CHAR_y = 89
        CHAR_Z = CHAR_z = 90 
                        
    class Key:
        
        KEY_BACKSPACE    = 0x08
        KEY_TAB          = 0x09
        KEY_CLEAR        = 0x0C
        KEY_ENTER        = 0x0D
        KEY_SHIFT        = 0x10
        KEY_CTRL         = 0x11
        KEY_ALT          = 0x12
        KEY_PAUSE        = 0x13
        KEY_CAPS_LOCK    = 0x14
        KEY_ESC          = 0x1B
        KEY_SPACE        = 0x20
        KEY_PAGE_UP      = 0x21
        KEY_PAGE_DOWN    = 0x22
        KEY_END          = 0x23
        KEY_HOME         = 0x24
        KEY_LEFT_ARROW   = 0x25
        KEY_UP_ARROW     = 0x26
        KEY_RIGHT_ARROW  = 0x27
        KEY_DOWN_ARROW   = 0x28
        KEY_SELECT       = 0x29
        KEY_PRINT        = 0x2A
        KEY_EXECUTE      = 0x2B
        KEY_SNAPSHOT     = 0x2C
        KEY_INSERT       = 0x2D
        KEY_DELETE       = 0x2E
        KEY_HELP         = 0x2F
        KEY_LEFT_WINDOW  = 0x5B
        KEY_RIGHT_WINDOW = 0x5C
        KEY_APPLICATION  = 0x5D
        KEY_SLEEP        = 0x5F
        KEY_NUMPAD_0     = 0x60
        KEY_NUMPAD_1     = 0x61
        KEY_NUMPAD_2     = 0x62
        KEY_NUMPAD_3     = 0x63
        KEY_NUMPAD_4     = 0x64
        KEY_NUMPAD_5     = 0x65
        KEY_NUMPAD_6     = 0x66
        KEY_NUMPAD_7     = 0x67
        KEY_NUMPAD_8     = 0x68
        KEY_NUMPAD_9     = 0x69
        KEY_MULTIPLY     = 0x6A
        KEY_ADD          = 0x6B
        KEY_SEPARATOR    = 0x6C
        KEY_SUBTRACT     = 0x6D
        KEY_DECIMAL      = 0x6E
        KEY_DIVIDE       = 0x6F
        KEY_F1           = 0x70
        KEY_F2           = 0x71
        KEY_F3           = 0x72
        KEY_F4           = 0x73
        KEY_F5           = 0x74
        KEY_F6           = 0x75
        KEY_F7           = 0x76
        KEY_F8           = 0x77
        KEY_F9           = 0x78
        KEY_F10          = 0x79
        KEY_F11          = 0x7A
        KEY_F12          = 0x7B
        KEY_F13          = 0x7C
        KEY_F14          = 0x7D
        KEY_F15          = 0x7E
        KEY_F16          = 0x7F
        KEY_F17          = 0x80
        KEY_F18          = 0x81
        KEY_F19          = 0x82
        KEY_F20          = 0x83
        KEY_F21          = 0x84
        KEY_F22          = 0x85
        KEY_F23          = 0x86
        KEY_F24          = 0x87
        KEY_NUMLOCK      = 0x90
        KEY_SCROLL       = 0x91
        KEY_LEFT_SHIFT   = 0xA0
        KEY_RIGHT_SHIFT  = 0xA1 
        KEY_LEFT_CTRL    = 0xA2
        KEY_RIGHT_CTRL   = 0xA3 
        KEY_LEFT_ALT     = 0xA4
        KEY_RIGHT_ALT    = 0xA5
        KEY_OEM_1        = 0xBA
        KEY_OEM_PLUS     = 0xBB
        KEY_OEM_COMMA    = 0xBC
        KEY_OEM_MINUS    = 0xBD
        KEY_OEM_PERIOD   = 0xBE
        KEY_OEM_2        = 0xBF
        KEY_OEM_3        = 0xC0
        KEY_OEM_4        = 0xDB
        KEY_OEM_5        = 0xDC
        KEY_OEM_6        = 0xDD
        KEY_OEM_7        = 0xDE
        KEY_OEM_8        = 0xDF
        KEY_OEM_102      = 0xE2 
    
    @classmethod 
    def configure_quantum(class_, quantum : Union[ float, int ], preemptive : bool = False) -> Type[ "KeyUtils" ]:
       class_.QUANTUM    = quantum 
       class_.PREEMPTIVE = preemptive 
       return class_ 
    
    def __init__(self) -> None:
        self.library = ctypes.cdll.LoadLibrary(self.library_name)
        self.library.set_key_indices.argtypes           = [  ctypes.c_void_p, ctypes.c_size_t  ]
        self.library.key_down.argtypes                  = [  ctypes.c_size_t  ]
        self.library.key_down.restype                   =    ctypes.c_bool 
        self.library.get_latest_key_states.argtypes     = [  ctypes.c_void_p  ]
        self.library.get_latest_key_states.restype      =    ctypes.c_size_t 
        self.library.get_previous_key_states.argtypes   = [  ctypes.c_void_p  ]
        self.library.get_previous_key_states.restype    =    ctypes.c_size_t 
        self.library.get_key_state_differences.argtypes = [  ctypes.c_void_p  ]
        self.library.get_key_state_differences.restype  =    ctypes.c_size_t 
        self.library.press_key.argtypes                 = [  ctypes.c_size_t  ]
        self.library.release_key.argtypes               = [  ctypes.c_size_t  ] 
        
        self.__monitor_key_indices                      = []
        
        self.__monitor_key_mapping                      = []
        
        self.key_indices                                = list(range(self.NUM_KEYS))
        
        self.funct_list                                 = []
        
        self.use_monitor                                = False 
        
        self.monitor_thread                             = None
    
    @classmethod 
    def sleep(class_, sleep_duration : Union[ float, int ]) -> Type[ "KeyUtils" ]:
        if (class_.PREEMPTIVE):
            SOT = datetime.datetime.now()
            while ((datetime.datetime.now() <= SOT)):
                pass 
        else:
            time.sleep(sleep_duration)
        return class_ 
    
    def press_key(self, target_key : int) -> "KeyUtils":
        self.library.press_key(target_key)
        return self 
    
    def release_key(self, target_key : int) -> "KeyUtils":
        self.library.release_key(target_key)
        return self 
    
    def preset_key_states(self) -> "KeyUtils":
        self.library.preset_key_states()
        return self 
        
    def set_latest_key_states(self) -> "KeyUtils":
        self.library.set_latest_key_states()
        return self 
        
    def set_previous_key_states(self) -> "KeyUtils":
        self.library.set_previous_key_states()
        return self 
        
    def set_key_state_differences(self) -> "KeyUtils":
        self.library.set_key_state_differences()
        return self 
    
    def set_key_indices(self, key_indices : List[ int ]) -> "KeyUtils":
        __num_indices    = len(key_indices)
        __key_indices    = (ctypes.c_size_t * __num_indices)(*key_indices)
        self.key_indices = key_indices 
        self.library.set_key_indices(__key_indices, __num_indices)
        return self 
    
    def key_down(self, target_key : int) -> bool:
        return self.library.key_down(target_key)
    
    def get_latest_key_states(self) -> List[ Tuple[ int ] ]:
        __key_states = (ctypes.c_bool * len(self.key_indices))()
        self.library.get_latest_key_states(__key_states)
        return list(zip(self.key_indices, list(__key_states)))
    
    def get_previous_key_states(self) -> List[ Tuple[ int ] ]:
        __key_states = (ctypes.c_bool * len(self.key_indices))()
        self.library.get_previous_key_states(__key_states)
        return list(zip(self.key_indices, list(__key_states)))
    
    def get_key_state_differences(self) -> List[ Tuple[ int ] ]:
        __key_states = (ctypes.c_bool * len(self.key_indices))()
        self.library.get_key_state_differences(__key_states)
        return list(zip(self.key_indices, list(__key_states)))
    
    def monitor(self, key_code : Union[ List[ int ], int, str ]) -> Callable:
        if (isinstance(key_code, str)):
            if (key_code.__len__()):
                key_code = [  ord(char) for char in key_code.upper()  ]
            else:
                key_code = ord(key_code)            
        if (isinstance(key_code, list)):
            self.__monitor_key_indices.append(key_code)
        else:
            self.__monitor_key_indices.append([ key_code ])
            
        def monitor_code(function : Callable) -> Callable:
            self.funct_list.append(function)
            return function
        return monitor_code 
    
    def initialize_monitors(self) -> "KeyUtils":
        if (self.funct_list.__len__()):
            key_indices = []
            for i, row in enumerate(self.__monitor_key_indices):
                for j, col in enumerate(row):
                    key_indices.append(col)
                    self.__monitor_key_mapping.append((i, j))
            self.set_key_indices(key_indices)
            self.use_monitor = True
        return self 
            
    def stop_thread(self) -> "KeyUtils":
        if ((self.use_monitor) and (self.monitor_thread is not None)):
            self.terminate()
            self.monitor_thread.join()
        return self 
        
    def start_thread(self) -> "KeyUtils":
        if (self.use_monitor):
            self.monitor_thread = threading.Thread(target = self.run)
            self.monitor_thread.start()
        return self
    
    def terminate(self) -> "KeyUtils":
        self.use_monitor = False 
        return self         
    
    def run(self) -> "KeyUtils":
        self.preset_key_states()
        while (self.use_monitor):
            self.set_latest_key_states()
            self.set_key_state_differences()
            diffs = self.get_key_state_differences()
            for index, (key, diff) in enumerate(diffs):
                if (diff):
                    (i, j) = self.__monitor_key_mapping[index]
                    self.funct_list[i](key, self.key_down(key))
            self.set_previous_key_states()
            if (self.QUANTUM != 0):
                self.sleep(self.QUANTUM)
        return self 
           