# FaceBook-Scrape
Fbtxtscraper is a tool for scraping your personal Facebook conversations, written in python, based on the Scrapy framework.
 
## Introduction
  Fbtxtscraper is based on Python Web Scraping framework Scrapy. For simple beginner understanding items, pipeline, middleware were not used, contents are directly written to csv. From this, we can scrape out our facebook conversation with our friends, and store it structured.
  
1. Why scraping??? &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;       It's super boring to scroll through conversations every time. 


2. Why not FB API??  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;    We can't get whole of the contents, There is a cap for it. 


3. Why python??Scrapy?? &nbsp; &nbsp; &nbsp; &nbsp;  For Web scraping Scrapy is the widely used framework for its numerous advantages over its counterparts like Suitable for broad crawling and scaling, Easy setup and detailed documentation, Active Community and Superfast. 

## Installation
   Requirements are python3 (python2 is also supported), scrapy and other dependencies libraries (twisted, libxml2 etc.).
   [Installazion guide](https://doc.scrapy.org/en/latest/intro/install.html) for scrapy.
    
    
        
## How to use
   Make sure that scrapy is installed and clone this repository. Navigate through the project's top-level directory and launch scrapy with:
        
        scrapy crawl fb -a email="EMAILTOLOGIN" -a password="PASSWORDTOLOGIN" 
   
This will give last 10 recent conversations, from that select the conversation to be scraped, bot will scrape till very last text in that conversation and return a csv file with columns Name, Text, Date.


## Future updates
   To scrape every conversation, Then public post's reactions and comments with replies.
        
New to scraping ??? [Check Here](https://medium.com/@athithyavijay/stepping-into-web-scraping-and-available-tools-11a0f9b8876a)
for intro and available tools across languages.  



