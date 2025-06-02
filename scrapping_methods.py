

class ScrapperFunctions:
    def __init__(self,soup):
        self.soup = soup
        
    def find_all_headings(self):
        HEADING_TAGS = ["h1","h2","h3"]
        headings = self.soup.find_all(HEADING_TAGS)
        
        for heading in headings:
            print(heading.text)
            
    def find_all_links(self,crawl_queue,crawled):
        base_url = "https://en.wikipedia.org/"
        
        links = self.soup.find_all("a", href=True) 
                
        for link_tag in links:  # Iterate through the ResultSet
            href = link_tag.get('href')  # Use .get() for safety, returns None if 'href' doesn't exist

            if not href:  # Skip if href is None or empty, or if link_tag has no 'href'
                continue
                    
            # Construct absolute URLs for relative links and add to queue
            if href.startswith("/wiki/") and \
               not href.startswith("/wiki/File:") and \
               not href.startswith("/wiki/Special:"):
                full_url = base_url.rstrip('/') + href
                
                if full_url not in crawled and full_url not in crawl_queue:
                    crawl_queue.append(full_url)  # Use append for adding to the right
            # You might want to handle other types of links or external links here or log them