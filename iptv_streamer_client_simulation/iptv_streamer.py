import json
import requests
import cv2


def fetch_streams() -> dict:
    try:
        response = requests.post(
            'https://dd.swordlion.org/iptv/streams', headers={"Content-Type": "application/json"}, json={}
        )
        print(response.json())
        response.raise_for_status()  # This will raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Failed to fetch streams: {e}')
        return {}


streams = fetch_streams()
if streams:
    try:
        # Parse the result field which is a JSON string
        streams_list = json.loads(streams['result'])
        stream_url = streams_list[0]['url']
        cap = cv2.VideoCapture(stream_url)
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break
            cv2.imshow('Stream', frame)
            if cv2.waitKey(1) == 27:  # Press 'Esc' to exit
                break
        cap.release()
        cv2.destroyAllWindows()
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        print(f'Failed to process streams data: {e}')
else:
    print("No streams available")
