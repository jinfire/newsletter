import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config
from crawling import NewsCrawler
from htmlGenerator import HTMLGenerator


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
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Recipients
    recipients = ["jensoo7023@naver.com", "qejlfn@naver.com"]

    # Step 1: Fetch news
    crawler = NewsCrawler()
    news_data = crawler.fetch_news()

    # Step 2: Generate HTML
    html_generator = HTMLGenerator()
    final_html = html_generator.generate_html(news_data)

    # Step 3: Send email
    send_email("오늘의 주요 경제뉴스", final_html, recipients)


