import json, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ------------ DATA SOAL NUMERASI ------------
soal7_paket1 = [
    {
        "pertanyaan": "Rina membantu ibunya berjualan kue. Setiap kantong berisi 2 buah risol dan 3 buah pastel. Harga satu risol adalah r rupiah, dan harga satu pastel adalah p rupiah. Bentuk aljabar yang menyatakan total harga isi satu kantong adalah...",
        "opsi": ["2r + 3p",
                 "3r + 2p",
                 "5(r + p)",
                 "r + p"],
        "jawaban": "2r + 3p",
        "gambar": None
    },
    {
        "pertanyaan": "Puncak Bogor terkenal karena udaranya yang sejuk dan dingin, terutama di malam hari, karena lokasinya yang berada di dataran tinggi dan dikelilingi perbukitan hijau seperti kebun teh. Pada saat malam hari, suhu di puncak Bogor 12°. Saat siang hari, suhu naik menjadi di puncak Bogor 18°. Berapakah kenaikan suhu udara di Puncak Bogor dari malam hari ke siang hari pada hari tersebut?",
        "opsi": ["-6°", 
                 "6°", 
                 "30°", 
                 "-30°"],
        "jawaban": "6°",
        "gambar": None
    },
    {
        "pertanyaan": "Ibu Sari memiliki dua buah foto persegi panjang yang berbeda ukuran. Foto pertama berukuran 10 cm × 15 cm, sedangkan foto kedua berukuran 20 cm × 30 cm. Ia ingin mengetahui apakah kedua foto tersebut sebangun. Menurut konsep kesebangunan, dua bangun datar dikatakan sebangun jika memenuhi syarat...",        
        "opsi": ["Bentuknya sama dan warnanya sama", 
                 "Ukurannya sama persis", 
                 "Hanya sisi-sisinya yang sebanding",
                 "Sudut-sudut yang bersesuaian sama besar dan sisi-sisi yang bersesuaian sebanding"],
        "jawaban": "Sudut-sudut yang bersesuaian sama besar dan sisi-sisi yang bersesuaian sebanding",
        "gambar": None
    },
    {
        "pertanyaan": "Rani sangat senang berkreasi. Untuk tugas seni di sekolahnya, ia berencana membuat hiasan dinding yang cerah dari kertas warna. Ia pergi ke toko alat tulis untuk membeli persediaan kertas. Rani memilih 3 lembar kertas warna merah. Harga untuk satu lembar kertas merah adalah (2x + 3) rupiah. Selain itu, Rani juga membeli 2 lembar kertas warna biru. Harga untuk satu lembar kertas biru adalah (x + 5) rupiah. Tulislah sebuah bentuk aljabar yang menyatakan total uang yang harus dibayarkan Rani untuk semua kertas yang dibelinya!",
        "opsi": ["5x + 16", 
                 "8x + 19", 
                 "8x + 21", 
                 "4x + 11"],
        "jawaban": "8x + 19",
        "gambar": None
    },
    {
        "pertanyaan": "Sebuah lift di sebuah gedung pertemuan mulai bergerak dari lantai dasar (yang ditandai sebagai lantai 0). Mula-mula, lift itu turun sebanyak 3 lantai menuju ruang parkir bawah tanah. Kemudian, dari posisi itu, lift naik sebanyak 5 lantai. Tak lama kemudian, lift kembali turun sebanyak 4 lantai. Di lantai berapakah lift itu berhenti setelah serangkaian pergerakan tersebut?",
        "opsi": ["Lantai 1", 
                 "Lantai -1", 
                 "Lantai -2", 
                 "Lantai 2"],
        "jawaban": "Lantai -2",
        "gambar": None
    },
    {
        "pertanyaan": "Di kelas, Bu Ani memberikan sebuah soal perkalian desimal, yaitu 0,4 × 0,25. Dina, salah seorang siswa, dengan cepat mengangkat tangan dan berkata, 'Bu, saya sudah menghitungnya. Caranya mudah, tinggal kalikan saja 4 × 25, hasilnya 100. Karena ada dua angka di belakang koma di soal tadi, kita taruh dua angka di belakang koma, jadi hasilnya 0,1.' Menurutmu, bagaimana penjelasan yang tepat mengenai klaim Dina tersebut?",
        "opsi": ["Benar, karena hasil akhir perkaliannya memang 0,1.", 
                 "Salah, karena jumlah total angka di belakang koma pada bilangan yang dikalikan tidak dihitung dengan benar.", 
                 "Salah, karena seharusnya hasil perkaliannya adalah 0,01.", 
                 "Salah, karena perkalian bilangan desimal tidak bisa dilakukan langsung seperti perkalian bilangan bulat."],
        "jawaban": "Salah, karena jumlah total angka di belakang koma pada bilangan yang dikalikan tidak dihitung dengan benar.",
        "gambar": None
    },
    {
        "pertanyaan": "Pada liburan sekolah, Andi dan keluarganya menginap di sebuah penginapan di daerah pegunungan. Saat baru bangun tidur di pagi hari, Andi melihat termometer di luar jendela menunjukkan suhu udara sangat dingin, yaitu –3°C. Sepanjang pagi hingga siang, matahari bersinar cerah sehingga suhu udara perlahan-lahan menjadi lebih hangat. Setiap dua jam, suhu naik sebesar 2°C. Namun, ketika sore hari mulai tiba, cuaca mendung dan angin bertiup kencang. Akibatnya, suhu udara turun drastis sebesar 4°C dari suhu terakhir yang tercatat di siang hari. Jika Andi berharap suhu udara tepat 0°C pada saat sore hari sebelum terjadi penurunan suhu, berapa lamakah (dalam jam) waktu yang dibutuhkan sejak pagi hari hingga sebelum suhu turun di sore hari?",
        "opsi": ["2 jam", 
                 "3 jam", 
                 "4 jam", 
                 "6 jam"],
        "jawaban": "3 jam",
        "gambar": None
    },
    {
        "pertanyaan": "Sebuah taman berbentuk persegi panjang. Panjangnya 5 meter lebihnya dari lebarnya. Jika lebar taman dinyatakan sebagai l meter, maka bentuk aljabar untuk keliling taman tersebut adalah...",
        "opsi": ["2l + 5", 
                 "4l + 10", 
                 "l(l + 5)", 
                 "l + (l + 5)"],
        "jawaban": "4l + 10",
        "gambar": None
    },
    {
        "pertanyaan": "Perhatikan gambar diagram batang di bawah ini, diagram menunjukkan 10 provinsi dengan jumlah usaha kuliner terbanyak di Indonesia pada tahun 2020! Berdasarkan data pada diagram tersebut, manakah pernyataan berikut yang benar?",
        "opsi": ["Jumlah usaha kuliner di Jawa Barat lebih dari dua kali lipat jumlah usaha kuliner di Jawa Timur.", 
                 "Selisih jumlah usaha kuliner antara peringkat pertama dan peringkat kedua adalah 3.745 usaha.", 
                 "Rata-rata jumlah usaha kuliner untuk lima provinsi teratas adalah sekitar 1.680 usaha.", 
                 "Jumlah usaha kuliner di Sulawesi Selatan dan DI Yogyakarta jika digabungkan lebih banyak daripada di Jawa Tengah."],
        "jawaban": "Selisih jumlah usaha kuliner antara peringkat pertama dan peringkat kedua adalah 3.745 usaha.",
        "gambar": None #"no 3 halaman 2"
    },
    {
        "pertanyaan": "Ibu Rani membeli gula pasir sebanyak 2,5 kg untuk persiapan acara keluarga di rumah. Pada hari itu, ia ingin membuat beberapa hidangan. Pertama, ia menggunakan gula sebanyak 0,75 kg untuk membuat loyang kue bolu. Kemudian, ia juga membuat sirup jahe segar untuk minuman yang menghabiskan gula sebanyak 0,8 kg. Setelah kedua keperluan itu terpenuhi, berapa kilogramkah sisa gula pasir yang masih dimiliki Ibu Rani?",
        "opsi": ["0,85 kg", 
                 "0,9 kg", 
                 "0,95 kg", 
                 "1 kg"],
        "jawaban": "0,95 kg",
        "gambar": None
    },
    {
        "pertanyaan": "Rani dan ibunya membuat campuran jus jeruk dan jus apel dengan perbandingan 3 : 2. Campuran itu menghasilkan 20 liter jus buah. Karena jus terasa terlalu asam, ibunya menambahkan 8 liter jus apel lagi agar rasanya lebih manis. Setelah penambahan itu, bagaimana perbandingan baru antara jus jeruk dan jus apel?",
        "opsi": ["3 : 4", 
                 "4 : 3", 
                 "2 : 3", 
                 "5 : 4"],
        "jawaban": "3 : 4",
        "gambar": None
    },
    {
        "pertanyaan": "Dalam rangka mengajarkan literasi keuangan, Bu Sari meminta empat siswanya, yaitu Rina, Bima, Lala, dan Danu, untuk mencatat perubahan saldo uang saku mereka selama satu minggu. Catatan tersebut menggunakan tanda positif (+) untuk menandakan penambahan saldo (seperti mendapat uang tambahan atau menyisihkan uang) dan tanda negatif (–) untuk menandakan pengurangan saldo (seperti pengeluaran atau keperluan mendadak). Hasil catatan mereka akan di lampirkan pada tabel di bawah, dan berdasarkan data di bawah, manakah pernyataan berikut yang paling tepat?",
        "opsi": ["Rina mengalami pengurangan uang saku yang paling besar.", 
                 "Danu mengalami penambahan saldo terkecil.", 
                 "Bima mengalami pengurangan saldo yang lebih kecil daripada Danu.", 
                 "Selisih uang saku akhir Rina dan Lala adalah Rp. 7.000,00."],
        "jawaban": "Bima mengalami pengurangan saldo yang lebih kecil daripada Danu.",
        "gambar": None #no 1 hal 4
    },
    {
        "pertanyaan": "Suatu hari, saat pelajaran IPS, Bu Sinta memberikan tugas kepada murid-muridnya untuk menghitung jarak sebenarnya antara dua kota di peta. Pada peta tersebut, skala yang digunakan adalah 1 : 250.000, artinya 1 cm di peta mewakili 250.000 cm jarak sebenarnya di dunia nyata. Hakim mengukur jarak antara Kota A dan Kota B pada peta dan mendapatkan hasil 6 cm. Ia kemudian menghitung jarak sebenarnya dan menuliskannya di buku tugasnya sebagai berikut: \n “Jarak sebenarnya antara Kota A dan Kota B adalah 12 km.” \n Ketika mengumpulkan tugas, guru meminta kamu untuk menilai apakah perhitungan Hakim sudah benar atau belum. Bagaimana penilaianmu terhadap hasil perhitungan Hakim?",
        "opsi": ["Benar, karena 6 × 250.000 = 1.500.000 cm = 15 km", 
                 "Salah, karena seharusnya 6 × 250.000 = 1.500.000 cm = 15 km", 
                 "Benar, karena 6 × 250.000 = 1.200.000 cm = 12 km", 
                 "Salah, karena 6 × 250.000 = 1.500.000 cm = 10 km"],
        "jawaban": "Salah, karena seharusnya 6 × 250.000 = 1.500.000 cm = 15 km",
        "gambar": None
    },
    {
        "pertanyaan": "Rina memiliki dua foto persegi panjang. Foto A berukuran 4 cm × 6 cm, dan Foto B berukuran 6 cm × 9 cm. Apakah kedua foto tersebut sebangun? Berikan alasan!",
        "opsi": ["Ya, karena perbandingan panjang dan lebarnya sama", 
                 "Tidak, karena ukurannya berbeda", 
                 "Ya, karena bentuknya sama-sama persegi panjang", 
                 "Tidak, karena luasnya berbeda"],
        "jawaban": "Ya, karena perbandingan panjang dan lebarnya sama",
        "gambar": None
    },
    {
        "pertanyaan": "Wisata menyelam di Banyuwangi bisa dilakukan di beberapa lokasi populer seperti Teluk Biru yang menawarkan keindahan bawah laut untuk snorkeling. Seorang penyelam yang bernama Andry, memulai eksplorasinya dengan menyelam hingga kedalaman 20 meter di bawah permukaan laut untuk mengamati kehidupan laut. Kemudian, ia memutuskan untuk naik sejauh 7 meter untuk melihat lebih dekat sebuah formasi karang yang unik. Tidak lama setelah itu, ia turun lagi sejauh 5 meter untuk mengambil foto spesies kerang langka. Pada akhir rangkaian aktivitasnya ini, berapakah kedalaman Dani dari permukaan laut?",
        "opsi": ["8 meter", 
                 "18 meter", 
                 "12 meter", 
                 "22 meter"],
        "jawaban": "18 meter",
        "gambar": None
    },
    {
        "pertanyaan": "Sebuah perusahaan ingin memasang iklan di platform media sosial yang paling banyak diakses oleh kelompok usia 16-64 tahun. Mereka memutuskan untuk memilih dua platform teratas. Berdasarkan data berikut, menunjukkan presentase pengguna internet berusia 16-64 tahun di Indonesia yang mengakses berbagai jenis media sosial dalam satu bulan terakhir. Pada platform manakah perusahaan tersebut seharusnya memasang iklan?",
        "opsi": ["YouTube dan Instagram", 
                 "WhatsApp dan Facebook", 
                 "YouTube dan WhatsApp", 
                 "Instagram dan Facebook"],
        "jawaban": "Youtube dan WhatsApp",
        "gambar": None #no 6 hal 4
    },
    {
        "pertanyaan": "Bu Ani adalah wali kelas 7A yang sangat perhatian. Suatu hari, dia ingin merencanakan acara kelas untuk mempererat persahabatan antara siswa laki-laki dan perempuan. Untuk memastikan acara berjalan lancar, Bu Ani perlu mengetahui komposisi siswanya. Dia mengingat bahwa di kelasnya, perbandingan jumlah siswa laki-laki dan perempuan adalah 3 banding 4. Bu Ani lalu menghitung total semua siswa di kelasnya, dan ternyata ada 28 orang. Melihat data ini, Bu Ani meminta bantuan para siswa untuk membantunya menghitung. 'Anak-anak, kalau kita punya 28 orang di sini, dengan perbandingan anak laki-laki dan perempuan 3:4, kira-kira berapa banyak teman perempuan kita di kelas ini?' Bisakah kamu membantu Bu Ani dan siswa kelas 7A memecahkan teka-teki ini? Berapakah sebenarnya jumlah siswa perempuan di kelas 7A?",
        "opsi": ["12", 
                 "14", 
                 "16", 
                 "18"],
        "jawaban": "16",
        "gambar": None
    },
    {
        "pertanyaan": "Setiap minggu, Rina membantu ibunya berjualan minuman segar di depan rumah. Harga 1 gelas es jeruk adalah Rp5.000,00 dan harga 1 gelas es teh adalah Rp4.000,00. Dalam satu hari, Rina bisa menjual x gelas es jeruk dan (2x + 10) gelas es teh. Untuk membeli bahan-bahan, Rina mengeluarkan biaya Rp2.000,00 per gelas es jeruk dan Rp1.500,00 per gelas es teh. Rina ingin menghitung keuntungan bersihnya dalam satu hari, yang merupakan selisih antara total pendapatan dan total biaya. Bentuk aljabar yang menunjukkan keuntungan bersih Rina dalam satu hari adalah...",
        "opsi": ["5000x + 4000(2x + 10) - [2000x + 1500(2x+10)]", 
                 "5000x - 2000x + 4000x - 1500x + 10", 
                 "(5000 + 4000)x - (2000x + 15000)(2x+ 10)", 
                 "7000x + 10"],
        "jawaban": "5000x + 4000(2x + 10) - [2000x + 1500(2x+10)]",
        "gambar": None
    },
    {
        "pertanyaan": "1.	Fadil sedang mengamati perubahan suhu udara di dua kota berbeda pada hari yang sama. Di Kota A, suhu udara pada pagi hari adalah 10°C, namun pada malam hari turun drastis menjadi -4°C. Sementara itu, di Kota B, suhu udara pagi hari adalah 5°C dan pada malam hari berubah menjadi -2°C. Kota manakah yang mengalami penurunan suhu lebih besar, dan berapa besar penurunannya?",
        "opsi": ["Kota A, turun 14°C", 
                 "Kota B, turun 7°C", 
                 "Kota A, turun 9°C", 
                 "Kota B, turun 12°C"],
        "jawaban": "Kota A, turun 14°C",
        "gambar": None
    },
    {
        "pertanyaan": "Ibu memiliki sebuah tangki air besar di rumah untuk persediaan sehari-hari. Suatu pagi, setelah dicek, ternyata tangki itu berisi air sebanyak 2/3 bagian dari total kapasitasnya. Kemudian, air dalam tangki tersebut digunakan untuk mencuci dan menyiram tanaman sebanyak 1/4  bagian dari air yang ada di dalam tangki. Setelah penggunaan tersebut, berapa bagian dari total tangki yang masih terisi air?",
        "opsi": ["2/5", 
                 "1/2", 
                 "7/12", 
                 "5/12"],
        "jawaban": "1/2",
        "gambar": None
    },
    {
        "pertanyaan": "Perhatikan diagram batang dibawah ini yang menunjukkan 10 provinsi dengan usaha kuliner terbanyak di Indonesia pada tahun 2020! Seorang pengusaha berpendapat, 'Dari data dibawah ini, terlihat jelas bahwa Jawa Barat memiliki potensi pasar kuliner yang hampir tiga kali lipat lebih besar dibandingkan Jawa Timur' Berdasarkan data pada diagram batang dibawah berikut ini, bagaimana kebenaran pernyataan pengusaha tersebut?",
        "opsi": ["Pernyataan tersebut salah, karena usaha kuliner di Jawa Barat kurang dari dua kali lipat usaha kuliner di Jawa Timur.", 
                 "Pernyataan tersebut benar, karena selisih jumlah usaha antara Jawa Barat dan Jawa Timur sangat besar.", 
                 "Pernyataan tersebut salah, karena Jawa Timur justru memiliki usaha kuliner yang lebih banyak daripada Jawa Barat.", 
                 "Pernyataan tersebut benar, karena 1.414 memang lebih besar dari 821."],
        "jawaban": "Pernyataan tersebut salah, karena usaha kuliner di Jawa Barat kurang dari dua kali lipat usaha kuliner di Jawa Timur.",
        "gambar": None #no 6 hal 6
    },
    {
        "pertanyaan": "Setiap akhir pekan, Pak Rudi berjualan jus buah di taman kota dengan dua jenis minuman, yaitu jus mangga dan jus jambu. Harga satu gelas jus mangga adalah Rp7.000 dan jus jambu Rp6.000, dengan biaya bahan serta kemasan masing-masing Rp3.000 untuk jus mangga dan Rp2.500 untuk jus jambu. Dalam sehari, ia memperkirakan dapat menjual x gelas jus mangga dan (x + 20) gelas jus jambu. Keuntungan bersih hariannya dapat dinyatakan sebagai K = [7000x + 6000(x + 20)] – [3000x + 2500(x + 20)]. Pak Rudi kemudian ingin mengetahui jenis jus yang memberikan tambahan keuntungan lebih besar jika ia menambah penjualan salah satunya sebanyak 10 gelas per hari, sehingga ia dapat menentukan pilihan yang paling menguntungkan berdasarkan perhitungan aljabar.",
        "opsi": ["Menambah 10 gelas jus mangga, karena keuntungannya bertambah Rp40.000", 
                 "Menambah 10 gelas jus jambu, karena keuntungannya bertambah Rp35.000", 
                 "Menambah 10 gelas jus mangga, karena keuntungannya bertambah Rp45.000", 
                 "Menambah 10 gelas jus jambu, karena keuntungannya bertambah Rp30.000"],
        "jawaban": "Menambah 10 gelas jus mangga, karena keuntungannya bertambah Rp40.000",
        "gambar": None
    },
    {
        "pertanyaan": "Rani dan teman-temannya berencana membuka stand minuman sehat di acara sekolah dengan menjual jus buah campuran yang awalnya dibuat menggunakan perbandingan air, sirup, dan sari buah sebesar 4 : 2 : 1. Setelah dicoba, mereka merasa minuman tersebut terlalu manis. Untuk membuat rasa yang lebih segar tanpa mengubah jumlah sari buah, Rani ingin mengurangi jumlah sirup, menambah porsi air, dan tetap menghasilkan total 7 liter minuman. Dengan ketentuan bahwa sari buah tetap 1 liter dan jumlah sirup dikurangi menjadi setengah dari resep awal, tentukanlah perbandingan baru yang sesuai untuk menciptakan rasa yang lebih segar.",
        "opsi": ["6 : 1 : 1", 
                 "5 : 1 : 1", 
                 "8 : 1 : 1", 
                 "4 : 1 : 2"],
        "jawaban": "5 : 1 : 1",
        "gambar": None
    },
    {
        "pertanyaan": "Bu Ani, seorang guru matematika, menerapkan sistem penilaian khusus pada ujian harian murid-muridnya, di mana jawaban benar diberi skor +4, jawaban salah diberi skor –2, dan soal yang tidak dijawab mendapatkan skor 0. Pada ujian yang terdiri dari 20 soal tersebut, dua siswa—Adit dan Rani—mencapai hasil berbeda: Adit menjawab 15 soal dengan benar, 3 salah, dan 2 tidak diisi, sedangkan Rani menjawab 14 soal benar, 2 salah, dan 4 soal kosong. Berdasarkan data tersebut, tentukan siapa yang memperoleh nilai lebih tinggi serta berapa selisih nilai keduanya.",
        "opsi": ["Adit lebih tinggi, dengan selisih 4 poin", 
                 "Rani lebih tinggi, dengan selisih 6 poin", 
                 "Adit lebih tinggi, dengan selisih 8 poin", 
                 "Nilai Adit dan Rani sama"],
        "jawaban": "Adit lebih tinggi, dengan selisih 4 poin",
        "gambar": None
    },
    {
        "pertanyaan": "Sekelompok siswa—Andi, Bima, Citra, dan Dani—akan berkemah selama dua hari dan sepakat untuk membawa bahan makanan secara gotong royong. Ibu Andi menyediakan 8 liter air mineral untuk dibagi rata sebagai persediaan minum, Ibu Bima menyumbang 3,5 kg beras, dan Ibu Citra memberikan 2,25 kg gula. Sementara itu, Dani membeli 4,5 meter tali tambang yang nantinya akan dipotong untuk kebutuhan tenda. Setelah semua perlengkapan terkumpul, mereka membaginya dengan ketentuan: air dibagi menjadi empat bagian yang sama, beras dibagi untuk tujuh kali makan, gula digunakan untuk tiga jenis minuman sehingga dibagi menjadi tiga bagian, dan tali tambang dipotong menjadi enam bagian. Berdasarkan informasi tersebut, tentukan pernyataan yang paling tepat.",
        "opsi": ["Setiap siswa akan mendapatkan 2,5 liter air mineral.", 
                 "Setiap kali makan akan menggunakan 0,4 kg beras.", 
                 "Setiap bagian minuman akan menggunakan 1,25 kg gula.", 
                 "Setiap potongan tali tambang memiliki panjang 1,3 meter."],
        "jawaban": "Setiap potongan tali tambang memiliki panjang 1,3 meter.",
        "gambar": None
    },
]

soal7_paket2 = [
    {
        "pertanyaan": "Sebuah persegi memiliki sisi x cm. Luas persegi tersebut adalah...",
        "opsi": ["2x", "4x", "x²", "x + x"],
        "jawaban": "x²",
        "gambar": None
    }
]

soal7_paket3 = [
    {
        "pertanyaan": "Jika a = 3 dan b = 5, maka nilai dari a + b adalah...",
        "opsi": ["8", "15", "35", "2"],
        "jawaban": "8",
        "gambar": None
    }
]

soal8_paket1 = [
    {
        "pertanyaan": "Sebuah perusahaan sabun memproduksi 200 batang sabun setiap hari. Untuk memperluas usahanya, perusahaan memutuskan untuk meningkatkan kapasitas produksi sebesar 2 kali lipat setiap minggu selama 3 minggu berturut-turut. Berapa banyak sabun yang dihasilkan perusahaan pada minggu ketiga?",
        "opsi": ["800 batang", "1.600 batang", "3.200 batang", "400 batang"],
        "jawaban": "3.200 batang",
        "gambar": None
    },
    {
        "pertanyaan": "Raka memiliki uang saku Rp80.000 untuk seminggu. Ia ingin memastikan agar uang sakunya cukup sampai akhir minggu. Setiap hari, ia berencana mengeluarkan paling banyak Rp12.000. Tulislah pertidaksamaan yang menunjukkan hubungan antara banyaknya hari (x) dan batas pengeluaran Raka agar uangnya tidak habis.",
        "opsi": ["12.000x ≥ 80.000", "12.000x ≤ 80.000", "12.000x = 80.000", "12.000 x <80.000"],
        "jawaban": "12.000x ≤ 80.000",
        "gambar": None
    },
    {
        "pertanyaan": "Sebuah taman berbentuk persegi panjang memiliki panjang 24 meter dan lebar 7 meter. Petugas kebersihan ingin menarik kabel air dari satu sudut taman ke sudut berlawanan secara diagonal. Berapa panjang kabel minimum yang diperlukan agar dapat menjangkau kedua sudut taman tersebut?",
        "opsi": ["25 meter", "26 meter", "24,5 meter", "25,5 meter"],
        "jawaban": "26 meter",
        "gambar": None
    },
    {
        "pertanyaan": "Seorang petani ingin membangun pagar di sekitar sawah berbentuk segitiga siku-siku dengan panjang sisi-sisinya belum diketahui. Ia tahu bahwa salah satu sisi tegak sawah berukuran 9 meter, dan sisi miringnya 15 meter. Ia berencana membeli kawat pagar sepanjang sisi-sisi sawah. Berapakah total panjang kawat pagar yang harus dibeli petani tersebut?",
        "opsi": ["33 meter", "36 meter", "37 meter", "38 meter"],
        "jawaban": "36 meter",
        "gambar": None
    },
    {
        "pertanyaan": "Seorang arsitek merancang model bangunan yang tingginya mengecil dalam skala berpangkat untuk simulasi komputer. Model pertama memiliki tinggi 256 cm, dan setiap versi berikutnya memiliki tinggi  1/2  dari versi sebelumnya. Arsitek ingin membuat model hingga tinggi terakhir 4 cm. Berapa banyak versi model yang akan dibuat?",
        "opsi": ["4 versi", "6 versi", "7 versi", "8 versi"],
        "jawaban": "7 versi",
        "gambar": None
    },
    {
        "pertanyaan": "Tagihan listrik bulanan rumah Dina bergantung pada banyaknya pemakaian listrik (kWh). Rumus tagihan listrik dinyatakan oleh fungsi f(x) = 1.500x + 20.000, dengan x adalah jumlah kWh yang digunakan. Jika pemerintah memberikan subsidi sebesar Rp50.000 bagi pelanggan dengan penggunaan di bawah 30 kWh, apakah Dina yang menggunakan 25 kWh berhak mendapatkan subsidi, dan berapa total tagihan akhirnya?",
        "opsi": ["Tidak berhak, Rp57.500", "Berhak, Rp.32.500", "Berhak, Rp.7.500", "Berhak, Rp.45.000"],
        "jawaban": "Berhak, Rp.7.500",
        "gambar": None
    },
    {
        "pertanyaan": "Sebuah bakteri membelah diri menjadi dua setiap 6 jam. Jika pada awalnya terdapat 50 bakteri, berapa banyak bakteri setelah 2 hari (48 jam)?",
        "opsi": ["50 × 2^12 = 204.800", "50 × 2^8 = 12.800", "50 × 2^6 = 3.200", "50 × 2^4 = 800"],
        "jawaban": "50 × 2^8 = 12.800",
        "gambar": None
    },
    {
        "pertanyaan": "Sebuah kelas melakukan survei tentang kegiatan yang dilakukan siswa di waktu luang. Hasilnya disajikan dalam diagram lingkaran di atas. Jika jumlah seluruh siswa adalah 72 orang, maka banyak siswa yang gemar membaca adalah ....",
        "opsi": ["8 orang", "9 orang", "10 orang", "11 orang"],
        "jawaban": "10 orang",
        "gambar": None #no 1 hal 1
    },
    {
        "pertanyaan": "Sebuah kelompok siswa membuat gantungan kunci. Biaya bahan tetap Rp30.000 dan biaya pembuatan tiap gantungan kunci Rp5.000. Mereka menjualnya seharga Rp8.000 per buah. Tentukan banyak gantungan kunci yang harus terjual agar mereka tidak rugi!",
        "opsi": ["Minimal 8 buah", "Minimal 9 buah", "Minimal 10 buah", "Minimal 12 buah"],
        "jawaban": "Minimal 10 buah",
        "gambar": None
    },
    {
        "pertanyaan": "Rian ingin mengecat dinding rumahnya yang berbentuk persegi panjang. Untuk mencapai bagian atas dinding, ia harus menggunakan tangga yang disandarkan pada dinding tersebut. Kaki tangga berada sejauh 1,5 meter dari tembok, sedangkan bagian atas tangga menyentuh dinding pada ketinggian 3,5 meter. Panjang tangga yang digunakan Rian adalah ...",
        "opsi": ["3 meter", "4 meter", "4,8 meter", "3,8 meter"],
        "jawaban": "3,8 meter",
        "gambar": None
    },
    {
        "pertanyaan": "Banyak tenaga kerja laki-laki berusia lebih dari 20 tahun yang bekerja di suatu kota bertambah secara linear. Jika digambarkan, grafik pertambahan tenaga kerja laki-laki dapat direpresentasikan oleh garis lurus berikut. Pada tahun 1980, sekitar 600 laki-laki berusia di atas 20 tahun yang bekerja. Pada tahun 2000, jumlah ini meningkat menjadi 800. Berapa banyak tenaga kerja laki-laki di kota tersebut pada tahun 2015?",
        "opsi": ["950 orang", "1.050 orang", "1.000 orang", "1.150 orang"],
        "jawaban": "950 orang",
        "gambar": None #no 5 hal 3
    },
    {
        "pertanyaan": "Sinta sedang mempersiapkan dekorasi untuk acara ulang tahun adiknya. Ia pergi ke toko perlengkapan party dan memilih dua jenis barang, yaitu pita warna-warni dan balon helium. Setelah memilih, Sinta membeli 4 meter pita dan 3 buah balon. Saat membayar di kasir, total belanjaannya adalah Rp41.000,00. Diketahui bahwa harga pita per meter adalah Rp5.000,00. Sinta kemudian mencoba mengira-ngira, kira-kira apakah harga satu buah balon yang ia beli adalah Rp3.000,00? Ia merasa perlu memastikan apakah angka tersebut masuk akal dengan total belanjaannya. Berdasarkan informasi di atas, tentukan apakah perkiraan harga balon Rp3.000,00 per buah itu masuk akal atau tidak?",
        "opsi": ["Masuk akal, karena harganya sesuai dengan perhitungan", "Tidak masuk akal, karena berdasarkan perhitungan, harga seharusnya Rp7.000,00 per balon", "Masuk akal, karena total belanjaannya menjadi pas", "Tidak bisa ditentukan dari informasi yang diberikan"],
        "jawaban": "Tidak masuk akal, karena berdasarkan perhitungan, harga seharusnya Rp7.000,00 per balon",
        "gambar": None
    },
    {
        "pertanyaan": "Di halaman sekolah, terdapat tiang bendera setinggi 12 meter. Dari puncak tiang, sebuah tali bendera ditarik ke tanah sejauh 5 meter dari kaki tiang, lalu diikat pada pasak pertama. Agar tali tidak terlalu tegang, guru meminta untuk menambahkan pasak kedua yang berada 3 meter lebih jauh dari pasak pertama di garis yang sama. Jika tali baru akan dipasang dari puncak tiang ke pasak kedua, berapa tambahan panjang tali yang harus disiapkan dibandingkan tali pertama?",
        "opsi": ["2,5 meter", "3 meter", "3,2 meter", "4 meter"],
        "jawaban": "3,2 meter",
        "gambar": None
    },
    {
        "pertanyaan": "Dita dan Rani melakukan percobaan sains tentang pertumbuhan jamur. Dita menuliskan data bahwa jumlah spora jamur bertambah 3 kali lipat setiap hari, sedangkan Rani menuliskan bahwa pertambahannya 2 kali lipat setiap hari. Jika pada hari pertama jumlah spora ada 5, maka pada hari ke -4 berapa perbandingan hasil perhitungan Dita dan Rani?",
        "opsi": ["135 ∶ 40", "5 × 2^4 : 5 × 2^3", "	3^4 : 2^4", "Semua benar"],
        "jawaban": "Semua benar",
        "gambar": None
    },
    {
        "pertanyaan": "Seorang pengemudi taksi online menerapkan tarif yang bergantung pada jarak tempuh, dan grafik di bawah ini menunjukkan hubungan antara jarak x (dalam kilometer) dan tarif y (dalam ribuan rupiah). Dari grafik terlihat bahwa tarif untuk 2 km adalah Rp14.000, untuk 4 km sebesar Rp22.000, dan untuk 6 km mencapai Rp30.000. Karena hubungan antara jarak dan tarif bersifat linear, tentukan persamaan garis yang menggambarkan hubungan tersebut serta hitung tarif perjalanan untuk jarak 10 km!",
        "opsi": ["y = 3x + 8, tarif Rp. 38.000", "y = 4x + 6, tarif Rp. 46.000", "y = 2x + 10, tarif Rp. 30.000", "y = 5x + 4, tarif Rp. 54.000"],
        "jawaban": "y = 4x + 6, tarif Rp. 46.000",
        "gambar": None #no 6 hal 3
    },
    {
        "pertanyaan": "Andi memarkir mobilnya di sebuah pusat perbelanjaan yang menerapkan tarif parkir dengan dua komponen, yaitu biaya tetap untuk 2 jam pertama sebesar Rp5.000 dan biaya tambahan Rp2.000 untuk setiap jam berikutnya. Setelah berbelanja dan menghabiskan waktu cukup lama, Andi kembali ke area parkir dan sistem otomatis menghitung total biaya yang harus dibayarkan. Ia pun memahami bahwa durasi parkirnya selalu mencapai 2 jam atau lebih karena kebiasaannya menghabiskan waktu lama di pusat perbelanjaan tersebut. ia ingin mengetahui fungsi yang tepat untuk menghitung total biaya parkir berdasarkan lama parkir x jam. Manakah fungsi yang benar untuk menggambarkan aturan tarif tersebut?",
        "opsi": ["f(x) = 5.000x + 2.000", "f(x) = 2.000x + 1.000", "f(x) = 5.000(x-2) + 2.000", "f(x) = 2.000(x-2) + 5.000"],
        "jawaban": "f(x) = 2.000(x-2) + 5.000",
        "gambar": None
    },
    {
        "pertanyaan": "Rafi bekerja sebagai pengemudi ojek online dan menerima bayaran berdasarkan jarak yang ditempuh. Ia mendapatkan tarif awal sebesar Rp5.000 sebagai biaya tetap, kemudian setiap kilometer berikutnya dihitung dengan biaya Rp2.500. Hubungan antara jarak tempuh x (dalam kilometer) dan biaya perjalanan f(x) (dalam rupiah) dinyatakan melalui fungsi f(x) = 2.500x + 5.000. Jika seorang penumpang menempuh perjalanan sejauh 8 km, tentukan berapa biaya yang perlu dibayarkan!",
        "opsi": ["Rp. 15.000", "Rp. 20.000", "Rp. 25.000", "Rp. 30.000"],
        "jawaban": "Rp. 25.000",
        "gambar": None
    },
    {
        "pertanyaan": "Panitia kelas 8C sedang menyiapkan bazar sekolah untuk acara pentas seni akhir tahun dan telah mempersiapkan sebuah stan yang akan digunakan untuk menjual minuman kemasan serta kue tradisional. Dari hasil rapat, diketahui bahwa biaya tetap sewa stan sebesar Rp150.000, harga jual setiap produk Rp20.000, dan modal per produk adalah Rp12.000. Panitia menargetkan keuntungan lebih dari Rp250.000 untuk membantu pendanaan studi tur ke kebun raya. Berdasarkan informasi tersebut, tentukan model pertidaksamaan yang menyatakan syarat keuntungan lebih dari Rp250.000 serta jumlah minimal produk yang harus terjual agar target keuntungan dapat tercapai.",
        "opsi": ["x > 40", "x > 45", "x > 50", "x > 55"],
        "jawaban": "x > 50",
        "gambar": None
    },
]

soal8_paket2 = [
    {
        "pertanyaan": "Sebuah persegi memiliki sisi x cm. Luas persegi tersebut adalah...",
        "opsi": ["2x", "4x", "x²", "x + x"],
        "jawaban": "x²",
        "gambar": None
    }
]

soal8_paket3 = [
    {
        "pertanyaan": "Jika a = 3 dan b = 5, maka nilai dari a + b adalah...",
        "opsi": ["8", "15", "35", "2"],
        "jawaban": "8",
        "gambar": None
    }
]

# ================= GABUNG =================
soal_numerasi = {
    "Kelas 7": {
        "Paket 1": soal7_paket1,
        "Paket 2": soal7_paket2,
        "Paket 3": soal7_paket3
    },
    "Kelas 8": {
        "Paket 1": soal8_paket1,
        "Paket 2": soal8_paket2,
        "Paket 3": soal8_paket3
    }
}

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
