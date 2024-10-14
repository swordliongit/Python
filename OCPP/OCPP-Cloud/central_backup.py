#!/ocpp/.venv/bin/python3
try:
    import websockets
    import aiohttp
except ModuleNotFoundError:
    print("This example relies on the 'websockets' and 'aiohttp' packages.")
    print("Please install them by running:")
    print()
    print(" $ pip install websockets aiohttp")
    import sys

    sys.exit(1)

import asyncio
import json
import logging
from datetime import datetime
from threading import Lock
from dotenv import load_dotenv
import os

from ocpp.routing import on
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call_result, call

load_dotenv()
logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

# Dictionary to keep track of connected charge points
connected_charge_points: dict = {}
connected_charge_points_lock = Lock()

# Global variables
headers = {
    'Content-Type': 'application/json',
    'Accept-Language': 'tr,en;q=0.9,tr-TR;q=0.8,en-US;q=0.7',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Cookie': 'session_id=528a2e7872652432189d812afcfeec0ec2806589',
}
url = "https://panel.xsarj.com/create/dc-report-device"


async def post_request(url, payload):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, data=payload) as response:
            return await response.json()


class ChargePoint(cp):
    @on("BootNotification")
    async def on_boot_notification(self, charging_station, reason, **kwargs):
        payload = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "create",
                "params": {
                    "device_id": self.id,
                    "code": "dc_boot_notification",
                    "zone": "1",
                    "create_report": True,
                    "device_update": "1",
                },
                "id": 569151295,
            }
        )
        response = await post_request(url, payload)
        return call_result.BootNotificationPayload(
            current_time=datetime.utcnow().isoformat(), interval=10, status="Accepted"
        )

    @on("Heartbeat")
    async def on_heartbeat(self):
        print("Got a Heartbeat!")
        return call_result.Heartbeat(current_time=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S") + "Z")

    @on("StatusNotification")
    async def on_status_notification(self, connector_id, connector_status, evse_id, timestamp):
        payload = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "create",
                "params": {
                    "device_id": self.id,
                    "code": connector_status,
                    "zone": evse_id,
                    "create_report": True,
                    "device_update": "1",
                },
                "id": 569151295,
            }
        )
        response = await post_request(url, payload)
        return call_result.StatusNotificationPayload()

    @on("Authorize")
    async def on_authorize(self, id_token):
        url = "https://panel.xsarj.com/ocpp/authorize"
        payload = json.dumps(id_token)
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(url, data=payload) as response:
                response_data = await response.json()
                status = response_data.get('result', {}).get('status')
                if status == "Active":
                    id_token_info = {'status': "Accepted"}
                elif status == "Passive":
                    id_token_info = {'status': "Blocked"}
                else:
                    id_token_info = {'status': "Unknown"}
                _logger.info(msg=str(response_data))
                return call_result.AuthorizePayload(id_token_info=id_token_info)

    @on("TransactionEvent")
    async def on_transaction_event(
        self,
        event_type,
        evse,
        meter_value,
        seq_no,
        timestamp,
        transaction_info,
        trigger_reason,
        **kwargs,
    ):
        transaction_info.update({'device_id': str(self.id)})
        tract_info = {'meterValue': meter_value, 'transactionInfo': transaction_info}
        payload = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "create",
                "params": {
                    "device_id": self.id,
                    "code": tract_info,
                    "zone": evse["id"],
                    "create_report": True,
                    "device_update": "1",
                },
                "id": 569151295,
            }
        )
        response = await post_request(url, payload)
        _logger.info(msg=response)
        return call_result.TransactionEventPayload()

    @on("RequestStartTransaction")
    async def on_request_start_transaction(self, id_token, remote_start_id, **kwargs):
        _logger.info(msg=f"Received kwargs: {kwargs}")
        target_charge_points = kwargs['custom_data']['target_charge_points']
        evse_id = kwargs['custom_data']['evse_id']
        _logger.info(msg=str(f"Connected CPs: {connected_charge_points}"))
        _logger.info(msg=str(f"Target CPs: {target_charge_points}"))

        try:
            with connected_charge_points_lock:
                for cp_id, cp_instance in list(connected_charge_points.items()):
                    if cp_instance.id in target_charge_points:
                        request = call.RequestStartTransactionPayload(
                            id_token=id_token, evse_id=int(evse_id), remote_start_id=remote_start_id
                        )
                        _logger.info(msg=f"Sending request to {cp_instance.id} with payload: {request}")
                        try:
                            response = await cp_instance.call(request)
                            _logger.info(msg=f"Received response from {cp_instance.id}: {response}")

                            if response.status == "Accepted":
                                payload = json.dumps(
                                    {
                                        "jsonrpc": "2.0",
                                        "method": "create",
                                        "params": {
                                            "device_id": cp_id,
                                            "code": "dc_transaction_accepted",
                                            "zone": evse_id,
                                            "create_report": True,
                                            "device_update": "1",
                                        },
                                        "id": 569151295,
                                    }
                                )
                                await post_request(url, payload)
                                _logger.info(msg=f"Transaction started at {cp_instance.id}")
                            elif response.status == "Rejected":
                                payload = json.dumps(
                                    {
                                        "jsonrpc": "2.0",
                                        "method": "create",
                                        "params": {
                                            "device_id": cp_id,
                                            "code": "dc_transaction_rejected",
                                            "zone": evse_id,
                                            "create_report": True,
                                            "device_update": "1",
                                        },
                                        "id": 569151295,
                                    }
                                )
                                await post_request(url, payload)
                                _logger.info(msg=f"Transaction request failed at {cp_instance.id}")
                            else:
                                _logger.info(msg=f"Unhandled response status: {response.status}")

                        except Exception as e:
                            _logger.error(msg=f"Error sending request to {cp_instance.id}: {e}")
                            continue
        except Exception as e:
            _logger.error(msg=f"Unexpected error: {e}")

    @on("RequestStopTransaction")
    async def on_request_stop_transaction(self, transaction_id, **kwargs):
        _logger.info(msg=f"Received kwargs: {kwargs}")
        payload = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "create",
                "params": {
                    "device_id": self.id,
                    "code": "dc_transaction_stopped",
                    "zone": "1",
                    "create_report": True,
                    "device_update": "1",
                },
                "id": 569151295,
            }
        )
        await post_request(url, payload)
        _logger.info(msg=f"Transaction stopped at {self.id}")

        for cp_id, cp_instance in connected_charge_points.items():
            request = call.RequestStopTransactionPayload(transaction_id=transaction_id)
            await cp_instance.call(request)


async def on_connect(websocket, path):
    try:
        requested_protocols = websocket.request_headers["Sec-WebSocket-Protocol"]
    except KeyError:
        logging.info("Client hasn't requested any Subprotocol. Closing Connection")
        return await websocket.close()
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return await websocket.close()

    if websocket.subprotocol:
        logging.info("Protocols Matched: %s", websocket.subprotocol)
    else:
        logging.warning(
            "Protocols Mismatched | Expected Subprotocols: %s, but client supports %s | Closing connection",
            websocket.available_subprotocols,
            requested_protocols,
        )
        return await websocket.close()

    charge_point_id = path.strip("/")
    charge_point = ChargePoint(charge_point_id, websocket)
    connected_charge_points[charge_point_id] = charge_point

    payload = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "create",
            "params": {
                "device_id": charge_point_id,
                "code": "dc_connected",
                "zone": "1",
                "create_report": True,
                "device_update": "1",
            },
            "id": 569151295,
        }
    )
    await post_request(url, payload)

    try:
        await charge_point.start()
    except websockets.exceptions.ConnectionClosedError:
        logging.error(f"Connection to charge point {charge_point_id} closed unexpectedly.")
    finally:
        del connected_charge_points[charge_point_id]
        payload = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "create",
                "params": {
                    "device_id": charge_point_id,
                    "code": "dc_disconnected",
                    "zone": "1",
                    "create_report": True,
                    "device_update": "1",
                },
                "id": 569151295,
            }
        )
        await post_request(url, payload)


async def start_server():
    async with websockets.serve(
        on_connect, os.getenv("HOST"), os.getenv("PORT"), subprotocols=["ocpp2.0.1"]
    ) as server:
        await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(start_server())
