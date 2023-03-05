### Notes:
*It's a lock but additionally we can stop running threads with ==wait== and then we can wake them up with ==notify==*

```python
import time
from threading import Thread, Condition

class StingySpendy:
	money = 100
	cv = Condition()

	def stingy(self):
		for i in range(1000000):
			self.cv.acquire()
			self.money += 10
			self.cv.notify()
			self.cv.release()
		print("Stingy Done")


	def spendy(self):
		for i in range(500000):
			self.cv.acquire()
			while self.money < 20:
				self.cv.wait() # wait until notified, releases lock
			self.money -= 20
			self.cv.release()
		print("Spendy Done")


ss = StingySpendy()
Thread(target=ss.stingy, args=()).start()
Thread(target=ss.spendy, args=()).start()
time.sleep(5)
print("Money in the end", ss.money)
```