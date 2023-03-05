### Notes
*When a parent thread calls join() on a child thread, the parent thread has to wait until the child thread completes*

```python
def child():
	print("Child thread is doing work...")
	sleep(5)
	print("Child thread done...")

def parent():
	t = Thread(target=child)
	t.start()
	print("Parent thread is waiting...")
	t.join()
	print("Parent thread is unblocked...")

parent()
```
