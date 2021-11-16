# importing the scrapy module
import scrapy

class ExtractUrls(scrapy.Spider):
	name = "extract"

	# request function
	def start_requests(self):
		urls = [ 'http://www.geeksforgeeks.org', ]
		
		for url in urls:
			yield scrapy.Request(url = url, callback = self.parse)

	# Parse function
	def parse(self, response):
		
		# Extra feature to get title
		title = response.css('title::text').extract_first()
		
		# Get anchor tags
		links = response.css('a::attr(href)').extract()	
		
		for link in links:
			yield
			{
				'title': title,
				'links': link
			}
			
			if 'geeksforgeeks' in link:		
				yield scrapy.Request(url = link, callback = self.parse)
