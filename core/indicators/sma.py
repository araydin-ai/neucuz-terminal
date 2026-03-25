import pandas as pd
from .base import Indicator

class SMAIndicator(Indicator):
    def __init__(self, period: int, color: str, title: str):
        self.period = period
        self.color = color
        self.title = title

    def calculate(self, df: pd.DataFrame) -> list[dict]:
        # Hesaplama
        sma_series = df['close'].rolling(window=self.period).mean()
        
        # Veriyi formatla
        data = []
        for time, value in zip(df['time'], sma_series):
            if pd.notna(value):
                data.append({"time": time, "value": value})

        # Konfigürasyonu döndür
        return [{
            "type": 'Line',
            "data": data,
            "options": {
                "color": self.color,
                "lineWidth": 2,
                "priceScaleId": "right",
                "title": self.title,
                "priceLineVisible": False, # Yatay çizgi GİZLİ (Grafik temizliği için)
                "lastValueVisible": True   # Etiket GÖRÜNÜR (Değeri okumak için)
            }
        }]