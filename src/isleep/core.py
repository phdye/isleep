"""Interruptible Sleep - isleep

Usage:
  isleep <seconds>
  isleep (-h | --help)
  isleep --version

Arguments:
  <seconds>   Number of seconds to sleep (can exit early if key is pressed).

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import time
import sys
from docopt import docopt

if sys.platform == "win32":
    import msvcrt
else:
    import select
    import tty
    import termios

def consume_keypress():
    """ Consume a keypress from stdin, if available. """
    if sys.platform == "win32":
        msvcrt.getch()  # Consume the keypress on Windows
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())  # Set terminal to raw mode
            if select.select([sys.stdin], [], [], 0.1)[0]:
                sys.stdin.read(1)  # Read and discard the keypress
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def have_input(input_stream, interval=0.1):
    if sys.platform == "win32":
        return msvcrt.kbhit()
    return select.select([input_stream], [], [], interval)[0]

def interruptible_sleep(seconds, input_stream=sys.stdin, interval=0.1):
    start = time.time()
    while time.time() - start < seconds:
        if have_input(input_stream, interval):
            consume_keypress()
            # Interrupted! Exiting early
            return 0
        time.sleep(interval)
    # Completed without interruption
    return 0

def main(argv=sys.argv):
    args = docopt(__doc__, argv[1:], version="isleep 1.0.0")
    seconds = float(args["<seconds>"])
    # print(f"Sleeping for {seconds} seconds...")
    return interruptible_sleep(seconds)
