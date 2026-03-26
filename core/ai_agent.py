import streamlit as st
import google.generativeai as genai
import pandas as pd

class AIAgent:
    def __init__(self):
        try: # try except yapısı sayesinde hata durumunda mesaj fırlatılır
            # Streamlit secrets içinde google API key aranır
            if "GOOGLE_API_KEY" in st.secrets:
                api_key = st.secrets["GOOGLE_API_KEY"]
                genai.configure(api_key=api_key)
                self.model = genai.GenerativeModel('gemini-2.5-flash')
            else:
                st.error("Google API Anahtarı bulunamadı! Lütfen .streamlit/secrets.toml dosyasını kontrol edin.")
                self.model = None
        except Exception as e:
            st.error(f"AI Başlatma Hatası: {str(e)}")
            self.model = None

    def ask(self, user_query: str, df: pd.DataFrame, symbol: str) -> str:
        """
        Kullanıcı sorusunu ve TÜM veri setini Gemini'ye gönderir.
        """
        if not self.model:
            return "Yapay zeka modeli aktif değil. API anahtarını kontrol edin."

        
        if df is None or df.empty:
            data_context = "Elimizde güncel veri yok."
        else:
            # DataFrame'i CSV formatına çeviriyoruz çünkü LLM'e tabloyu metin olarak sunmamız lazım
            # index=True diyerek tarihleri de alıyoruz.
            full_data_csv = df.to_csv(index=True)
            
            # İndikatörlerin son değerlerini özet olarak alalım
            try:
                latest = df.iloc[-1]
                # data_manager.py sütunları lowercase yaptığı için küçük harf kullanıyoruz
                close_val = latest.get('close', 0)
                date_val = latest.get('time', latest.name)
                summary = f"Son Fiyat: {close_val:.2f} | Tarih: {date_val}"
            except:
                summary = "Özet veri oluşturulamadı."

            data_context = f"""
            ANALİZ EDİLEN ENSTRÜMAN: {symbol}
            GENEL ÖZET: {summary}
            
            TÜM ZAMAN ARALIĞI İÇİN VERİ SETİ (CSV FORMATINDA):
            {full_data_csv}
            """

        # 2. HİBRİT ANALİST PROMPTU
        full_prompt = f"""
        Sen uzman bir Finansal Veri Analistisin. 
        Sana kullanıcının seçtiği periyoda ait OLAN TÜM FİYAT VE İNDİKATÖR VERİLERİNİ (CSV olarak) sundum.

        VERİ SETİ:
        {data_context}

        KULLANICI SORUSU:
        "{user_query}"

        GÖREVİN:
        1. Öncelikle kullanıcının sorusunu analiz et.
        2. EĞER soru teknik analiz, trend, destek/direnç veya geçmiş performansla ilgiliyse: 
           - Verilen CSV verisinin tamamını bir bütün olarak incele.
           - Sadece son güne değil, genel trende bak.
           - Verilere dayanarak profesyonel yorum yap.
        3. EĞER soru genel kültür veya finansal terimlerle ilgiliyse (Örn: "RSI nedir?", "Hacim neden önemlidir?"):
           - Veri setini kullanmana gerek yok, kendi finansal bilgini kullan.
        4. Asla kesin yatırım tavsiyesi (Al/Sat sinyali) verme. "Görünüm pozitif/negatif", "Teknik olarak güçlü/zayıf" gibi ifadeler kullan.
        5. Cevabını Türkçe ver.
        """

        try:
            # Veri seti büyük olabileceği için stream yerine tam yanıt bekliyoruz
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"Analiz sırasında bir hata oluştu: {str(e)}"
