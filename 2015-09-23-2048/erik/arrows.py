try:
    from msvcrt import getch  # try to import Windows version
except ImportError:
    def getch():   # define non-Windows version
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class Arrow:
    NONE, UP, DOWN, RIGHT, LEFT = ("NONE", "UP", "DOWN", "RIGHT", "LEFT")

    @classmethod
    def input(cls):
        key = getch()
        if key in ('\x1b', b'\xe0'):
            key += getch()
        if key == '\x1b[':
            key += getch()

        if key is not None:
            if key in ('\x1b[A', b'\xe0H'):
                return cls.UP
            elif key in ('\x1b[B', b'\xe0P'):
                return cls.DOWN
            elif key in ('\x1b[C', b'\xe0M'):
                return cls.RIGHT
            elif key in ('\x1b[D', b'\xe0K'):
                return cls.LEFT
            else:
                return cls.NONE
