# 🤖 Gemini AI Chatbot

Bu proje, **Google Gemini 2.5 Flash** modelini kullanarak geliştirilmiş, **Streamlit** altyapısı üzerinde çalışan modern, hızlı ve akıllı bir yapay zeka asistanıdır.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Gemini API](https://img.shields.io/badge/Gemini%20API-8E75B2?style=for-the-badge&logo=google&logoColor=white)

## 🚀 Özellikler

* **🧠 Akıllı Hafıza:** Sohbet geçmişini (Session State) tutar, bağlamdan kopmaz.
* **⚡ Streaming Yanıt:** Cevapları bekletmeden, daktilo efektiyle anlık yazar.
* **🎨 Modern Arayüz:** Kullanıcı dostu, karanlık mod destekli şık tasarım.
* **🔌 Güçlü Altyapı:** Google'ın en yeni `gemini-2.5-flash` modelini kullanır.

## 🛠️ Kurulum

Projeyi kendi bilgisayarınızda çalıştırmak için:

1.  **Repoyu indirin:**
    ```bash
    git clone [https://github.com/muhammetkaradeniz20/gemini-ai-chatbot.git](https://github.com/KULLANICI_ADIN/gemini-ai-chatbot.git)
    cd gemini-ai-chatbot
    ```

2.  **Gereksinimleri yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **API Anahtarını Ayarlayın:**
    * Proje ana dizininde `.streamlit` klasörü oluşturun.
    * İçine `secrets.toml` dosyası açın ve anahtarınızı ekleyin:
    ```toml
    GOOGLE_API_KEY = "BURAYA_GOOGLE_API_ANAHTARINIZ_GELECEK"
    ```

4.  **Çalıştırın:**
    ```bash
    streamlit run chatbot.py
    ```

## 📷 Proje Hakkında
Bu proje açık kaynaklıdır ve eğitim amaçlı geliştirilmiştir.

---
*Developed by Muhammet Karadeniz*
