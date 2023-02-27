### Notes:
1. .json files must enclose in [] or {}

**Reading from a json file**
```python
import json                                                      
with open("questions.json") as file:                                                    
    data = json.loads(file.read())  -> list or dict
```
**Writing to a json file**
```python
import json                                                      
with open("questions.json", "w") as file:                                                
    json.dump(data, file, indent=5)
```