from multiprocessing import Pipe, Process
import websockets

from client import client1
import time

def server(websocket):
    while(True):
        websocket.send(["server", time.time()])
        msgfrom_client = websocket.recv()
        print(msgfrom_client)
        time.sleep(1)
        
if __name__ == "__main__":
    pipe_end_server, pipe_end_client = Pipe()
    
    start_server = websockets.serve(server, "localhost", 8000)
    
    p1 = Process(target=server, args=(pipe_end_server,))
    p2 = Process(target=client1, args=(pipe_end_client,))
    p1.start()
    p2.start()
    
    