from functools import wraps
import time
import tracemalloc
import random


def stat(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_t = time.time()
        tracemalloc.start()

        steps, weight = func(*args, **kwargs)

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_t = time.time()

        return {
            "steps": steps,
            "weight": weight,
            "memory": (peak-current)/10**6,
            "time": end_t-start_t
        }

    return wrapper

                    
    