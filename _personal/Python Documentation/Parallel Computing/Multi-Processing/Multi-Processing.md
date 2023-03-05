### Notes
1. *Each process executes the code outside of the target function as well so, make sure that only the first runner executes the code.*

```python
import multiprocessing
from multiprocessing import Process

  
def do_work():
    print("Starting work")
    i = 0
    for _ in range(20000000):
        i += 1
    print("Finished work")


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    for _ in range(0, 5):
        p = Process(target=do_work) # call do_work 5 times simultaneously
        p.start()
```
**Output**
Starting work
Starting work
Starting work
Starting work
Starting work
-> waiting
Finished work
Finished work
Finished work
Finished work
Finished work