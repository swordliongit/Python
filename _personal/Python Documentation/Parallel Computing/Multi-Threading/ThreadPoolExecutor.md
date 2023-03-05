
### Notes
Saves resources. Because it doesn't create new threads each time they are requested, instead re-uses those threads to continue executing tasks.*

**Submitting tasks to the ThreadPoolExecutor to run them simultaneously**
```python
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=2)
future1 = executor.submit(func1, arg1, arg2)
future2 = executor.submit(func2, arg1, arg2)

executor.shutdown() # Release resources held by executor
```
---
**ThreadPoolExecutor With Context Manager**
*Handles shutdown automatically*
```python
def func1(arg1):
	return arg1

def func2(arg2):
	return arg2

with ThreadPoolExecutor() as executor:
	future1 = executor.submit(func1, arg1)
	future2 = executor.submit(func2, arg1)

	print(future1.result())
	print(future2.result()) # result() gets the return value from the future object
# that is the return value of the func
```
---
**Running high number of threads**
*as_completed function is an iterator over the given futures that yields each as it completes.*
```python
with ThreadPoolExecutor() as executor:
	for arg in range(50): # 50 threads
		future = executor.submit(func, arg)
		futures.append(future)
		
	for future in as_completed(futures):
		print(future.result())
```
**Using the Map function to run multiple threads**
*Mainly used for calling the same function.
Calls the function as many times as the length of the iterable by passing each item from the iterable as argument.*
```python
with ThreadPoolExecutor() as executor:
	results = executor.map(func1, [1, 2, 3]) # results is a generator that yields return values of each function call
```

```python
with ThreadPoolExecutor() as executor:
	results = executor.map(func, [i for i in range(50)]) # 50 threads

for res in results:
	print(res)
```
