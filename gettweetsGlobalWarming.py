from classtweetgetter import TweetGetter
from classtweetreader import TweetReader
import datetime

myTweets=TweetGetter("twitterdata_query=Global_Warming_time=04_01_0151_lastid=285934106267762687.pkl")
myTweets.query('"Global Warming"',160000, False)

#Write log file
with open("logGlobalWarming.txt", "a") as myfile:
    now = datetime.datetime.now()
    timestr=now.strftime("%d_%m_%H%M")
    myfile.write(timestr+"\n")
    readTweet=TweetReader(filename=None, dict=myTweets.twitterdict)
    print "Total number of tweets: " + str(len(myTweets.twitterdict.keys()))
    myfile.write("Total number of tweets: " + str(len(myTweets.twitterdict.keys()))+"\n")
    udict=readTweet.getUsernames()
    print "Total number of users: " + str(len(udict.keys()))
    myfile.write("Total number of users: " + str(len(udict.keys()))+"\n")
    for item in udict.items():
        if item[1]<3:
            del udict[item[0]]
    print "Total number of users with 3 tweets or more: " + str(len(udict.keys()))
    myfile.write("Total number of users with 3 tweets or more: " + str(len(udict.keys()))+"\n")

#modify this script
with open("gettweetsGlobalWarming.py", "r") as myfile:
    mytext=myfile.read()

st=mytext.index("myTweets=TweetGetter")+22
end=mytext.index('")', st)

newtext=mytext[0:st] + myTweets.savedname + mytext[end:]
#print newtext
print "GlobalWarming finished"

with open("gettweetsGlobalWarming.py", "w") as myfile:
    myfile.write(newtext)