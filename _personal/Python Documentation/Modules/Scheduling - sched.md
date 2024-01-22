```python
import sched
import time


def foo(name):
    print("testing " + name)


def poo(name):
    print("testing " + name)


s = sched.scheduler(time.time, time.sleep)

s.enter(1, 1, foo, ("foo",))
s.enter(3, 1, poo, ("poo",))

s.run()
```

```
testing foo
testing poo
```