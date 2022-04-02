import googleapiclient.discovery
from collections import defaultdict 
from pprint import pprint
from pathlib import Path
import os
import time
import json


PARTS = [
    "id", 
    "contentDetails", 
    "liveStreamingDetails", 
    "localizations", 
    "player", 
    "recordingDetails", 
    "snippet", 
    "statistics", 
    "status", 
    "topicDetails"
    ]
def get_ids():
    all_ids = defaultdict(lambda: defaultdict(lambda: []))
    time_periods = ["before", "during", "after"]
    categories = [10, 24, 25, 27, 28, 34]
    for when in time_periods:
        for category in categories:
            ids = open(os.path.join(when, str(category), "ids")).read()
            ids = ids.replace("\'", "\"")
            ids = json.loads(ids)
            video_ids = [item["id"]["videoId"] for item in ids["items"]]
            all_ids[when][category] = video_ids
    return all_ids

def build_requests(youtube):
    all_ids = get_ids()
    requests = defaultdict(lambda: defaultdict(lambda: []))
    for when in all_ids:
        for category in all_ids[when]:
            video_ids = all_ids[when][category]
            if video_ids:   # ensure no requests are made without videoIds
                ids = ",".join(video_ids)
                # print(video_ids)
                # print(len(video_ids))
                # print(ids)
                # print(ids.count(","))
                request = youtube.videos().list(
                    part=",".join(PARTS),
                    id=ids
                )
                requests[when][category].append(request)
    return requests

def save_response(when, category, response):
    path = Path(os.path.join(when, category))
    path.mkdir(exist_ok=True, parents=True)
    filename = os.path.join(when, category, "videoInfo")
    pprint(response, stream=open(filename, "w"))

def main(youtube):
    requests = build_requests(youtube)
    for when in requests:
        for category in requests[when]:
            print("Fetching", when, category)
            try:
                response = requests[when][category][0].execute() # inner list always has exactly one element for now
                save_response(when, str(category), response)
                print("Fetched", when, category)
                time.sleep(1)
            except Exception as e:
                print(e)
    
if __name__ == "__main__":
    API_KEY = open(".apikey").read().strip()
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = API_KEY)
    main(youtube)