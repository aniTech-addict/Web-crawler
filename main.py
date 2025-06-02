# deque is a double-ended queue, suitable for adding/removing elements efficiently.
from collections import deque
import requests
from bs4 import BeautifulSoup

def main():
    topic = input("Enter the Wikipedia topic title you want to crawl: ")

    print(f"You entered the topic: {topic}")

    base_url = "https://en.wikipedia.org/"
    page_url = f"{base_url}/wiki/{topic}"

    print(f"Crawling page: {page_url}")
    
    
    crawl_queue = deque ([page_url])
    crawled = set()
    
    while(crawl_queue):
        try:
            to_crawl = crawl_queue.popleft()
            response = requests.get(to_crawl)
            
            status_code = response.status_code
            
            if status_code == 200:
                print("Succesfully Crawlled")
                crawled.add(to_crawl)
                
                soup = BeautifulSoup(response.content,"html.parser")
            
            else:
                print(f"Some Error Occured , Status Code{status_code}")
                break
        
        except Exception as e:
            print(f"An Error occured {e}")
        


if __name__ == "__main__":
    main()