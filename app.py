import pandas as pd
import streamlit as st

# Konfigurasi Judul Halaman Web
st.set_page_config(
    page_title="Form Survei Kepuasan", page_icon="📝", layout="centered"
)

st.title("📝 Formulir Survei Kepuasan Pengguna")
st.write(
    "Silakan isi survei di bawah ini untuk membantu kami meningkatkan"
    " layanan."
)

# Membuat Form Survei
with st.form("form_survei"):
  # 1. Input teks biasa (Nama)
  nama = st.text_input("Nama Lengkap:")

  # 2. Input pilihan (Radio Button)
  usia = st.radio(
      "Kelompok Usia:",
      ["Di bawah 20 tahun", "20 - 30 tahun", "31 - 40 tahun", "Di atas 40 tahun"],
  )

  # 3. Input angka / skala (Slider)
  kepuasan = st.slider(
      "Seberapa puas Anda dengan layanan kami? (1 = Sangat Buruk, 5 ="
      " Sangat Baik)",
      min_value=1,
      max_value=5,
      value=3,
  )

  # 4. Pilihan ganda (Checkbox / Selectbox untuk fitur yang disukai)
  fitur_favorit = st.selectbox(
      "Fitur mana yang paling Anda sukai?",
      ["Kecepatan", "Tampilan Antarmuka", "Kemudahan Penggunaan", "Lainnya"],
  )

  # 5. Input teks panjang (Kritik & Saran)
  saran = st.text_area("Kritik dan Saran:")

  # Tombol Kirim Survei
  submitted = st.form_submit_button("Kirim Jawaban")

  # Aksi ketika tombol dikirim
  if submitted:
    if nama.strip() == "":
      st.warning("Mohon masukkan nama Anda terlebih dahulu!")
    else:
      # Menyimpan data ke dalam file CSV secara otomatis
      data_baru = pd.DataFrame(
          [[nama, usia, kepuasan, fitur_favorit, saran]],
          columns=[
              "Nama",
              "Usia",
              "Kepuasan",
              "Fitur Favorit",
              "Kritik & Saran",
          ],
      )

      # Cek apakah file CSV sudah ada, jika belum buat baru, jika sudah tambahkan datanya
      try:
        df_lama = pd.read_csv("hasil_survei.csv")
        df_final = pd.concat([df_lama, data_baru], ignore_index=True)
      except FileNotFoundError:
        df_final = data_baru

      df_final.to_csv("hasil_survei.csv", index=False)

      # Pesan sukses ke pengguna
      st.success(
          f"Terima kasih banyak, {nama}! Jawaban survei Anda berhasil disimpan."
      )