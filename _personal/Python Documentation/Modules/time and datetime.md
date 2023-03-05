```python
import time
print(time.strftime("%Y")) #year format %A : current day - Thursday, a% - Thu

import datetime
print(datetime.datetime.now())
print(datetime.datetime.today())
```
---
**Checking how much time has passed between points**
```python
from time import perf_counter
start = perf_counter()
...
end = perf_counter()
print(end-start)
```
