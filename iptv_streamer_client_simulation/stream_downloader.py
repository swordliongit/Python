import requests
import json
import cv2
import subprocess
from pymkv import MKVFile


def fetch_streams() -> dict:
    try:
        response = requests.post(
            'https://dd.swordlion.org/iptv/streams', headers={"Content-Type": "application/json"}, json={}
        )
        response.raise_for_status()  # This will raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Failed to fetch streams: {e}')
        return {}


def download_file(url: str, local_filename: str):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)


def extract_mkv_info(file_path: str):
    mkv = MKVFile(file_path)

    for track in mkv.tracks:
        print(f"Track ID: {track.track_id}")
        print(f"Track Type: {track.track_type}")
        print(f"Language: {track.language}")
        print(f"Codec: {track.codec}")
        if track.track_type == 'subtitles':
            print("This is a subtitle track.")
        print()

    # Get detailed info about the MKV file using mkvinfo
    result = subprocess.run(['mkvinfo', file_path], stdout=subprocess.PIPE, text=True)
    print(result.stdout)


streams = fetch_streams()
if streams:
    try:
        # Parse the result field which is a JSON string
        streams_list = json.loads(streams['result'])
        stream_url = streams_list[0]['url']

        # Download the MKV file
        local_filename = 'stream.mkv'
        download_file(stream_url, local_filename)

        # Extract MKV file info
        extract_mkv_info(local_filename)

        # Stream the video using OpenCV
        cap = cv2.VideoCapture(local_filename)
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
