    # Music: 10
    # Entertainment: 24
    # News/Politics: 25
    # Education: 27
    # Science/Tech: 28
    # Comedy: 34
    # TODO: replace Comedy category with something equivalent, as there seem to be no results

categories = {
    "10": "music",
    "23": "comedy",
    "24": "entertainment",
    "25": "news/politics",
    "27": "education",
    "28": "science/tech"
}

time_periods = ["before", "during", "after"]

from fileinput import filename
import os
import json
import csv


def na(obj, key):
    return obj[key] if key in obj else "NA"

def get_info(item, category, time_period):
    snippet = item["snippet"]
    contentDetails = item["contentDetails"]
    status = item["status"]
    statistics = item["statistics"]
    return [
        item["id"],
        na(snippet, "publishedAt"),
        category,
        time_period,
        na(snippet, "title"),
        na(contentDetails, "duration"),
        na(contentDetails, "definition"),
        na(contentDetails, "caption"),
        na(status, "madeForKids"),
        na(statistics, "viewCount"),
        na(statistics, "likeCount"),
        na(statistics, "commentCount"),               
    ]

csvfile = open("data.csv", "w", newline="")
writer = csv.writer(csvfile)
writer.writerow([
    "videoId", 
    "publishedAt", 
    "category", 
    "timePeriod", 
    "title", 
    "duration", 
    "definition", 
    "caption", 
    "madeForKids", 
    "views", 
    "likes", 
    "comments"
    ])
for when in time_periods:
    for category in categories:
        filename = os.path.join(when, str(category), "videoInfo")
        print(filename)
        videoInfo = open(filename).read()
        data = json.loads(videoInfo)["items"]
        for item in data:
            writer.writerow(get_info(item, categories[category], when))
csvfile.close()