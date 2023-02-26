### Notes
Calls the function on each element of the iterable

```python
map(func, *iterables) # -> map object
```
---
```python
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
```
**Output**
[2, 4, 6, 8]

