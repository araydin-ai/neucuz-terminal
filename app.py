import streamlit as st

# 1. Sayfa Ayarları (Tam Ekran ve Sekme Başlığı)
st.set_page_config(
    page_title="NeUcuz | Yapay Zeka Destekli Finans Terminali", 
    page_icon="📈", 
    layout="wide"
)

# 2. CSS Makyajı (CryptoJawern ve BUders Tarzı Modern Görünüm)
st.markdown("""
<style>
    /* Üst menü ve gereksiz boşlukları gizleme */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Ana Başlık (Hero Section) Gradient Efekti */
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #FF8A00, #E52E71);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
        padding-top: 50px;
    }
    .hero-subtitle {
        font-size: 1.3rem;
        color: #A0AEC0;
        text-align: center;
        margin-top: 15px;
        margin-bottom: 40px;
    }
    
    /* Özellik Kartları (Bento Box Mimarisi) */
    .feature-card {
        background-color: #1E1E2F;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #2D2D44;
        text-align: center;
        transition: transform 0.3s ease, border-color 0.3s ease;
        height: 250px;
    }
    .feature-card:hover {
        transform: translateY(-10px);
        border-color: #FF8A00;
    }
    .feature-icon {
        font-size: 3.5rem;
        margin-bottom: 15px;
    }
    
    /* Alt Bilgi (Footer) */
    .footer {
        text-align: center;
        margin-top: 80px;
        padding-bottom: 20px;
        color: #718096;
        font-size: 0.9rem;
        border-top: 1px solid #2D2D44;
        padding-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 3. HERO SECTION (Karşılama Ekranı)
st.markdown('<div class="hero-title">Borsa Analizinde Yapay Zeka Dönemi</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">NeUcuz ile teknik ve temel analizi tek bir terminalde birleştirin.<br>Karmaşık verileri yapay zeka ile saniyeler içinde okuyun.</div>', unsafe_allow_html=True)

# Terminale Git Butonu (Sayfanın tam ortasına hizalamak için kolonları kullanıyoruz)
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    # Kullanıcıyı pages/1_Terminal.py dosyasına yönlendiren Streamlit butonu
    st.page_link("pages/1_Terminal.py", label="🚀 Terminali Ücretsiz Başlat", use_container_width=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

# 4. ÖZELLİKLER KARTLARI (Neden NeUcuz?)
st.markdown("<h3 style='text-align: center; margin-bottom: 30px; color: white;'>Platform Özellikleri</h3>", unsafe_allow_html=True)

f_col1, f_col2, f_col3 = st.columns(3)

with f_col1:
    st.markdown('''
    <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <h4 style="color: white;">Yapay Zeka Asistanı</h4>
        <p style="color: #A0AEC0;">Gemini AI entegrasyonu ile grafiklerinizi anında yorumlatın ve profesyonel öngörüler alın.</p>
    </div>
    ''', unsafe_allow_html=True)

with f_col2:
    st.markdown('''
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <h4 style="color: white;">Anlık Veri Akışı</h4>
        <p style="color: #A0AEC0;">Borsa İstanbul (BIST) hisselerini saniyeler içinde çekin. Gecikmesiz ve güvenilir altyapı.</p>
    </div>
    ''', unsafe_allow_html=True)

with f_col3:
    st.markdown('''
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <h4 style="color: white;">Gelişmiş İndikatörler</h4>
        <p style="color: #A0AEC0;">Hareketli ortalamalar, osilatörler ve hacim profilleri ile TradingView kalitesinde analiz yapın.</p>
    </div>
    ''', unsafe_allow_html=True)

# 5. ALT BİLGİ (Footer)
st.markdown('''
<div class="footer">
    © 2026 neucuz.com.tr | Tüm hakları saklıdır.<br>
    Bu platform bir Selçuk Üniversitesi Bilgisayar Mühendisliği projesidir.
</div>
''', unsafe_allow_html=True)