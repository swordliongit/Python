### Notes
1. *recv() function stops the process until it recieves data from the other end of the pipe.*

**End to End Pipe Communication**
```python
from multiprocessing import Pipe, Process
import time


def server(pipe):
	while(True):
		pipe.send(["server", time.time()])
		msgfrom_client = pipe.recv()
		print(msgfrom_client)
		time.sleep(1)


def client(pipe):
	while(True):
		msgfrom_server = pipe.recv()
		print(msgfrom_server)
		pipe.send(["client", time.time()])
		time.sleep(1)


if __name__ == "__main__":
	pipe_end_server, pipe_end_client = Pipe()
	p1 = Process(target=server, args=(pipe_end_server,))
	p2 = Process(target=client, args=(pipe_end_client,))
	p1.start()
	p2.start()
```
**Output(2 lines every 1 second):**
['server', 1677571014.013562]
['client', 1677571014.0225604]
['server', 1677571015.0245261]
['client', 1677571015.0245261]
['server', 1677571016.0258203]
['client', 1677571016.0258203]
['server', 1677571017.0284038]
['client', 1677571017.0364022]
['server', 1677571018.0416312]
['client', 1677571018.0416312]
['server', 1677571019.042912]
['client', 1677571019.0449164]
['server', 1677571020.0469146]

---
**Polling a Pipe end**
```python
if not pipe_end_server.poll(timeout=5):
	print("server is offline!")
```