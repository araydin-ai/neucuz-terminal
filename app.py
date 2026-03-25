import streamlit as st

st.set_page_config(
    page_title="NeUcuz | Yapay Zeka Destekli Finans Terminali", 
    page_icon="📈", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    .stApp {
        background-color: #11131a;
        color: #d1d4dc;
        font-family: 'Inter', sans-serif;
    }
    
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        max-width: 100%;
        padding-left: 0;
        padding-right: 0;
    }

    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 50px;
        background-color: #11131a;
        border-bottom: 1px solid #222631;
    }
    
    .logo-text {
        font-size: 24px;
        font-weight: 800;
        color: white;
        margin: 0;
    }
    .logo-highlight {
        color: #ff8a00;
    }
    
    .hero-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 100px 20px;
        text-align: center;
        background: radial-gradient(circle at 50% 50%, #1e222d 0%, #11131a 100%);
    }

    .hero-title {
        font-size: 4rem;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 20px;
        line-height: 1.1;
    }
    
    .hero-title span {
        background: -webkit-linear-gradient(45deg, #FF8A00, #ffb347);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        font-size: 1.2rem;
        color: #8fa3b0;
        max-width: 700px;
        margin-bottom: 40px;
        line-height: 1.6;
    }

    .section-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 800;
        color: white;
        margin-top: 80px;
        margin-bottom: 50px;
    }
    .section-title span {
        color: #ff8a00;
    }

    .custom-footer {
        background-color: #0b0e14;
        padding: 60px 50px 30px 50px;
        border-top: 1px solid #222631;
        margin-top: 100px;
    }
    
    .footer-grid {
        display: grid;
        grid-template-columns: 2fr 1fr 1fr 1fr;
        gap: 40px;
        margin-bottom: 40px;
    }
    
    .footer-col h4 {
        color: white;
        font-weight: 700;
        margin-bottom: 20px;
        font-size: 1.1rem;
    }
    
    .footer-col p, .footer-col a {
        color: #8fa3b0;
        text-decoration: none;
        font-size: 0.9rem;
        line-height: 1.8;
        display: block;
    }
    
    .disclaimer-box {
        background-color: #131722;
        border: 1px solid #222631;
        border-radius: 8px;
        padding: 20px;
        color: #6b7a85;
        font-size: 0.75rem;
        line-height: 1.5;
        margin-bottom: 20px;
        text-align: justify;
    }
    
    .copyright-row {
        display: flex;
        justify-content: space-between;
        color: #6b7a85;
        font-size: 0.8rem;
        border-top: 1px solid #222631;
        padding-top: 20px;
    }

    .feature-card {
        background-color: #1a1e29;
        border: 1px solid #222631;
        border-radius: 12px;
        padding: 30px;
        height: 100%;
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        border-color: #ff8a00;
    }
    .card-icon {
        width: 50px;
        height: 50px;
        background-color: rgba(255, 138, 0, 0.1);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        color: #ff8a00;
        margin-bottom: 20px;
    }
    .feature-card h3 {
        color: white;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 15px;
    }
    .feature-card p {
        color: #8fa3b0;
        font-size: 0.95rem;
        line-height: 1.5;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="navbar">
    <div class="logo-text">Ne<span class="logo-highlight">Ucuz</span></div>
    <div style="display: flex; gap: 30px; color: white; font-weight: 600; font-size: 0.9rem;">
        <span style="cursor:pointer; color: #ff8a00;">Ana Sayfa</span>
        <span style="cursor:pointer; color: #8fa3b0;">Özellikler</span>
        <span style="cursor:pointer; color: #8fa3b0;">Yapay Zeka AI</span>
        <span style="cursor:pointer; color: #8fa3b0;">İletişim</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">Borsa Analizinde<br><span>Yapay Zeka</span> Dönemi</h1>
    <p class="hero-subtitle">NeUcuz ile teknik ve temel analizi tek bir terminalde birleştirin. Piyasayı tahmin etmiyoruz, karmaşık verileri yapay zeka ile saniyeler içinde okuyup disiplinli bir şekilde önünüze seriyoruz.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 2])
with col3:
    st.page_link("pages/1_terminal.py", label="🚀 Terminali Başlat", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>Neden <span>NeUcuz?</span></div>", unsafe_allow_html=True)

# Özellik Kartları Bölümü (Container ile ortalama)
with st.container():
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="card-icon">🤖</div>
            <h3>Hibrit AI Analisti</h3>
            <p>Gemini AI entegrasyonu ile grafiklerinizi, fiyat baskılarını ve trend dönüşlerini yapay zekaya anında yorumlatın. Sadece fiyatı değil, piyasa psikolojisini okuyun.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="card-icon">⚡</div>
            <div style="background-color: rgba(38, 166, 154, 0.2); color: #26a69a; padding: 4px 8px; border-radius: 4px; font-size: 0.7rem; font-weight: bold; width: fit-content; margin-bottom: 10px;">ANLIK VERİ</div>
            <h3>Gecikmesiz Altyapı</h3>
            <p>BIST, Kripto, ABD Borsaları ve Emtia piyasalarındaki tüm verileri tek bir platformda toplayın. Hızlı veri çekimi ile fırsatları kaçırmayın.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="card-icon">📊</div>
            <h3>Şeffaf İndikatörler</h3>
            <p>Karmaşıklıktan uzak, sade ve anlaşılır grafikler. Yüksek zaman dilimi odaklı analizler ile piyasadaki gürültüden uzaklaşarak asıl trendi yakalayın.</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="custom-footer">
<div class="footer-grid">
<div class="footer-col">
<h4><span style="color:white;">Ne</span><span style="color:#ff8a00;">Ucuz</span></h4>
<p>NeUcuz, piyasa döngülerini doğru okumaya odaklanan, şeffaf paylaşımlar yapan bir finansal analiz topluluğudur.</p>
</div>
<div class="footer-col">
<h4>Navigasyon</h4>
<p>Ana Sayfa</p>
<p>Terminal (Platform)</p>
<p>Özellikler</p>
<p>SSS</p>
</div>
<div class="footer-col">
<h4>Kaynaklar</h4>
<p>Telegram Kanalı</p>
<p>X Paylaşımları</p>
<p>Eğitimler</p>
</div>
<div class="footer-col">
<h4>Hızlı Destek</h4>
<p>Analizler, platform veya topluluğumuz hakkında her türlü sorunuz için resmi mail adresimiz üzerinden bize ulaşabilirsiniz.</p>
<br>
<p style="color: #ff8a00;">✉️ destek@neucuz.com.tr</p>
</div>
</div>

<div style="background-color: #1a1e29; border-radius: 12px; padding: 24px; color: #8fa3b0; font-size: 0.8rem; line-height: 1.6; margin-bottom: 30px; border: 1px solid #222631;">
Burada yer alan bilgi, yorum ve tavsiyeler yatırım danışmanlığı kapsamında değildir. Yatırım danışmanlığı hizmeti, aracı kurumlar, portföy yönetim şirketleri, mevduat kabul etmeyen bankalar ile müşteri arasında imzalanacak yatırım danışmanlığı sözleşmesi çerçevesinde sunulmaktadır. Bu sayfada yazılanlar sadece kişisel görüşlerdir ve mali durumunuz ile risk-getiri tercihlerinize uygun olmayabilir. Bu nedenle bu sayfada yer alan bilgi ve yazılara dayanarak yatırım yapılmamalıdır.
</div>

<div class="copyright-row">
<div>© 2026 NeUcuz. Tüm hakları saklıdır.</div>
<div style="display: flex; gap: 20px;">
<span>İletişim</span>
<span>SSS</span>
</div>
</div>
</div>
""", unsafe_allow_html=True)