import yfinance as yf
import pandas as pd
import streamlit as st

class StockDataManager:
    """
    Yahoo Finance üzerinden veri çekme ve temizleme işlemlerini yönetir.
    """

    @staticmethod
    def _format_symbol(symbol: str, market_type: str) -> str:
        """
        Kullanıcı girdisini seçilen piyasaya göre Yahoo Finance formatına çevirir.
        """
        symbol = symbol.strip().upper()
        
        # Yahoo finance türk hisselerini .IS ile tanır
        if market_type == "BIST":
            return f"{symbol}.IS"
        
        return symbol

    @staticmethod
    @st.cache_data(ttl=3600) # Hız ve API limitlerine takılmamak için 1 saat cache'de tutar
    def get_history(symbol: str, period: str, market_type: str = "BIST") -> pd.DataFrame | None:
        """
        Belirtilen sembol, periyot ve piyasa türü için hisse verisini çeker ve formatlar.
        """
        try:
            formatted_symbol = StockDataManager._format_symbol(symbol, market_type)
            ticker = yf.Ticker(formatted_symbol)
            df = ticker.history(period=period)

            if df.empty:
                return None

            # 1. Index'i sütuna çevir ve kolon isimlerini küçült
            df = df.reset_index()
            df.columns = df.columns.str.lower()

            # 2. Tarih sütununu standartlaştır ('date' olarak)
            col_map = {col: 'date' for col in df.columns if col in ['date', 'datetime', 'timestamp']}
            df.rename(columns=col_map, inplace=True)

            # Eğer map işlemi sonrası date yoksa ilk sütunu date yap
            if 'date' not in df.columns:
                df.rename(columns={df.columns[0]: 'date'}, inplace=True)

            # 3. Timezone bilgisini temizle ve string formata çevir (Grafik kütüphanesi için)
            if df['date'].dt.tz is not None:
                df['date'] = df['date'].dt.tz_localize(None)
            
            df['time'] = df['date'].dt.strftime('%Y-%m-%d')

            return df

        except Exception as e:
            st.error(f"Veri çekme hatası: {e}")
            return None