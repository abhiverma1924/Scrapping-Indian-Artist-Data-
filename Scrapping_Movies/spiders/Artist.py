import scrapy
from ..items import ScrappingMoviesItem

class scrapper(scrapy.Spider):
  name = 'artists'
  #page_number = 2 # For scrapping multiple page
  start_urls = [
                'https://www.imdb.com/list/ls002913270/' # link of the home page we are scrapping


  ]

  def parse(self, response):
    items = ScrappingMoviesItem()
    actor_name = response.css('.lister-item-header::text').extract() # Scrapping Artist Name
    actor_info = response.css('p:nth-child(3)::text').extract()  # Scrapping Artist Info
    actor_movie = response.css('.text-small a::text').extract()   # Scrapping Artist Famous Movie
    actor_imageLink = response.css('.cfMarker::attr(src)').extract() # Scrapping Artist Image Link

    items['actor_name'] = actor_name
    items['actor_info'] = actor_info
    items['actor_movie'] = actor_movie
    items['actor_imageLink'] = actor_imageLink


    yield items
    #For scrapping multiple pages at a time un-comment the below secction and page_number on the top
    #next_page = 'https://www.imdb.com/list/ls002913270/?sort=list_order,asc&mode=detail&page='+ str(scrapper.page_number)
    #if scrapper.page_number <= 5:
      #scrapper.page_number+=1
      #yield response.follow(next_page, callback = self.parse)

