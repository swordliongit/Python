import asyncio
import websockets
import json


async def send_remote_start_request():
    async with websockets.connect(
        "ws://192.168.100.44:9000/CP_1", subprotocols=["ocpp1.6"]
    ) as websocket:
        request_payload = {
            "connectorId": 1,
            "idTag": "0123456789ABCD",  # Replace with the actual ID tag
        }

        request = [
            2,
            "e40f3024-5c91-4e8d-b514-35ec785f4713",
            "RemoteStartTransaction",
            request_payload,
        ]
        await websocket.send(json.dumps(request))

        response = await websocket.recv()
        print("Received response:", response)


if __name__ == "__main__":
    asyncio.run(send_remote_start_request())
