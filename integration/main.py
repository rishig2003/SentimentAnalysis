import twitterbot as tb
import pandas as pd
import os

#tells how many times to scroll to fetch tweets. the larger the more tweets can be fetched and more time the code will take
rate =5



print(os.getcwd())
hashtag = ["","India", "bjp", "terrorism", "congress", "modi","kashmir"] #change this to any hashtag you want
#hashtag = ["","India", "bjp", "terrorism"]
#username="DevanshGup58080" #change this to add seperate account
#password="thisisallweknow1234567890#@&D" #change to the password of the user
username="DiscordM8285"
password="helloworld1234567890"

bot = tb.Twitterbot(username,password )

#login
bot.login()
#get clean-text tweets
tweets,usernames=bot.get_tweets(hashtag,rate)
print("done")
df=pd.DataFrame({'username':usernames,'tweet':tweets})
#df['username']=usernames
df.to_csv('output.csv', index=False)
print("csv file saved")


 