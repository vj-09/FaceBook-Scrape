import scrapy
from scrapy.loader import ItemLoader
from scrapy.http import FormRequest
from scrapy import Selector
import pandas as pd
# from fbcrawl.items import FbcrawlItem


class FacebookSpider(scrapy.Spider):
    """
    Parse FB pages (needs credentials)
    """
    name = "fb"

    def __init__(self, email='', password='',  **kwargs):
        super(FacebookSpider, self).__init__(**kwargs)

        self.dict = {}

        self.Name=[]
        self.Text=[]
        self.Time=[]

        if not email or not password:
            raise ValueError("You need to provide valid email and password!")
        else:
            self.email = email
            self.password = password

        self.start_urls = ['https://mbasic.facebook.com']

    def parse(self, response):
        return FormRequest.from_response(
                response,
                formxpath='//form[contains(@action, "login")]',
                formdata={'email': self.email,'pass': self.password},
                callback=self.parse_home
        )

    def parse_home(self, response):

        res = response.url
        href = 'https://mbasic.facebook.com/messages/?ref_component=mbasic_home_header&ref_page=%2Fwap%2Fprofile_timeline.php&refid=17'
        return scrapy.Request(
            url=href,
            callback=self.parse_page,
        )

    def parse_page(self, response):
        res = response.body
        peoples = Selector(text=res).xpath('//h3/a/text()').extract()
        people_link = Selector(text=res).xpath('//h3/a/@href').extract()
        print('Choose the conversation')
        print(peoples,people_link)
        for i in range(len(peoples)):
            print(i,peoples[i])
        convo = int(input())

        yield scrapy.Request(url='https://mbasic.facebook.com'+ people_link[convo], callback=self.parse_convo)

    def parse_convo(self,response):
        res =response.body
        old_txt = Selector(text=res).xpath('//div[@id="see_older"]/a/@href').extract()
        txt = Selector(text=res).xpath('//div[@id="messageGroup"]/div/div').extract()
        dict1={'Name':[],'Text':[],'Time':[]}
        for a in txt:
            content = Selector(text=a).xpath('//div/div/a/strong/text()').extract()
            contentt = Selector(text=a).xpath('//div/div/div/span/text()').extract()
            time =  Selector(text=a).xpath('//div/div/abbr/text()').extract()
            try:
                dict1['Name'].append(content[0])
                dict1['Text'].append(' '.join(contentt))
                dict1['Time'].append(time[0])
            except:
                pass
        self.Name.insert(0,dict1['Name'])
        self.Text.insert(0,dict1['Text'])
        self.Time.insert(0,dict1['Time'])
        # df = pd.DataFrame({'Name':})
        # print(sum(self.Name,[]),sum(self.Time,[]),sum(self.Text,[]))
        df = pd.DataFrame({'Name':sum(self.Name,[]),'Text':sum(self.Text,[]),'Time':sum(self.Time,[])})
        df.to_csv('fb_text.csv')
        print(df)

        yield scrapy.Request(url='https://mbasic.facebook.com'+ old_txt[0], callback=self.parse_convo)
