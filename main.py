# deque is a double-ended queue, suitable for adding/removing elements efficiently.
from collections import deque
from re import S
import requests
import time # Import the time module
from bs4 import BeautifulSoup

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
                # Use find_all to get all links, not just the first one
                links = soup.find_all("a", href=True) # Also ensure 'href' attribute exists
                
                for link_tag in links: # Iterate through the ResultSet
                    href = link_tag['href'] # More direct way to get href if it exists
                    
                    # Construct absolute URLs for relative links
                    if href.startswith("/wiki/") and not href.startswith("/wiki/File:") and not href.startswith("/wiki/Special:"):
                        full_url = base_url.rstrip('/') + href
                        if full_url not in crawled and full_url not in crawl_queue:
                             crawl_queue.append(full_url) # Use append for adding to the right
                    # You might want to handle other types of links or external links too

                # The popleft() here was likely a mistake, as you pop from the queue at the start of the loop.
                # If you intended to limit queue size, that's a different logic.
                # crawl_queue.popleft() # This line seems to be an error and is removed.
            
            else:
                print(f"Error crawling {to_crawl}, Status Code: {status_code}")
                # Decide if you want to break on any error or just log and continue
                # break # Uncomment if you want to stop on any non-200 status
        
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