import scrapy
import pandas as pd
# from review.items import ReviewItem
from scrapy import Selector
class CarSpider(scrapy.spiders.Spider):
     name = "cardeko"
     def start_requests(self):
         self.dict = {}
         self.dict['Brand'] = []
         self.dict['Car_name'] = []
         self.dict['Rating'] = []
         self.dict['Review_head'] = []
         self.dict['Review'] = []
         self.dict['Author'] = []
         self.dict['Likes'] = []
         self.dict['Dislikes'] = []
         self.dict['Review_date'] = []


         yield scrapy.Request(url='https://www.cardekho.com/newcars#brands', callback=self.parse)

     def parse(self, response):
         res = response.body
         Urls = Selector(text=res).xpath('//li[@class="gsc_col-xs-4 gsc_col-sm-3 gsc_col-md-3 gsc_col-lg-2"]/a/@href').extract()
         # print(Urls)
         for url in Urls:
             url = 'https://www.cardekho.com' + url
             yield scrapy.Request(url=url, callback=self.parse_next)
             # break
     def parse_next(self, response):
         res =  response.body

         # print(response.url)
         Urls = Selector(text=res).xpath('//div[@class="gsc_col-sm-12 gsc_col-xs-12 gsc_col-md-8 listView holder"]/h3/a/@href').extract()
         # print(len(Urls))
         print(Urls)

         for url in Urls:
             yield scrapy.Request(url=url, callback=self.parse_pages)
             # break
     def parse_pages(self,response):
         res =response.body
         Url = response.url
         Url = Url[:-12]
         # print(Url)
         page_count = 10
         page_count = Selector(text=res).xpath('//span[@class="bottomText"]/a/text()').extract()[0].split(' ')[2]

         page_link = Selector(text=res).xpath('//div[@class="linkAtBottomViewAll"]/a/@href').extract()[0]
         # print(page_link)
         page_count = int(page_count)/10 + 2
         # print(page_count)
         for page_no in range(1,int(page_count)):
             url = page_link +'/'+str(page_no)
             # print(url)
             yield scrapy.Request(url=url, callback=self.parse_reviews)
             # break
     def parse_reviews(self,response):

         res =response.body
         Url = response.url
         # print(Url)
         Urls = Selector(text=res).xpath('//div[@class="contentspace"]/h3/a/@href').extract()
         # print(Urls)

         for url in Urls:
             url = 'https://www.cardekho.com' + url
             yield scrapy.Request(url=url, callback=self.parse_data)
             # break
     def parse_data(self,response):
         res =response.body
         url = response.url
         # item = ReviewItem()
         # name = url.split('/')[-4]
         # brand = url.split('/')[-5]
         review_heading = Selector(text=res).xpath('//section[@class="clearfix userDetail shadow24 marginBottom20"]/h1/text()').extract()[0]
         review = Selector(text=res).xpath('//p[@class="contentheight"]/text()').extract()[0]
         author = Selector(text=res).xpath('//div[@class="authorSummary"]/div/text()').extract()
         likes_dislikes = Selector(text=res).xpath('//span[@class="hover"]/text()').extract()
         # starRating
         rating = Selector(text=res).xpath('//div[@class="readReviewHolder"]/div/div/span/span/@class').extract()[:5]
         title = Selector(text=res).xpath('//div[@class="title"]/text()').extract()[0].split(' ')[2:]
         brand = title[0]
         car_name  = ' '.join(title[1:])
         rate = 0

         print(car_name)
         for rat in rating:
             if rat.split(' ')[-2] == 'icon-star-full-fill':
                 rate += 1
             elif rat.split(' ')[-2] == 'icon-star-half-empty':
                 rate += 0.5
         # print(rate)
         likes = int(likes_dislikes[0])
         dislikes = int(likes_dislikes[2])
         date = author[2]
         author_name = author[0]
         self.dict['Brand'].append(brand)
         self.dict['Car_name'].append(car_name)
         self.dict['Review_head'].append(review_heading)
         self.dict['Review'].append(review)
         self.dict['Author'].append(author_name)
         self.dict['Likes'].append(likes)
         self.dict['Dislikes'].append(dislikes)
         self.dict['Review_date'].append(date)
         self.dict['Rating'].append(rate)
         df = pd.DataFrame(self.dict)
         #item['Product'] = df
         #yield item
         df.to_csv('reviews_cardheko.csv')
