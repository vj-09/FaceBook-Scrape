# FaceBook-Message-Scrape
Fbtxtscraper is tool for scraping your personal Facebook messgaes with your loved ones, written in python, based on the Scrapy framework.
 
Introduction
  Fbtxtscraper is beased on Python Web Scrapying framework Scrapy.For simple biginner understanding items, pipeline, middleware were not used, contents are directly written to csv.From this we can scrape out our facebook coversation with our friends, and store it structured.
  
Why scrapying???      It's super boring to scroll through conversations every time. 
Why not fb api??      We can't get whole of the contents, There is a cap for it. 
Why python??Scrapy??  For Web scrapying Scrapy is widely used framework for its numourous advantages over its counterparts                           like Suitable for broad crawling and scaling, Easy setup and detailed documentation, Active Community                           and Super fast. 

Installation
        Requirements are: python3 (python2 is also supported), scrapy and other dependencies libraries (twisted, libxml2 etc.).
        Installazion guide:https://doc.scrapy.org/en/latest/intro/install.html
        
        
How to use
        Make sure that scrapy is installed and clone this repository. Navigate through the project's top level directory and launch scrapy with:
        
        scrapy crawl fb -a email="EMAILTOLOGIN" -a password="PASSWORDTOLOGIN" 
   
This will give last 10 recent conversations, from that select the conversation to be scraped, bot will scrape till very last text in that conversation and resturn a csv file with columns Name , Text , Date.


Future updates
        To scrape every conversation ,Then public post's reactions and comments with replies.
        
 New to scraping ??? Check https://medium.com/@athithyavijay/stepping-into-web-scraping-and-available-tools-11a0f9b8876a 
 for intro and available tools across languages.  



