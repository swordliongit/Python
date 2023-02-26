
**Variable Arguments using*** *
```python
def func(*args): # arguments are packed into a tuple
	for item in args:
		sum += item
	print(sum)


func(1, 2) # variable number of arguments
func(1, 2, 3)
```
**Output**
3
6

---
**Variable Arguments using*** **
```python
def func(**kwargs): # arguments are packed into a dictionary
	for k, v in kwargs.items():
		print(k, v)


func(key1="value1", key2="value2") # variable number of keyword arguments
func(key1="value1", key2="value2", key3="value3")
```
**Output**
key1 "value1"
key2 "value2"
-
key1 "value1"
key2 "value2"
key3 "value3"

---
**Unpacking Collections**
```python
 def func(a, b, c): # a=1, b=2, c=3
	print(a+b+c)


mlist = [1,2,3]
func(*mlist) # unpacked as 1 2 3
```
**Output**
6

```python
def func(*args):
	res = 0
	for item in args:
		res+=item
	return res


mlist1 = [1,2,3]
mlist2 = [4,5,6,7]
mlist3 = [8,9]
print(func(*mlist1, *mlist2, *mlist3)) # evaluates to : func(1,2,3,4,5,6,7,8,9)
```
**Output**
45

---
**Unpacking Strings**
```python
a = [*"Python"] # a = ['P', 'y', 't', 'h', 'o', 'n']
*a, = "Python"  # a = ['P', 'y', 't', 'h', 'o', 'n']
```
, operator automatically creates a tuple in Python


---
**Splitting Collections**
```python
 my_list = [1, 2, 3, 4, 5, 6]
a, *b, c = my_list # first value goes into a, last value goes into c, all inbetween goes to b

print(a) # 1
print(b) # [2, 3, 4, 5]
print(c) # 6
```
**Output**
1
[2, 3, 4, 5]
6

---
**Merging Collections**
```python
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list) # [1, 2, 3, 4, 5, 6]
```
**Output**
[1, 2, 3, 4, 5, 6]

```python
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict) # {"A": 1, "B": 2, "C": 3, "D": 4}
```
**Output**
{"A": 1, "B": 2, "C": 3, "D": 4}

---
