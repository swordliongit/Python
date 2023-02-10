
import time
import websockets

def client1(pipe):
    while(True):
        websockets.connect('ws://localhost:8000')
        msgfrom_server = pipe.recv()
        print(msgfrom_server)
        pipe.send(["client", time.time()])
        time.sleep(1)