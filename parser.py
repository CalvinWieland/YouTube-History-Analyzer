#goal: look at json of YT history and categorize it into most watched videos, 
#most watched users/artists. Other goals are to separate the history by years/months/weeks/days,
#to be able to get history from a specific time frame, ...

import json
from collections import Counter

titleList =	[] #stores video titles retrieved
channelList = [] #stores channel names in a list

with open('MyActivity.json', 'r') as f:
    dataFile = json.load(f)

for entry in dataFile:
    title = entry.get("title")
    #print("before: ", title)
    timestamp = entry.get("time")
    timestamp = timestamp.split("-")
    if title.startswith("Watched ") and title != "Watched https://www.youtube.com/watch?v\u003d":
        #title = title.strip("Watched ") #remove "Watched " from list entry
        title = title[8:]
        #print("after:  ", title)
        if "subtitles" in entry: #if there's a subtitles section
            subtitle = entry.get("subtitles")[0] #get "subtitle"
            if "name" in subtitle: #if there's a channel name
                channelName = subtitle.get("name")
                if channelName.endswith(" - Topic"):
                    #print(channelName)
                    channelName = channelName[:-8]
                    #print(channelName)
                titleList.append(title) #append title to titleList
                channelList.append(channelName) #append channel name to channelList

listCounts = Counter(titleList)
print(listCounts.most_common(10))
channelCounts = Counter(channelList)
print(channelCounts.most_common(10))
#print(titleList)
#print(channelList)


        



#titles = [entry["title"] for entry in dataFile if "title" in entry] #load every title of every video into a list
#counts = Counter(titles)  #count the number of occurrences of each title
#print(counts.most_common(10)) #print the 10 most common titles to the screen