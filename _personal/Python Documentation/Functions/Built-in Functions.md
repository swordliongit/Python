
**Common functions**
```python
input() -> str
len(object)
isinstance(item, type)
type(item)
round(float, digit)
sum(iterable)
print()
exit("msg") # shows red text
help(func_name)
all(iterable) -> True if all elements are True or the list is empty
```
---
**Map**
Calls the function on each element of the iterable
```python
map(func, *iterables) -> map object
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

---
**Filter**
Returns an iterator yielding those items of iterable for which function(item) is True. If function is None, return the items that are True.
```python
filter(function or None, iterable) -> filter object
```
---
```python
# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]
# result contains odd numbers of the list

result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))
```
**Dictionary Filter**
```python
# Original dictionary
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Use filter() to filter out odd values
filtered_dict = dict(filter(lambda x: x[1] % 2 == 0, d.items()))
```
**Output**
{'b': 2, 'd': 4}

---
**Sorted**
```python
sorted(iterable, /, *, key=None, reverse=False) -> iterable
```
---
```python
sorted_list_of_dicts = sorted(list_of_dicts, key=lambda x: x['x_ip']) # how to sort a list of dicts
sorted_dict = sorted(mydict) # sort by keys
sorted_dict = sorted(mydict, key=mydict.get) # sort by values
```
