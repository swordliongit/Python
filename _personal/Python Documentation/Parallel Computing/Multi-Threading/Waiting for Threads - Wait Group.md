### Notes
*Calling standard join method on each thread can be resource heavy. Instead, we can make each thread subscribe itself to a group and then notify the parent thread when group reaches a certain threshold*

**File search example with standard join()**
```python
import os
from os.path import isdir, join
from threading import Lock, Thread

mutex = Lock()
matches = []


def file_search(root, filename):
	print("Searching in:", root)
	child_threads = []
	for file in os.listdir(root):
		full_path = join(root, file)
		if filename in file:
			mutex.acquire()
			matches.append(full_path)
			mutex.release()
		if isdir(full_path):
			t = Thread(target=file_search, args=([full_path, filename]))
			t.start()
			child_threads.append(t)
	for t in child_threads:
		t.join()


def main():
	t = Thread(target=file_search, args=(["c:/tools", "README.md"]))
	t.start()
	t.join()
	for m in matches:
		print("Matched:", m)


main()
```
**Same example using a wait group**
```python
import os
from os.path import isdir, join
from threading import Lock, Thread
from wait_group import WaitGroup

mutex = Lock()
matches = []


def file_search(root, filename, wait_group):
	print("Searching in:", root)
	for file in os.listdir(root):
		full_path = join(root, file)
		if filename in file:
			mutex.acquire()
			matches.append(full_path)
			mutex.release()
		if isdir(full_path):
			wait_group.add(1) # subscribe to group
			t = Thread(target=file_search, args=([full_path, filename, wait_group]))
			t.start()
	wait_group.done() # signal when work done


def main():
	wait_group = WaitGroup()
	wait_group.add(1)
	t = Thread(target=file_search, args=(["c:/tools", "README.md", wait_group]))
	t.start()
	wait_group.wait() # wait until threshold
	for m in matches:
		print("Matched:", m)


main()
```

**Wait Group class**
```python
from threading import Condition

class WaitGroup:
	wait_count = 0
	cv = Condition()
	def add(self, count):
		self.cv.acquire()
		self.wait_count += count
		self.cv.release()

	def done(self):
		self.cv.acquire()
		if self.wait_count > 0:
			self.wait_count -= 1
		if self.wait_count == 0:
			self.cv.notify_all()
		self.cv.release()

	def wait(self):
		self.cv.acquire()
		while self.wait_count > 0:
			self.cv.wait()
		self.cv.release()
```