
```python
from threading import Thread
```

**Basic threading**
*Calling another function while running the current thread*
```python
def main():
	thread = Thread(target=another_func, args=(arg1,))
	thread.start()
```
---
**Multi-threading**
*Calling multiple versions of the function simultaneously*
```python
threads = []
for ip in ip_list: 
	t = threading.Thread(target=modem_login, args=(driver, ip, output))
	threads.append(t)
	t.start()

for t in threads: # wait for all threads to finish
	t.join() 
# parent thread is waiting
```
---
**Message passing between threads using Queue**
```python
from queue import Queue
from threading import Thread
import time


def consumer(q):
    while (True):
        txt = q.get()
        print(txt)
        time.sleep(1)


def producer(q):
    while (True):
        q.put("Hello there")
        print("Message Sent")

  
q = Queue(maxsize=10)
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
```


