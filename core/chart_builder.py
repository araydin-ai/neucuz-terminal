import pandas as pd
from core.indicators import Indicator

class ChartBuilder:
    #Bu sınıfta yahoo finance'den çekilen ve düzenlenen dataframe yapısı lightweightcharts kütüphanesinin anlayacağı formata(JSON) dönüştürülür.
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.series = []
        self._add_candlestick_series()

    def _add_candlestick_series(self):
        """Ana mum grafiğini oluşturur."""
        # JSON formatında NaN veriye yer yok bu yüzden .dropna fonksiyonu ile eksik verileri temizliyoruz
        ohlc_df = self.df[['time', 'open', 'high', 'low', 'close']].dropna()
        
        candlestick_data = ohlc_df.to_dict('records')
        
        self.series.append({
            "type": 'Candlestick',
            "data": candlestick_data,
            "options": {
                "upColor": '#26a69a', "downColor": '#ef5350',
                "borderVisible": False, "wickUpColor": '#26a69a', "wickDownColor": '#ef5350',
                "priceScaleId": "right",
                "priceLineVisible": True,
                "lastValueVisible": True   
            }
        })

    def add_indicator(self, indicator: Indicator):
        #bir indikatör nesnesinin hesaplamasını yaptırıp grafiğe ekler
        indicator_series_list = indicator.calculate(self.df)
        self.series.extend(indicator_series_list)

    def build_options(self, has_volume: bool) -> dict:
        #GRAfiğin genel ayarları
        chart_options = {
            "layout": {
                "textColor": '#d1d4dc',
                "background": {"type": 'solid', "color": '#131722'}
            },
            "grid": {
                "vertLines": {"color": "rgba(42, 46, 57, 0.5)"},
                "horzLines": {"color": "rgba(42, 46, 57, 0.5)"}
            },
            "height": 600,
            "rightPriceScale": {
                "visible": True,
                "scaleMargins": {"top": 0.1, "bottom": 0.2}
            },
            "leftPriceScale": {
                "visible": False,
                "borderVisible": False,
                "scaleMargins": {"top": 0.8, "bottom": 0}
            },
            "crosshair": {"mode": 0}
        }
            
        return chart_options

    def get_chart_config(self, has_volume: bool) -> dict:
        return {
            "chart": self.build_options(has_volume),
            "series": self.series
        }