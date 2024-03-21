from bs4 import BeautifulSoup
import sqlite3


def urlToDB(url, soup):

    text = ""
    for string in soup.stripped_strings:
        text += " " + string

    urls = ""
    link_elements = soup.select("a[href]")
    for link_element in link_elements:
        url_page = link_element['href']
        if "https://" in url_page:
            urls += " " + url_page


    data = [
        url,
        soup.title.string, 
        text, 
        urls
    ]
    try:
        conn = sqlite3.connect('ma_base.db')
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO sitesreferences (URL, TITLE, PAGETEXT, LINKS) VALUES(?, ?, ?, ?)""",
                    data)
        conn.commit()
        # fin
        conn.close()
            
    except:
        pass