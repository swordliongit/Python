#### Notes:
1. When you import a module, function definitions and calls are executed.

**Importing modules:**
```python
# module:            # main:                      # alternative:
def func():         from module import func     import module       
    print("")       func()                      module.func()
```
---
**Running code parts only if the file is the main file(starter):**

```python
if __name__ == "__main__":
    print("ran from here")
```
**if module is ran, its __name__ is __main__, if the module is imported and executed from somewhere else, then __name__ is name of the module itself.**

---
**Directory Imports:**
```python
# testD/test.py     # main.py
def func():         from testD.test import func
    print("")       func()
```
---
**Relative Imports:**
```python
# module_2nd.py     # module_base.py
gl_var = 10         from .module_2nd import gl_var
```
Note : 1 dot means the module is in the same directory, 2 means outside of the current directory.
