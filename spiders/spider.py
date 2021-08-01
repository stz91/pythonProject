import scrapy
import json
import os


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    with open("城市.json", "r") as f:
        cities = json.load(f)
    base_url = "https://www.creprice.cn/city/"
    start_urls = []
    temp = []
    for item in range(len(cities)):
        temp.append(base_url + cities[item] + ".html?type=newha&sinceyear=10")
    start_urls = temp[160:170]

    def parse(self, response):
        filename = response.url.split('?')[-2].split('/')[-1]
        with open("city/" + filename, 'wb') as f:
            f.write(response.body)
