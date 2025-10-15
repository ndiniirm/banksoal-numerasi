import streamlit as st
import json, os
from gamepsm import soal_numerasi

LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r") as f:
        return json.load(f)

def save_leaderboard(data):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------- Streamlit Setup ----------
st.set_page_config(page_title="Bank Soal Numerasi", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "awal"
if "nama" not in st.session_state:
    st.session_state.nama = ""
if "jawaban_user" not in st.session_state:
    st.session_state.jawaban_user = {}
if "index" not in st.session_state:
    st.session_state.index = 0

# ---------- Halaman Awal ----------
if st.session_state.page == "awal":
    st.title("📝 Bank Soal Numerasi SMP")
    st.session_state.nama = st.text_input("Masukkan nama kamu:")

    if st.button("Mulai Kuis"):
        if not st.session_state.nama.strip():
            st.warning("Masukkan nama dulu ya!")
        else:
            st.session_state.page = "kuis"
            st.rerun()

# ---------- Halaman Kuis ----------
elif st.session_state.page == "kuis":
    col_kiri, col_kanan = st.columns([1, 3])

    # --- Sidebar kiri: Nomor Soal ---
    with col_kiri:
        st.subheader("Nomor Soal")
        for i in range(len(soal_numerasi)):
            # Warna tombol sesuai status
            if i in st.session_state.jawaban_user:
                color = "#90EE90"  # hijau
            else:
                color = "#D3D3D3"  # abu

            # Tombol interaktif tanpa reload
            if st.button(f"{i+1}", key=f"btn{i}"):
                st.session_state.index = i
                st.rerun()

            # Styling tombol nomor
            st.markdown(
                f"""
                <style>
                div[data-testid="stButton"][key="btn{i}"] button {{
                    background-color: {color};
                    color: black;
                    border-radius: 6px;
                    border: none;
                    width: 60px;
                    height: 40px;
                    margin: 3px 3px;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )

    # --- Kanan: Tampilan Soal ---
    with col_kanan:
        no = st.session_state.index
        soal = soal_numerasi[no]

        st.header(f"Soal {no + 1}")

        # --- tampilkan gambar di atas teks soal ---
        path_gambar = soal.get("gambar")
        if path_gambar:
            img_path = os.path.join(os.path.dirname(__file__), path_gambar)
            if os.path.exists(img_path):
                st.image(img_path, use_column_width=True)
            else:
                st.warning(f"Gambar tidak ditemukan: {path_gambar}")

        # --- teks soal ---
        st.write(soal["pertanyaan"])

        # --- opsi jawaban ---
        jawaban = st.radio(
            "Pilih jawaban:",
            soal["opsi"],
            index=soal["opsi"].index(st.session_state.jawaban_user.get(no, soal["opsi"][0]))
            if no in st.session_state.jawaban_user else 0,
        )
        st.session_state.jawaban_user[no] = jawaban

        # --- navigasi bawah ---
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("⬅ Sebelumnya") and no > 0:
                st.session_state.index -= 1
                st.rerun()
        with col2:
            if st.button("Selesai"):
                benar = sum(
                    1 for i, j in st.session_state.jawaban_user.items()
                    if soal_numerasi[i]["jawaban"] == j
                )
                leaderboard = load_leaderboard()
                leaderboard.append({"nama": st.session_state.nama, "skor": benar})
                save_leaderboard(leaderboard)
                st.session_state.skor = benar
                st.session_state.page = "hasil"
                st.rerun()
        with col3:
            if st.button("Selanjutnya ➡") and no < len(soal_numerasi) - 1:
                st.session_state.index += 1
                st.rerun()

# ---------- Halaman Hasil ----------
elif st.session_state.page == "hasil":
    st.success(f"🎉 Selamat, {st.session_state.nama}! Skor kamu: {st.session_state.skor}")
    st.subheader("🏆 Leaderboard")

    leaderboard = load_leaderboard()
    data_sorted = sorted(leaderboard, key=lambda x: x["skor"], reverse=True)
    st.dataframe(data_sorted)

    if st.button("🔁 Ulangi"):
        st.session_state.page = "awal"
        st.session_state.index = 0
        st.session_state.jawaban_user = {}
        st.rerun()