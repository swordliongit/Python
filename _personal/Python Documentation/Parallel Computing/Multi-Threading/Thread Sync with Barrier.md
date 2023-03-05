### Notes
1. *A barrier for a group of threads or processes in the source code means any thread/process must stop at this point and cannot proceed until all other threads/processes reach this barrier.*

2. When a thread calls barrier.wait(), it is blocked until another thread calls barrier.wait(), then they both continue.

3. barrier.abort() places the barrier into a 'broken' state. Useful in case of error.
    Any currently waiting threads and threads attempting to 'wait()' will have BrokenBarrierError raised.

```python
from threading import Barrier

barrier = Barrier(2) # 2 threads


def wait_on_barrier(name, time_to_sleep):
	for i in range(10):
		print(name, "running")
		time.sleep(time_to_sleep)
		print(name, "is waiting on barrier")
		barrier.wait()
	print(name, "is finished")


red = Thread(target=wait_on_barrier, args=("red", 4))
blue = Thread(target=wait_on_barrier, args=("blue", 10))
red.start()
blue.start()
```
**Output**
red running
blue running
red is waiting on barrier
blue is waiting on barrier
blue running
red running 
red is waiting on barrier
...