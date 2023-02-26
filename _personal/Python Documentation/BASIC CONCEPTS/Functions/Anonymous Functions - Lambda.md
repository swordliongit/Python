### Notes:
1. Lambdas can't contain statements
---

**func is now a function returning arg and can be called like func(3):**
```python
func = lambda arg: arg*arg
multiparam_func = lambda x, y: x*y
```
---
**Lambda List Comprehension:**
```python
is_even_list = [lambda arg = x: arg*10 for in range(1, 5)]
```
**Iterate on each lambda function and invoke the function to get the calculated value:**
```python
for item in is_even_list:
	print(item())
```