
**Example : Creating a directory from a filename path**
```python
def create_directory(filename): # create directory based on filename e.g. = "./hosts/"
    # Extract the directory name from the file path
    dirname = os.path.dirname(filename)
    # Create the directory if it does not exist
    if not os.path.exists(dirname):
        os.makedirs(dirname)
```
---
**Listing directory content**
```python
content = os.listdir("path/to/directory/") # -> list
```
---
**Concatenating path names**
```python
from os.path import join
full_path = join("C:/odoo-15/odoo", "bla.txt") # join(path, *paths) -> full_path == "C:/odoo-15/odoo/bla.txt"
```
---
**Checking if a path name is a directory or not**
```python
from os.path import isdir
if isdir("path/to/dir/"):
	... # if is directory
```
