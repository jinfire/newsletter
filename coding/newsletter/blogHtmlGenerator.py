class BlogHtmlGenerator:
    def __init__(self):
        self.html_template = """
        <!DOCTYPE html>
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>청약소식</title>
        </head>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; background-color: #f9f9f9; margin: 20px; padding: 20px;">

            <!-- 뉴스레터 헤더 -->
            <div style="background-color: white; color: black; padding: 20px; text-align: center; 
                        border-radius: 8px; border: 2px solid black;">
                <h1 style="margin: 0; font-size: 24px;">📢 이번주 줍줍 청약 소식</h1>
                <p style="margin: 5px 0;">청약 업데이트를 확인하세요!</p>
            </div>

            <!-- 블로그 리스트 -->
            <div style="margin-top: 20px; background: white; padding: 15px; border-radius: 8px; 
                        box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                <h2 style="border-bottom: 2px solid black; padding-bottom: 5px;">📝 최신 줍줍 관련 블로그</h2>
                
                <ul style="list-style: none; padding: 0;">
                    {articles}
                </ul>
            </div>

        </body>
        </html>
        """

        self.article_template = """
        <li style="padding: 10px 0; border-bottom: 1px solid #ddd;">
             <a href="{url}" style="color: #0073e6; text-decoration: none; font-weight: bold;">{title}</a>
             - <strong>{date}</strong>
        </li>
        """


    def generate_html(self, articles):
        """블로그 뉴스레터 HTML 생성"""
        if not articles:
            articles_html = "<p>최근 줍줍일정이 없습니다.</p>"
        else:
            articles_html = "".join(
                self.article_template.format(title=item[0], url=item[1],date=item[2]) for item in articles
            )
        return self.html_template.format(articles=articles_html)
