import pandas as pd
from .base import Indicator

class BollingerIndicator(Indicator):
    def __init__(self, period: int = 20, std_dev: int = 2):
        self.period = period
        self.std_dev = std_dev

    def calculate(self, df: pd.DataFrame) -> list[dict]:
        sma = df['close'].rolling(window=self.period).mean()
        std = df['close'].rolling(window=self.period).std()
        upper = sma + (self.std_dev * std)
        lower = sma - (self.std_dev * std)

        upper_data = [{"time": t, "value": v} for t, v in zip(df['time'], upper) if pd.notna(v)]
        lower_data = [{"time": t, "value": v} for t, v in zip(df['time'], lower) if pd.notna(v)]

        # Bollinger iki çizgiden oluşur, bu yüzden liste içinde iki konfigürasyon döneriz
        # priceLineVisible: False -> Yatay çizgiyi kapat
        # lastValueVisible: True  -> Sağ eksendeki etiketi aç
        common_options = {
            "color": 'rgba(46, 204, 113, 0.5)', 
            "lineWidth": 1, 
            "priceScaleId": "right",
            "priceLineVisible": False,
            "lastValueVisible": True
        }
        
        return [
            {"type": 'Line', "data": upper_data, "options": {**common_options}}, 
            {"type": 'Line', "data": lower_data, "options": {**common_options}}  
        ]
