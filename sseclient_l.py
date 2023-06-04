# listen.py
import json
import datetime

import sseclient
import urllib3

def open_stream(url, headers):
    """Get a streaming response for the given event feed using urllib3."""
    http = urllib3.PoolManager()
    return http.request('GET', url, preload_content=False, headers=headers)

if __name__ == '__main__':
    url = 'http://20.51.237.16:8081/time'
    headers = {'Accept': 'text/event-stream'}
    response = open_stream(url, headers)
    client = sseclient.SSEClient(response)
    stream = client.events()

    while True:
        event = next(stream)
        json_data = json.dumps(data)
        time_gap = datetime.datetime.now().time() - json_data[1]
        print(f"event: {json_data[0]} \ntime: {time_gap}" )
#         print(f"event: {event.event} \ndata: {event.data}")
