
It has built-in exception handling and no need to close the file, it's automated:
```python
with open("path/to/file", "w") as file:
    file.read()
```