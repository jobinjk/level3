# main code

import scrapy
from myntra.items import MyntraItem

# create a class to run the spider
class MyntraProductSpider(scrapy.Spider):
    name = "MyntraDeals" # name of the crawl eg: scrapy crawl ('name')
    allowed_domains = ["myntra.com"] # select the domain to be crawled
  
  #Use working product URL below
    start_urls = [
         "https://www.myntra.com/tshirts/ether/ether-navy--white-striped-polo-t-shirt/1377369/buy",
         "https://www.myntra.com/helmets/ls2/ls2-men-black-printed-full-face-helmet-ff-352/1764707/buy",
         "https://www.myntra.com/helmets/ls2/ls2-men-black--red-full-face-helmet-ff-320/1764738/buy",
         "https://www.myntra.com/helmets/ls2/ls2-men-black-printed-full-face-helmet-ff-386/1792311/buy",
         "https://www.myntra.com/helmets/ls2/ls2-men-grey-melange-printed-full-face-helmet-ff-352/1764712/buy",
     ]
 
    def parse(self, response):# create a parse function which scraps and requests url etc etc
        items = MyntraItem()
        title = response.xpath('//meta[@itemprop="name"]/@content').extract() # to get the xpath of title
        product_details = response.xpath('//meta[@itemprop="description"]/@content').extract() #to get the xpath of product details
        sale_price = response.xpath('//meta[@itemprop="description"]/@content').extract() #to get the xpath of price
        product_image_location = response.xpath('//meta[@itemprop="image"]/@content').extract() #to get the xpath of image location
        
        
        items['product_image_location'] = ''.join(product_image_location).strip()
        items['product_details'] = ''.join(product_details).strip("Buy")# joined the details in list items and striped off the word buy
        items['product_price'] = ''.join(sale_price).split('at ')[1].strip()# joined the price in list items and splited off the text till at
        items['product_name'] = ''.join(title[0].split("|")[0]).strip("Buy")
        return items