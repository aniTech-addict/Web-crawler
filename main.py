# deque is a double-ended queue, suitable for adding/removing elements efficiently.
from collections import deque
import requests
import time # Import the time module
from bs4 import BeautifulSoup
from scrapping_methods import ScrapperFunctions

def main():
    topic = input("Enter the Wikipedia topic title you want to crawl: ")

    print(f"You entered the topic: {topic}")
    wiki_search = topic.replace(" ","_")

    base_url = "https://en.wikipedia.org/"
    page_url = f"{base_url}/wiki/{wiki_search}"

    print(f"Crawling page: {page_url}")
    
    
    crawl_queue = deque ([page_url])
    crawled = set()

    start_time = time.time() # Record the start time
    duration_limit = 100  # Set the duration limit in seconds
    
    # Modify the loop condition to also check the time
    while crawl_queue and (time.time() - start_time) < duration_limit:
        try:
            # Check elapsed time at the beginning of each iteration
            if (time.time() - start_time) >= duration_limit:
                print(f"Time limit of {duration_limit} seconds reached. Stopping crawl.")
                break

            to_crawl = crawl_queue.popleft()

            # Avoid re-crawling pages already processed
            if to_crawl in crawled:
                continue

            print(f"Attempting to crawl: {to_crawl}") # More informative print
            response = requests.get(to_crawl, timeout=10) # Add a timeout to requests.get
            
            status_code = response.status_code
            
            if status_code == 200:
                print(f"Successfully Crawled: {to_crawl}")
                crawled.add(to_crawl)
                
                soup = BeautifulSoup(response.content,"html.parser")
                crawler = ScrapperFunctions(soup)
                
                crawler.find_all_headings()
                crawler.find_all_links(crawl_queue,crawled)

            
            else:
                print(f"Error crawling {to_crawl}, Status Code: {status_code}")
                break 
        
        except requests.exceptions.RequestException as e: # Be more specific with request exceptions
            print(f"A request error occurred for {to_crawl}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
    if not crawl_queue and (time.time() - start_time) < duration_limit :
        print("Crawling finished: Queue is empty.")
    elif (time.time() - start_time) >= duration_limit:
        print(f"Crawling stopped due to time limit ({duration_limit} seconds).")

    print(f"Total pages crawled: {len(crawled)}")
    # print(f"Crawled pages: {crawled}") # Uncomment to see the list of crawled pages

if __name__ == "__main__":
    main()