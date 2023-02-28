### Notes
1. if you use standard lists, each process will copy it and we cannot change the contents of it in a different process. multiprocessing.Array lets us share it between different processes so the code below works as intended.

```python
import multiprocessing
from multiprocessing.context import Process

import time


def print_array_contents(array):
	while True:
		print(*array, sep = ", ")
		time.sleep(1)


if __name__ == "__main__":
	arr = multiprocessing.Array('i', [-1]*10, lock=True)
	p = Process(target=print_array_contents, args=(arr,))
	p.start()
	for j in range(10):
		time.sleep(2)
		for i in range(10):
			arr[i] = j
```
**Output**(2 lines every 1 second)
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1
0, 0, 0, 0, 0, 0, 0, 0, 0, 0
0, 0, 0, 0, 0, 0, 0, 0, 0, 0
1, 1, 1, 1, 1, 1, 1, 1, 1, 1
1, 1, 1, 1, 1, 1, 1, 1, 1, 1
2, 2, 2, 2, 2, 2, 2, 2, 2, 2
2, 2, 2, 2, 2, 2, 2, 2, 2, 2
3, 3, 3, 3, 3, 3, 3, 3, 3, 3
3, 3, 3, 3, 3, 3, 3, 3, 3, 3
4, 4, 4, 4, 4, 4, 4, 4, 4, 4
4, 4, 4, 4, 4, 4, 4, 4, 4, 4
5, 5, 5, 5, 5, 5, 5, 5, 5, 5
5, 5, 5, 5, 5, 5, 5, 5, 5, 5
6, 6, 6, 6, 6, 6, 6, 6, 6, 6
6, 6, 6, 6, 6, 6, 6, 6, 6, 6
7, 7, 7, 7, 7, 7, 7, 7, 7, 7
7, 7, 7, 7, 7, 7, 7, 7, 7, 7
8, 8, 8, 8, 8, 8, 8, 8, 8, 8
8, 8, 8, 8, 8, 8, 8, 8, 8, 8
9, 9, 9, 9, 9, 9, 9, 9, 9, 9
9, 9, 9, 9, 9, 9, 9, 9, 9, 9
9, 9, 9, 9, 9, 9, 9, 9, 9, 9
9, 9, 9, 9, 9, 9, 9, 9, 9, 9
9, 9, 9, 9, 9, 9, 9, 9, 9, 9
9, 9, 9, 9, 9, 9, 9, 9, 9, 9