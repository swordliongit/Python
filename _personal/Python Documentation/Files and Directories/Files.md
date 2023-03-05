
**Opening a file to read**
```python
file = open("fname", "r") # files are opened with r default. You can omit "r" here
...
file.close()
```

---
**File operations**
```python
file.readlines() # -> list of elements in the line
file.read() # -> string --- Reads all of the file. Places the cursor at the end after executing
file = open("storage.txt", 'w') # -> open() has default "r" already
file = open(r"C\Users\Downloads\st.txt", "w") # -> r to bypass special characters. (raw) 
file = open("../files/doc.txt", "w") # -> .. goes up 1 directory
file.writelines(str(list)) # -> list
file.write("txt") # -> string
```

---
**Opening files with With Context Manager**
```python
with open("filename", "w") as f:
	f.write(content)
# automatically handles closing the file
```

---
**Checking if a file is empty or not**
```python
import os
if os.stat("filename.txt").st_size == 0:
	... # if empty
```
