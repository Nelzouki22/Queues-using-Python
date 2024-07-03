# Import necessary modules
import queue
from collections import deque
from multiprocessing import Process, Queue

# Using queue.Queue (thread-safe)
def use_queue_module():
    q = queue.Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    while not q.empty():
        print(q.get())

# Using collections.deque (double-ended queue)
def use_deque():
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    while q:
        print(q.popleft())

# Using multiprocessing.Queue (process-safe)
def worker(q):
    q.put('Hello')
    q.put('World')

def use_multiprocessing_queue():
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    p.join()
    while not q.empty():
        print(q.get())

if __name__ == '__main__':
    print("Using queue.Queue:")
    use_queue_module()
    print("\nUsing collections.deque:")
    use_deque()
    print("\nUsing multiprocessing.Queue:")
    use_multiprocessing_queue()

