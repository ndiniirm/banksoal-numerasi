import streamlit as st
import json, os
from gamepsm import soal_numerasi_7, soal_numerasi_8

# --- Path absolut supaya JSON selalu tersimpan di folder ini ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LEADERBOARD_FILE = os.path.join(BASE_DIR, "leaderboard.json")

def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    try:
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_leaderboard(data):
    try:
        with open(LEADERBOARD_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        st.error(f"Gagal menyimpan leaderboard: {e}")

# ---------- Streamlit Setup ----------
st.set_page_config(page_title="Bank Soal Numerasi", layout="wide")

# ---------- Inisialisasi Session ----------
if "page" not in st.session_state:
    st.session_state.page = "opening"
if "nama" not in st.session_state:
    st.session_state.nama = ""
if "jenjang" not in st.session_state:
    st.session_state.jenjang = ""
if "jawaban_user" not in st.session_state:
    st.session_state.jawaban_user = {}
if "index" not in st.session_state:
    st.session_state.index = 0

# ---------- Pilih soal ----------
def get_soal():
    if st.session_state.jenjang == "Kelas 7":
        return soal_numerasi_7
    elif st.session_state.jenjang == "Kelas 8":
        return soal_numerasi_8
    else:
        return []

# ---------- Halaman Opening ----------
if st.session_state.page == "opening":
    st.title("🎓 Selamat Datang di Bank Soal Numerasi SMP")
    st.markdown("""
        Halo! 👋  
        Platform ini dirancang untuk membantu kamu berlatih **soal numerasi interaktif** sesuai jenjang kelasmu.  
        Yuk uji kemampuan berhitungmu dan lihat peringkatmu di leaderboard! 🏆
    """)
    
    if st.button("Mulai ▶️", key="mulai_opening"):
        st.session_state.page = "awal"
        st.rerun()

# ---------- Halaman Input Nama ----------
elif st.session_state.page == "awal":
    st.title("📝 Persiapan Kuis Numerasi")

    st.session_state.nama = st.text_input("Masukkan nama kamu:")
    st.session_state.jenjang = st.selectbox(
        "Pilih jenjang kelas:",
        ["", "Kelas 7", "Kelas 8"]
    )

    if st.button("Mulai Kuis", key="mulai_kuis"):
        if not st.session_state.nama.strip():
            st.warning("Masukkan nama dulu ya!")
        elif not st.session_state.jenjang:
            st.warning("Pilih jenjang kelas dulu ya!")
        else:
            st.session_state.page = "kuis"
            st.session_state.index = 0
            st.session_state.jawaban_user = {}
            st.rerun()

# ---------- Halaman Kuis ----------
elif st.session_state.page == "kuis":
    soal_numerasi = get_soal()

    col_kiri, col_kanan = st.columns([1, 3])

    with col_kiri:
        st.subheader("Nomor Soal")
        for i in range(len(soal_numerasi)):
            color = "#90EE90" if i in st.session_state.jawaban_user else "#D3D3D3"

            if st.button(f"{i+1}", key=f"nomor_{i}"):
                st.session_state.index = i
                st.rerun()

            st.markdown(
                f"""
                <style>
                div[data-testid="stButton"][key="nomor_{i}"] button {{
                    background-color: {color};
                    color: black;
                    border-radius: 6px;
                    width: 60px;
                    height: 40px;
                    margin: 3px 3px;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )

    with col_kanan:
        no = st.session_state.index
        soal = soal_numerasi[no]

        st.header(f"Soal {no+1}")

        # gambar
        path_gambar = soal.get("gambar")
        if path_gambar:
            img_path = os.path.join(os.path.dirname(__file__), path_gambar)
            if os.path.exists(img_path):
                st.image(img_path, use_column_width=True)

        # teks soal
        st.write(soal["pertanyaan"])

        # opsii
        jawaban_sebelumnya = st.session_state.jawaban_user.get(no, None)

        jawaban = st.radio(
            "Pilih jawaban:",
            soal["opsi"],
            index=soal["opsi"].index(jawaban_sebelumnya) if jawaban_sebelumnya in soal["opsi"] else None,
            key=f"radio_{no}",
        )

        if jawaban:
            st.session_state.jawaban_user[no] = jawaban

        # tombol navigasi
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("⬅ Sebelumnya", key=f"prev_{no}") and no > 0:
                st.session_state.index -= 1
                st.rerun()

        with col2:
            if st.button("Selesai", key=f"selesai_{no}"):
                benar = sum(
                    1 for i, j in st.session_state.jawaban_user.items()
                    if soal_numerasi[i]["jawaban"] == j
                )

                leaderboard = load_leaderboard()
                leaderboard.append({
                    "nama": st.session_state.nama,
                    "jenjang": st.session_state.jenjang,
                    "skor": benar,
                    "jawaban": [st.session_state.jawaban_user.get(i, None) for i in range(len(soal_numerasi))]
                })
                save_leaderboard(leaderboard)

                st.session_state.skor = benar
                st.session_state.page = "hasil"
                st.rerun()

        with col3:
            if st.button("Selanjutnya ➡", key=f"next_{no}") and no < len(soal_numerasi) - 1:
                st.session_state.index += 1
                st.rerun()

# ---------- Halaman Hasil ----------
elif st.session_state.page == "hasil":
    st.success(f"🎉 Selamat, {st.session_state.nama}!")
    st.write(f"**Jenjang:** {st.session_state.jenjang}")
    st.write(f"**Skor kamu:** {st.session_state.skor}")

    st.subheader("🏆 Leaderboard")

    leaderboard = load_leaderboard()
    data_sorted = sorted(leaderboard, key=lambda x: x["skor"], reverse=True)

    for idx, entry in enumerate(data_sorted):
        nama = entry.get("nama", "Tanpa Nama")
        skor = entry.get("skor", 0)
        jenjang = entry.get("jenjang", "Kelas 7")
        jawaban_user = entry.get("jawaban", [])

        soal_numerasi = soal_numerasi_7 if jenjang == "Kelas 7" else soal_numerasi_8

        with st.expander(f"{nama} — Skor: {skor} ({jenjang})", expanded=False):
            st.write("**Rincian Jawaban:**")
            for i, soal in enumerate(soal_numerasi):
                kunci = soal["jawaban"]
                jawab = jawaban_user[i] if i < len(jawaban_user) else None

                warna = "green" if jawab == kunci else "red"

                st.markdown(
                    f"**Soal {i+1}:** <span style='color:{warna}'>{jawab}</span> "
                    f"(Kunci: {kunci})",
                    unsafe_allow_html=True
                )

    if st.button("🔁 Ulangi", key="ulang_hasil"):
        st.session_state.page = "opening"
        st.session_state.index = 0
        st.session_state.jawaban_user = {}
        st.rerun()
