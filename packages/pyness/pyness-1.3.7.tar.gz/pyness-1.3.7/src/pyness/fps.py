import time

def fps():
    start_time = time.time()
    time.sleep(0.0001)
    fps = f"{1.0 / (time.time() - start_time)}"[:2]
    return fps