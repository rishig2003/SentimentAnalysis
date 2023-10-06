import twitterbot as tb
import pandas as pd
import os

#tells how many times to scroll to fetch tweets. the larger the more tweets can be fetched and more time the code will take
rate =100

print(os.getcwd())
hashtag = "politics" #change this to any hashtag you want

username="DiscordM8285" #change this to add seperate account
password="helloworld1234567890" #change to the password of the user
bot = tb.Twitterbot(username,password )

#login
bot.login()
#get clean-text tweets
tweets=bot.get_tweets(hashtag,rate)
print("done")
df=pd.DataFrame(tweets,columns=['tweet'])
df.to_csv('output.csv', index=False)
print("csv file saved")


 