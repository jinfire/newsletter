import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from datetime import datetime

class BlogCrawler:
    
    def fetch_news(self):
        """Fetch news articles from Naver Finance."""
        query = "줍줍청약"
        response = requests.get(f"https://search.naver.com/search.naver?ssc=tab.blog.all&query={query}&sm=tab_opt&nso=so%3Ar%2Cp%3A1w")
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        items = soup.select(".view_wrap")
        cnt =0
        result =[]
        for item in items:
            title = item.select_one(".title_link").text
            link = item.select_one(".title_link").attrs['href']
            date = item.select_one(".user_info > span").text
            result.append([title, link, date])
            if cnt == 4 :
                break
            cnt=cnt+1

        return result
