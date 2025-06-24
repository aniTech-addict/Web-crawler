

class ScrapperFunctions:
    def __init__(self,soup):
        self.soup = soup
        
    def find_paras(self):
        paragraph_tag = "p"
        return self.soup.find(paragraph_tag)
        
    def main_heading (self):
            soup = self.soup 
            main_heading = soup.find("span",{"class":"mw-page-title-main"})
            print(main_heading)
            self.para()
    
    def para(self):
        soup = self.soup
        content_div = soup.find("div", {"class": "mw-parser-output"})

        paras = []
        paras.extend(
            elem.get_text(strip=True)
            for elem in content_div.find_all(['p'], recursive=True)
            if elem.get_text(strip=True)
        )
        print(paras)
        
            
    def find_all_links(self,crawl_queue,crawled):
        base_url = "https://en.wikipedia.org/"
        
        links = self.soup.find_all("a", href=True) 
                
        for link_tag in links:
            href = link_tag.get('href')  # Use .get() for safety, returns None if 'href' doesn't exist

            if not href:  # Skip if href is None or empty, or if link_tag has no 'href'
                continue
                    
            # Construct absolute URLs for relative links and add to queue
            if href.startswith("/wiki/") and \
               not href.startswith("/wiki/File:") and \
               not href.startswith("/wiki/Special:"):
                full_url = base_url.rstrip('/') + href
                
                if full_url not in crawled and full_url not in crawl_queue:
                    crawl_queue.append(full_url)

def main():
    print('~~~~~~~~~~~~~~~~~ATTENTION~~~~~~~~~~~~~~~~~')
    print("This file is not to be ran directly.")
    input()

if __name__ == "__main__":
    main()
