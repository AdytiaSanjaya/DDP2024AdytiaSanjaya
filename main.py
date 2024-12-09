import streamlit as st
import datetime
import time
import winsound

# Judul aplikasi
st.title("Alarm Waktu")

# Warna tema
st.markdown("""
<style>
body {
    background-color: #222;
    color: #fff;
}
</style>
""", unsafe_allow_html=True)

# Input waktu alarm
waktu_alarm = st.text_input("Masukkan waktu alarm yang kamu inginkan", value="00:00:00", placeholder="Contoh: 07:00:00")

# Tombol untuk mengaktifkan alarm
aktifkan_alarm = st.button("Aktifkan Alarm")

# Fungsi untuk memeriksa waktu
def periksa_waktu(waktu_alarm):
    waktu_sekarang = datetime.datetime.now().strftime("%H:%M:%S")
    if waktu_sekarang == waktu_alarm:
        return True
    else:
        return False

# Fungsi untuk memainkan suara alarm
def mainkan_alarm():
    for i in range(10):
        winsound.Beep(2500, 1000)  # Suara beep

# Loop untuk memeriksa waktu
if aktifkan_alarm:
    while True:
        if periksa_waktu(waktu_alarm):
            mainkan_alarm()
            st.success("Waktu alarm selesai!")
            break
        time.sleep(1)
        

# Tampilan tambahan
col1, col2 = st.columns(2)
col1.metric("Waktu Sekarang", datetime.datetime.now().strftime("%H:%M:%S"))
col2.metric("Waktu Alarm", waktu_alarm)

st.image("download.png", width=100)
