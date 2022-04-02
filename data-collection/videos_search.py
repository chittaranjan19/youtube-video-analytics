import googleapiclient.discovery
from collections import defaultdict 
from pprint import pprint
from pathlib import Path
import os, time

def build_requests(youtube):
    requests = defaultdict(lambda: defaultdict(lambda: []))
    time_periods = {
        "before": ("2019-01-01T00:00:00Z", "2020-03-01T00:00:00Z"), 
        "during": ("2020-04-01T00:00:00Z", "2021-07-01T00:00:00Z"), 
        "after": ("2021-08-01T00:00:00Z", "2022-03-01T00:00:00Z")
     } # represents before, during, and after pandemic

    # https://www.googleapis.com/youtube/v3/videoCategories
    # Music: 10
    # Entertainment: 24
    # News/Politics: 25
    # Education: 27
    # Science/Tech: 28
    # Comedy: 34
    # TODO: replace Comedy category with something equivalent, as there seem to be no results
    categories = [10, 24, 25, 27, 28, 34]
    for when in time_periods:
        for category in categories:
            request = youtube.search().list(
                part="id",
                type="video",
                videoCategoryId=category,
                maxResults=50,
                order="searchSortUnspecified",
                publishedAfter=time_periods[when][0],
                publishedBefore=time_periods[when][1]
            )
            requests[when][category].append(request)
    return requests

def save_response(when, category, response):
    path = Path(os.path.join(when, category))
    path.mkdir(exist_ok=True, parents=True)
    filename = os.path.join(when, category, "ids")
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