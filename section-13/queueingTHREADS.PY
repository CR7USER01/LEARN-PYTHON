import threading
import queue

q = queue.Queue()

def producer():
    for i in range(5):
        print("Producing", i)
        q.put(i)

def consumer():
    while True:
        item = q.get()
        print("Consuming", item)
        q.task_done()

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer, daemon=True)

t1.start()
t2.start()

t1.join()
q.join()