## Notes:
1. Used when we want to fetch elements from a large list, useful for performance
2. Don't use for small files/data
3. Called only once in a statement, will provide 0 if called again

**Generators act like a for loop because it's an iterable**
```python
def generator():
	for i in range(10):
		yield i


for i in generator():
	print(i)
```
---
**Yielding multiple values**
```python
def generator():
	for i, j in zip(range(5), range(5, 10)):
		yield i, j # -> (i, j) tuple
```
---
**Generator Comprehension. Result is a tuple**
```python
generated = (i for i in range(10))
```

