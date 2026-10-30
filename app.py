import streamlit as st
import random

# Sayfa Yapılandırması
st.set_page_config(page_title="EduLingo - 5. Sınıf Sosyal Kampüs", page_icon="🍋", layout="centered")

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
        font-size: 34px;
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
    .chat-bubble {
        background-color: #FFFFFF;
        padding: 10px 15px;
        border-radius: 10px;
        margin-bottom: 8px;
        border: 1px solid #FFE066;
    }
    </style>
""", unsafe_allow_html=True)

# Oturum Veritabanı ve 5. Sınıf Öğrencileri
if "giris_yapildi" not in st.session_state:
    st.session_state.giris_yapildi = False
if "ogrenci_bilgi" not in st.session_state:
    st.session_state.ogrenci_bilgi = {}
if "ogrenciler_veritabani" not in st.session_state:
    st.session_state.ogrenciler_veritabani = {
        "11111111111": {"no": "501", "ad": "Zeynep Yılmaz", "puan": 240, "streak": 5},
        "22222222222": {"no": "502", "ad": "Ali Rıza Demir", "puan": 210, "streak": 3},
        "33333333333": {"no": "503", "ad": "Rana Aksoy", "puan": 290, "streak": 7},
        "44444444444": {"no": "504", "ad": "Kerem Çelik", "puan": 180, "streak": 2}
    }
if "haberler" not in st.session_state:
    st.session_state.haberler = [
        {"baslik": "🚨 Çikolata Krizi!", "icerik": "5-A sınıfında Ali Rıza dün fen hocasına çikolata ikram etti, hoca mutluluktan havalara uçtu! 🍫😂", "begenen": 42},
        {"baslik": "🏆 Zirve Yarışı Kızıştı", "icerik": "Rana, son 5. sınıf matematik testinde tam puan alarak liderliği ele geçirdi. 🔥", "begenen": 19}
    ]
if "chat_odasi" not in st.session_state:
    st.session_state.chat_odasi = [
        {"isim": "Ali Rıza Demir", "mesaj": "Arkadaşlar sosyal bilgilerdeki ilk Türk devletleri sorusunu bilen var mı? 🏛️"},
        {"isim": "Rana Aksoy", "mesaj": "Asya Hun Devleti'ni unuttun mu Ali Rıza? Ben çözdüm bile! 😎"}
    ]

# --- 1. GİRİŞ EKRANI ---
if not st.session_state.giris_yapildi:
    st.markdown('<p class="main-title">🍋 EduLingo 5. Sınıf Sosyal Kampüs</p>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style="background-color: #FFFFFF; padding: 20px; border-radius: 15px; text-align: center; border: 2px dashed #FFD700; margin-bottom: 20px;">
            <p style="font-size: 18px; color: #333; font-style: italic; font-weight: bold;">
                "5. Sınıfın en kral kampüsüne hoş geldin! Soruları çöz, sohbet et, haftanın Sosyal Kelebeği ol! 🚀"
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🔐 Güvenli Öğrenci Girişi")
    
    with st.form("giris_formu"):
        tc_input = st.text_input("T.C. Kimlik Numarası (11 Haneli):", max_chars=11)
        no_input = st.text_input("5. Sınıf Öğrenci Numarası:")
        ad_input = st.text_input("Adın ve Soyadın (Örn: Defne Kaya):")
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
                if len(tc_input) == 11 and no_input and ad_input:
                    yeni_ogrenci = {"no": no_input, "ad": ad_input, "puan": 20, "streak": 1}
                    st.session_state.ogrenciler_veritabani[tc_input] = yeni_ogrenci
                    st.session_state.giris_yapildi = True
                    st.session_state.ogrenci_bilgi = yeni_ogrenci
                    st.rerun()
                else:
                    st.error("⚠️ Lütfen tüm alanları eksiksiz ve doğru doldur.")

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
        mesaj = f"Harika gidiyorsun {ogrenci['ad']}! 🔥 5. sınıf serin {ogrenci['streak']} gün oldu. Canlı sohbette arkadaşların seni bekliyor, testleri çözüp rozetleri kapma vakti!"
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

    sekme1, sekme2, sekme3, sekme4, sekme5 = st.tabs([
        "📰 Kampüs Panosu", 
        "💬 Canlı Sohbet", 
        "🏆 Liderlik Tablosu", 
        "📝 5. Sınıf Testleri", 
        "👑 Mahlaslar & Rozetler"
    ])
    
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
        st.subheader("💬 5. Sınıf Kampüs Canlı Sohbet Odası")
        st.markdown("Sınıf arkadaşlarınla anlaş, soruları tartış, kampüsün tadını çıkar!")
        
        for chat in st.session_state.chat_odasi:
            st.markdown(f"""
            <div class="chat-bubble">
                <b>{chat['isim']}:</b> {chat['mesaj']}
            </div>
            """, unsafe_allow_html=True)
            
        with st.form("chat_formu", clear_on_submit=True):
            yeni_mesaj = st.text_input("Mesajını yaz...")
            gonder = st.form_submit_button("Gönder 🚀")
            if gonder and yeni_mesaj:
                st.session_state.chat_odasi.append({"isim": ogrenci["ad"], "mesaj": yeni_mesaj})
                st.rerun()

    with sekme3:
        st.subheader("🏆 5. Sınıf Liderlik Tablosu")
        st.markdown("En çok XP toplayan kampüsinciler:")
        
        sirali_ogrenciler = sorted(st.session_state.ogrenciler_veritabani.values(), key=lambda x: x["puan"], reverse=True)
        
        for sira, o in enumerate(sirali_ogrenciler, 1):
            ikon = "🥇" if sira == 1 else "🥈" if sira == 2 else "🥉" if sira == 3 else f"{sira}."
            st.markdown(f"""
            <div style="background-color: white; padding: 10px 15px; border-radius: 8px; margin-bottom: 8px; border-left: 4px solid #D4A017; display: flex; justify-content: space-between;">
                <span><b>{ikon} {o['ad']}</b> (No: {o['no']})</span>
                <span style="color: #D4A017; font-weight: bold;">{o['puan']} XP</span>
            </div>
            """, unsafe_allow_html=True)

    with sekme4:
        st.subheader("📝 5. Sınıf Seviye Testleri")
        ders = st.selectbox("Hangi dersten soru çözmek istersin?", ["Matematik", "Fen Bilimleri", "Türkçe", "Sosyal Bilgiler"])
        
        if ders == "Matematik":
            st.markdown("#### Soru 1/2: Kesirler")
            q1 = st.radio("Yarım ile çeyreğin toplamı hangi kesiri ifade eder?", ["3/4", "1/2", "1/8", "2/3"], key="m1")
            q2 = st.radio("Bir çiftlikte 48 koyunun 1/4'ü satıldı. Geriye kaç koyun kaldı?", ["12", "36", "24", "40"], key="m2")
            if st.button("Matematik Testini Gönder"):
                dogru_sayisi = 0
                if q1 == "3/4": dogru_sayisi += 1
                if q2 == "36": dogru_sayisi += 1
                
                if dogru_sayisi == 2:
                    st.balloons()
                    ogrenci["puan"] += 50
                    st.success("Mükemmel! 2/2 yaptın, +50 Puan kazandın! 📐")
                else:
                    st.warning(f"Doğru sayısı: {dogru_sayisi}/2. Eksiklerini kapatıp tekrar dene!")
                    
        elif ders == "Fen Bilimleri":
            st.markdown("#### Soru 1/2: Güneş, Dünya ve Ay")
            q1 = st.radio("Güneş'in kendi ekseni etrafındaki dönme hareketi sonucu ne olur?", ["Güneş kendi etrafında dönerken ısı yayar", "Güneş lekeleri yer değiştirir", "Gece ve gündüz oluşur", "Mevsimler oluşur"], key="f1")
            q2 = st.radio("Ay'ın ana evreleri arasındaki süre yaklaşık kaç gündür?", ["1 hafta", "1 ay", "2 hafta", "29-30 gün (yaklaşık 1 hafta ara ile 4 ana evre)"], key="f2")
            if st.button("Fen Testini Gönder"):
                dogru_sayisi = 0
                if q1 == "Güneş lekeleri yer değiştirir": dogru_sayisi += 1
                if q2 == "29-30 gün (yaklaşık 1 hafta ara ile 4 ana evre)": dogru_sayisi += 1
                
                if dogru_sayisi >= 1:
                    st.balloons()
                    ogrenci["puan"] += 40
                    st.success("Tebrikler Tesla adayı! +40 Puan kaptın! ⚡")
                else:
                    st.error("Bir dahaki sefere başaracaksın!")

        elif ders == "Türkçe":
            st.markdown("#### Soru 1/2: Sözcükte Anlam ve Noktalama")
            q1 = st.radio("'Tatlı' sözcüğü hangi cümlede mecaz anlamda kullanılmıştır?", ["Annemin yaptığı tatlı kurabiyeleri çok sevdim.", "Bize çok tatlı ve güler yüzlü bir öğretmen geldi.", "Çorbaya biraz daha tatlı biber salçası ekledik.", "Yediğimiz karpuz inanılmaz tatlıydı."], key="t1")
            q2 = st.radio("Aşağıdaki cümlelerin hangisinde yazım yanlışı vardır?", ["Ankara'ya yarın gideceğiz.", "Yarınki sınavda başarılar dilerim.", "Kitap'ı masanın üstüne bıraktı.", "Kedimiz pamuk da bizimle yaşıyor."], key="t2")
            if st.button("Türkçe Testini Gönder"):
                dogru_sayisi = 0
                if q1 == "Bize çok tatlı ve güler yüzlü bir öğretmen geldi.": dogru_sayisi += 1
                if q2 == "Kitap'ı masanın üstüne bıraktı.": dogru_sayisi += 1
                
                if dogru_sayisi == 2:
                    st.balloons()
                    ogrenci["puan"] += 50
                    st.success("TDK Başkanlığına göz kırpıyorsun! +50 Puan! 📜")
                else:
                    st.warning("Tekrar deneyerek puanını katlayabilirsin!")

        else:
            st.markdown("#### Soru 1/2: Ülkemizin Doğal Güzellikleri ve Tarihi")
            q1 = st.radio("Aşağıdakilerden hangisi UNESCO Dünya Miras Listesi'nde yer alan illerimizden biridir?", ["Nevşehir (Kapadokya)", "Ankara", "Eskişehir", "Yozgat"], key="s1")
            q2 = st.radio("İlk Türk devletlerinde göçebe yaşam tarzının temel geçim kaynağı hangisiydi?", ["Tarım", "Hayvancılık", "Denizcilik", "Dokumacılık"], key="s2")
            if st.button("Sosyal Bilgiler Testini Gönder"):
                dogru_sayisi = 0
                if q1 == "Nevşehir (Kapadokya)": dogru_sayisi += 1
                if q2 == "Hayvancılık": dogru_sayisi += 1
                
                if dogru_sayisi == 2:
                    st.balloons()
                    ogrenci["puan"] += 50
                    st.success("Süpersin! +50 Puan kazandın! 🌍")
                else:
                    st.warning("Biraz daha sosyal bilgiler tekrarı harika olur!")

    with sekme5:
        st.subheader("👑 Haftanın Efsane Mahlasları ve Rozetleri")
        st.markdown("Okul hocası tarafından her pazartesi bizzat atanan resmi kampüs unvanları:")
        
        st.markdown("""
            <div class="badge-box">
                <h3 style="color: #D4A017; margin: 0;">⚡ Haftanın Nikola Tesla'sı (Fen)</h3>
                <p style="margin: 5px 0 0 0; font-size: 16px; font-weight: bold; color: #333;">Zeynep Yılmaz</p>
                <p style="font-size: 13px; color: #666; margin: 2px 0 0 0;">Fen laboratuvarının altını üstüne getiren dahi!</p>
            </div>
            
            <div class="badge-box">
                <h3 style="color: #D4A017; margin: 0;">📜 Haftanın TDK Başkanı (Türkçe)</h3>
                <p style="margin: 5px 0 0 0; font-size: 16px; font-weight: bold; color: #333;">Ali Rıza Demir</p>
                <p style="font-size: 13px; color: #666; margin: 2px 0 0 0;">Dil kurallarına uymayan cümleleri affetmiyor!</p>
            </div>

            <div class="badge-box">
                <h3 style="color: #D4A017; margin: 0;">📐 Haftanın Cahit Arf'ı (Matematik)</h3>
                <p style="margin: 5px 0 0 0; font-size: 16px; font-weight: bold; color: #333;">Rana Aksoy</p>
                <p style="font-size: 13px; color: #666; margin: 2px 0 0 0;">Matematik problemlerini tek hamlede çözen lider!</p>
            </div>

            <div class="badge-box" style="border: 2px solid #FF69B4; background: linear-gradient(135deg, #FFF0F5, #FFE4E1);">
                <h3 style="color: #FF1493; margin: 0;">🦋 Haftanın Sosyal Kelebeği (Hoca Seçimi)</h3>
                <p style="margin: 5px 0 0 0; font-size: 16px; font-weight: bold; color: #333;">Kerem Çelik</p>
                <p style="font-size: 13px; color: #666; margin: 2px 0 0 0;">Okulun en neşeli, sohbete en çok katkı sağlayan ve hocanın gözdesi olan ismi!</p>
            </div>
        """, unsafe_allow_html=True)
