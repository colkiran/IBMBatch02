# Asynchronous code execution

import time
import threading

st = time.perf_counter()

def doJob():
    print("sleeping for 2 secs.........")
    time.sleep(2)
    print("Just woke up......")

thrd1 = threading.Thread(target=doJob, name="t1")
thrd2 = threading.Thread(target=doJob, name="t2")
thrd3 = threading.Thread(target=doJob, name="t3")
thrd4 = threading.Thread(target=doJob, name="t4")
thrd5 = threading.Thread(target=doJob, name="t5")

thrd1.start()
thrd2.start()
thrd3.start()
thrd4.start()
thrd5.start()

# main thread waits for these threads to complete
thrd1.join()
thrd2.join()
thrd3.join()
thrd4.join()
thrd5.join()


et = time.perf_counter()
print(f"completed the task in {round(et - st, 2)} seconds......")
