import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from datetime import datetime

class NewsCrawler:
    
    @staticmethod
    def change_url(url):
        """Change the URL format to the mobile-friendly version."""
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        article_id = query_params.get("article_id", [""])[0]
        office_id = query_params.get("office_id", [""])[0]
        return f"https://n.news.naver.com/article/{office_id}/{article_id}"

    def fetch_news(self):
        """Fetch news articles from Naver Finance."""
        now = datetime.now()
        input_date = now.strftime("%Y-%m-%d")
        response = requests.get(f"https://finance.naver.com/news/mainnews.naver?date={input_date}&page=1")
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        items = soup.select(".block1")
        cnt = 0
        result =[]

        for item in items:
            title = item.find(class_="articleSubject").get_text(strip=True)
            url = "https://finance.naver.com" + item.select_one(".articleSubject a").attrs['href']
            url = self.change_url(url)
            summary = item.select_one('.articleSummary').contents[0].strip()
            press = item.select_one(".press").get_text(strip=True)
            date = item.select_one(".wdate").get_text(strip=True)

            result.append([title, url, summary, press, date])

            if cnt > 8:
                break
            cnt += 1

        return result