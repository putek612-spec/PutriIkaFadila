import streamlit as st
import pandas as pd
import numpy as np

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="SPK KNN Risiko Diabetes",
    page_icon="🩺",
    layout="wide"
)

# ==========================================
# JUDUL
# ==========================================

st.title("🩺 Sistem Pendukung Keputusan")
st.subheader("Prediksi Risiko Diabetes Menggunakan Metode KNN")

st.write(
    "Sistem ini menggunakan metode K-Nearest Neighbor "
    "untuk menentukan risiko diabetes pasien."
)

# ==========================================
# DATASET
# ==========================================

data = {
    "Pasien": [
        "P01", "P02", "P03", "P04", "P05",
        "P06", "P07", "P08", "P09", "P10"
    ],

    "Usia": [
        25, 30, 35, 40, 45,
        50, 55, 28, 38, 48
    ],

    "BMI": [
        21.5, 23.1, 25.0, 27.5, 30.2,
        31.5, 33.0, 22.5, 26.8, 29.5
    ],

    "Glukosa": [
        90, 95, 105, 120, 140,
        155, 165, 92, 115, 145
    ],

    "Tekanan Darah": [
        110, 115, 120, 125, 135,
        140, 145, 112, 122, 130
    ],

    "Riwayat Keluarga": [
        0, 0, 0, 1, 1,
        1, 1, 0, 0, 1
    ],

    "Kelas": [
        "Rendah", "Rendah", "Rendah",
        "Tinggi", "Tinggi", "Tinggi",
        "Tinggi", "Rendah", "Rendah",
        "Tinggi"
    ]
}

df = pd.DataFrame(data)

# ==========================================
# DATASET
# ==========================================

st.markdown("### 📊 Dataset Pasien")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================
# INPUT PASIEN BARU
# ==========================================

st.markdown("### 👤 Input Data Pasien Baru")

col1, col2 = st.columns(2)

with col1:

    usia = st.number_input(
        "Usia",
        min_value=1,
        max_value=100,
        value=42
    )

    bmi = st.number_input(
        "BMI",
        min_value=1.0,
        max_value=60.0,
        value=28.5,
        step=0.1
    )

    glukosa = st.number_input(
        "Glukosa",
        min_value=1,
        max_value=300,
        value=130
    )

with col2:

    tekanan = st.number_input(
        "Tekanan Darah",
        min_value=50,
        max_value=250,
        value=128
    )

    riwayat = st.selectbox(
        "Riwayat Diabetes Keluarga",
        [0, 1],
        format_func=lambda x:
        "0 - Tidak Ada" if x == 0 else "1 - Ada"
    )

    k = st.selectbox(
        "Nilai K",
        [3, 5, 7],
        index=0
    )

# ==========================================
# PROSES KNN
# ==========================================

if st.button(
    "🔍 PROSES PREDIKSI",
    use_container_width=True
):

    # --------------------------------------
    # Fitur yang digunakan
    # --------------------------------------

    fitur = [
        "Usia",
        "BMI",
        "Glukosa",
        "Tekanan Darah",
        "Riwayat Keluarga"
    ]

    # Data pasien baru
    pasien_baru = np.array([
        usia,
        bmi,
        glukosa,
        tekanan,
        riwayat
    ])

    # --------------------------------------
    # NORMALISASI MIN-MAX
    # --------------------------------------

    nilai_min = df[fitur].min().values
    nilai_max = df[fitur].max().values

    data_normalisasi = (
        df[fitur].values - nilai_min
    ) / (
        nilai_max - nilai_min
    )

    pasien_normalisasi = (
        pasien_baru - nilai_min
    ) / (
        nilai_max - nilai_min
    )

    # --------------------------------------
    # HITUNG EUCLIDEAN DISTANCE
    # --------------------------------------

    jarak = np.sqrt(
        np.sum(
            (data_normalisasi - pasien_normalisasi) ** 2,
            axis=1
        )
    )

    hasil = df.copy()

    hasil["Jarak"] = jarak

    # --------------------------------------
    # URUTKAN JARAK
    # --------------------------------------

    hasil = hasil.sort_values(
        by="Jarak"
    ).reset_index(drop=True)

    hasil["Peringkat"] = (
        hasil.index + 1
    )

    # --------------------------------------
    # AMBIL K TETANGGA TERDEKAT
    # --------------------------------------

    tetangga = hasil.head(k)

    # --------------------------------------
    # VOTING
    # --------------------------------------

    jumlah_rendah = (
        tetangga["Kelas"] == "Rendah"
    ).sum()

    jumlah_tinggi = (
        tetangga["Kelas"] == "Tinggi"
    ).sum()

    if jumlah_tinggi > jumlah_rendah:
        hasil_prediksi = "Tinggi"
    else:
        hasil_prediksi = "Rendah"

    # ======================================
    # HASIL PASIEN
    # ======================================

    st.divider()

    st.markdown("### 👤 Data Pasien Baru")

    hasil_input = pd.DataFrame({
        "Atribut": [
            "Usia",
            "BMI",
            "Glukosa",
            "Tekanan Darah",
            "Riwayat Keluarga"
        ],

        "Nilai": [
            usia,
            bmi,
            glukosa,
            tekanan,
            "Ada" if riwayat == 1 else "Tidak Ada"
        ]
    })

    st.dataframe(
        hasil_input,
        use_container_width=True,
        hide_index=True
    )

    # ======================================
    # RANKING
    # ======================================

    st.markdown(
        f"### 📏 Ranking Jarak "
        f"(K = {k})"
    )

    tabel_jarak = hasil[
        [
            "Peringkat",
            "Pasien",
            "Jarak",
            "Kelas"
        ]
    ].copy()

    tabel_jarak["Jarak"] = (
        tabel_jarak["Jarak"]
        .round(4)
    )

    st.dataframe(
        tabel_jarak,
        use_container_width=True,
        hide_index=True
    )

    # ======================================
    # TETANGGA TERDEKAT
    # ======================================

    st.markdown(
        f"### 🏆 {k} Tetangga Terdekat"
    )

    tabel_tetangga = tetangga[
        [
            "Pasien",
            "Jarak",
            "Kelas"
        ]
    ].copy()

    tabel_tetangga["Jarak"] = (
        tabel_tetangga["Jarak"]
        .round(4)
    )

    st.dataframe(
        tabel_tetangga,
        use_container_width=True,
        hide_index=True
    )

    # ======================================
    # VOTING
    # ======================================

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Risiko Rendah",
            jumlah_rendah
        )

    with col2:

        st.metric(
            "Risiko Tinggi",
            jumlah_tinggi
        )

    # ======================================
    # HASIL AKHIR
    # ======================================

    st.markdown("### 🎯 HASIL PREDIKSI")

    if hasil_prediksi == "Tinggi":

        st.error(
            "🔴 RISIKO TINGGI"
        )

        st.write(
            "Berdasarkan hasil klasifikasi "
            "KNN, pasien termasuk kategori "
            "*Risiko Tinggi*."
        )

    else:

        st.success(
            "🟢 RISIKO RENDAH"
        )

        st.write(
            "Berdasarkan hasil klasifikasi "
            "KNN, pasien termasuk kategori "
            "*Risiko Rendah*."
        )