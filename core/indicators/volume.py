import pandas as pd
from .base import Indicator

class VolumeIndicator(Indicator):
    def calculate(self, df: pd.DataFrame) -> list[dict]:
        volume_data = []
        for _, row in df.iterrows():
            color = '#26a69a' if row['close'] >= row['open'] else '#ef5350'
            volume_data.append({
                "time": row['time'],
                "value": row['volume'],
                "color": color
            })

        return [{
            "type": 'Histogram',
            "data": volume_data,
            "options": {
                "priceFormat": {"type": 'volume'},
                "priceScaleId": "left",
                "lastValueVisible": True,  # Son değer etiketi görünsün (Örn: 14M)
                "priceLineVisible": False  # Ancak yatay çizgi görünmesin (karmaşayı önlemek için)
            }
        }]