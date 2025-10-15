import json, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ------------ DATA SOAL NUMERASI ------------
soal_numerasi = [
    {
        "pertanyaan": "Perusahaan PT. Candy Land memproduksi dua jenis produk, yaitu produk candy fruit mulberry dan candy fruit raspberry. "
                      "Untuk memproduksi setiap produk candy fruit mulberry dibutuhkan 3 kg gula dan 2 kg berry. "
                      "Sedangkan untuk memproduksi setiap produk candy fruit raspberry dibutuhkan 1 kg gula dan 4 kg berry. "
                      "Harga yang ditetapkan untuk produk candy fruit mulberry adalah Rp. 100.000,00 dan harga yang ditetapkan untuk produk candy fruit raspberry adalah Rp. 80.000,00. "
                      "Manakah model matematikanya yang sesuai dengan kondisi diatas?",
        "opsi": ["3x + 2y = Rp. 100.000\nx + 4y = Rp. 80.000",
                 "4x + 3y = Rp. 20.000\n2x + y = Rp. 180.000",
                 "x + 2y = Rp. 60.000\n2x + 4y = Rp. 80.000",
                 "3x + 2y = Rp. 100.000\nx + 3y = Rp. 80.000"],
        "jawaban": "3x + 2y = Rp. 100.000\nx + 4y = Rp. 80.000",
        "gambar": None
    },
    {
        "pertanyaan": "Dina adalah salah satu siswa SMP Negeri 25 Surabaya yang berasal dari Bandung. Dina biasanya pulang ke Bandung satu atau dua kali dalam sebulan. Dalam perjalanan pulang pergi dari Surabaya ke Bandung, Dina menggunakan transportasi kereta api dan angkot. Pada bulan ini, Dina telah melakukan dua kali perjalanan ke Bandung. Pada perjalanan pertama, ia membeli 2 tiket kereta api dan naik angkot sebanyak 4 kali. Pada perjalanan kedua, Dina hanya membeli 1 tiket kereta api (karena perjalanan balik ke Surabaya dibiayai oleh orang tuanya) dan menggunakan angkot sebanyak 5 kali. Harga masing-masing tiket kereta adalah Rp 95.000,00 dan untuk naik angkot 1 kali Rp 6.000,00. Dari kedua kondisi permasalahan didapat persamaan yaitu 3x + 9y. Tentukan persamaan yang ekuivalen dengan persamaan diatas!",
        "opsi": ["(3x + 3y) + (x + 5y)", "2(x + 2y) + (x + 5y)", "2(2x + 4y) + 2(x + 5y)", "2(x + 2y) + (x + 5y)"],
        "jawaban": "2(x + 2y) + (x + 5y)",
        "gambar": None
    },
    {
        "pertanyaan": "Boni mempunyai adik yang akan berusia 5 tahun. Ibunya meminta ia membantu menyiapkan perlengkapan ulang tahun. Jumlah tamu keluarga besar 15 orang dengan 7 orang dewasa. Setiap anak yang hadir mendapat topi ulang tahun. Jika harga 1 topi Rp2.500 dan uang yang disiapkan Rp150.000, jumlah maksimal teman adik Boni yang bisa dapat topi adalah...",
        "opsi": ["60", "52", "45", "44"],
        "jawaban": "60",
        "gambar": None
    },
    {
        "pertanyaan": "Pak Angga berencana membangun rumah. Ia mengunjungi dua toko material, Raffi Jaya Makmur dan Jaya Abadi, untuk membandingkan harga paket material bangunan. Berikut adalah harga paket yang tersedia di kedua toko tersebut:",
        "opsi": ["Harga 1 sak semen di toko Raffi Jaya Makmur lebih mahal dari toko Jaya Abadi",
                 "Harga 1 kg pasir di toko Jaya Abadi lebih murah dari toko Raffi Jaya Makmur",
                 "Selisih harga 1 sak semen antara toko Raffi Jaya Makmur dan toko Jaya Abadi adalah Rp. 7.000",
                 "Harga 1 sak semen di toko Raffi Jaya Makmur sama dengan 20 kali harga 1 kg pasir di toko Jaya Abadi"],
        "jawaban": "Harga 1 kg pasir di toko Jaya Abadi lebih murah dari toko Raffi Jaya Makmur",
        "gambar": "images/Gambar5.png"
    },
    # --- tambahkan soal lainmu seperti sebelumnya ---
]

# ------------ FILE LEADERBOARD ------------
LEADERBOARD_FILE = "leaderboard.json"


# ---------- SIMPAN LEADERBOARD ----------
def simpan_leaderboard(nama, skor, jawaban_user):
    """Simpan hasil kuis ke file leaderboard.json"""
    data = []
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    data.append({"nama": nama, "skor": skor, "jawaban": jawaban_user})
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------- LOAD LEADERBOARD ----------
def load_leaderboard():
    """Membaca data leaderboard dan mengurutkannya dari skor tertinggi"""
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r") as f:
        try:
            data = json.load(f)
            for entry in data:
                if "jawaban" in entry:
                    entry["jawaban"] = {int(k): v for k, v in entry["jawaban"].items()}
        except json.JSONDecodeError:
            data = []
    return sorted(data, key=lambda x: x["skor"], reverse=True)
