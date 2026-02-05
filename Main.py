import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config
from newsCrawling import NewsCrawler
from blogCrawling import BlogCrawler
from stockCrawling import StockCrawler
from newsHtmlGenerator import NewsHTMLGenerator
from blogHtmlGenerator import BlogHtmlGenerator
from stockHtmlGenerator import StockHtmlGenerator

def send_email(subject, html_content, recipients):
    """Send email using SMTP."""
    provider = "naver"
    smtp_config = Config.get_smtp_config(provider)

    if smtp_config:
        SMTP_USER = smtp_config['email']
        SMTP_PASSWORD = smtp_config['password']
        SMTP_NAME = smtp_config['smtpName']
        SMTP_PORT = smtp_config['smtpPort']
    else :
        raise ValueError(f"SMTP Provider '{provider} is not supported")

    try:
        with smtplib.SMTP(SMTP_NAME, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)

            for recipient in recipients:
                msg = MIMEMultipart()
                msg['From'] = SMTP_USER
                msg['To'] = recipient
                msg['Subject'] = subject
                msg.attach(MIMEText(html_content, 'html'))

                server.sendmail(SMTP_USER, recipient, msg.as_string())
                print(f"Email sent to {recipient}")
    except smtplib.SMTPAuthenticationError as e:
        print(f"[ERROR] 인증 실패: {e}")
        print(f"[HINT] 네이버 메일 설정을 확인하세요:")
        print(f"       1. https://mail.naver.com 로그인")
        print(f"       2. 환경설정 > POP3/IMAP 설정")
        print(f"       3. IMAP/SMTP 사용 체크")
        print(f"       4. 2단계 인증 사용 시 '앱 비밀번호' 생성 필요")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Recipients
    news_recipients = ["jensoo7023@naver.com", "qejlfn@naver.com"]
    blog_recipients = ["qejlfn@naver.com","jensoo7023@gmail.com"]
    stock_recipients = ["jensoo7023@gmail.com", "qejlfn@naver.com"]

    # Step 1: Fetch news
    news_crawler = NewsCrawler()
    news_data = news_crawler.fetch_news()
    blog_crawler = BlogCrawler()
    blog_data = blog_crawler.fetch_news()
    stock_crawler = StockCrawler() 
    stock_data = stock_crawler.fetch_stock_data()  

    # Step 2: Generate HTML
    news_html_generator = NewsHTMLGenerator()
    final_html = news_html_generator.generate_html(news_data)
    blog_html_generator = BlogHtmlGenerator()
    blog_html = blog_html_generator.generate_html(blog_data)
    stock_html_generator = StockHtmlGenerator()  
    stock_html = stock_html_generator.generate_html(stock_data)

    # Step 3: Send email
    #send_email("오늘의 주요 경제뉴스", final_html, news_recipients)
    #send_email("이번주 청약 소식", blog_html, blog_recipients)
    send_email("오늘의 주요 시황", stock_html, stock_recipients)


