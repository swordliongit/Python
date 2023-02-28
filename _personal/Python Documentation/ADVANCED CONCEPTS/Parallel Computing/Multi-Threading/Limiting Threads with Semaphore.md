### Notes:
1. *Limits active running thread number. If it's set to 5 for example, and you requested 30 threads, then only 5 threads will be running at a time and other threads will run whenever a thread finishes the work to replace its place.*

**Caller function**
```python
from threading import Semaphore 

threads = []   
thread_limit = 25
thread_semaphore = Semaphore(thread_limit)   
							 
for i in range(100): # request 100 threads
	t = threading.Thread(target=func, args=(thread_semaphore))
	threads.append(t)
	t.start()
for t in threads:
	t.join()
```
**Target Function**
```python
def func(thread_semaphore):
	with thread_semaphore:
		...
```