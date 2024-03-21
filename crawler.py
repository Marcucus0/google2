import requests
from bs4 import BeautifulSoup
import queue
import re
import time
import UrlToDB as UTDB

#https://fr.wikipedia.org/wiki/Louis_XIV
urls = queue.PriorityQueue()
urls.put((0.5, "https://lesoir.be/"))

visited_urls = []

while not urls.empty():
    # get the page to visit from the list
    # current_url = urls.pop()
    _, current_url = urls.get()

    try:
        # Recuperer la page
        response = requests.get(current_url)
        soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")
        

        if ("noindex" not in response.text or "nofollow" not in response.text):
            
            visited_urls.append(current_url)
            link_elements = soup.select("a[href]")
            for link_element in link_elements:
                url = link_element['href']
                if "https://" in url:
                    if url not in visited_urls and url not in [item[1] for item in urls.queue]:
                        # default priority score
                        priority_score = 1
                        # if the current URL refers to a pagination page
                        if re.match(r"^https://lesoir\.be/\d+/?$", url):
                            priority_score = 0.5
                        urls.put((priority_score, url))
                        UTDB.urlToDB(url, soup)



    except:
        pass

    time.sleep(2)