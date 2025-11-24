import streamlit as st
import google.generativeai as genai

# --- 1. AYARLAR VE KONFIGÜRASYON ---
st.set_page_config(
    page_title="Kralın Botu", 
    page_icon="🤖", 
    layout="centered"
)

# --- 2. API ANAHTARI YÖNETİMİ ---
# NOT: GitHub'a yüklemeden önce bu satırı silip, alttaki st.secrets satırını açmalısın!
GOOGLE_API_KEY = "AIzaSyCbpcKgxsu7gm4uo_u7U2scbV2haySHyoI"

# GitHub için güvenli yöntem (secrets.toml dosyası oluşturursan bunu aç):
# if "GOOGLE_API_KEY" in st.secrets:
#     GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

# API'yi yapılandır
try:
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    st.error("API Anahtarı hatası! Lütfen geçerli bir anahtar girdiğinden emin ol.")
    st.stop()

# --- 3. MODEL SEÇİMİ ---
# Senin hesabında aktif olan güçlü ve hızlı model
target_model = 'gemini-2.5-flash'

try:
    model = genai.GenerativeModel(target_model)
except:
    # Eğer 2.5 anlık sorun çıkarırsa en son kararlı sürüme geç
    model = genai.GenerativeModel('gemini-flash-latest')

# --- 4. ARAYÜZ BAŞLIĞI ---
st.title("💬 Yapay Zeka Asistanı")
st.caption(f"🚀 Güç Ünitesi: {target_model} | Python & Streamlit")

# --- 5. SOHBET GEÇMİŞİ (MEMORY) ---
# Mesajlar listesini başlat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Google Chat oturumunu başlat (Geçmişi hatırlar)
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# --- 6. GEÇMİŞ MESAJLARI EKRANA YAZDIR ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 7. KULLANICI GİRDİSİ VE BOT CEVABI ---
if prompt := st.chat_input("Mesajını yaz kral..."):
    
    # 7.1 Kullanıcı mesajını ekrana bas ve listeye ekle
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 7.2 Botun cevabını oluştur
    with st.chat_message("assistant"):
        message_placeholder = st.empty() # Cevap akarken burası güncellenecek
        full_response = ""
        
        try:
            # Modeli çağır ve cevabı 'stream' (akış) olarak al
            response = st.session_state.chat_session.send_message(prompt, stream=True)
            
            # Gelen parçaları (chunk) tek tek yazdır (Daktilo efekti)
            for chunk in response:
                if chunk.text:
                    full_response += chunk.text
                    message_placeholder.markdown(full_response + "▌")
            
            # İmleci kaldır ve tam metni yaz
            message_placeholder.markdown(full_response)
            
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")
            full_response = "Üzgünüm, şu an bağlantıda bir sorun var."

    # 7.3 Bot cevabını hafızaya kaydet
    st.session_state.messages.append({"role": "assistant", "content": full_response})