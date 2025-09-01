import time
start = ""


def initialize_timer():
    global start
    start = time.time()
    return start


def elapsed_time(end):
    return end - start

