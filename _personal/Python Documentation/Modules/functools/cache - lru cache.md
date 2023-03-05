

```python
from functools import cache
@cache
def func():
	...
```

```python
from functools import lru_cache
@lru_cache(10)
def func():
	...
```