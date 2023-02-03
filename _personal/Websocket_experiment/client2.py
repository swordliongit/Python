import asyncio
import websockets
 
async def test(client_id):
    async with websockets.connect('ws://localhost:8000') as websocket:
        # send client identifier to the server
        await websocket.send(client_id)
        response = await websocket.recv()
        print(response)
        await asyncio.sleep(10)
        return True

 
async def run_client(client_id):
    closed = False
    while not closed:
        closed = await test(client_id)
        
 
 
asyncio.get_event_loop().run_until_complete(run_client("client2"))