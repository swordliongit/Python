### Notes:
Decorators are useful when you have behavior which you want to apply to one or more functions, without having to modify the function directly. It allows for cleaner and more compact code. Good for function testing.

---
**Following code pieces do the exact same job**
```python
def decor(func):
    def wrapper():
        print("========")
        func()
        print("========")
    return wrapper


def printer():
	printer("Hello")


printer = decor(printer)
printer()
```

```python
def decor(func):
    def wrapper():
        print("========")
        func()
        print("========")
    return wrapper


@decor
def printer():
	printer("Hello")


printer()
```
---
**How to use parameters when using a decorator**
```python
def decor(func):
	def wrapper(*args, **kwargs):
		print("========")
		func(*args, **kwargs)
		print("========")
	return wrapper


@decor
def adder(x, y):
	print(x+y)


adder(2, 3)
```


