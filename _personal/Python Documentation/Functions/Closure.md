### Notes
Maintains the value of the variables between function calls. Counters unnecessary global variable usage.

---
```python
def outer_function():
    mlist = []
    def inner_function(item):
        mlist.append(item)
        print(mlist)
    return inner_function
  

closure = outer_function()
closure(1) # mlist = [1]
closure(2) # mlist = [1, 2]
```

