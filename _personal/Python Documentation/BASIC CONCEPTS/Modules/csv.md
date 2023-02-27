
**Reading a csv file**

.csv:
"Antalya", "42"
"Mersin", "40"
"Erzurum", "22"
```python
import csv                                                              
with open("weather.csv") as file:                                                       
    data = list(csv.reader(file))
```

