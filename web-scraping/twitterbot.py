from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time, os
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import re

def remove_non_ascii(input_string):
    return ''.join(char if ord(char) < 128 else '' for char in input_string)

def remove_extra_spaces(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = cleaned_text.strip()
    return cleaned_text

def keep_alphabets_and_spaces(input_string):
    cleaned_string = re.sub(r'[^a-zA-Z\s]', '', input_string)
    return cleaned_string

def remove_duplicates(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


def listToString(s):
    str1 = " "
    return (str1.join(map(str, s)))

class Twitterbot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        chrome_options = Options()
        chrome_options.add_argument('--headless') 
        self.bot = webdriver.Chrome(options=chrome_options)

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/i/flow/login?input_flow_data=%7B"requested_variant"%3A"eyJsYW5nIjoiZW4ifQ%3D%3D"%7D')
        time.sleep(3)
        page_source = bot.page_source
        soup = BeautifulSoup(page_source,'html.parser')
        email=bot.find_element(By.NAME,'text')
        email.send_keys(self.email)
        button=bot.find_element(By.CSS_SELECTOR,"div[class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu'] span[class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0']")
        button.click()
        time.sleep(3)
        page_source=bot.page_source
        soup = BeautifulSoup(page_source,'lxml')
        password = bot.find_element(By.CSS_SELECTOR,"input[name='password']")
        password.send_keys(self.password)
        time.sleep(1)
        button1=bot.find_element(By.XPATH,"(//div[@class='css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0'])[3]")
        button1.click()
        time.sleep(2)
    def get_tweets(self, hashtag,t): 
        tweets=[]
        bot = self.bot
        bot.get('https://twitter.com/search?q=%23' + hashtag + '&src=typed_query&f=live')
        time.sleep(3)

        while(t>0):
            page_source = bot.page_source
            soup = BeautifulSoup(page_source,'lxml')
            t-=1
            q= soup.find('div',{'class':'css-1dbjc4n'})
            a=q.find_all('div',{'data-testid':'cellInnerDiv'})
            k=1 
            for b in a:
                w=b.find_all('div',{'dir':'auto'})
                for z in w:
                    m=z.find('span',{'class':'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})
                    if m is not None:                
                        k+=1
                        z=keep_alphabets_and_spaces(remove_extra_spaces(remove_non_ascii(m.text)))
                        if z is not None:
                            tweets.append(z)
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            print(t)
        t=1
        tweets=remove_duplicates(tweets)       
        for i in tweets:
            print(f"{t} : {i}")
            t+=1
        return tweets


       

     

        



            
