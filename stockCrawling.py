import json
import yfinance as yf

class StockCrawler:
    def __init__(self):
        self.symbols = {
            'QQQ': 'QQQ',
            'SPY': 'SPY',
            'USD/KRW': 'KRW=X',
            'EUR/KRW': 'EURKRW=X',
            'Gold': 'GC=F',  # Gold Futures
            'Oil': 'CL=F',   # Crude Oil Futures
            'Silver': 'SI=F', # Silver Futures
            'Copper': 'HG=F'  # Copper Futures
        }
    
    def fetch_stock_data(self):
        """모든 주식 및 원자재 데이터 가져오기"""
        all_data = []
        
        for name, symbol in self.symbols.items():
            try:
                data = self._get_price_data(name, symbol)
                if data:
                    all_data.append(data)
            except Exception as e:
                print(f"Error fetching {name}: {e}")
                all_data.append({
                    'name': name,
                    'symbol': symbol,
                    'current_price': 'N/A',
                    'prev_price': 'N/A',
                    'change': 'N/A',
                    'change_percent': 'N/A',
                    'is_up': None
                })
        
        return all_data
    
    def _get_price_data(self, name, symbol):
        """개별 종목의 가격 데이터 가져오기"""
        try:
            # 최근 5일 데이터 가져오기 (주말 고려)
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="5d")
            
            if len(hist) < 2:
                return None
            
            # 최근 2일 데이터 (오늘, 어제)
            current_price = hist['Close'].iloc[-1]
            prev_price = hist['Close'].iloc[-2]
            
            # 변화량 및 변화율 계산
            change = current_price - prev_price
            change_percent = (change / prev_price) * 100 
            #if change < 0: change_percent = change_percent * -1 
            
            # 가격 포맷팅
            if 'KRW' in symbol:
                # 환율은 소수점 2자리
                formatted_current = f"{current_price:,.2f}"
                formatted_prev = f"{prev_price:,.2f}"
                formatted_change = f"{abs(change):,.2f}"
            elif name in ['Gold', 'Oil', 'Silver', 'Copper']:
                # 원자재는 소수점 2자리
                formatted_current = f"${current_price:,.2f}"
                formatted_prev = f"${prev_price:,.2f}"
                formatted_change = f"${abs(change):,.2f}"
            else:
                # 주식은 소수점 2자리
                formatted_current = f"${current_price:,.2f}"
                formatted_prev = f"${prev_price:,.2f}"
                formatted_change = f"${abs(change):,.2f}"
            
            return {
                'name': name,
                'symbol': symbol,
                'current_price': formatted_current,
                'prev_price': formatted_prev,
                'change': formatted_change,
                'change_percent': f"{(change_percent):.2f}%",
                'last_update': hist.index[-1].strftime('%Y-%m-%d')
            }
            
        except Exception as e:
            print(f"Error in _get_price_data for {name}: {e}")
            return None

if __name__ == "__main__":
    stock_crawler = StockCrawler()
    stock_data=stock_crawler.fetch_stock_data()

    # JSON 형태로 보기 좋게 출력
    print(json.dumps(stock_data, indent=2, ensure_ascii=False))