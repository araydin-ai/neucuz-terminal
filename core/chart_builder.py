import pandas as pd
from core.indicators import Indicator

class ChartBuilder:
    """
    Lightweight Charts için gerekli JSON yapısını hazırlar.
    """
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.series = []
        self._add_candlestick_series()

    def _add_candlestick_series(self):
        """Ana mum grafiğini oluşturur."""
        # NaN kontrolü: OHLC verilerinde NaN varsa o satırları çıkarıyoruz.
        # JSON formatında NaN hatası almamak için bu adım kritiktir.
        ohlc_df = self.df[['time', 'open', 'high', 'low', 'close']].dropna()
        
        candlestick_data = ohlc_df.to_dict('records')
        
        self.series.append({
            "type": 'Candlestick',
            "data": candlestick_data,
            "options": {
                "upColor": '#26a69a', "downColor": '#ef5350',
                "borderVisible": False, "wickUpColor": '#26a69a', "wickDownColor": '#ef5350',
                "priceScaleId": "right",
                # "title": "" -> Başlık boş, yazı yazmasın
                "priceLineVisible": True,  # Yatay fiyat çizgisi GÖRÜNSÜN
                "lastValueVisible": True   # Güncel fiyat etiketi GÖRÜNSÜN
            }
        })

    def add_indicator(self, indicator: Indicator):
        """Bir Indicator nesnesini grafiğe ekler."""
        indicator_series_list = indicator.calculate(self.df)
        # Önceki versiyondaki toplu priceLineVisible gizleme döngüsü kaldırıldı.
        # Artık her indikatör kendi ayarını (volume.py, sma.py) kendisi belirliyor.
        self.series.extend(indicator_series_list)

    def build_options(self, has_volume: bool) -> dict:
        """Grafik genel ayarlarını döndürür."""
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
                # Fiyat grafiğini alttan %20 yukarı itiyoruz.
                # Böylece alttaki hacim barları ile mumlar üst üste binmez.
                "scaleMargins": {"top": 0.1, "bottom": 0.2}
            },
            "leftPriceScale": {
                "visible": False, # Eksen çizgileri ve yazıları GİZLİ (Hayalet Eksen)
                "borderVisible": False, # Kenar çizgisi de yok
                # GİZLİ AMA ETKİLİ: Eksen görünmese bile bu margin ayarı çalışır.
                # Hacim barları grafiğin sadece en alt %20'sine hapsolur.
                "scaleMargins": {"top": 0.8, "bottom": 0}
            },
            "crosshair": {"mode": 0}
        }
            
        return chart_options

    def get_chart_config(self, has_volume: bool) -> dict:
        """Render için son çıktıyı verir."""
        return {
            "chart": self.build_options(has_volume),
            "series": self.series
        }