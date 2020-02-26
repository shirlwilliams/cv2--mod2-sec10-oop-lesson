import requests
from bs4 import BeautifulSoup


class EbayScraper():
    
    def __init__(self):
        # this is called an attribute
        self.url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1311.R2.TR11.TRC2.A0.H0.TRS1&_nkw={}"
        pass
    

    # get search content
    def search_item(self, keyword):
        """
        input
        
        returns html of results
        """
        keyword = keyword.replace(" ", "+")
        search_url = self.url.format(keyword)
        
        req = requests.get(search_url)
        html_content = req.content
        return html_content
    
    # parst html content
    def make_soup_search_object(self, keyword):
        html_content = self.search_item(keyword)
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup
    
    # parse 
    def parse_soup_search_object(self, keyword):
        soup = self.make_soup_search_object(keyword)
        title_boxes = soup.find_all("h3", class_="s-item__title")
        titles = [title_box.text for title_box in title_boxes]
        return titles
    

    
    
if __name__=="__main__":
    #instantiate EbayScraper object -> triggers the __init__ method
    scraper = EbayScraper()

    # pass in a keyword into our search
    # check the search url
    titles = scraper.parse_soup_search_object(keyword="face mask medical")
    print(titles)