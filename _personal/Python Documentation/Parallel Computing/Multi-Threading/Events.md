### Notes
1. Events can stop a thread/program until it's set.


**This funtion won't continue until the event is set**
```python
# main.py
def main(event):
    while not event.is_set():         
        pass
```

```python
# other.py
from threading import Event

event = Event()
def func():
	...
	event.set()
```
