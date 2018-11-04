import scrapy
import pandas as pd
from review.items import ReviewItem
from scrapy import Selector
class CarSpider(scrapy.spiders.Spider):
     name = "carwale"
     def start_requests(self):
         self.dict = {}
         self.dict['Brand'] = []
         self.dict['Car_name'] = []
         self.dict['Review_head'] = []
         self.dict['Review'] = []
         yield scrapy.Request(url='https://www.carwale.com/', callback=self.parse)
         
     def parse(self, response):
         res = response.body
         Urls = Selector(text=res).xpath('//div[@class="brand-type-container"]/ul/li/a/@href').extract()
         # print(Urls)
         for url in Urls:
             url = 'https://www.carwale.com' + url
             yield scrapy.Request(url=url, callback=self.parse_next)
             # break
     def parse_next(self, response):
         res =  response.body
         Urls = Selector(text=res).xpath('//div[@class="grid-7 omega"]/a/@href').extract()
         # print(len(Urls))
         # print(Urls)

         for url in Urls:
             url = 'https://www.carwale.com' + url + 'userreviews/'
             yield scrapy.Request(url=url, callback=self.parse_pages)
             # break
     def parse_pages(self,response):
         res =response.body
         Url = response.url
         Url = Url[:-12]
         # print(Url)
         page_count = Selector(text=res).xpath('//span[@id="reviewCountId"]/text()').extract()
         page_count = int(page_count[0])/10 + 5
         # print(page_count)
         for page_no in range(1,int(page_count)):
             url = Url + 'userreviews-p'+str(page_no)+'/'
             yield scrapy.Request(url=url, callback=self.parse_reviews)
             # break
     def parse_reviews(self,response):

         res =response.body
         Url = response.url
         print(Url)
         Urls = Selector(text=res).xpath('//div[@style="margin-top: 20px;"]/a/@href').extract()
         print(Urls)
         for url in Urls:
             url = 'https://www.carwale.com' + url
             yield scrapy.Request(url=url, callback=self.parse_data)

     def parse_data(self,response):
         res =response.body
         url = response.url
         print(url)
         item = ReviewItem()
         name = url.split('/')[-4]
         brand = url.split('/')[-5]
         review_heading = Selector(text=res).xpath('//h1[@class="font30 text-black leftfloat margin-top10 special-skin-text"]/text()').extract()
         review = Selector(text=res).xpath('//h3[@class="font14"]/../div/p/text()').extract()
         self.dict['Brand'].append(brand)
         self.dict['Car_name'].append(name)
         self.dict['Review_head'].append(review_heading)
         self.dict['Review'].append(review)
         df = pd.DataFrame(self.dict)
         #item['Product'] = df
         #yield item
         df.to_csv('reviews.csv')
