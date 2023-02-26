
**Python automatically stores the value of the last expression in
the interpreter to a particular variable called _
You can also assign these value to another variable if you want.**
```python
>>> 5 + 4
9
>>> _     # returns the result of the above expression
9
>>> _ + 6
15
```
---
**Used in loop as anonymous filler**
```python
for _ in range(0, 5):
	...
```
---
**Ignoring values**
```python
a, _, b = (1, 2, 3) # a = 1, b = 3
```
---
**Separating digits of numbers**
```python
million = 1_000_000 # prints 1000000
binary = 0b_0010
octa = 0o_64
hexa = 0x_23_ab
```
