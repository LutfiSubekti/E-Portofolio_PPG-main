/**
 * generate_course_pages.js  (v2 — dengan PDF Preview & Download)
 * Jalankan: node generate_course_pages.js
 */
const fs = require('fs');
const path = require('path');
const BASE = __dirname;

// ─── Data semua mata kuliah ───
const courses = [
    {
        file: 'course-ct.html',
        title: 'Computational Thinking',
        subtitle: '34619 Informatika - 002 [2026]',
        accent: '#1a7b5d', accentLight: 'rgba(26,123,93,0.15)', accentBorder: 'rgba(26,123,93,0.3)',
        icon: 'fa-microchip',
        refleksi: {
            connection: 'Materi Computational Thinking menghubungkan cara berpikir sistematis yang sudah saya terapkan saat mengajar coding dan robotika dengan kerangka pedagogis yang lebih terstruktur. Saya menemukan bahwa konsep dekomposisi, pengenalan pola, abstraksi, dan algoritma bukan hanya alat pemrograman — melainkan cara berpikir yang bisa ditanamkan sejak dini kepada peserta didik Informatika SMP.',
            challenge: 'Tantangan terbesar yang saya hadapi adalah mengadaptasi konsep abstrak CT ke dalam aktivitas pembelajaran yang konkret dan menarik bagi siswa kelas 7–9. Banyak siswa yang masih berpikir bahwa CT hanya berkaitan dengan komputer, padahal esensinya jauh lebih luas. Saya juga kesulitan merancang asesmen yang benar-benar mengukur kemampuan berpikir, bukan sekadar mengingat istilah.',
            concept: 'Konsep utama yang saya pelajari adalah bahwa CT adalah fondasi literasi digital — bukan konten hafalan. Pembelajaran berbasis proyek (Project-Based Learning) terbukti efektif untuk membuat siswa mengalami sendiri proses berpikir komputasional: mulai dari mendefinisikan masalah, memecahnya, menemukan pola, hingga merancang solusi algoritma sederhana.',
            change: 'Ke depan, saya ingin merancang unit pembelajaran CT yang terintegrasi dengan konteks kehidupan siswa — misalnya menggunakan algoritma untuk menyelesaikan masalah sehari-hari sebelum beralih ke kode. Saya juga berencana mengembangkan rubrik penilaian CT yang lebih komprehensif dan mudah digunakan rekan guru.'
        },
        artefak: [
            { icon: 'fa-file-contract', nama: 'Analisis Perencanaan Mengajar', alasan: 'Modul ajar CT yang saya susun mengintegrasikan 4 pilar CT (dekomposisi, pengenalan pola, abstraksi, algoritma) dalam satu alur pembelajaran yang kohesif. Artefak ini membuktikan kemampuan saya merancang pembelajaran berbasis prinsip CT secara terstruktur.', pdf: 'assets/docs/ct-perencanaan-mengajar.pdf' },
            { icon: 'fa-desktop', nama: 'Analisis Media Pembelajaran', alasan: 'Media interaktif berbasis Scratch dan unplugged activity yang saya rancang menjadi bukti nyata bahwa CT bisa diajarkan dengan dan tanpa teknologi — menjangkau semua kondisi kelas.', pdf: 'assets/docs/ct-media-pembelajaran.pdf' },
            { icon: 'fa-video', nama: 'Analisis Video Praktik Mengajar', alasan: 'Video praktik mengajar merekam momen ketika siswa berhasil menerapkan konsep dekomposisi untuk memecah masalah — bukti kongkret keberhasilan pembelajaran CT di kelas.', pdf: 'assets/docs/ct-video-mengajar.pdf' }
        ],
        kaitan: {
            konsep: 'Computational Thinking mengajarkan saya bahwa cara berpikir lebih penting dari sintaks kode. Sebagai guru Informatika, tugas utama saya bukan mengajarkan bahasa pemrograman tertentu, melainkan melatih siswa berpikir logis, sistematis, dan kreatif dalam menghadapi masalah.',
            perubahan: 'Saya ingin mengintegrasikan sesi refleksi CT di setiap akhir unit — meminta siswa menuliskan bagaimana mereka memecah masalah. Selain itu, saya berencana merancang bank soal CT yang dikaitkan langsung dengan konteks lokal (budaya, lingkungan Kediri) agar lebih relevan bagi siswa.'
        }
    },
    {
        file: 'course-filosofi.html',
        title: 'Philosophy of Education and Value Education',
        subtitle: 'Filosofi Pendidikan',
        accent: '#4a7c59', accentLight: 'rgba(74,124,89,0.15)', accentBorder: 'rgba(74,124,89,0.3)',
        icon: 'fa-brain',
        refleksi: {
            connection: 'Mata kuliah Filosofi Pendidikan membantu saya menghubungkan pengalaman mengajar selama tiga tahun dengan landasan teoritis yang kokoh. Saya mulai memahami mengapa praktik tertentu berhasil — bukan hanya secara intuitif, tetapi berdasarkan pandangan filsuf seperti Ki Hadjar Dewantara, Freire, dan Dewey tentang hakikat pendidikan sebagai proses humanisasi.',
            challenge: 'Tantangan terbesar adalah menjembatani teori filosofi yang abstrak dengan realitas kelas yang kompleks. Ketika mendiskusikan konsep "pendidikan yang membebaskan" ala Freire, saya harus jujur mengakui bahwa masih ada praktik di kelas saya yang cenderung transmisif — guru sebagai satu-satunya sumber kebenaran.',
            concept: 'Konsep paling transformatif yang saya pelajari adalah pendidikan sebagai dialog, bukan monolog. Nilai-nilai pendidikan yang ditanamkan tidak cukup hanya disampaikan lewat ceramah — ia harus dihidupi dan dicontohkan guru dalam setiap interaksi di kelas.',
            change: 'Saya ingin mengubah cara saya memulai setiap pembelajaran — dari "saya akan mengajarkan kalian tentang..." menjadi "hari ini kita akan bersama-sama mengeksplorasi...". Pergeseran kecil dalam bahasa ini mencerminkan pergeseran fundamental dalam pandangan saya tentang siapa yang memegang otoritas pengetahuan di kelas.'
        },
        artefak: [
            { icon: 'fa-book-open', nama: 'Analisis Materi Pembelajaran', alasan: 'Analisis materi yang saya susun mencerminkan upaya mengintegrasikan nilai-nilai lokal (kearifan budaya Jawa) ke dalam pembelajaran Informatika — wujud konkret pendidikan nilai yang tidak tercerabut dari akar budaya siswa.', pdf: 'assets/docs/filosofi-materi-pembelajaran.pdf' },
            { icon: 'fa-file-contract', nama: 'Analisis Perencanaan Mengajar', alasan: 'Modul ajar yang saya rancang mencantumkan profil pelajar Pancasila sebagai tujuan pembelajaran yang aktif — bukan sekadar kelengkapan administratif — membuktikan internalisasi nilai dalam perencanaan.', pdf: 'assets/docs/filosofi-perencanaan-mengajar.pdf' },
            { icon: 'fa-users-gear', nama: 'Analisis Kegiatan Nonmengajar', alasan: 'Keterlibatan dalam kegiatan sekolah (ekstrakurikuler, rapat wali murid) menjadi bukti bahwa saya memahami pendidikan sebagai proses sosial yang terjadi di luar ruang kelas.', pdf: 'assets/docs/filosofi-nonmengajar.pdf' }
        ],
        kaitan: {
            konsep: 'Filosofi pendidikan mengajarkan saya bahwa setiap keputusan pedagogis adalah keputusan etis. Memilih metode, materi, atau cara evaluasi bukan sekadar soal teknis — melainkan pernyataan tentang nilai apa yang kita percaya dan jenis manusia seperti apa yang ingin kita bantu tumbuhkan.',
            perubahan: 'Saya ingin memulai setiap unit pembelajaran dengan pertanyaan esensial yang mengundang refleksi nilai — bukan hanya pertanyaan kognitif. Saya juga berkomitmen untuk lebih sering melakukan refleksi diri tentang praktik mengajar saya, menggunakan jurnal reflektif sebagai alat pertumbuhan profesional.'
        }
    },
    {
        file: 'course-pemahaman.html',
        title: 'Pemahaman Tentang Peserta Didik dan Pembelajaran',
        subtitle: 'Pemahaman Peserta Didik',
        accent: '#c0392b', accentLight: 'rgba(192,57,43,0.12)', accentBorder: 'rgba(192,57,43,0.3)',
        icon: 'fa-users',
        refleksi: {
            connection: 'Mata kuliah ini mengkonfirmasi dan memperdalam intuisi yang saya bangun selama tiga tahun mengajar coding: setiap anak belajar dengan cara yang berbeda. Teori perkembangan kognitif Piaget dan konsep Zone of Proximal Development (ZPD) Vygotsky memberikan kerangka ilmiah untuk praktik diferensiasi yang selama ini saya lakukan secara intuitif.',
            challenge: 'Tantangan terbesar adalah mengelola keberagaman gaya belajar dan kecepatan pemahaman dalam satu kelas yang sama. Di SMP Negeri 8 Malang, saya menghadapi siswa dengan latar belakang yang sangat beragam — dari yang sudah mahir menggunakan teknologi hingga yang baru pertama kali memegang komputer.',
            concept: 'Konsep "readiness, interest, dan learning profile" dalam diferensiasi pembelajaran menjadi landasan utama cara saya merancang kegiatan belajar. Saya belajar bahwa asesmen diagnostik bukan hanya alat ukur, melainkan jembatan untuk memahami titik awal setiap siswa.',
            change: 'Saya ingin menerapkan asesmen diagnostik yang lebih sistematis di awal setiap unit — bukan hanya pretest kognitif, tetapi juga inventori gaya belajar dan minat siswa. Data ini akan menjadi dasar untuk merancang pembelajaran yang benar-benar responsif.'
        },
        artefak: [
            { icon: 'fa-clipboard-check', nama: 'Instrumen Penilaian & Analisis', alasan: 'Instrumen penilaian yang saya rancang menggunakan pendekatan asesmen formatif berkelanjutan — bukan sekadar ujian akhir — membuktikan pemahaman saya tentang pentingnya memantau perkembangan belajar siswa secara holistik.', pdf: 'assets/docs/pemahaman-instrumen-penilaian.pdf' },
            { icon: 'fa-users-gear', nama: 'Analisis Kegiatan Nonmengajar', alasan: 'Observasi dan wawancara informal dengan siswa di luar kelas memberikan data berharga tentang motivasi, tantangan, dan minat mereka — memperkaya pemahaman saya sebagai pendidik.', pdf: 'assets/docs/pemahaman-nonmengajar.pdf' },
            { icon: 'fa-video', nama: 'Analisis Video Praktik Mengajar', alasan: 'Video praktik merekam respons nyata siswa terhadap berbagai strategi pembelajaran — data autentik tentang apa yang benar-benar bekerja di konteks kelas ini.', pdf: 'assets/docs/pemahaman-video-mengajar.pdf' }
        ],
        kaitan: {
            konsep: 'Pemahaman mendalam tentang peserta didik mengubah cara saya memandang "kegagalan" siswa. Yang dulu saya anggap sebagai siswa yang "tidak mau belajar" kini saya pahami sebagai siswa yang belum menemukan pintu masuk yang tepat. Tugas saya adalah menemukan pintu itu.',
            perubahan: 'Saya berencana membuat "profil belajar" untuk setiap siswa di awal semester — dokumen singkat yang merangkum gaya belajar, minat, dan tantangan utama mereka. Dokumen ini akan menjadi panduan saya dalam merancang pembelajaran yang inklusif dan bermakna.'
        }
    },
    {
        file: 'course-pembelajaran.html',
        title: 'Pembelajaran Mendalam dan Asesmen',
        subtitle: 'Pembelajaran Mendalam',
        accent: '#1a3799', accentLight: 'rgba(26,55,153,0.15)', accentBorder: 'rgba(26,55,153,0.3)',
        icon: 'fa-layer-group',
        refleksi: {
            connection: 'Mata kuliah ini menghubungkan berbagai pendekatan pembelajaran yang pernah saya coba — PBL, discovery learning, flipped classroom — ke dalam satu kerangka yang kohesif: pembelajaran yang bertujuan membangun pemahaman mendalam (deep learning), bukan sekadar penguasaan permukaan (surface learning).',
            challenge: 'Tantangan utama adalah merancang asesmen yang benar-benar mengukur pemahaman mendalam, bukan hafalan. Tekanan ujian nasional dan target nilai sering membuat baik guru maupun siswa terjebak dalam pembelajaran permukaan. Mengubah pola ini membutuhkan keberanian dan dukungan sistemik.',
            concept: 'Konsep "backward design" — merancang pembelajaran dimulai dari hasil yang diinginkan, bukan dari konten — mengubah cara saya menyusun unit pembelajaran. Pertanyaan pertama bukan lagi "apa yang akan saya ajarkan?" melainkan "bukti apa yang menunjukkan siswa telah benar-benar memahami?"',
            change: 'Saya ingin mengimplementasikan portofolio pembelajaran sebagai asesmen utama — menggantikan sebagian peran ujian tertulis. Portofolio memungkinkan siswa menunjukkan pemahaman mereka melalui karya nyata, bukan hanya jawaban soal.'
        },
        artefak: [
            { icon: 'fa-file-contract', nama: 'Analisis Perencanaan Mengajar', alasan: 'Modul ajar yang menggunakan kerangka backward design menjadi bukti kemampuan saya merancang pembelajaran yang berorientasi pada pemahaman mendalam, bukan konten semata.', pdf: 'assets/docs/pma-perencanaan-mengajar.pdf' },
            { icon: 'fa-clipboard-check', nama: 'Instrumen Penilaian & Analisis', alasan: 'Rubrik penilaian proyek yang saya kembangkan mengukur kemampuan berpikir tingkat tinggi (analisis, evaluasi, kreasi) — bukan sekadar mengingat fakta.', pdf: 'assets/docs/pma-instrumen-penilaian.pdf' },
            { icon: 'fa-box-archive', nama: 'Kumpulan Artefak', alasan: 'Kumpulan karya siswa selama satu semester menjadi portofolio autentik yang merekam perjalanan belajar mereka — bukti nyata pembelajaran mendalam yang terjadi.', pdf: 'assets/docs/pma-kumpulan-artefak.pdf' }
        ],
        kaitan: {
            konsep: 'Pembelajaran mendalam mengajarkan saya bahwa kualitas pertanyaan lebih penting dari kualitas jawaban. Guru yang baik tidak hanya memberikan jawaban yang tepat — ia merancang pertanyaan yang mendorong siswa berpikir lebih dalam dan menemukan pemahaman mereka sendiri.',
            perubahan: 'Saya akan mengadopsi strategi "essential questions" di setiap unit — pertanyaan besar yang tidak bisa dijawab dengan satu kalimat dan mendorong eksplorasi sepanjang unit. Selain itu, saya berencana memberikan lebih banyak ruang untuk "productive struggle" — membiarkan siswa bergulat dengan masalah sebelum saya memberikan bantuan.'
        }
    },
    {
        file: 'course-growth.html',
        title: 'Dasar Pola Pikir Bertumbuh (Growth Mindset) dalam Pembelajaran',
        subtitle: 'Growth Mindset',
        accent: '#0b8004', accentLight: 'rgba(11,128,4,0.12)', accentBorder: 'rgba(11,128,4,0.3)',
        icon: 'fa-seedling',
        refleksi: {
            connection: 'Konsep growth mindset Carol Dweck menjadi cermin bagi saya untuk merefleksikan cara saya merespons kesalahan — baik kesalahan siswa maupun kesalahan saya sendiri. Saya menyadari bahwa selama ini saya sudah memiliki benih growth mindset dalam praktik mengajar, namun belum cukup eksplisit dalam mengkomunikasikannya kepada siswa.',
            challenge: 'Tantangan terbesar adalah mengubah budaya kelas yang sudah terbentuk: siswa terbiasa menghindari tugas sulit karena takut salah. Mengubah persepsi ini tidak bisa dilakukan dalam satu pertemuan — ia membutuhkan konsistensi dalam setiap interaksi, setiap umpan balik, dan setiap respons guru terhadap kesalahan.',
            concept: 'Perbedaan fundamental antara fixed mindset dan growth mindset terletak pada cara memaknai kesulitan. Dalam growth mindset, kesulitan bukan hambatan — melainkan tanda bahwa otak sedang bekerja keras dan tumbuh. Siswa yang memahami ini akan lebih berani mengambil risiko intelektual.',
            change: 'Saya ingin mengubah cara saya memberikan umpan balik: dari "jawaban kamu salah" menjadi "kamu sudah sampai di titik ini, langkah selanjutnya adalah...". Saya juga akan memperkenalkan "kesalahan minggu ini" sebagai momen positif di kelas — mendiskusikan bersama apa yang bisa dipelajari dari kesalahan tersebut.'
        },
        artefak: [
            { icon: 'fa-file-contract', nama: 'Analisis Perencanaan Mengajar', alasan: 'Rencana pembelajaran yang saya susun mengintegrasikan aktivitas yang sengaja dirancang untuk membangun toleransi terhadap ambiguitas dan keberanian mencoba — fondasi growth mindset dalam konteks Informatika.', pdf: 'assets/docs/growth-perencanaan-mengajar.pdf' },
            { icon: 'fa-desktop', nama: 'Analisis Media Pembelajaran', alasan: 'Media pembelajaran yang menampilkan proses berpikir (bukan hanya hasil akhir) membantu siswa melihat bahwa kesulitan adalah bagian normal dari proses belajar.', pdf: 'assets/docs/growth-media-pembelajaran.pdf' },
            { icon: 'fa-users-gear', nama: 'Analisis Kegiatan Nonmengajar', alasan: 'Kegiatan mentoring dan bimbingan individual di luar kelas menjadi ruang aman bagi siswa untuk mengekspresikan kebingungan mereka tanpa takut dinilai.', pdf: 'assets/docs/growth-nonmengajar.pdf' }
        ],
        kaitan: {
            konsep: 'Growth mindset bukan sekadar motivational speech — ia adalah framework tentang bagaimana otak belajar. Ketika saya memahami bahwa kecerdasan bisa ditumbuhkan, seluruh cara saya merancang pembelajaran berubah: dari memberikan tugas yang "aman" menjadi merancang tantangan yang "tepat-tepat susah".',
            perubahan: 'Saya akan menambahkan jurnal refleksi mingguan untuk siswa — bukan tentang apa yang mereka pelajari, tetapi tentang bagaimana mereka belajar: apa yang sulit, bagaimana mereka mengatasinya, dan apa yang berubah dalam pemahaman mereka. Ini melatih metakognisi sekaligus membangun growth mindset secara sistematis.'
        }
    },
    {
        file: 'course-selektif.html',
        title: 'Refleksi Mata Kuliah Selektif / Elektif',
        subtitle: 'Mata Kuliah Selektif',
        accent: '#d17c14', accentLight: 'rgba(209,124,20,0.13)', accentBorder: 'rgba(209,124,20,0.3)',
        icon: 'fa-star',
        refleksi: {
            connection: 'Mata kuliah selektif yang saya ambil memperkaya perspektif saya tentang pendidikan dari sudut pandang yang tidak selalu diajarkan dalam kurikulum inti. Saya menemukan koneksi yang kuat antara topik yang dipilih dengan tantangan nyata yang saya hadapi di sekolah mitra — memberikan warna berbeda dalam cara saya memandang praktik mengajar.',
            challenge: 'Mengintegrasikan wawasan dari mata kuliah selektif ke dalam praktik PPL menjadi tantangan tersendiri. Tidak semua konsep bisa langsung diterapkan di konteks SMP Negeri 8 Malang, sehingga diperlukan adaptasi yang kreatif dan pertimbangan matang tentang kesesuaian konteks.',
            concept: 'Mata kuliah selektif mengajarkan saya bahwa pendidikan adalah bidang yang luas dan dinamis — selalu ada perspektif baru, pendekatan baru, dan temuan penelitian baru yang bisa memperkaya praktik mengajar. Sikap sebagai "lifelong learner" bukan hanya slogan, melainkan keharusan profesional.',
            change: 'Ke depan, saya ingin terus mengikuti perkembangan riset pendidikan dan teknologi pembelajaran — tidak berhenti hanya pada apa yang dipelajari di PPG. Saya berencana bergabung dengan komunitas praktisi guru Informatika untuk terus berbagi dan belajar bersama rekan sejawat.'
        },
        artefak: [
            { icon: 'fa-book-open', nama: 'Analisis Materi Pembelajaran', alasan: 'Materi pembelajaran yang mengintegrasikan wawasan dari mata kuliah selektif menjadi bukti kemampuan saya menyintesis pengetahuan lintas disiplin untuk kepentingan pembelajaran siswa.', pdf: 'assets/docs/selektif-materi-pembelajaran.pdf' },
            { icon: 'fa-file-contract', nama: 'Analisis Perencanaan Mengajar', alasan: 'Perencanaan pembelajaran yang menunjukkan pengaruh perspektif dari mata kuliah selektif membuktikan refleksi yang mendalam dan keseriusan dalam mengintegrasikan berbagai sumber wawasan.', pdf: 'assets/docs/selektif-perencanaan-mengajar.pdf' },
            { icon: 'fa-box-archive', nama: 'Kumpulan Artefak', alasan: 'Kumpulan artefak ini merekam perjalanan belajar yang tidak linear — dengan berbagai eksperimen pedagogis yang diinspirasi oleh wawasan dari mata kuliah selektif.', pdf: 'assets/docs/selektif-kumpulan-artefak.pdf' }
        ],
        kaitan: {
            konsep: 'Mata kuliah selektif mengokohkan keyakinan saya bahwa guru yang baik adalah guru yang tidak pernah berhenti menjadi murid. Setiap sumber belajar — baik dari kurikulum formal maupun pengalaman lapangan — berkontribusi membentuk identitas dan kompetensi profesional saya.',
            perubahan: 'Saya berkomitmen untuk mengalokasikan waktu khusus setiap bulan untuk membaca literatur pendidikan terbaru dan mendiskusikannya dengan rekan guru. Saya percaya bahwa refleksi dan pembelajaran profesional yang berkelanjutan adalah fondasi guru yang benar-benar profesional.'
        }
    }
];

// ─── Template builder ───
function buildPage(c) {

    // Artefak cards dengan tombol preview & download
    const artefakCards = c.artefak.map((a, i) => `
                    <div class="artefak-card">
                        <div class="artefak-top">
                            <div class="artefak-icon" style="background:${c.accentLight};color:${c.accent};">
                                <i class="fa-solid ${a.icon}"></i>
                            </div>
                            <div class="artefak-info">
                                <div class="artefak-nama">${a.nama}</div>
                                <p class="artefak-alasan">${a.alasan}</p>
                            </div>
                        </div>
                        <div class="artefak-footer">
                            <div class="artefak-file">
                                <i class="fa-solid fa-file-pdf" style="color:#f87171;font-size:1.1rem;"></i>
                                <div>
                                    <div class="artefak-filename">${a.nama}.pdf</div>
                                    <div class="artefak-filetype">Dokumen PDF</div>
                                </div>
                            </div>
                            <div class="artefak-actions">
                                <button class="btn-preview" onclick="openPreview('${a.pdf}','${a.nama}')" title="Pratinjau Dokumen" style="--btn-color:${c.accent};">
                                    <i class="fa-solid fa-eye"></i>
                                    <span>Lihat</span>
                                </button>
                                <a class="btn-download" href="${a.pdf}" download="${a.nama}.pdf" title="Unduh Dokumen" style="--btn-color:${c.accent};">
                                    <i class="fa-solid fa-download"></i>
                                    <span>Unduh</span>
                                </a>
                            </div>
                        </div>
                    </div>`).join('\n');

    return `<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${c.title} | Seminar PPL | E-Portfolio PPG</title>
    <meta name="description" content="Refleksi 4C, Analisis Artefak, dan Kaitan Praktis mata kuliah ${c.title} — PPG Prajabatan Lutfi Subekti">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Lora:ital,wght@0,400;0,600;1,400;1,600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
    <style>
        .crs-wrap { max-width: 860px; margin: 0 auto; padding: 0 1.5rem; }

        /* Back */
        .back-link { display:inline-flex;align-items:center;gap:.5rem;color:var(--text-muted);text-decoration:none;font-size:.88rem;font-weight:500;padding:.4rem 0;transition:color .2s;margin-bottom:2.5rem; }
        .back-link:hover { color:var(--primary-light); }

        /* Header */
        .crs-badge { display:inline-flex;align-items:center;gap:.5rem;padding:.3rem 1rem;border-radius:50px;font-size:.75rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;background:${c.accentLight};border:1px solid ${c.accentBorder};color:${c.accent};margin-bottom:1rem; }
        .crs-title { font-family:'Lora',Georgia,serif;font-size:clamp(1.6rem,4vw,2.4rem);font-weight:600;color:#fff;line-height:1.25;margin-bottom:.3rem; }
        html[data-theme="light"] .crs-title { color:#1e293b; }
        .crs-subtitle { font-size:.9rem;color:var(--text-muted);margin-bottom:1.5rem; }
        .crs-divider { height:2px;background:linear-gradient(90deg,${c.accent},transparent);border:none;border-radius:2px;margin-bottom:2.5rem; }

        /* Section */
        .crs-section { margin-bottom:2.5rem;padding:1.8rem;background:rgba(15,23,42,.45);border:1px solid var(--glass-border);border-radius:18px; }
        html[data-theme="light"] .crs-section { background:rgba(255,255,255,.85);box-shadow:0 2px 16px rgba(0,0,0,.06); }

        /* Section label */
        .sec-label { display:flex;align-items:center;gap:.75rem;margin-bottom:1.4rem; }
        .sec-label-icon { width:36px;height:36px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:.95rem;flex-shrink:0;background:${c.accentLight};color:${c.accent}; }
        .sec-label-text { font-family:'Outfit',sans-serif;font-size:1.1rem;font-weight:700;color:#fff; }
        html[data-theme="light"] .sec-label-text { color:#1e293b; }
        .sec-label-sub { font-size:.78rem;color:var(--text-muted);font-weight:400; }

        /* 4C */
        .c4-grid { display:grid;grid-template-columns:1fr 1fr;gap:1rem; }
        @media(max-width:600px){ .c4-grid{grid-template-columns:1fr;} }
        .c4-card { padding:1.15rem;border-radius:12px;border-left:3px solid; }
        .c4-card.connection { background:rgba(79,70,229,.06);border-color:#818cf8; }
        .c4-card.challenge  { background:rgba(236,72,153,.06);border-color:#f472b6; }
        .c4-card.concept    { background:${c.accentLight};border-color:${c.accent}; }
        .c4-card.change     { background:rgba(245,158,11,.06);border-color:#fbbf24; }
        html[data-theme="light"] .c4-card.connection { background:rgba(79,70,229,.05); }
        html[data-theme="light"] .c4-card.challenge  { background:rgba(236,72,153,.05); }
        html[data-theme="light"] .c4-card.change     { background:rgba(245,158,11,.05); }
        .c4-label { font-size:.68rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;margin-bottom:.5rem;display:flex;align-items:center;gap:.4rem; }
        .c4-card.connection .c4-label { color:#818cf8; }
        .c4-card.challenge  .c4-label { color:#f472b6; }
        .c4-card.concept    .c4-label { color:${c.accent}; }
        .c4-card.change     .c4-label { color:#fbbf24; }
        .c4-text { font-size:.86rem;line-height:1.7;color:var(--text-muted);margin:0; }
        html[data-theme="light"] .c4-text { color:#475569; }

        /* ─── Artefak cards ─── */
        .artefak-list { display:flex;flex-direction:column;gap:1rem; }
        .artefak-card { border-radius:14px;border:1px solid var(--glass-border);background:rgba(0,0,0,.15);overflow:hidden;transition:border-color .2s; }
        .artefak-card:hover { border-color:${c.accentBorder}; }
        html[data-theme="light"] .artefak-card { background:rgba(0,0,0,.025);border-color:rgba(0,0,0,.08); }

        .artefak-top { display:flex;align-items:flex-start;gap:1rem;padding:1.1rem 1.2rem 1rem; }
        .artefak-icon { width:42px;height:42px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.05rem;flex-shrink:0;margin-top:.1rem; }
        .artefak-info { flex:1; }
        .artefak-nama { font-size:.9rem;font-weight:700;color:#fff;margin-bottom:.25rem; }
        html[data-theme="light"] .artefak-nama { color:#1e293b; }
        .artefak-alasan { font-size:.82rem;line-height:1.6;color:var(--text-muted);margin:0; }
        html[data-theme="light"] .artefak-alasan { color:#475569; }

        /* Artefak footer row */
        .artefak-footer { display:flex;align-items:center;justify-content:space-between;padding:.75rem 1.2rem;background:rgba(0,0,0,.2);border-top:1px solid var(--glass-border);gap:1rem; }
        html[data-theme="light"] .artefak-footer { background:rgba(0,0,0,.04);border-top-color:rgba(0,0,0,.08); }
        .artefak-file { display:flex;align-items:center;gap:.6rem;min-width:0; }
        .artefak-filename { font-size:.8rem;font-weight:600;color:#fff;white-space:nowrap;overflow:hidden;text-overflow:ellipsis; }
        html[data-theme="light"] .artefak-filename { color:#1e293b; }
        .artefak-filetype { font-size:.68rem;color:var(--text-muted); }
        .artefak-actions { display:flex;gap:.5rem;flex-shrink:0; }

        /* Preview & Download buttons */
        .btn-preview, .btn-download {
            display:inline-flex;align-items:center;gap:.35rem;
            padding:.4rem .85rem;border-radius:8px;font-size:.78rem;font-weight:600;
            cursor:pointer;text-decoration:none;border:none;
            transition:all .18s ease;
        }
        .btn-preview {
            background:rgba(255,255,255,.08);
            color:#fff;
            border:1px solid rgba(255,255,255,.12);
        }
        .btn-preview:hover { background:var(--btn-color);border-color:var(--btn-color);color:#fff; }
        html[data-theme="light"] .btn-preview { background:rgba(0,0,0,.05);color:#334155;border-color:rgba(0,0,0,.12); }
        html[data-theme="light"] .btn-preview:hover { background:var(--btn-color);color:#fff;border-color:var(--btn-color); }

        .btn-download {
            background:var(--btn-color);
            color:#fff;
            border:1px solid transparent;
        }
        .btn-download:hover { filter:brightness(1.15); }

        /* ─── PDF Preview Modal ─── */
        .pdf-modal-overlay {
            display:none;position:fixed;inset:0;z-index:9999;
            background:rgba(0,0,0,.75);backdrop-filter:blur(6px);
            align-items:center;justify-content:center;padding:1rem;
        }
        .pdf-modal-overlay.open { display:flex; }

        .pdf-modal {
            background:#0f172a;
            border:1px solid rgba(255,255,255,.1);
            border-radius:18px;
            width:100%;max-width:900px;
            height:90vh;
            display:flex;flex-direction:column;
            overflow:hidden;
            box-shadow:0 30px 80px rgba(0,0,0,.6);
            animation:modalIn .25s cubic-bezier(.34,1.3,.64,1);
        }
        html[data-theme="light"] .pdf-modal { background:#f8fafc;border-color:rgba(0,0,0,.1); }

        @keyframes modalIn {
            from { opacity:0;transform:scale(.94) translateY(16px); }
            to   { opacity:1;transform:scale(1) translateY(0); }
        }

        .pdf-modal-header {
            display:flex;align-items:center;justify-content:space-between;
            padding:.9rem 1.2rem;
            border-bottom:1px solid rgba(255,255,255,.08);
            flex-shrink:0;
        }
        html[data-theme="light"] .pdf-modal-header { border-bottom-color:rgba(0,0,0,.08); }

        .pdf-modal-title {
            font-family:'Outfit',sans-serif;font-size:.95rem;font-weight:700;color:#fff;
            display:flex;align-items:center;gap:.5rem;
        }
        html[data-theme="light"] .pdf-modal-title { color:#1e293b; }
        .pdf-modal-title i { color:#f87171; }

        .pdf-modal-btns { display:flex;gap:.5rem; }

        .btn-modal-dl {
            display:inline-flex;align-items:center;gap:.4rem;
            padding:.4rem .9rem;border-radius:8px;font-size:.8rem;font-weight:600;
            background:${c.accent};color:#fff;text-decoration:none;
            transition:filter .15s;border:none;cursor:pointer;
        }
        .btn-modal-dl:hover { filter:brightness(1.15); }

        .btn-modal-close {
            display:inline-flex;align-items:center;justify-content:center;
            width:34px;height:34px;border-radius:8px;
            background:rgba(255,255,255,.08);color:#fff;
            border:1px solid rgba(255,255,255,.1);cursor:pointer;
            font-size:.95rem;transition:background .15s;
        }
        .btn-modal-close:hover { background:rgba(239,68,68,.2);color:#f87171;border-color:rgba(239,68,68,.3); }
        html[data-theme="light"] .btn-modal-close { background:rgba(0,0,0,.06);color:#334155;border-color:rgba(0,0,0,.1); }

        .pdf-modal-body { flex:1;position:relative;overflow:hidden; }

        .pdf-iframe {
            width:100%;height:100%;border:none;
            background:#fff;
        }

        /* Placeholder saat PDF belum diisi */
        .pdf-placeholder {
            display:flex;flex-direction:column;align-items:center;justify-content:center;
            height:100%;gap:1rem;
            color:var(--text-muted);text-align:center;padding:2rem;
        }
        .pdf-placeholder i { font-size:3rem;color:rgba(255,255,255,.15);margin-bottom:.5rem; }
        html[data-theme="light"] .pdf-placeholder i { color:rgba(0,0,0,.1); }
        .pdf-placeholder p { font-size:.9rem;line-height:1.6;max-width:340px; }
        .pdf-placeholder code { font-size:.78rem;background:rgba(255,255,255,.06);padding:.2rem .5rem;border-radius:4px;color:#818cf8; }
        html[data-theme="light"] .pdf-placeholder code { background:rgba(0,0,0,.06);color:#4338ca; }

        /* Kaitan Praktis */
        .kaitan-grid { display:grid;grid-template-columns:1fr 1fr;gap:1.2rem; }
        @media(max-width:600px){ .kaitan-grid{grid-template-columns:1fr;} }
        .kaitan-box { padding:1.3rem;border-radius:12px;background:rgba(0,0,0,.15);border:1px solid var(--glass-border); }
        html[data-theme="light"] .kaitan-box { background:rgba(0,0,0,.025);border-color:rgba(0,0,0,.08); }
        .kaitan-label { font-size:.7rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:${c.accent};margin-bottom:.75rem;display:flex;align-items:center;gap:.4rem; }
        .kaitan-text { font-size:.86rem;line-height:1.75;color:var(--text-muted);margin:0; }
        html[data-theme="light"] .kaitan-text { color:#475569; }
    </style>
</head>
<body>
    <div class="ambient-bg"><div class="blob blob-1"></div><div class="blob blob-2"></div><div class="blob blob-3"></div></div>

    <nav id="navbar">
        <a href="index.html" class="logo" style="display:flex;align-items:center;gap:12px;text-decoration:none;">
            <div style="display:flex;align-items:center;gap:8px;background:rgba(255,255,255,.95);padding:6px 12px;border-radius:50px;border:1px solid rgba(255,255,255,.2);box-shadow:0 4px 15px rgba(0,0,0,.15);">
                <img src="assets/images/Logo%20Kemdikdasmen.png" alt="Kemdikdasmen" style="height:28px;width:auto;object-fit:contain;display:block;">
                <img src="assets/images/Logo-UM.png" alt="UM" style="height:28px;width:auto;object-fit:contain;display:block;">
                <img src="assets/images/Logo%20PPG.png" alt="PPG" style="height:28px;width:auto;object-fit:contain;display:block;">
            </div>
            <span style="font-size:1.25rem;font-weight:700;color:#fff;font-family:'Outfit',sans-serif;">E-Portfolio PPG</span>
        </a>
        <ul class="nav-links">
            <li><a href="index.html">Home</a></li>
            <li class="dropdown">
                <a href="semester-1.html" class="dropbtn">Semester 1</a>
                <ul class="dropdown-content">
                    <li><a href="e-portfolio-1.html"><i class="fa-solid fa-folder-open" style="margin-right:6px;"></i>E-Portfolio 1</a></li>
                    <li><a href="e-portfolio-2.html"><i class="fa-solid fa-folder-open" style="margin-right:6px;"></i>E-Portfolio 2</a></li>
                </ul>
            </li>
            <li class="dropdown">
                <a href="semester-2.html" class="dropbtn">Semester 2</a>
                <ul class="dropdown-content">
                    <li><a href="profil-mahasiswa-s2.html"><i class="fa-solid fa-user" style="margin-right:6px;"></i>Profil Mahasiswa</a></li>
                    <li><a href="uts-ppl.html"><i class="fa-solid fa-file-pen" style="margin-right:6px;"></i>UTS PPL</a></li>
                    <li><a href="uas-ppl.html"><i class="fa-solid fa-file-circle-check" style="margin-right:6px;"></i>UAS PPL</a></li>
                    <li><a href="seminar.html"><i class="fa-solid fa-chalkboard-user" style="margin-right:6px;"></i>Seminar</a></li>
                </ul>
            </li>
            <li><a href="e-portfolio-2.html#dokumentasi">Dokumentasi</a></li>
            <li><button id="theme-toggle" class="theme-toggle-btn" aria-label="Toggle Theme"><i class="fa-solid fa-moon"></i></button></li>
        </ul>
        <button class="hamburger" id="hamburger-btn" aria-label="Buka Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </nav>

    <div class="mobile-nav-overlay" id="mobile-overlay"></div>
    <div class="mobile-nav-drawer" id="mobile-drawer">
        <a href="index.html"><i class="fa-solid fa-house" style="margin-right:.5rem;color:var(--primary-light);"></i> Home</a>
        <div class="mobile-nav-divider"></div>
        <button class="mobile-dropdown-toggle" data-target="mob-s1" onclick="window.location.href='semester-1.html'">
            <span><i class="fa-solid fa-folder-open" style="margin-right:.5rem;color:var(--secondary);"></i> Semester 1</span>
            <i class="fa-solid fa-chevron-down"></i>
        </button>
        <div class="mobile-submenu" id="mob-s1">
            <a href="e-portfolio-1.html">E-Portfolio 1</a>
            <a href="e-portfolio-2.html">E-Portfolio 2</a>
        </div>
        <button class="mobile-dropdown-toggle" data-target="mob-s2" onclick="window.location.href='semester-2.html'">
            <span><i class="fa-solid fa-folder" style="margin-right:.5rem;color:#10b981;"></i> Semester 2</span>
            <i class="fa-solid fa-chevron-down"></i>
        </button>
        <div class="mobile-submenu" id="mob-s2">
            <a href="profil-mahasiswa-s2.html"><i class="fa-solid fa-user" style="margin-right:6px;"></i> Profil Mahasiswa</a>
            <a href="uts-ppl.html"><i class="fa-solid fa-file-pen" style="margin-right:6px;"></i> UTS PPL</a>
            <a href="uas-ppl.html"><i class="fa-solid fa-file-circle-check" style="margin-right:6px;"></i> UAS PPL</a>
            <a href="seminar.html"><i class="fa-solid fa-chalkboard-user" style="margin-right:6px;"></i> Seminar</a>
        </div>
        <a href="e-portfolio-2.html#dokumentasi"><i class="fa-solid fa-images" style="margin-right:.5rem;color:var(--warning);"></i> Dokumentasi</a>
        <div class="mobile-nav-divider"></div>
        <div class="mobile-theme-row">
            <span><i class="fa-solid fa-circle-half-stroke" style="margin-right:.5rem;"></i> Mode Tampilan</span>
            <button id="theme-toggle-mobile" class="theme-toggle-btn" aria-label="Toggle Theme Mobile"><i class="fa-solid fa-moon"></i></button>
        </div>
    </div>

    <!-- ── PDF PREVIEW MODAL ── -->
    <div class="pdf-modal-overlay" id="pdfModal" onclick="handleModalClick(event)">
        <div class="pdf-modal" id="pdfModalBox">
            <div class="pdf-modal-header">
                <div class="pdf-modal-title">
                    <i class="fa-solid fa-file-pdf"></i>
                    <span id="pdfModalTitle">Dokumen</span>
                </div>
                <div class="pdf-modal-btns">
                    <a id="pdfModalDl" href="#" download class="btn-modal-dl">
                        <i class="fa-solid fa-download"></i> Unduh
                    </a>
                    <button class="btn-modal-close" onclick="closePreview()" title="Tutup">
                        <i class="fa-solid fa-xmark"></i>
                    </button>
                </div>
            </div>
            <div class="pdf-modal-body" id="pdfModalBody">
                <!-- diisi JS -->
            </div>
        </div>
    </div>

    <!-- ── MAIN CONTENT ── -->
    <div style="margin-top:130px;margin-bottom:6rem;">
        <div class="crs-wrap">

            <a href="seminar.html" class="back-link">
                <i class="fa-solid fa-arrow-left"></i> Kembali ke Seminar PPL
            </a>

            <div style="margin-bottom:2.5rem;">
                <div class="crs-badge"><i class="fa-solid ${c.icon}"></i> ${c.subtitle}</div>
                <h1 class="crs-title">${c.title}</h1>
                <p class="crs-subtitle">Refleksi 4C · Analisis Artefak · Kaitan Praktis — PPG Prajabatan Gelombang 1 · 2026</p>
                <hr class="crs-divider">
            </div>

            <!-- ─ REFLEKSI 4C ─ -->
            <div class="crs-section">
                <div class="sec-label">
                    <div class="sec-label-icon"><i class="fa-solid fa-rotate"></i></div>
                    <div><div class="sec-label-text">Refleksi 4C</div><div class="sec-label-sub">Connection · Challenge · Concept · Change</div></div>
                </div>
                <div class="c4-grid">
                    <div class="c4-card connection"><div class="c4-label"><i class="fa-solid fa-link"></i> Connection</div><p class="c4-text">${c.refleksi.connection}</p></div>
                    <div class="c4-card challenge"><div class="c4-label"><i class="fa-solid fa-bolt"></i> Challenge</div><p class="c4-text">${c.refleksi.challenge}</p></div>
                    <div class="c4-card concept"><div class="c4-label"><i class="fa-solid fa-lightbulb"></i> Concept</div><p class="c4-text">${c.refleksi.concept}</p></div>
                    <div class="c4-card change"><div class="c4-label"><i class="fa-solid fa-seedling"></i> Change</div><p class="c4-text">${c.refleksi.change}</p></div>
                </div>
            </div>

            <!-- ─ ANALISIS ARTEFAK ─ -->
            <div class="crs-section">
                <div class="sec-label">
                    <div class="sec-label-icon"><i class="fa-solid fa-magnifying-glass-chart"></i></div>
                    <div><div class="sec-label-text">Analisis Artefak</div><div class="sec-label-sub">Bukti dukung hasil refleksi pembelajaran · Klik Lihat untuk pratinjau atau Unduh untuk menyimpan</div></div>
                </div>
                <div class="artefak-list">
                    ${artefakCards}
                </div>
            </div>

            <!-- ─ KAITAN PRAKTIS ─ -->
            <div class="crs-section">
                <div class="sec-label">
                    <div class="sec-label-icon"><i class="fa-solid fa-compass-drafting"></i></div>
                    <div><div class="sec-label-text">Kaitan Praktis</div><div class="sec-label-sub">Konsep utama &amp; perubahan di masa depan</div></div>
                </div>
                <div class="kaitan-grid">
                    <div class="kaitan-box">
                        <div class="kaitan-label"><i class="fa-solid fa-book-open-reader"></i> Konsep Utama yang Dipelajari</div>
                        <p class="kaitan-text">${c.kaitan.konsep}</p>
                    </div>
                    <div class="kaitan-box">
                        <div class="kaitan-label"><i class="fa-solid fa-arrow-trend-up"></i> Perubahan di Masa Depan</div>
                        <p class="kaitan-text">${c.kaitan.perubahan}</p>
                    </div>
                </div>
            </div>

        </div>
    </div>

    <footer>
        <div class="container">
            <h3 style="font-family:'Outfit',sans-serif;font-size:1.5rem;margin-bottom:1rem;">E-Portfolio Pendidikan Profesi Guru</h3>
            <p>&copy; 2026 Disusun untuk memenuhi komponen penilaian PPL.</p>
            <p style="margin-top:.5rem;font-size:.9rem;color:rgba(255,255,255,.3);">Lutfi Subekti &nbsp;·&nbsp; PPG Prajabatan Gelombang 1 &nbsp;·&nbsp; Universitas Negeri Malang</p>
        </div>
    </footer>

    <script>
        /* ─── Theme ─── */
        const themeToggle = document.getElementById('theme-toggle');
        const htmlEl = document.documentElement;
        const icon = themeToggle.querySelector('i');
        const savedTheme = localStorage.getItem('theme');
        function applyTheme(t) {
            if (t === 'light') { htmlEl.setAttribute('data-theme','light'); icon.classList.replace('fa-moon','fa-sun'); }
            else { htmlEl.removeAttribute('data-theme'); icon.classList.replace('fa-sun','fa-moon'); }
        }
        applyTheme(savedTheme || 'dark');
        themeToggle.addEventListener('click', () => {
            const newT = htmlEl.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
            localStorage.setItem('theme', newT); applyTheme(newT);
        });
        const tmm = document.getElementById('theme-toggle-mobile');
        if (tmm) {
            const mi = tmm.querySelector('i');
            if (savedTheme === 'light') mi.classList.replace('fa-moon','fa-sun');
            tmm.addEventListener('click', () => { themeToggle.click(); const d = !htmlEl.hasAttribute('data-theme'); mi.classList.toggle('fa-moon',d); mi.classList.toggle('fa-sun',!d); });
        }

        /* ─── Navbar ─── */
        window.addEventListener('scroll', () => document.getElementById('navbar').classList.toggle('scrolled', window.scrollY > 50));
        const hBtn = document.getElementById('hamburger-btn'), mD = document.getElementById('mobile-drawer'), mO = document.getElementById('mobile-overlay');
        const openD  = () => { hBtn.classList.add('open'); hBtn.setAttribute('aria-expanded','true'); mD.classList.add('open'); mO.classList.add('active'); document.body.style.overflow='hidden'; };
        const closeD = () => { hBtn.classList.remove('open'); hBtn.setAttribute('aria-expanded','false'); mD.classList.remove('open'); mO.classList.remove('active'); document.body.style.overflow=''; };
        hBtn.addEventListener('click', () => mD.classList.contains('open') ? closeD() : openD());
        mO.addEventListener('click', closeD);
        document.querySelectorAll('.mobile-dropdown-toggle').forEach(btn => {
            btn.addEventListener('click', () => {
                const sub = document.getElementById(btn.dataset.target), was = btn.classList.contains('open');
                document.querySelectorAll('.mobile-dropdown-toggle').forEach(b => b.classList.remove('open'));
                document.querySelectorAll('.mobile-submenu').forEach(m => m.classList.remove('open'));
                if (!was) { btn.classList.add('open'); sub.classList.add('open'); }
            });
        });
        mD.querySelectorAll('a').forEach(l => l.addEventListener('click', closeD));

        /* ─── PDF Preview Modal ─── */
        const modal      = document.getElementById('pdfModal');
        const modalTitle = document.getElementById('pdfModalTitle');
        const modalDl    = document.getElementById('pdfModalDl');
        const modalBody  = document.getElementById('pdfModalBody');

        function openPreview(pdfPath, title) {
            modalTitle.textContent = title;
            modalDl.href = pdfPath;
            modalDl.download = title + '.pdf';

            // Cek apakah file path masih placeholder
            if (!pdfPath || pdfPath.endsWith('#') || pdfPath === '') {
                modalBody.innerHTML = \`
                    <div class="pdf-placeholder">
                        <i class="fa-solid fa-file-pdf"></i>
                        <p>Dokumen belum tersedia.<br>Tambahkan file PDF ke:</p>
                        <code>\${pdfPath}</code>
                    </div>\`;
            } else {
                modalBody.innerHTML = \`<iframe class="pdf-iframe" src="\${pdfPath}" title="\${title}"></iframe>\`;
            }

            modal.classList.add('open');
            document.body.style.overflow = 'hidden';
        }

        function closePreview() {
            modal.classList.remove('open');
            modalBody.innerHTML = '';
            document.body.style.overflow = '';
        }

        function handleModalClick(e) {
            if (e.target === modal) closePreview();
        }

        document.addEventListener('keydown', e => { if (e.key === 'Escape') closePreview(); });
    </script>
    <script src="dropdown.js"></script>
</body>
</html>`;
}

// ─── Generate semua file ───
courses.forEach(c => {
    const dest = path.join(BASE, c.file);
    fs.writeFileSync(dest, buildPage(c), 'utf8');
    console.log('✅ Written:', c.file);
});
console.log('\nSemua halaman berhasil diperbarui dengan fitur Preview & Download!');
