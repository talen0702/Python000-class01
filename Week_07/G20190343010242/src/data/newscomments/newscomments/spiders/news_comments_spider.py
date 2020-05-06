import os
import re
import scrapy
from models.news import News
from newscomments.newscomments.items.comments_item import CommentsItem
from utils.db_helper import DbHelper
from utils.helper import Helper
from utils.logger import get_logger


class NewsCommentsSpider(scrapy.Spider):

    url = os.getenv("NEWS_URL")
    comments_url = os.getenv("COMMENTS_URL")
    name = "news_comments"
    start_urls = [url]
    comments_per_page = int(os.getenv("COMMENTS_PER_PAGE", "20"))
    dbUtils = DbHelper()
    logger = get_logger('news_comments_spider')
    max_pages = int(os.getenv("MAX_PAGES", "10"))

    def parse(self, response):
        try:
            news_name = response.xpath("//div[@id='wrapper']/h1[1]/span[1]/text()").extract_first().strip()
            news_id = Helper.md5(news_name)
            self.__add_news(News(news_id=news_id, news_name=news_name, source=self.url))
            item = CommentsItem()
            item['news_id'] = news_id
            total_comments = int(re.findall(r'\d+', response.xpath("//div[@id='content']/div/div[@class='article']/div[@class='related_info']/div[@class='mod-hd']/h2[1]/span[@class='pl']/a/text()").extract_first().strip())[0])
            pages = int(total_comments / self.comments_per_page) if total_comments % self.comments_per_page == 0 else int(total_comments / self.comments_per_page) + 1
            # Get all comments in pages, but crawl up to max_pages
            if pages > self.max_pages:
                pages = self.max_pages
            urls = [f'{self.comments_url}?p={p+1}' for p in range(pages)]
            for c_url in urls:
                yield scrapy.Request(c_url, meta={'item': item}, callback=self.__parse_comments)
        except Exception as ex:
            self.logger.error(f"Exception occurred when parsing page {self.url}", ex)

    def __parse_comments(self, response):
        for sel in response.xpath("//div[@id='comments']/ul/li"):
            try:
                item = response.meta['item']
                item['comment_id'] = int(sel.xpath("@data-cid").extract_first().strip())
                item['comment'] = sel.xpath("div[@class='comment']/p[1]/span[1]//text()").extract_first().strip()
                item['comment_time'] = Helper.parse_comment_time(sel.xpath("div[@class='comment']/h3[1]/span[2]/span[2]/text()").extract_first().strip())
                yield item
            except Exception as ex:
                self.logger.error(f"Exception occurred when parsing comment with response {response}", ex)
                yield None

    def __add_news(self, news_item):
        if self.__check_news(news_item) == 0:
            self.dbUtils.insert([news_item])

    def __check_news(self, news_item):
        session = self.dbUtils.Session()
        try:
            result = session.query(News).filter(News.news_id == news_item.news_id).count()
            return result
        except Exception as ex:
            raise ex
        finally:
            session.close()

