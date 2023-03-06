
**Shutil way**

*Creating  a zip file named "output" from the folder named "folder"*
```python
import shutil
shutil.make_archive("output", "zip", "folder")
```

**Zipfile way**

*Creating a zip file named test.zip with the 2 files*

```python
from zipfile import ZipFile
```

```python
with ZipFile("test.zip", "w") as archive:
    archive.write("weather.csv")
    archive.write("test.ini")
```

*Extracting the zip file into directory named dir*
```python
with ZipFile("test.zip", "r") as archive:
    archive.extractall("dir")
```