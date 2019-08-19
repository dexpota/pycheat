import fcntl
import sys
import termios

for c in "ls":
    fcntl.ioctl(sys.stdin, termios.TIOCSTI, c)
