from abc import ABC, abstractmethod
import pandas as pd
# Her indikatörün miras almak zorunda olacağı indikatör soyut sınıfımız,böylece OOP'ye uygun bir mimari kurdum
class Indicator(ABC):

    @abstractmethod
    def calculate(self, df: pd.DataFrame) -> list[dict]:
       # Yine tüm indikatörler için overwrite edilmesi zorunlu bir hesaplama fonksiyonu.Bu fonksiyon lightweightcharts kütüphanesine uygun çıktı üretir(liste).
        pass
