from collections import deque
import logging
from crawler_obj import Crawler

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    topic = input("Enter the Wikipedia topic title you want to crawl: ")

    print(f"You entered the topic: {topic}")
    wiki_search = topic.replace(" ","_")

    base_url = "https://en.wikipedia.org/"
    page_url = f"{base_url}/wiki/{wiki_search}"

    logging.info(f"Crawling page: {page_url}")
    
    
    crawl_queue = deque ([page_url])
    crawled = set()

    crawler = Crawler(crawl_queue,crawled)
    crawler.crawller_main_body()
    
    
if __name__ == "__main__":
    main()