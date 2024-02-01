from sys import stdout
from time import sleep


def stream_to_console(message: str):
    for char in message:
        sleep(0.01)
        stdout.write(char)
        stdout.flush()
