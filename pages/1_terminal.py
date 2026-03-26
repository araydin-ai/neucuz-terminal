import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts
from core.data_manager import StockDataManager
from core.chart_builder import ChartBuilder
from core.indicators import SMAIndicator, BollingerIndicator, VolumeIndicator
from core.market_symbols import BIST_SYMBOLS, CRYPTO_SYMBOLS, US_SYMBOLS, COMMODITY_SYMBOLS
from core.ai_agent import AIAgent

# --- Sayfa Ayarları ---
st.set_page_config(page_title="NeUcuz? - Global Terminal", page_icon="🌍", layout="wide")

def main():
    try:
        # --- UI Başlık ---
        st.title("🌍 NeUcuz? | Global Piyasa Terminali")

        # --- SIDEBAR ---
        st.sidebar.header("⚙️ Piyasa & Grafik Ayarları")
        
        # 1. Piyasa Seçimi
        piyasa_tipi = st.sidebar.selectbox(
            "Piyasa Seçimi",
            ["BIST", "ABD", "Kripto", "Emtia/Forex"]
        )

        # Seçilen piyasaya göre sembol listesini belirle
        aktif_sozluk = {}
        if piyasa_tipi == "BIST":
            aktif_sozluk = BIST_SYMBOLS
        elif piyasa_tipi == "ABD":
            aktif_sozluk = US_SYMBOLS
        elif piyasa_tipi == "Kripto":
            aktif_sozluk = CRYPTO_SYMBOLS
        elif piyasa_tipi == "Emtia/Forex":
            aktif_sozluk = COMMODITY_SYMBOLS

        # 2. Hisse/Varlık Seçimi (Arama Özellikli Selectbox)
        secilen_kod = st.sidebar.selectbox(
            "Varlık Seçiniz",
            options=list(aktif_sozluk.keys()),
            format_func=lambda x: f"{x} - {aktif_sozluk[x]}"
        )
        
        # Seçilen kodun adını al (Grafik başlığı için)
        varlik_adi = aktif_sozluk[secilen_kod]

        # 3. Zaman Seçimi
        zaman_secenekleri = ["1 Ay", "3 Ay", "6 Ay", "1 Yıl", "3 Yıl", "5 Yıl", "10 Yıl", "Tümü"]
        zaman_secimi = st.sidebar.selectbox("Zaman Aralığı", zaman_secenekleri, index=3)
        
        periyot_map = {
            "1 Ay": "1mo", "3 Ay": "3mo", "6 Ay": "6mo", 
            "1 Yıl": "1y", "3 Yıl": "3y", "5 Yıl": "5y", 
            "10 Yıl": "10y", "Tümü": "max"
        }
        
        st.sidebar.divider()
        
        # 4. İndikatör Seçimi
        mevcut_indikatorler = ["Hacim", "SMA 50", "SMA 200", "Bollinger Bantları"]
        secilen_indikatorler = st.sidebar.multiselect(
            "📊 İndikatörler",
            options=mevcut_indikatorler,
            default=["Hacim", "SMA 50"]
        )

        # --- 1. VERİ YÖNETİMİ ---
        # secilen_kod artık doğrudan sözlükten geliyor (Örn: "BTC-USD" veya "THYAO")
        df = StockDataManager.get_history(secilen_kod, periyot_map[zaman_secimi], market_type=piyasa_tipi)

        if df is None:
            st.error(f"Veri bulunamadı! '{secilen_kod}' için veri çekilemedi.")
            return

        # --- 2. GRAFİK İNŞASI ---
        builder = ChartBuilder(df)

        # İndikatörleri ekle
        if "Hacim" in secilen_indikatorler:
            builder.add_indicator(VolumeIndicator())
            
        if "SMA 50" in secilen_indikatorler:
            builder.add_indicator(SMAIndicator(period=50, color='#f39c12', title="SMA 50"))
            
        if "SMA 200" in secilen_indikatorler:
            builder.add_indicator(SMAIndicator(period=200, color='#3498db', title="SMA 200"))
            
        if "Bollinger Bantları" in secilen_indikatorler:
            builder.add_indicator(BollingerIndicator())

        # --- 3. BİLGİ KARTI ---
        son_fiyat = df['close'].iloc[-1]
        ilk_fiyat = df['close'].iloc[0]
        degisim_yuzde = ((son_fiyat - ilk_fiyat) / ilk_fiyat) * 100
        fiyat_farki = son_fiyat - ilk_fiyat
        
        son_hacim = df['volume'].iloc[-1] if 'volume' in df.columns else 0
        
        st.markdown(f"### {secilen_kod} - {varlik_adi}")
        
        m_col1, m_col2, m_col3 = st.columns(3)
        
        with m_col1:
            st.metric(
                label="Son Fiyat", 
                value=f"{son_fiyat:,.2f}", 
                delta=f"{fiyat_farki:,.2f} ({degisim_yuzde:+.2f}%)"
            )
            
        with m_col2:
            st.metric(
                label="Periyot Analizi", 
                value=zaman_secimi,
                delta="Zaman Aralığı",
                delta_color="off"
            )
            
        with m_col3:
            st.metric(
                label="İşlem Hacmi (Son)", 
                value=f"{son_hacim:,.0f}" if son_hacim > 0 else "Veri Yok",
                delta="Güncel Bar",
                delta_color="off"
            )
            
        st.markdown("<br>", unsafe_allow_html=True)

        # --- 4. RENDER ---
        has_volume = "Hacim" in secilen_indikatorler
        chart_config = builder.get_chart_config(has_volume)
        
        renderLightweightCharts([chart_config], key='grafik_final')

        # --- 5. YAPAY ZEKA ANALİSTİ ---
        st.divider()
        st.subheader("🤖 Yapay Zeka Analisti")
        st.caption("Grafikteki verileri ve trendleri sizin için yorumlar.")

        # Sohbet geçmişini başlat (Session State)
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Geçmiş mesajları ekrana bas
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Kullanıcıdan girdi al
        if prompt := st.chat_input("Bu grafik hakkında ne öğrenmek istersin?"):
            # 1. Kullanıcı mesajını ekrana bas
            st.chat_message("user").markdown(prompt)
            # 2. Mesajı geçmişe kaydet
            st.session_state.messages.append({"role": "user", "content": prompt})

            # 3. AI Cevabını Üret
            with st.chat_message("assistant"):
                agent = AIAgent()
                with st.spinner(f"{secilen_kod} verileri analiz ediliyor..."):
                    # O anki DataFrame'i ve Sembolü ajana gönderiyoruz
                    response = agent.ask(prompt, df, secilen_kod)
                    st.markdown(response)
            
            # 4. AI Cevabını geçmişe kaydet
            st.session_state.messages.append({"role": "assistant", "content": response})

    except Exception as e:
        st.error(f"Beklenmedik bir hata oluştu: {e}")

if __name__ == "__main__":
    main()