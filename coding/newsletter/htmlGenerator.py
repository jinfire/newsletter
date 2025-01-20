class HTMLGenerator:
    def __init__(self):
        self.html_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>News Update</title>
        </head>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; background-color: #f9f9f9; margin: 20px; padding: 0;">
            <h1 style="text-align: center; color: #333;">Today's News</h1>
            {articles}
        </body>
        </html>
        """
        self.article_template = """
        <div style="background-color: #ffffff; border: 1px solid #ddd; border-radius: 5px; 
                    padding: 15px; margin-bottom: 20px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
            <div style="font-size: 20px; font-weight: bold; margin-bottom: 5px;">{title}</div>
            <div style="font-size: 14px; color: gray; text-align: right; margin-bottom: 10px;">{press} | {date}</div>
            <div style="font-size: 16px; margin-bottom: 10px;">{summary}</div>
            <a href="{url}" style="font-size: 14px; color: #007bff; text-decoration: none; font-weight: bold;">
                Read more...
            </a>
        </div>
        """

    def generate_html(self, articles):
        """Generate HTML content for email."""
        articles_html = ""
        for item in articles:
            title, url, summary, press, date = item
            articles_html += self.article_template.format(
                title=title, url=url, summary=summary, press=press, date=date
            )
        return self.html_template.format(articles=articles_html)