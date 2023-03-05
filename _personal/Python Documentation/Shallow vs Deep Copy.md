```python
list1 = [1, 2, 3]
list2 = list1
```
Now if we assign to list2, it will also change list1, this is a shallow copy:
```python
list2[0] = 4
```
---
We may think of doing a list slice copying:
```python
list2 = list1[:]
```
Now if we assign to list2, it won't change list1 but there's a catch:
```python
list2[0] = 4
```
If the list is a nested list:
```python
list1 = [1, 2, 3, [4, 5]]
list2 = list1[:]
```
If we assign to the sublist, it will also change the list1's sublist, this is also a shallow copy:
```python
list2[3][0] = 6
```
==To solve the shallow copy problem, use deep copy:==
```python
from copy import deepcopy
list2 = deepcopy(list1)
list2[3][0] = 6
```
