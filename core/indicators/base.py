from abc import ABC, abstractmethod
import pandas as pd

class Indicator(ABC):
    """
    Tüm indikatörler için soyut temel sınıf (Abstract Base Class).
    """
    @abstractmethod
    def calculate(self, df: pd.DataFrame) -> list[dict]:
        """
        Verilen DataFrame üzerinde indikatörü hesaplar ve
        lightweight-charts formatında bir liste (series configuration) döndürür.
        """
        pass
