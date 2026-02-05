# stockHtmlGenerator.py
from datetime import datetime

class StockHtmlGenerator:
    def generate_html(self, stock_data):
        """주식 데이터를 HTML로 변환"""
        
        current_date = datetime.now().strftime('%Y년 %m월 %d일')
        
        # 데이터를 카테고리별로 분류
        etf_data = [d for d in stock_data if d['name'] in ['QQQ', 'SPY']]
        stock_individual_data = [d for d in stock_data if d['name'] in ['Apple', 'NVIDIA', 'Google', 'Microsoft']]
        forex_data = [d for d in stock_data if 'KRW' in d['name']]
        commodity_data = [d for d in stock_data if d['name'] in ['Gold', 'Oil', 'Silver', 'Copper']]
        treasury_data = [d for d in stock_data if 'Treasury' in d['name']]
        
        html = f"""
        <!DOCTYPE html>
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>오늘의 투자 정보</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f5f5f5;
                }}
                .container {{
                    background-color: white;
                    border-radius: 10px;
                    padding: 30px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }}
                .header {{
                    text-align: center;
                    border-bottom: 3px solid #2c3e50;
                    padding-bottom: 20px;
                    margin-bottom: 30px;
                }}
                .header h1 {{
                    color: #2c3e50;
                    margin: 0;
                    font-size: 28px;
                }}
                .header p {{
                    color: #7f8c8d;
                    margin: 10px 0 0 0;
                    font-size: 14px;
                }}
                .section {{
                    margin-bottom: 35px;
                }}
                .section-title {{
                    font-size: 20px;
                    color: #2c3e50;
                    border-left: 4px solid #3498db;
                    padding-left: 15px;
                    margin-bottom: 20px;
                    font-weight: bold;
                }}
                .stock-card {{
                    background-color: #f8f9fa;
                    border-radius: 8px;
                    padding: 20px;
                    margin-bottom: 15px;
                    border-left: 4px solid #95a5a6;
                    transition: transform 0.2s;
                }}
                .stock-card:hover {{
                    transform: translateX(5px);
                }}
                .stock-card.up {{
                    border-left-color: #e74c3c;
                    background-color: #fff5f5;
                }}
                .stock-card.down {{
                    border-left-color: #3498db;
                    background-color: #f0f8ff;
                }}
                .stock-name {{
                    font-size: 18px;
                    font-weight: bold;
                    color: #2c3e50;
                    margin-bottom: 10px;
                }}
                .stock-symbol {{
                    font-size: 12px;
                    color: #95a5a6;
                    margin-left: 8px;
                }}
                .price-row {{
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-top: 12px;
                }}
                .current-price {{
                    font-size: 24px;
                    font-weight: bold;
                    color: #2c3e50;
                }}
                .change-info {{
                    text-align: right;
                }}
                .change {{
                    font-size: 16px;
                    font-weight: bold;
                }}
                .change.up {{
                    color: #e74c3c;
                }}
                .change.down {{
                    color: #3498db;
                }}
                .prev-price {{
                    font-size: 13px;
                    color: #7f8c8d;
                    margin-top: 5px;
                }}
                .arrow {{
                    display: inline-block;
                    margin-right: 5px;
                }}
                .footer {{
                    margin-top: 40px;
                    text-align: center;
                    color: #95a5a6;
                    font-size: 12px;
                    border-top: 1px solid #ecf0f1;
                    padding-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>📊 오늘의 투자 정보</h1>
                    <p>{current_date}</p>
                </div>
        """
        
        # ETF 섹션
        if etf_data:
            html += """
                <div class="section">
                    <div class="section-title">🎯 미국 ETF</div>
            """
            for stock in etf_data:
                html += self._generate_stock_card(stock)
            html += "</div>"
        
         # 개별 주식 섹션
        if stock_individual_data:
            html += """
                <div class="section">
                    <div class="section-title">💼 미국 주식</div>
            """
            for stock in stock_individual_data:
                html += self._generate_stock_card(stock)
            html += "</div>"
        
        # 환율 섹션
        if forex_data:
            html += """
                <div class="section">
                    <div class="section-title">💱 환율</div>
            """
            for stock in forex_data:
                html += self._generate_stock_card(stock)
            html += "</div>"
        
        # 원자재 섹션
        if commodity_data:
            html += """
                <div class="section">
                    <div class="section-title">🏭 원자재</div>
            """
            for stock in commodity_data:
                html += self._generate_stock_card(stock)
            html += "</div>"
        
        # 국채 금리 섹션
        if treasury_data:
            html += """
                <div class="section">
                    <div class="section-title">📈 미국 국채 금리</div>
            """
            for stock in treasury_data:
                html += self._generate_stock_card(stock)
            html += "</div>"
        
        html += """
                <div class="footer">
                    <p>본 정보는 투자 참고용이며, 투자 결정에 대한 책임은 투자자 본인에게 있습니다.</p>
                    <p>Data provided by Yahoo Finance</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        return html
    
    def _generate_stock_card(self, stock):
        """개별 주식 카드 HTML 생성"""
        is_up = stock.get('is_up', None)
        if is_up is True:
            arrow = '▲'
            card_class = 'up'
            change_class = 'up'
        elif is_up is False:
            arrow = '▼'
            card_class = 'down'
            change_class = 'down'
        else:
            arrow = '-'
            card_class = ''
            change_class = ''
        
        return f"""
                    <div class="stock-card {card_class}">
                        <div class="stock-name">
                            {stock['name']}
                            <span class="stock-symbol">{stock['symbol']}</span>
                        </div>
                        <div class="price-row">
                            <div class="current-price">{stock['current_price']}</div>
                            <div class="change-info">
                                <div class="change {change_class}">
                                    <span class="arrow">{arrow}</span>
                                    {stock['change']} ({stock['change_percent']})
                                </div>
                                <div class="prev-price">전일: {stock['prev_price']}</div>
                            </div>
                        </div>
                    </div>
        """