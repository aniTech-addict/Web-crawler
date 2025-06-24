import time
import requests
from bs4 import BeautifulSoup
from scrapping_methods import ScrapperFunctions

class Crawler:
    
    def __init__(self, crawl_queue,crawled,limit = 50):
        self.crawl_queue = crawl_queue
        self.crawled = crawled
        self.duration_limit = limit
        
    def crawller_main_body(self):
    
        start_time = time.time()  
        duration_limit = self.duration_limit
        
        time_frame = [start_time,duration_limit]
        
        while self.crawl_queue and (time.time() - start_time) < duration_limit:
            try:
                
                if (time.time() - start_time) >= duration_limit:
                    print(f"Time limit of {duration_limit} seconds reached. Stopping crawl.")
                    break

                to_crawl = self.crawl_queue.popleft()

                if to_crawl in self.crawled:
                    continue

                print(f"Attempting to crawl: {to_crawl}") 
                response = requests.get(to_crawl, timeout=10) 
                
                status_code = response.status_code
                
                if status_code == 200:
                    print(f"Successfully Crawled: {to_crawl}")
                    self.crawled.add(to_crawl)
                    
                    soup = BeautifulSoup(response.content,"html.parser")
                    crawler = ScrapperFunctions(soup)
                    
                    crawler.main_heading()
                    #crawler.find_all_links(self.crawl_queue,crawled)

                
                else:
                    print(f"Error crawling {to_crawl}, Status Code: {status_code}")
                    break 
            
            except requests.exceptions.RequestException as e: 
                print(f"A request error occurred for {to_crawl}: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        
        self.duration_limit = duration_limit
        
        #Automatically calls the summary fn        
        Crawler.crawl_end_summary(self,time_frame)      

    
     # ATTENTION !! Do not call this fn explicitly (already called in crawler_main_body)
    def crawl_end_summary(self,time_frame):
        
        start_time, duration_limit = time_frame
        
        while True:
            if not self.crawl_queue and (time.time() - start_time) < duration_limit :
                print("Crawling finished: Queue is empty.")
                break
                
            elif (time.time() - start_time) >= duration_limit:
                print(f"Crawling stopped due to time limit ({duration_limit} seconds).")

                print(f"Total pages crawled: {len(self.crawled)}")
        

def main():
    print('~~~~~~~~~~~~~~~~~ATTENTION~~~~~~~~~~~~~~~~~')
    print("This file is not to be ran directly.")
    input()

if __name__ == "__main__":
    main()
