import threading
import time

def task1():
    print("Task 1 started")
    time.sleep(3)
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    time.sleep(3)
    print("Task 2 completed")

start = time.time()

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Total time:", time.time() - start)

"""
Methods:
threading.Thread()->Creates a thread object.
start()	          ->Starts execution in a new thread.
join()	          ->Waits for a thread to finish.
is_alive()	      ->Checks whether a thread is still running.
current_thread()  ->Returns information about the current thread.

"""