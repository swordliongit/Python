import json
import requests
import cv2
import subprocess
import os


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


def get_subtitle_streams(file_path):
    try:
        cmd = f"ffmpeg -i {file_path} -c copy -f null -"
        result = subprocess.run(cmd, shell=True, stderr=subprocess.PIPE, universal_newlines=True)
        subtitle_streams = []
        for line in result.stderr.split('\n'):
            if 'Subtitle' in line:
                subtitle_streams.append(line)
        return subtitle_streams
    except Exception as e:
        print(f"Failed to get subtitle streams: {e}")
        return []


def play_stream_with_subtitles(stream_url, subtitle_index):
    # Create a named pipe for ffmpeg output
    pipe = 'pipe:1'

    # Construct ffmpeg command to add subtitles
    cmd = [
        'ffmpeg',
        '-i',
        stream_url,
        '-vf',
        f'subtitles={stream_url}:si={subtitle_index}',
        '-f',
        'rawvideo',
        '-pix_fmt',
        'bgr24',
        pipe,
    ]

    # Start ffmpeg process
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Read video frames from ffmpeg process
    while True:
        raw_frame = process.stdout.read(640 * 480 * 3)
        if len(raw_frame) != (640 * 480 * 3):
            break
        frame = np.frombuffer(raw_frame, np.uint8).reshape((480, 640, 3))
        cv2.imshow('Stream', frame)
        if cv2.waitKey(1) == 27:  # Press 'Esc' to exit
            break

    # Release resources
    process.stdout.close()
    process.stderr.close()
    process.wait()
    cv2.destroyAllWindows()


streams = fetch_streams()
if streams:
    try:
        # Parse the result field which is a JSON string
        streams_list = json.loads(streams['result'])
        stream_url = streams_list[0]['url']

        # Fetch subtitle streams
        subtitle_streams = get_subtitle_streams(stream_url)
        print("Available subtitle streams:")
        for idx, subtitle in enumerate(subtitle_streams):
            print(f"{idx}: {subtitle}")

        # Select a subtitle index
        subtitle_index = int(input("Enter the subtitle stream index to use: "))

        # Play the stream with the selected subtitle
        play_stream_with_subtitles(stream_url, subtitle_index)
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        print(f'Failed to process streams data: {e}')
else:
    print("No streams available")
