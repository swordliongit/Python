
```python
try:
    ...
except ValueError: # Catch all exceptions if empty e.g. except:
    ...
else: # if not caught anything
    ...
finally: # run this no matter what
```
---
**How to get name and type of the caught exception**
```python
try:
	raise Exception("Dummy Exception")
except Exception as e:
	print(e.__class__.__name__) # prints the name of exception -> Exception
	print(e.args[0]) # prints the exception's message -> Dummy Exception
```