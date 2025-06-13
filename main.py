
import time
import requests
from bs4 import BeautifulSoup
from collections import deque
from .scrapping_methods import ScrapperFunctions


def crawller_main_body():
    #the function is defined below , this is for forward reference
    pass

def main():
    topic = input("Enter the Wikipedia topic title you want to crawl: ")

    print(f"You entered the topic: {topic}")
    wiki_search = topic.replace(" ","_")

    base_url = "https://en.wikipedia.org/"
    page_url = f"{base_url}/wiki/{wiki_search}"

    print(f"Crawling page: {page_url}")
    
    
    crawl_queue = deque ([page_url])
    crawled = set()

    crawller_main_body(crawl_queue,crawled)
    
        
    

def crawl_end_summary(crawl_queue,crawled,time_frame):
    
    start_time, duration_limit = time_frame
    
    while True:
        if not crawl_queue and (time.time() - start_time) < duration_limit :
            print("Crawling finished: Queue is empty.")
        elif (time.time() - start_time) >= duration_limit:
            print(f"Crawling stopped due to time limit ({duration_limit} seconds).")

        print(f"Total pages crawled: {len(crawled)}")
        
def crawller_main_body(crawl_queue,crawled):
    
    start_time = time.time() 
    duration_limit = 100  
    
    time_frame = [start_time,duration_limit]
    
    while crawl_queue and (time.time() - start_time) < duration_limit:
        try:
            
            if (time.time() - start_time) >= duration_limit:
                print(f"Time limit of {duration_limit} seconds reached. Stopping crawl.")
                break

            to_crawl = crawl_queue.popleft()

            if to_crawl in crawled:
                continue

            print(f"Attempting to crawl: {to_crawl}") 
            response = requests.get(to_crawl, timeout=10) 
            
            status_code = response.status_code
            
            if status_code == 200:
                print(f"Successfully Crawled: {to_crawl}")
                crawled.add(to_crawl)
                
                soup = BeautifulSoup(response.content,"html.parser")
                crawler = ScrapperFunctions(soup)
                
                crawler.main_heading()
                #crawler.find_all_links(crawl_queue,crawled)

            
            else:
                print(f"Error crawling {to_crawl}, Status Code: {status_code}")
                break 
        
        except requests.exceptions.RequestException as e: 
            print(f"A request error occurred for {to_crawl}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
    crawl_end_summary(crawl_queue,crawled,time_frame)
    
if __name__ == "__main__":
    main()