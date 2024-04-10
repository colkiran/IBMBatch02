# synchronous code execution

import time

st = time.perf_counter()
def doJob():

    print("Sleeping for 2 secs.......")
    time.sleep(2)
    print("Just woke up......")


doJob()
doJob()
doJob()

et = time.perf_counter()
print(f"The total time taken is {round(et - st, 2)} seconds")

import os
print(os.cpu_count())