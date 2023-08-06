import time
start = time.time()
def runtime():
    return int(time.time() - start)
def reset():
    start = 0
    return 0