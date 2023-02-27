
**Where - Filtering iterables**
```python
from pipe import where
arr = [0, 1, 2, 3, 5, 6]
print(list(arr | where(lambda x: x > 5)))
```
**Output**
[6]

---
**select - Applies the function to every element of the iterable**
```python
arr = [0, 1, 2, 3, 5, 6]
print(list(arr | select(lambda x: x**2))) # takes power of every element in the iterable
```
**Combining multiple functions**
```python
arr = [0, 1, 2, 3, 5, 6]
print(list(arr
		| where(lambda x: x > 5)
		| select(lambda x: x**2))) # filter elements larger than 5 and raise them to the power of 2
```
---
**chain - Chaining multiple iterators together in 1 iterator**
```python
arr = [[0, 1, [2]], [[3, 4]]]
print(list(arr | chain))
```
**Output**
[0, 1, [2], [3, 4]]

---
**traverse - Flatten out a deeply nested iterator, Recursively unfolding iterables**
```python
arr = [[0, 1, [2]], [[3, 4]]]
print(list(arr | traverse))
```
**Output**
[0, 1, 2, 3, 4]

**Getting values from a dict and flattening the resulting list**
```python
fruits = [
            {"name": "apple", "price":[2,5]},
            {"name": "orange", "price": 4},
            {"name", "grape", "price": 5}
        ]
print(list(fruits
		| select(lambda fruit: fruit["price"])
		| traverse)) # [2, 5, 4, 5]
```
**Output**
[2, 5, 4, 5]

---

**groupby - dividing the iterable into chunks based on conditions**
```python
arr = (0, 1, 2, 3, 4, 5, 6)
print(list(arr
		| groupby(lambda x: "Even" if x % 2==0 else "Odd") # -> [('Even', <itertools._grouper at 0x7fbea8030550>), ('Odd', <itertools._grouper at 0x7fbea80309a0>)]
		| select(lambda x: {x[0]: list(x[1])} ))) # -> [{'Even': [0, 2, 4, 6]}, {'Odd': [1, 3, 5]}]
```
**selecting items larger than 2**
```python
arr = [0, 1, 2, 3, 4, 5, 6]
print(list(arr
	| groupby(lambda x: "Even" if x % 2==0 else "Odd")
	| select(lambda x: {x[0]: list(x[1] | where(lambda x: x > 2))}))) # -> [{'Even': [4, 6]}, {'Odd': [3, 5]}]
```
---
**dedup - Removing duplicates from an iterable**
```python
arr = [1, 1, 1, 2, 3, 4, 4, 5]
print(list(arr | dedup))
```
**Output**
[1, 2, 3, 4, 5]

**dedup can determine the uniqueness of the selection,
retrieves first occurances of elements smaller than or equal to 5 and remove their duplicates**
```python
arr = [1, 2, 2, 3, 4, 5, 6, 6, 7, 9, 3, 3, 1]
print(list(arr | dedup(lambda key: key < 5)))
```
**Output**
[1, 5]

---
