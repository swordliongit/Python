# import requests
# import json
# import cv2
# import subprocess
# import re


# def fetch_streams() -> dict:
#     try:
#         response = requests.post(
#             'https://dd.swordlion.org/iptv/streams', headers={"Content-Type": "application/json"}, json={}
#         )
#         response.raise_for_status()  # This will raise an HTTPError for bad responses
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f'Failed to fetch streams: {e}')
#         return {}


# def download_partial_file(url: str, local_filename: str, byte_range: int = 1024 * 1024):
#     headers = {'Range': f'bytes=0-{byte_range - 1}'}
#     with requests.get(url, headers=headers, stream=True) as r:
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192):
#                 f.write(chunk)


# def parse_mkvinfo_output(mkvinfo_output: str) -> dict:
#     info = {}
#     current_track = None
#     current_chapter = None

#     for line in mkvinfo_output.splitlines():
#         line = line.strip()

#         if (
#             line.startswith("+ EBML head")
#             or line.startswith("+ Segment information")
#             or line.startswith("+ Tracks")
#         ):
#             continue

#         if line.startswith("| + Track") or line.startswith("|  + Track"):
#             current_track = {}
#             if 'tracks' not in info:
#                 info['tracks'] = []
#             info['tracks'].append(current_track)

#         if line.startswith("|  + Chapter atom"):
#             current_chapter = {}
#             if 'chapters' not in info:
#                 info['chapters'] = []
#             info['chapters'].append(current_chapter)

#         key_value_match = re.match(r"\|?\s*\+ ([^:]+): (.+)", line)
#         if key_value_match:
#             key, value = key_value_match.groups()
#             if current_track is not None:
#                 current_track[key] = value
#             elif current_chapter is not None:
#                 current_chapter[key] = value
#             else:
#                 info[key] = value

#     return info


# def extract_mkv_info(file_path: str):
#     # Use mkvinfo to get metadata from the partial file
#     result = subprocess.run(
#         ['C:\\Program Files\\MKVToolNix\\mkvinfo.exe', file_path], stdout=subprocess.PIPE, text=True
#     )
#     if result.returncode != 0:
#         print(f"Failed to extract info: {result.stderr}")
#         return None

#     return parse_mkvinfo_output(result.stdout)


# streams = fetch_streams()
# if streams:
#     try:
#         # Parse the result field which is a JSON string
#         streams_list = json.loads(streams['result'])
#         stream_url = streams_list[0]['url']

#         # Download a small portion of the MKV file
#         local_filename = 'partial_stream.mkv'
#         download_partial_file(stream_url, local_filename)

#         # Extract MKV file info
#         mkv_info = extract_mkv_info(local_filename)
#         if mkv_info:
#             print(json.dumps(mkv_info, indent=2))

#         # Stream the video using OpenCV
#         cap = cv2.VideoCapture(stream_url)
#         while True:
#             ret, frame = cap.read()
#             if not ret:
#                 print("Failed to grab frame")
#                 break
#             cv2.imshow('Stream', frame)
#             if cv2.waitKey(1) == 27:  # Press 'Esc' to exit
#                 break
#         cap.release()
#         cv2.destroyAllWindows()

#     except (json.JSONDecodeError, KeyError, IndexError) as e:
#         print(f'Failed to process streams data: {e}')
# else:
#     print("No streams available")
