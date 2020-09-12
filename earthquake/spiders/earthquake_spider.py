import scrapy
import json
from earthquake.items import EarthquakeItem

class EarthquakeSpider(scrapy.Spider):
	name = 'earthquake'
	page_max = None
	def start_requests(self):
		url = 'http://www.ceic.ac.cn/ajax/search?page=1&start=&end=&jingdu1=&jingdu2=&weidu1=&weidu2=&height1=&height2=&zhenji1=&zhenji2='
		yield scrapy.Request(url=url, callback=self.rest_requests)

	def rest_requests(self, response):
		page_max = json.loads(response.text.strip('()'))['num']
		urls = [
			f'http://www.ceic.ac.cn/ajax/search?page={page}&start=&end=&jingdu1=&jingdu2=&weidu1=&weidu2=&height1=&height2=&zhenji1=&zhenji2='
			for page in range(1, page_max+1)
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		earthquakes = json.loads(response.text.strip('()'))['shuju']
		for earthquake in earthquakes:
			yield EarthquakeItem(
					latitude=earthquake['EPI_LAT'],
					longitude=earthquake['EPI_LON'],
					location=earthquake['LOCATION_C'],
					strength=earthquake['M'],
					earthquake_time=earthquake['O_TIME']
				)