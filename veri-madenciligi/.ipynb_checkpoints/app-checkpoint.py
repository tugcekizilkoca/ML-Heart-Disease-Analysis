import streamlit as st
import pandas as pd
import numpy as np
import joblib

# MODEL VE SCALER YÜKLE
final_model = joblib.load("final_model.pkl")
standScaler = joblib.load("standScaler.pkl")
feature_names = final_model.feature_names_in_

st.set_page_config(page_title="Kalp Hastalığı Tahmin Sistemi", page_icon="❤️")

st.title("🫀 Kalp Hastalığı Tahmin ve Klinik Rapor Sistemi")
st.write("Lütfen aşağıdaki bilgileri doldurun:")

# ---------------------------------------
# KULLANICI GİRDİLERİ
# ---------------------------------------
age = st.number_input("Yaş", min_value=1, max_value=120, value=40)
trestbps = st.number_input("İstirahat Kan Basıncı (trestbps)", min_value=80, max_value=200, value=130)
chol = st.number_input("Kolesterol (chol)", min_value=100, max_value=600, value=250)
thalach = st.number_input("Maks Nabız (thalach)", min_value=60, max_value=220, value=150)
oldpeak = st.number_input("ST Depresyonu (oldpeak)", min_value=0.0, max_value=6.0, step=0.1, value=1.0)

sex = st.selectbox("Cinsiyet", ["Kadın (0)", "Erkek (1)"])
sex = 0 if sex.startswith("Kadın") else 1

cp = st.selectbox("Göğüs Ağrısı Tipi (cp)", ["0: Tipik", "1: Atipik", "2: Non-anginal", "3: Asemptomatik"])
cp = int(cp[0])

fbs = st.selectbox("Açlık Kan Şekeri (fbs)", ["0: Normal", "1: Yüksek"])
fbs = int(fbs[0])

restecg = st.selectbox("İstirahat EKG (restecg)", ["0: Normal", "1: ST-T anormallik", "2: LVH"])
restecg = int(restecg[0])

exang = st.selectbox("Egzersizle Ağrı (exang)", ["0: Hayır", "1: Evet"])
exang = int(exang[0])

slope = st.selectbox("Eğim (slope)", ["0: Up", "1: Flat", "2: Down"])
slope = int(slope[0])

ca = st.selectbox("Damar Sayısı (ca)", ["0", "1", "2", "3", "4"])
ca = int(ca)

thal = st.selectbox("Thal (0–3)", ["0", "1", "2", "3"])
thal = int(thal)

# ---------------------------------------
# VERİ HAZIRLAMA
# ---------------------------------------
def prepare_input():
    yeni_veri = pd.DataFrame([[0]*len(feature_names)], columns=feature_names)

    numeric = pd.DataFrame([[age, trestbps, chol, thalach, oldpeak]],
                           columns=["age", "trestbps", "chol", "thalach", "oldpeak"])
    numeric_scaled = standScaler.transform(numeric)

    yeni_veri.loc[0, ["age","trestbps","chol","thalach","oldpeak"]] = numeric_scaled[0]

    for i in range(2):
        yeni_veri[f"sex_{i}"] = 1 if sex == i else 0
    for i in range(4):
        yeni_veri[f"cp_{i}"] = 1 if cp == i else 0
    for i in range(2):
        yeni_veri[f"fbs_{i}"] = 1 if fbs == i else 0
    for i in range(3):
        yeni_veri[f"restecg_{i}"] = 1 if restecg == i else 0
    for i in range(2):
        yeni_veri[f"exang_{i}"] = 1 if exang == i else 0
    for i in range(3):
        yeni_veri[f"slope_{i}"] = 1 if slope == i else 0
    for i in range(5):
        yeni_veri[f"ca_{i}"] = 1 if ca == i else 0
    for i in range(4):
        yeni_veri[f"thal_{i}"] = 1 if thal == i else 0

    return yeni_veri

# ---------------------------------------
# KLİNİK RAPOR FONKSİYONU
# ---------------------------------------
def klinik_rapor_uret(veri, model):
    tahmin = model.predict(veri)[0]
    olasilik = model.predict_proba(veri)[0][1]
    yuzde = round(olasilik * 100, 2)

    if yuzde < 30:
        risk = "Düşük Risk"
    elif yuzde < 60:
        risk = "Orta Risk"
    else:
        risk = "Yüksek Risk"

    st.markdown("### 🩺 Klinik Değerlendirme Raporu")
    st.write(f"**Risk Olasılığı:** %{yuzde}")
    st.write(f"**Risk Seviyesi:** {risk}")

    st.markdown("---")

    st.markdown("### 🔍 Bulguların Tıbbi Yorumu")

    # oldpeak
    if veri["oldpeak"].iloc[0] > 1.5:
        st.write("- ST depresyonu yüksek → iskemi riski artmış olabilir.")
    else:
        st.write("- ST depresyonu normal aralıkta.")

    # cp
    cp_cols = [col for col in veri.columns if col.startswith("cp_")]
    cp_value = cp_cols[veri[cp_cols].iloc[0].argmax()]
    cp_map = {
        "cp_0": "Tipik anjina",
        "cp_1": "Atipik anjina",
        "cp_2": "Non-anginal ağrı",
        "cp_3": "Asemptomatik"
    }
    st.write(f"- Göğüs Ağrısı Tipi: **{cp_map[cp_value]}**")

    # thal
    thal_cols = [col for col in veri.columns if col.startswith("thal_")]
    thal_value = thal_cols[veri[thal_cols].iloc[0].argmax()]
    thal_map = {
        "thal_0": "Normal",
        "thal_1": "Sabit kusur",
        "thal_2": "Tersinir kusur",
        "thal_3": "Reversible defect (yüksek risk)"
    }
    st.write(f"- Thal Bulgusu: **{thal_map[thal_value]}**")

    st.markdown("---")

    st.markdown("### 📝 Öneriler")
    if risk == "Düşük Risk":
        st.write("- Bulgular düşük risk profiliyle uyumludur.")
        st.write("- Sağlıklı yaşam tarzı önerilir.")
    elif risk == "Orta Risk":
        st.write("- Düzenli kontrol ve yaşam tarzı değişikliği önerilir.")
        st.write("- Gerekirse efor testi yapılabilir.")
    else:
        st.write("- Yüksek risk! Kardiyoloji uzmanı değerlendirmesi gerekir.")
        st.write("- Ekokardiyografi, efor testi ve kan değerleri kontrol edilmelidir.")

    st.markdown("---")

# ---------------------------------------
# TAHMİN BUTONU
# ---------------------------------------
if st.button("Tahmin ve Klinik Rapor Üret"):
    veri = prepare_input()
    klinik_rapor_uret(veri, final_model)
