### Notes:
1. Prevents threads accessing to the same resource at the same time, eliminating race conditions.

```python
from threading import Thread, Lock

class Worker:                  
	money = 100
	mutex = Lock() # mutex lock

	def WorkerAdder(self):
		for _ in range(10000000):
			self.mutex.acquire() # if lock can't be acquired, sleep. If not, acquire it and lock it for other threads.
			self.money += 10
			self.mutex.release() # release the lock so other threads can acquire it.
		print("Stingy done")

	def WorkerSubtractor(self):
		for _ in range(10000000):
			self.mutex.acquire()
			self.money -= 10
			self.mutex.release()
		print("Spendy done")    

ss = Worker()
Thread(target=ss.WorkerAdder, args=()).start()
Thread(target=ss.WorkerSubtractor, args=()).start()
time.sleep(10)
print(ss.money)
```

