
**How to kill a running .exe(process)**
```python
import psutil
PROCNAME = "Master Modem Odoo.exe"
for proc in psutil.process_iter():
	# check whether the process name matches
	if proc.name() == PROCNAME:
		proc.kill()
```
