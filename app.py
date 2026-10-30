import streamlit as st
import random

# Sayfa Yapılandırması
st.set_page_config(page_title="EduLingo - Akıllı Kampüs", page_icon="🍋", layout="centered")

# Tasarım & CSS Stilleri
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF9E6;
        overflow: auto !important;
    }
    .main {
        overflow: auto !important;
    }
    .main-title {
        color: #D4A017;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }
    .limoncan-box {
        background-color: #FFFFFF;
        padding: 15px 20px;
        border-radius: 15px;
        border-left: 6px solid #FFD700;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    .campus-feed {
        background-color: #FFFFFF;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #FFC107;
        margin-bottom: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .badge-box {
        background: linear-gradient(135deg, #FFF8DC, #FFFAF0);
        border: 2px solid #FFD700;
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Oturum Veritabanı Simülasyonu
if "giris_yapildi" not in st.session_state:
    st.session_state.giris_yapildi = False
if "ogrenci_bilgi" not in st.session_state:
    st.session_state.ogrenci_bilgi = {}
if "ogrenciler_veritabani" not in st.session_state:
    st.session_state.ogrenciler_veritabani = {
        "11111111111": {"no": "101", "ad": "Zeynep Yılmaz", "puan": 150, "streak": 5},
        "22222222222": {"no": "102", "ad": "Ali Rıza", "puan": 190, "streak": 3}
    }
if "haberler" not in st.session_state:
    st.session_state.haberler = [
        {"baslik": "🚨 Çikolata Krizi!", "icerik": "Etimesgut Kampüsü'nde Ali Rıza dün hocaya çikolata verdi, gören hoca ağlamaktan helak oldu! 🍫😂", "begenen": 42},
        {"baslik": "🏆 Zirve Yarışı", "icerik": "Zeynep son testte tam puan alarak liderlik koltuğunu sağlama aldı. 🔥", "begenen": 19}
    ]

# --- 1. GİRİŞ EKRANI ---
if not st.session_state.giris_yapildi:
    st.markdown('<p class="main-title">🍋 EduLingo Kampüsü</p>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style="background-color: #FFFFFF; padding: 20px; border-radius: 15px; text-align: center; border: 2px dashed #FFD700; margin-bottom: 20px;">
            <p style="font-size: 18px; color: #333; font-style: italic; font-weight: bold;">
                "Zirveye giden yol tıklamayla değil, her gün çözülen soruyla açılır! Haftanın rozetini kap, mahlasını al! 🚀"
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🔐 Güvenli Öğrenci Girişi")
    
    with st.form("giris_formu"):
        tc_input = st.text_input("T.C. Kimlik Numarası (11 Haneli):", max_chars=11)
        no_input = st.text_input("Öğrenci Numarası:")
        giris_butonu = st.form_submit_button("🚀 Kampüse Giriş Yap")
        
        if giris_butonu:
            if tc_input in st.session_state.ogrenciler_veritabani:
                kayitli = st.session_state.ogrenciler_veritabani[tc_input]
                if kayitli["no"] == no_input:
                    st.session_state.giris_yapildi = True
                    st.session_state.ogrenci_bilgi = kayitli
                    st.rerun()
                else:
                    st.error("❌ Hatalı Öğrenci Numarası!")
            else:
                if len(tc_input) == 11 and no_input:
                    yeni_ad = f"Öğrenci ({no_input})"
                    st.session_state.ogrenciler_veritabani[tc_input] = {"no": no_input, "ad": yeni_ad, "puan": 10, "streak": 1}
                    st.session_state.giris_yapildi = True
                    st.session_state.ogrenci_bilgi = st.session_state.ogrenciler_veritabani[tc_input]
                    st.rerun()
                else:
                    st.error("⚠️ Eksik veya hatalı bilgi girdin.")

# --- 2. ANA KAMPÜS EKRANI ---
else:
    ogrenci = st.session_state.ogrenci_bilgi
    
    col_baslik, col_cikis = st.columns([3, 1])
    col_baslik.title(f"🍋 Merhaba, {ogrenci['ad']}!")
    if col_cikis.button("Çıkış Yap"):
        st.session_state.giris_yapildi = False
        st.rerun()

    col_avatar, col_konusma = st.columns([1, 3])
    with col_avatar:
        st.markdown("""
            <div style="background: linear-gradient(135deg, #FFD700, #FFA500); width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 40px; box-shadow: 0 4px 8px rgba(0,0,0,0.15); margin: 0 auto;">
                🍋
            </div>
            <p style="text-align: center; font-weight: bold; color: #D4A017; margin-top: 5px;">Limoncan</p>
        """, unsafe_allow_html=True)
    
    with col_konusma:
        mesaj = f"Selam {ogrenci['ad']}! 🔥 {ogrenci['streak']} gündür seriyi bozmadın. Bu hafta rozetler çekişmeli, haftanın Nikola Tesla'sı olmak için testleri kaçırma!"
        st.markdown(f"""
            <div class="limoncan-box">
                <p style="margin: 0; font-size: 15px; color: #333333; font-weight: 500;">
                    🤖 <b>Limoncan diyor ki:</b><br>"{mesaj}"
                </p>
            </div>
        """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    c1.metric("🏆 Toplam Puan (XP)", ogrenci["puan"])
    c2.metric("🔥 Günlük Seri", f"{ogrenci['streak']} Gün")

    st.markdown("---")

    sekme1, sekme2, sekme3 = st.tabs(["📰 Kampüs Panosu", "📝 Günün Testi", "👑 Haftanın Mahlasları & Rozetler"])
    
    with sekme1:
        st.subheader("Okulda Neler Oluyor?")
        for index, haber in enumerate(st.session_state.haberler):
            st.markdown(f"""
            <div class="campus-feed">
                <h4 style="color: #D4A017; margin: 0;">{haber['baslik']}</h4>
                <p style="color: #333333; font-size: 15px; margin-top: 5px;">{haber['icerik']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"🔥 Beğen ({haber['begenen']})", key=f"beg_{index}"):
                haber['begenen'] += 1
                st.rerun()
                
        st.markdown("---")
        with st.expander("✍️ Panoya Bir Anı / Dedikodu Ekle"):
            yeni_b = st.text_input("Başlık:")
            yeni_i = st.text_input("Olay nedir?")
            if st.button("Paylaş"):
                if yeni_b and yeni_i:
                    st.session_state.haberler.insert(0, {"baslik": yeni_b, "icerik": yeni_i, "begenen": 1})
                    st.success("Panoda yayınlandı! 🎉")
                    st.rerun()

    with sekme2:
        st.subheader("Günün Soru Paketi")
        cevap = st.radio("1. Aşağıdakilerden hangisi bir yazılım dilidir?", ["Python", "HTML", "Tornavida", "Cetvel"])
        if st.button("Cevabı Gönder"):
            if cevap == "Python":
                st.balloons()
                ogrenci["puan"] += 25
                st.success("Tebrikler! +25 Puan kazandın! 🍋")
            else:
                st.error("Yanlış cevap, bir daha dene!")

    with sekme3:
        st.subheader("👑 Haftanın Efsane Mahlasları ve Rozetleri")
        st.markdown("Her pazartesi güncellenen resmi kampüs unvanları:")
        
        st.markdown("""
            <div class="badge-box">
                <h3 style="color: #D4A017; margin: 0;">⚡ Haftanın Nikola Tesla'sı (Fen)</h3>
                <p style="margin: 5px 0 0 0; font-size: 16px; font-weight: bold; color: #333;">Zeynep Yılmaz</p>
                <p style="font-size: 13px; color: #666; margin: 2px 0 0 0;">Laboratuvarda ampulü ilk o icat etti, kimse tutamıyor!</p>
            </div>
            
            <div class="badge-box">
                <h3 style="color: #D4A017; margin: 0;">📜 Haftanın Türk Dil Kurumu Başkanı (Türkçe)</h3>
                <p style="margin: 5px 0 0 0; font-size: 16px; font-weight: bold; color: #333;">Ali Rıza</p>
                <p style="font-size: 13px; color: #666; margin: 2px 0 0 0;">Devrik cümleleri tek bakışta yakalayıp imha ediyor!</p>
            </div>

            <div class="badge-box">
                <h3 style="color: #D4A017; margin: 0;">📐 Haftanın Cahit Arf'ı (Matematik)</h3>
                <p style="margin: 5px 0 0 0; font-size: 16px; font-weight: bold; color: #333;">Henüz Sahibi Çıkmadı! (Sen Kap)</p>
                <p style="font-size: 13px; color: #666; margin: 2px 0 0 0;">Matematik sorularını ağlatan ezici güç bekleniyor...</p>
            </div>
        """, unsafe_allow_html=True)
