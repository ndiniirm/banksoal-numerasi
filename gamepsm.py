#import tkinter as tk
#from tkinter import ttk, messagebox
#from PIL import Image, ImageTk, ImageSequence
import json, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ------------ Wallpaper (PNG/JPG/GIF) ------------
# pasang wallpaper
#def pasang_wallpaper(path):
#    global bg_frames, bg_index, bg_img_obj
#    if path.lower().endswith(".gif"):
#        gif = Image.open(path)
#        bg_frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif)]
#        bg_index = 0
#        def update_gif():
#            global bg_index
#            canvas_bg.create_image(0, 0, anchor="nw", image=bg_frames[bg_index])
#            bg_index = (bg_index + 1) % len(bg_frames)
#            root.after(100, update_gif)
#        update_gif()
#    else:
#        img = Image.open(path).resize((750, 500))
#        bg_img_obj = ImageTk.PhotoImage(img)
#        canvas_bg.create_image(0, 0, anchor="nw", image=bg_img_obj)

#pasang_wallpaper(r"C:\Users\Andin\Documents\PSM\project\wallpaper.gif")

# Data soal (pakai dictionary semua)
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
        "pertanyaan": "Dina adalah salah satu siswa SMP Negeri 25 Surabaya yang berasal dari Bandung. Dina biasanya pulang ke Bandung satu atau dua kali dalam sebulan. Dalam perjalanan pulang pergi dari Surabaya ke Bandung, Dina menggunakan transportasi kereta api dan angkot. Pada bulan ini, Dina telah melakukan dua kali perjalanan ke Bandung. Pada perjalanan pertama, ia membeli 2 tiket kereta api dan naik angkot sebanyak 4 kali. Pada perjalanan kedua, Dina hanya membeli 1 tiket kereta api (karena perjalanan balik ke Surabaya dibiayai oleh orang tuanya) dan menggunakan angkot sebanyak 5 kali. Harga masing-masing tiket kereta adalah 𝑅𝑝 95.000,00 dan untuk naik angkot 1 kali 𝑅𝑝 6.000,00. Dari kedua kondisi permasalahan didapat persamaan yaitu 3𝑥 + 9𝑦. Tentukan persamaan yang ekuivalen dengan persamaan diatas!",
        "opsi": ["(3x + 3y) + (x + 5y)", "2(x + 2y) + (x + 5y)", "2(2x + 4y) + 2(x + 5y)", "2(x + 2y) + (x + 5y)"],
        "jawaban": "2(x + 2y) + (x + 5y)",
        "gambar": None
    },
    {
        "pertanyaan": "Boni mempunyai adik yang tidak lama lagi berusia 5 tahun. Ibunya meminta ia membantu persiapan perayaan ulang tahun si adik dengan mendata perlengkapan yang akan dibagikan ke para tamu. Perayaan ulang tahun itu dihadiri oleh keluarga besar Boni sebanyak 15 orang dan sejumlah teman-teman adiknya. Jumlah orang dewasa di keluarga besar Boni ada 7 orang. Setiap anak yang hadir akan mendapatkan topi ulang tahun. Jika harga untuk 1 topi Rp2.500 dan ibu Boni telah menyiapkan uang sebesar Rp150.000 untuk pembelian topi, jumlah maksimal teman-teman adiknya Boni yang dapat pembagian topi adalah....",
        "opsi": ["60", "52", "45", "44"],
        "jawaban": "60",
        "gambar": None
    },
    {
        "pertanyaan": "Pak Angga berencana membangun sebuah rumah yang akan ditinggali oleh orang tuanya. Untuk itu, Pak Angga membutuhkan berbagai material bangunan. Ia mengunjungi dua toko material bangunan yaitu Toko Raffi Jaya Makmur dan Toko Jaya Abadi, untuk membandingkan harga material bangunan yang dibutuhkannya. Setiap toko memberikan paket material bangunan yang terdiri dari 2 barang namun dengan kuantitas yang berbeda. Berikut adalah harga paket yang tersedia di kedua toko tersebut:",
        "opsi": ["Harga 1 sak semen di toko Raffi Jaya Makmur lebih mahal dari toko Jaya Abadi", "Harga 1 kg pasir di toko Jaya Abadi lebih murah dari toko Raffi Jaya Makmur", "Selisih harga 1 sak semen antara toko Raffi Jaya Makmur dan toko Jaya Abadi adalah Rp. 7.000", "Harga 1 sak semen di toko Raffi Jaya Makmur sama dengan 20 kali harga 1 kg pasir di toko Jaya Abadi"],
        "jawaban": "Harga 1 kg pasir di toko Jaya Abadi lebih murah dari toko Raffi Jaya Makmur",
        "gambar": "images/Gambar5.png"
    },
    {
        "pertanyaan": "Dalam kompetisi Liga Inggris digunakan aturan peskoran sebagai menang mendapat 3 poin, kalah -1 poin, dan seri 0. Pada musim 2019/2020 klub Liverpool dinobatkan menjadi juara. Klub tersebut menjadi pemenang setelah 36 pertandingan dengan hanya bermain imbang dua kali. Jumlah skor 98 menjadi bukti kembalinya Liverpool sebagai kompetitor yang menakutkan bagi pesainganya. Dengan skor tersebut, berapa pertandingankah yang dimenangkan Liverpool?",
        "opsi": ["30 Pertandingan", "32 Pertandingan", "33 Pertandingan", "34 Pertandingan"],
        "jawaban": "33 Pertandingan",
        "gambar": None
    },
    {
        "pertanyaan": "Komposisi Biskuit A (berat 150 g)\n"
                    "• Lemak total 7% \n"
                    "• Lemak jenuh 18% \n"
                    "• Protein 5% \n"
                    "• Karbohidrat total 5% \n"
                    "• Natrium 7% \n"
                    "Dari informasi di atas, berikut adalah pernyataan yang benar ....",
        "opsi": ["Komposisi lemak total Biskuit A adalah 0,7 bagian", "Komposisi lemak jenuh Biskuit A adalah 0,18 bagian", "Komposisi protein Biskuit A adalah 5 bagian", "Komposisi natrium Biskuit A adalah 7 bagian"],
        "jawaban": "Komposisi lemak jenuh Biskuit A adalah 0,18 bagian",
        "gambar": None
    },
    {
        "pertanyaan": "Kota A memiliki populasi sebanyak 250.000 jiwa pada Desember 2020. Peningkatan jumlah penduduk adalah 3% setiap tahunnya. Walikota A akan membangun sebuah taman jika jumlah populasi minimal 350.000 jiwa. Pada tahun berapa taman tersebut akan dibangun oleh Walikota A?",
        "opsi": ["Desember 2023", "Desember 2040", "Desember 2044", "Desember 2025"],
        "jawaban": "Desember 2044",
        "gambar": None
    },
    {
        "pertanyaan": "Sebuah toko kue selama 8 hari dapat membuat 240 kotak kue. Banyak kue yang dapat dibuat oleh toko tersebut selama 12 hari adalah....",
        "opsi": ["160 kotak", "260 kotak", "360 kotak", "460 kotak"],
        "jawaban": "360 kotak",
        "gambar": None
    },
    {
        "pertanyaan": "Andi mengikuti kursus academic writing untuk melatih kemampuannya dalam menulis. Academic writing adalah kemampuan menulis karya ilmiah dalam Bahasa Inggris yang mengikuti kaidah Bahasa Inggris yang baik dan benar. Untuk belajar menulis dengan baik, guru meminta Andi untuk menulis sebuah teks yang terdiri dari 100 kata pada minggu pertama. Kemudian pada minggu-minggu berikutnya Andi harus menambahkan 20 kata untuk setiap minggu. Andi mendapat tugas untuk menulis sebuah teks yang terdiri dari 100 kata pada minggu pertama. Pada minggu-minggu berikutnya, Andi harus menambahkan 20 kata setiap minggu. Andi menuliskan teks dengan jumlah kata sesuai dengan permintaan. Pada minggu ke berapakah Andi menulis teks sebanyak 300 kata?",
        "opsi": ["9", "10", "11", "13"],
        "jawaban": "11",
        "gambar": None
    },
    {
        "pertanyaan": "esawat A terbang dengan suhu di luar sebesar 28 °C. Setiap pesawat naik 70 meter, suhu di luar pesawat akan turun sekitar 0,4 °C. Lantas, berapakah suhu di luar pesawat pada ketinggian 4.900 meter?",
        "opsi": ["56 °C", "10 °C", "-30 °C", "-49 °C"],
        "jawaban": "56 °C",
        "gambar": None
    },
    {
        "pertanyaan": "Air dalam bak mandi akan dikuras hingga habis. Sebelum dikuras, air yang ada di dalam bak mandi masih terisi sebanyak 1/4 bagian bak. Seluruh air dalam bak tersebut dikeluarkan melalui lubang pengeluaran selama 10 menit. Lantas, berapa debit air rata-rata yang keluar melalui lubang tersebut?",
        "opsi": ["20 liter/menit", "32 liter/menit", "36 liter/menit", "40 liter/menit"],
        "jawaban": "36 liter/menit",
        "gambar": None
    },
    {
        "pertanyaan": "Di suatu pulau, roti merupakan camilan yang banyak digemari. Setidaknya ada dua jenis roti yang sering dijual di pulau tersebut. Nah, daftar komposisi dari dua jenis roti kurang lebih sebagai berikut! Komposisi roti A terdiri dari lemak total yaitu 9%, Lemak jenuh yaitu 20%, Protein yaitu 3%, Karbohidrat total yaitu 6% dan Natrium yaitu 10%. Komposisi roti B terdiri dari dari lemak total sebesar 8%, Lemak jenuh sebesar 16%, Protein sebesar 2%, Karbohidrat total sebesar 4% dan Natrium sebesar 5%. Manakah dari empat pernyataan di atas yang paling tepat?",
        "opsi": ["Komposisi protein roti A adalah 0,02 bagian", "Komposisi natrium roti B adalah 0,01 bagian", "Komposisi lemak jenuh roti B adalah 0,16 bagian", "Lemak jenuh roti A sebesar 0,02 bagian"],
        "jawaban": "Komposisi lemak jenuh roti B adalah 0,16 bagian",
        "gambar": None
    },
    {
        "pertanyaan": "Empat pemain bola melakukan latihan tendangan penalti. Hasil latihan tersebut disajikan sebagai berikut:\n"
                    "• Andry: 12 tendangan & 10 tendangan sukses\n"
                    "• Bambang: 10 tendangan & 8 tendangan sukses\n"
                    "• Candra: 20 tendangan & 15 tendangan sukses\n"
                    "• Doni: 15 tendangan & 12 tendangan sukses\n"
                    "Pemain yang mempunyai peluang terbesar untuk sukses dalam melakukan tendangan penalti adalah...",
        "opsi": ["Doni", "Bambang", "Candra", "Andry"],
        "jawaban": "Andry",
        "gambar": None
    },
    {
        "pertanyaan": "Ibu Ani membeli buah di pasar. Harga 1 kg apel Rp25.000, harga 1 kg jeruk Rp20.000, dan harga 1 kg mangga Rp15.000. Ibu Ani membawa uang Rp100.000. Ia ingin membeli 2 kg apel, 1 kg jeruk, dan 2 kg mangga. Apakah uang Ibu Ani cukup? Jika tidak cukup, berapa kekurangan atau sisa uangnya?",
        "opsi": ["Uang cukup, sisa Rp. 5.000", "Uang cukup, sisa Rp. 10.000", "Uang tidak cukup, kurang Rp. 10.000", "Uang tidak cukup, kurang Rp. 5.000"],
        "jawaban": "Uang cukup, sisa Rp. 5.000",
        "gambar": None
    },
    {
        "pertanyaan": "Kafein merupakan salah satu zat yang berperan sebagai antioksidan yang dapat melindungi tubuh dari serangan penyakit. Selain itu, kafein mengandung asam klorogenat yang dapat menurunkan risiko penyakit jantung dan diabetes. Kafein juga dikenal dapat menekan nafsu makan serta menghilangkan rasa kantuk. Namun, yang perlu diperhatikan adalah konsumsi kafein tidak boleh berlebihan. Batas konsumsi kafein yang aman untuk sebagian besar orang dewasa adalah 400 mg per hari. Sedangkan untuk wanita hamil atau menyusui, batas konsumsi kafein yang disarankan adalah 200 mg per hari. Kafein dapat ditemukan dalam berbagai jenis makanan dan minuman, seperti kue brownies dan teh hijau. Dalam 3 cangkir teh hijau dan 6 potong kue brownies coklat susu terkandung 114 mg kafein. Sementara itu, dalam 2 cangkir teh hijau dan 10 potong kue brownies coklat susu terkandung 136 mg kafein. Jika hari ini Tina mengonsumsi 3 cangkir teh hijau dan 15 potong kue brownies dan kondisinya ia sedang hamil, apakah benar pernyataan yang menyatakan bahwa kafein yang dikonsumsi oleh Tina tidak melebihi batas konsumsi kafein per hari?",
        "opsi": ["Benar, karena Tina mengonsumsi kafein sebanyak 204 mg dan batas konsumsi yang ditetapkan adalah 400mg.", "Tidak benar, karena Tina mengonsumsi kafein sebanyak 204 mg dan batas konsumsi yang ditetapkan adalah 200mg.", "Benar, karena Tina mengonsumsi kafein sebanyak 214 mg dan batas konsumsi yang ditetapkan adalah 400mg.", "Tidak benar, karena Tina mengonsumsi kafein sebanyak 214 mg dan batas konsumsi yang ditetapkan adalah 200mg."],
        "jawaban": "Tidak benar, karena Tina mengonsumsi kafein sebanyak 204 mg dan batas konsumsi yang ditetapkan adalah 200mg.",
        "gambar": "images/Gambar1.jpg"
    },
    {
        "pertanyaan": "Raditya punya usaha kios penjualan ikan bandeng. Ikan bandeng disimpan dalam tiga lemari pendingin yang berbeda dan setiap lemari diberi label I, II dan III. Setiap lemari pendingin diatur dengan suhu berikut: Lemari I (-4 °C); Lemari II (-8 °C); dan Lemari III (0 °C). Selisih suhu antara ikan bandeng yang disimpan dalam lemari dengan suhu terendah dan tertinggi adalah...",
        "opsi": ["-8 °C", "4 °C", "8 °C", "12 °C"],
        "jawaban": "8 °C",
        "gambar": None
    },
    {
        "pertanyaan": "Alex mempunyai bak mandi berbentuk balok yang akan dialiri air melalui keran air. Ukuran bak itu adalah: tinggi (0,8 m); lebar (1,2 m); panjang (1,5 m). Setiap akhir pekan, air dalam bak mandi akan dikuras atau dikeluarkan hingga habis. Suatu hari, sebelum dikuras, bak mandi masih berisi air sebanyak 1/4 bagian bak. Seluruh air dalam bak itu dikeluarkan lewat lubang pengeluaran selama 10 menit. Debit air rata-rata yang keluar melalui lubang tersebut adalah...",
        "opsi": ["20 liter/menit", "36 liter/menit", "32 liter/menit", "24 liter/menit"],
        "jawaban": "36 liter/menit",
        "gambar": None
    },
    {
        "pertanyaan": "Seorang pedagang membeli satu lusin buku seharga Rp72.000,00. Jika ia menjual buku tersebut dengan harga Rp7.500,00 per buah, berapa persen keuntungan yang diperoleh pedagang tersebut?",
        "opsi": ["10%", "20%", "25%", "30%"],
        "jawaban": "25%",
        "gambar": None
    },
    {
        "pertanyaan": "Sebuah persegi panjang memiliki panjang (3x + 5) cm dan lebar (2x - 1) cm. Jika keliling persegi panjang tersebut 46 cm, maka nilai x adalah...",
        "opsi": ["3", "4", "5", "6"],
        "jawaban": "3",
        "gambar": None
    },
    {
        "pertanyaan": "Kenny sedang melihat artikel mengenai Sains dan menemukan gambar dibawah. Pada gambar, disajikan berbagai macam gelombang elektromagnetik yang disusun berdasarkan frekuensinya dalam satuan Hz. Warna yang memiliki frekuensi lebih tinggi daripada warna hijau, tetapi lebih rendah daripada warna ungu adalah...",
        "opsi": ["biru", "jingga", "merah", "kuning"],
        "jawaban": "biru",
        "gambar": "images/Gambar2.jpg"
    },
    {
        "pertanyaan": "Suatu hari, Mayer sedang berjalan-jalan mengelilingi beberapa titik. Rute perjalanan Mayer terlihat pada gambar di bawah. Terdapat 5 titik lokasi Mayer singgah, yaitu titik A, B, C, D, dan E.  Untuk mencapai titik-titik tertentu, Mayer menghabiskan energi setara dengan angka yang ditampilkan pada gambar. Sebagai ilustrasi: Mayer ingin mencapai titik B dari titik A. Rute ke B membutuhkan 1 energi. Dari titik B ke titik E membutuhkan 2 energi. Jadi, jika Mayer berjalan dari A ke B, lalu ke E, maka ia menghabiskan total 3 energi. Rute ini bisa ditulis sebagai A-B-E. Saat ini, Mayer berada di titik A dengan berbekal x energi. Jika kemudian Mayer menempuh rute A-B-C-A-D-E, dan yang tersisa adalah 7 energi, total energi Mayer awal mula-mula adalah ... energi",
        "opsi": ["30", "32", "16", "22"],
        "jawaban": "32",
        "gambar": "images/Gambar3.jpg"
    },
    {
        "pertanyaan": "Sampah anorganik lebih lama terurai dibandingkan dengan sampah organik. Waktu dekomposisi popok sekali pakai lebih lama dari plastik, namun kurang dari kulit sintetis. Berapa waktu dekomposisi yang mungkin dari popok sekali pakai?",
        "opsi": ["100 tahun", "250 tahun", "325 tahun", "475 tahun"],
        "jawaban": "475 tahun",
        "gambar": "images/Gambar4.jpg"
    },
    {
        "pertanyaan": "Pada saat terbang pada ketinggian tertentu, suhu di dalam pesawat adalah 21°C, sedangkan suhu di luar pesawat 34°C di bawah nol. Setiap naik 80 meter, suhu udara di luar pesawat akan turun 0,5°C. Jika ketinggian pesawat naik 2.400 meter, berapakah suhu udara di luar pesawat?",
        "opsi": ["17 °C", "29 °C", "30 °C", "49 °C"],
        "jawaban": "49 °C",
        "gambar": None
    },
    {
        "pertanyaan": "!",
        "opsi": ["", "", "", ""],
        "jawaban": "2",
        "gambar": "grafik.png"
    },
    {
        "pertanyaan": "!",
        "opsi": ["", "", "", ""],
        "jawaban": "2",
        "gambar": "grafik.png"
    }
]

LEADERBOARD_FILE = "leaderboard.json"

index_soal = 0
skor = 0
nama_pemain = ""
waktu_sisa = 1800
jawaban_user = {}  # simpan jawaban user per soal
gambar_label = None
gambar_cache = None

# ---------- Leaderboard Utility ----------
def simpan_leaderboard(nama, skor, jawaban_user):
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

def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r") as f:
        try:
            data = json.load(f)
            # konversi key jawaban_user jadi int lagi
            for entry in data:
                if "jawaban" in entry:
                    entry["jawaban"] = {int(k): v for k, v in entry["jawaban"].items()}
        except json.JSONDecodeError:
            data = []
    return sorted(data, key=lambda x: x["skor"], reverse=True)

def reset_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        os.remove(LEADERBOARD_FILE)
    refresh_leaderboard()
    messagebox.showinfo("Reset", "Leaderboard berhasil direset!")

# ---------- Kuis Logic ----------
def update_timer():
    global waktu_sisa
    if waktu_sisa > 0:
        menit, detik = divmod(waktu_sisa, 60)
        label_timer.config(text=f"⏰ {menit:02d}:{detik:02d}")
        waktu_sisa -= 1
        root.after(1000, update_timer)
    else:
        selesai_kuis()

def pilih_jawaban(jawaban):
    global skor
    benar = soal_numerasi[index_soal]["jawaban"]
    jawaban_user[index_soal] = jawaban
    
    # update skor (hitung ulang biar akurat)
    skor = sum(1 for i, j in jawaban_user.items() if soal_numerasi[i]["jawaban"] == j)

    # ubah warna tombol soal jadi hijau
    soal_buttons[index_soal].config(bg="lightgreen")

def tampilkan_soal(no):
    global index_soal, gambar_label, gambar_cache, opsi_buttons

    index_soal = no
    soal = soal_numerasi[no]

    # update teks soal (label_soal sudah didefinisikan pada setup GUI)
    label_soal.config(text=f"Soal {no+1}: {soal['pertanyaan']}")

    # set var_jawaban ke jawaban yang pernah disimpan (kalau ada)
    var_jawaban.set(jawaban_user.get(no, ""))

    # --- HAPUS opsi lama di frame_opsi (aman) ---
    for w in frame_opsi.winfo_children():
        w.destroy()
    opsi_buttons.clear()

    # --- HAPUS gambar lama kalau ada ---
    if gambar_label is not None:
        try:
            gambar_label.destroy()
        except Exception:
            pass
        gambar_label = None
        gambar_cache = None

    # --- TAMPILKAN gambar (jika ada) ---
    if soal.get("gambar"):
        try:
            img_path = os.path.join(BASE_DIR, soal["gambar"])
            img = Image.open(img_path)
            # optional: atur ukuran yg sesuai area tampilan
            img.thumbnail((400, 250), Image.LANCZOS)
            soal_img = ImageTk.PhotoImage(img)

            # buat label gambar **di scrollable_frame** (di atas frame_opsi)
            gambar_label = tk.Label(scrollable_frame, image=soal_img, bg=scrollable_frame.cget("bg"))
            gambar_label.image = soal_img    # simpan referensi supaya tidak ke-GC
            gambar_label.pack(pady=(0, 10), anchor="w")  # langsung di atas opsi
            gambar_cache = soal_img
        except Exception as e:
            print(f"Gagal load gambar {soal.get('gambar')}: {e}")
            gambar_label = None
            gambar_cache = None
    else:
        gambar_label = None
        gambar_cache = None

    for opsi in soal["opsi"]:
        rb = tk.Radiobutton(
            frame_opsi,
            text=opsi,
            variable=var_jawaban,
            value=opsi,
            font=("Segoe UI", 12),
            anchor="w",
            justify="left",
            wraplength=600,
            bg=frame_opsi.cget("bg"),
            command=lambda o=opsi: pilih_jawaban(o)   # <<--- ini yang bikin auto save
        )
        rb.pack(anchor="w", pady=4, fill="x")
        opsi_buttons.append(rb)

    # jika perlu, scroll ke atas setiap kali soal berubah
    canvas.yview_moveto(0.0)

def mulai_kuis():
    global nama_pemain
    nama_pemain = entry_nama.get().strip()
    if not nama_pemain:
        messagebox.showwarning("Peringatan", "Masukkan nama dulu!")
        return

    frame_awal.pack_forget()
    frame_kuis.pack(fill="both", expand=True)
    tampilkan_soal(0)
    update_timer()

def selesai_kuis():
    global skor, nama_pemain, jawaban_user

    skor = sum(1 for i, j in jawaban_user.items() if soal_numerasi[i]["jawaban"] == j)

    simpan_leaderboard(nama_pemain, skor, jawaban_user)
    frame_kuis.pack_forget()
    frame_hasil.pack(fill="both", expand=True)
    refresh_leaderboard()

# ---------- Leaderboard + Preview ----------
def refresh_leaderboard():
    for i in leaderboard_table.get_children():
        leaderboard_table.delete(i)
    data_sorted = load_leaderboard()
    for i, entry in enumerate(data_sorted, start=1):
        leaderboard_table.insert("", "end", values=(i, entry["nama"], entry["skor"]))

def on_select_leaderboard(event):
    selected = leaderboard_table.focus()
    if not selected:
        return
    values = leaderboard_table.item(selected, "values")
    nama = values[1]

    data_sorted = load_leaderboard()
    for entry in data_sorted:
        if entry["nama"] == nama:
            jawaban = entry.get("jawaban", {})
            tampilkan_preview(jawaban)
            break

def tampilkan_preview(jawaban_dict):
    for widget in frame_review.winfo_children():
        widget.destroy()
    tk.Label(frame_review, text="Preview Jawaban", font=("Comic Sans MS", 12, "bold")).pack(pady=5)

    for i, soal in enumerate(soal_numerasi):
        kunci = soal["jawaban"]
        jawaban = jawaban_dict.get(i, "")

        if jawaban == kunci:
            warna = "green"   # benar
        else:
            warna = "red"     # salah atau belum dijawab

        btn = tk.Button(
            frame_review, text=str(i+1), width=4,
            bg=warna, fg="white",
            command=lambda no=i, jw=jawaban: preview_detail(no, jw)
        )
        btn.pack(side="left", padx=3, pady=5)

def preview_detail(no, jawaban):
    top = tk.Toplevel(root)
    top.title(f"Detail Soal {no+1}")
    soal = soal_numerasi[no]
    pertanyaan = soal["pertanyaan"]
    kunci = soal["jawaban"]
    benar = "✅" if jawaban == kunci else "❌"

    tk.Label(top, text=f"Soal {no+1}:", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=10, pady=5)
    tk.Label(top, text=pertanyaan, wraplength=400, justify="left").pack(anchor="w", padx=10)
    tk.Label(top, text=f"Jawabanmu: {jawaban if jawaban else '(kosong)'} {benar}", fg="blue").pack(anchor="w", padx=10, pady=5)
    tk.Label(top, text=f"Jawaban benar: {kunci}", fg="green").pack(anchor="w", padx=10)

# ---------- Setup GUI ----------
root = tk.Tk()
root.title("Bank Soal Numerasi")
root.geometry("750x500")

# canvas background
canvas_bg = tk.Canvas(root)
canvas_bg.pack(fill="both", expand=True)

# frame utama langsung di atas wallpaper
frame_awal = tk.Frame(canvas_bg)  
frame_awal.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame_awal, text="📝 Bank Soal Numerasi 📝", font=("Cooper Black", 18, "bold")).pack(pady=20)
tk.Label(frame_awal, text="Masukkan Nama:", font=("Segoe UI", 14)).pack()
entry_nama = tk.Entry(frame_awal, font=("Segoe UI", 12))
entry_nama.pack(pady=10)
tk.Button(frame_awal, text="Mulai", font=("Comic Sans MS", 14, "bold"), command=mulai_kuis, bg="lightgreen").pack(pady=20)

# --- Frame Kuis ---
frame_kuis = tk.Frame(canvas_bg)  
frame_hasil = tk.Frame(canvas_bg)

# kiri → pakai canvas + scrollbar + grid 2 kolom
frame_kiri = tk.Frame(frame_kuis, bg="lightgray", width=180)
frame_kiri.pack(side="left", fill="y")

tk.Label(frame_kiri, text="Nomor Soal", font=("Cooper Black", 12, "bold"), bg="lightgray").pack(pady=10)

canvas_kiri = tk.Canvas(frame_kiri, bg="lightgray", width=160)
scrollbar_kiri = tk.Scrollbar(frame_kiri, orient="vertical", command=canvas_kiri.yview)
scrollable_kiri = tk.Frame(canvas_kiri, bg="lightgray")

scrollable_kiri.bind("<Configure>", lambda e: canvas_kiri.configure(scrollregion=canvas_kiri.bbox("all")))
canvas_kiri.create_window((0, 0), window=scrollable_kiri, anchor="nw")
canvas_kiri.configure(yscrollcommand=scrollbar_kiri.set)

canvas_kiri.pack(side="left", fill="y", expand=True)
scrollbar_kiri.pack(side="right", fill="y")

# tombol soal (grid 2 kolom)
soal_buttons = []  # simpan referensi

for i in range(len(soal_numerasi)):
    r, c = divmod(i, 2)
    btn = tk.Button(scrollable_kiri, text=str(i+1), width=5,
                    command=lambda no=i: tampilkan_soal(no))
    btn.grid(row=r, column=c, padx=5, pady=5)
    soal_buttons.append(btn)

# kanan dengan scroll
frame_kanan = tk.Frame(frame_kuis)
frame_kanan.pack(side="right", fill="both", expand=True)

canvas = tk.Canvas(frame_kanan)
scrollbar = tk.Scrollbar(frame_kanan, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", tags="frame")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

label_timer = tk.Label(scrollable_frame, text="⏰ 30:00", font=("Cooper Black", 12, "bold"), fg="red")
label_timer.pack(pady=5, anchor="w")

label_soal = tk.Label(scrollable_frame, text="", font=("Comic Sans MS", 14), wraplength=600, justify="left", anchor="w")
label_soal.pack(pady=20, anchor="w")

# frame khusus untuk opsi jawaban
frame_opsi = tk.Frame(scrollable_frame)
frame_opsi.pack(fill="x", padx=20, pady=10)

var_jawaban = tk.StringVar()
opsi_buttons = []

for opsi in ["A", "B", "C", "D"]:
    tk.Radiobutton(frame_opsi, text=opsi, variable=var_jawaban, value=opsi,
                   font=("Comic Sans MS", 12),
                   command=lambda o=opsi: pilih_jawaban(o)).pack(anchor="w")

frame_nav = tk.Frame(scrollable_frame)
frame_nav.pack(pady=10)

btn_prev = tk.Button(frame_nav, text="⬅ Sebelumnya", font=("Comic Sans MS", 12, "bold"),
                     command=lambda: tampilkan_soal(max(0, index_soal - 1)))
btn_prev.pack(side="left", padx=5)

btn_next = tk.Button(frame_nav, text="Selanjutnya ➡", font=("Comic Sans MS", 12, "bold"),
                     command=lambda: tampilkan_soal(min(len(soal_numerasi)-1, index_soal + 1)))
btn_next.pack(side="right", padx=5)

tk.Button(scrollable_frame, text="Selesai", font=("Comic Sans MS", 12, "bold"), command=selesai_kuis, bg="salmon").pack(pady=5)

label_skor = tk.Label(scrollable_frame, text="Skor: 0", font=("Segoe UI", 12, "italic"))
label_skor.pack(pady=10, anchor="w")

frame_bawah = tk.Frame(frame_kanan, bg="#f0f0f0")
frame_bawah.pack(fill="x")

btn_keluar_kuis = tk.Button(frame_bawah, text="KELUAR", width=15, font=("Comic Sans MS", 14, "bold"),
                            bg='#FF6B6B', fg='white',
                            command=lambda: [simpan_leaderboard(nama_pemain, skor, jawaban_user), root.destroy()],
                            cursor="hand2")
btn_keluar_kuis.pack(pady=5)

canvas.bind("<Configure>", lambda e: canvas.itemconfig("frame", width=e.width))

# --- Frame Hasil ---
#frame_hasil = tk.Frame(root)

tk.Label(frame_hasil, text="🏆 Leaderboard 🏆", font=("Comic Sans MS", 16, "bold")).pack(pady=10)

leaderboard_table = ttk.Treeview(frame_hasil, columns=("Rank", "Nama", "Skor"), show="headings", height=8)
leaderboard_table.heading("Rank", text="Rank")
leaderboard_table.heading("Nama", text="Nama")
leaderboard_table.heading("Skor", text="Skor")
leaderboard_table.column("Rank", width=50, anchor="center")
leaderboard_table.column("Nama", width=200, anchor="center")
leaderboard_table.column("Skor", width=80, anchor="center")
leaderboard_table.pack(pady=10)
leaderboard_table.bind("<<TreeviewSelect>>", on_select_leaderboard)

frame_review = tk.Frame(frame_hasil)
frame_review.pack(pady=10)

tk.Button(frame_hasil, text="🔄 Reset Leaderboard", font=("Comic Sans MS", 12, "bold"),
          bg="tomato", fg="white", command=reset_leaderboard).pack(pady=10)

btn_keluar_hasil = tk.Button(frame_hasil, text="KELUAR", width=15, font=("Comic Sans MS", 14, "bold"),
                             bg='#FF6B6B', fg='white',
                             command=lambda: [simpan_leaderboard(nama_pemain, skor, jawaban_user), root.destroy()],
                             cursor="hand2")
btn_keluar_hasil.pack(side=tk.BOTTOM, pady=30)

root.mainloop()
