#goal: look at json of YT history and categorize it into most watched videos, 
#most watched users/artists. Other goals are to separate the history by years/months/weeks/days,
#to be able to get history from a specific time frame, ... . The user should be able to search for
#the first time they watched a video

import json
from collections import Counter

titleList =	[] #stores video titles retrieved
channelList = [] #stores channel names in a list

with open('MyActivity.json', 'r') as f:
    dataFile = json.load(f)

#populates the titleList and channelList to the numRecords most played videos and channels ever
def getMostPlayedAllTime(numRecords):
    for entry in dataFile:
        title = entry.get("title")
        #print("before: ", title)
        dateStamp = entry.get("time")        #get data and time info from entry
        dateStamp = dateStamp.split("-")     #split the data into a list of [year, month, day+time]
        timeStamp = dateStamp[2].split("T")  #split day+time into [day, time] list named timestamp
        dateStamp[2] = timeStamp[0]          #store the day in the 2nd index of dateStamp
        timeStamp = timeStamp[1].split(":")  #split timestamp into [hour, minute, second+Z]
        if timeStamp[2].endswith("Z"):
            timeStamp[2] = timeStamp[2][:-1] #remove Z from second of the timeStamp


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

#gets most played channels and videos in a given month
def getMostPlayedMonth(numRecords, month, year):
    #set titleList and channelList to empty
    titleList =	[]
    channelList = [] 
    
    for entry in dataFile:
        title = entry.get("title")
        #print("before: ", title)
        dateStamp = entry.get("time")        #get data and time info from entry
        dateStamp = dateStamp.split("-")     #split the data into a list of [year, month, day+time]
        timeStamp = dateStamp[2].split("T")  #split day+time into [day, time] list named timestamp
        dateStamp[2] = timeStamp[0]          #store the day in the 2nd index of dateStamp
        timeStamp = timeStamp[1].split(":")  #split timestamp into [hour, minute, second+Z]
        if timeStamp[2].endswith("Z"):
            timeStamp[2] = timeStamp[2][:-1] #remove Z from second of the timeStamp

        #check if video month matches desired month
        if(month == int(dateStamp[1]) and year == int(dateStamp[0])):
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
    print(listCounts.most_common(numRecords))
    channelCounts = Counter(channelList)
    print(channelCounts.most_common(numRecords))
    #print(titleList)
    #print(channelList)


if __name__ == "__main__":
    getMostPlayedMonth(10, 8, 2024)
    #getMostPlayedAllTime(10)