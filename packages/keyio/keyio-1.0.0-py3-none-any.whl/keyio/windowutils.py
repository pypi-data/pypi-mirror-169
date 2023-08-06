from typing import Tuple
import ctypes, os

class WindowUtils:
    
    library_name = os.path.join(os.path.join(os.path.dirname(__file__), "lib"), "windowutils.dll")
    
    class WindowFlags:
        
        SWP_DRAWFRAME      = 0x0020
        SWP_FRAMECHANGED   = 0x0020
        SWP_HIDEWINDOW     = 0x0080
        SWP_NOACTIVATE     = 0x0010
        SWP_NOCOPYBITS     = 0x0100
        SWP_NOMOVE         = 0x0002
        SWP_NOSIZE         = 0x0001
        SWP_NOREDRAW       = 0x0008
        SWP_NOZORDER       = 0x0004
        SWP_SHOWWINDOW     = 0x0040
        SWP_NOOWNERZORDER  = 0x0200
        SWP_NOREPOSITION   = SWP_NOOWNERZORDER
        SWP_NOSENDCHANGING = 0x0400
        SWP_DEFERERASE     = 0x2000
        SWP_ASYNCWINDOWPOS = 0x4000
    
    def __init__(self) -> None:
        self.library = ctypes.cdll.LoadLibrary(self.library_name)
        self.library.get_foreground_bounding_box.argtypes = [  ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p  ]
        self.library.set_foreground_window.argtypes       = [  ctypes.c_int32,  ctypes.c_int32,  ctypes.c_int32,  ctypes.c_int32,  ctypes.c_int32  ] 
        self.library.move_foreground_window.argtypes      = [  ctypes.c_int32,  ctypes.c_int32,  ctypes.c_int32  ]
        
    def get_foreground_window(self) -> Tuple[ int ]:
        __sx = (ctypes.c_int32 * 1)()
        __sy = (ctypes.c_int32 * 1)()
        __ex = (ctypes.c_int32 * 1)()
        __ey = (ctypes.c_int32 * 1)()
        self.library.get_foreground_bounding_box(__sx, __sy, __ex, __ey)
        return (
            int(__sx[0]), int(__sy[0]),
            int(__ex[0]), int(__ey[0])
        )
    
    def set_foreground_window(self, sx : int, sy : int, dx : int = -1, dy : int = -1, flag : int = WindowFlags.SWP_SHOWWINDOW) -> "WindowUtils":
        self.library.set_foreground_window(sx, sy, dx, dy, flag)
        return self 
    
    def move_foreground_window(self, sx : int, sy : int, flag : int = WindowFlags.SWP_SHOWWINDOW) -> "WindowUtils":
        self.library.move_foreground_window(sx, sy, flag)
        return self 
    