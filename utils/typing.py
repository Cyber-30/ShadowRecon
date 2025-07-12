import sys
import time

def type_writer(text: str, delay: float = 0.0025):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
