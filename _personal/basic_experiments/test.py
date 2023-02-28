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