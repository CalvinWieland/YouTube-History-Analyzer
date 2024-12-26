import json
from collections import Counter

with open('SmallerActivity.json', 'r') as f:
    dataFile = json.load(f)

#goal: look at json of YT history and categorize it into most watched videos, 
#most watched users/artists. Other goals are to separate the history by years/months/weeks/days,
#to be able to get history from a specific time frame, ...

for entry in dataFile:
    title = entry.get("title")
    timestamp = entry.get("time")
    timestamp = timestamp.split("-")
    if "Watched " in title:
        if "subtitles" in entry:
            user = entry.get("subtitles")[0].get("name")
        title = title.strip("Watched ")


titles = [entry["title"] for entry in dataFile if "title" in entry]
counts = Counter(titles)
print(counts.most_common(10))