# -*- coding: utf-8 -*-
"""
build_course_pages.py
Menghasilkan seluruh halaman mata kuliah seminar dengan 5 tab interaktif:
1. Refleksi 4C
2. Analisis Artefak
3. Hasil Refleksi
4. Lembar Refleksi
5. Tugas Perkuliahan (dengan Sidebar Daftar Isi & Alur Topik)
"""

import json
import os
import re

with open('parsed_refleksi.json', 'r', encoding='utf-8') as f:
    ref_data = json.load(f)

def clean_val(v):
    if not v:
        return ''
    m = re.search(r'[\x00-\x1f\x7f-\xff]{4,}', v)
    c = v[:m.start()].strip() if m else v.strip()
    c = re.sub(r'\s+', ' ', c)
    return c

# Configuration for all courses
courses = [
    # 1. Filosofi Pendidikan
    {
        'id': 'filosofi',
        'file': 'course-filosofi.html',
        'badge': 'REFLEKSI PENGALAMAN BELAJAR',
        'title': 'Filosofi Pendidikan dan Pendidikan Nilai',
        'short_title': 'Filosofi Pendidikan dan Pendidikan Nilai',
        'subtitle': 'Refleksi pengalaman belajar mata kuliah Filosofi Pendidikan dan Pendidikan Nilai melalui kerangka 4C (Connection, Challenge, Concept, Change), analisis artefak pembelajaran, serta perumusan hasil refleksi.',
        'theme_color': '#10b981',
        'theme_gradient': 'linear-gradient(135deg, #c084fc, #f472b6, #e879f9)',
        'ref_pdf': 'assets/docs/Refleksi Mata Kuliah/Refleksi FILOSOFI PENDIDIKAN DAN PENDIDIKAN NILAI.pdf',
        'ref_key': 'Refleksi FILOSOFI PENDIDIKAN DAN PENDIDIKAN NILAI.pdf',
        'custom_q': {},
        'artefak_items': [
            {
                'nama': 'Tabel Connect-Extend-Challenge Pendidikan Nilai',
                'deskripsi': 'Analisis peran guru dalam pendidikan nilai, menghubungkan pengalaman lampau dengan lima peran strategis pendidik nilai.',
                'tipe': 'Lembar Analisis',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi FILOSOFI PENDIDIKAN DAN PENDIDIKAN NILAI.pdf'
            },
            {
                'nama': 'Komitmen Pribadi Calon Guru Profesional',
                'deskripsi': 'Rumusan komitmen konkret mengenai tanggung jawab moral, keteladanan, pembiasaan budaya positif, dan refleksi diri berkelanjutan.',
                'tipe': 'Dokumen Reflektif',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi FILOSOFI PENDIDIKAN DAN PENDIDIKAN NILAI.pdf'
            },
            {
                'nama': 'Hasil Diskusi 4Cs Pendidikan Karakter Siswa',
                'deskripsi': 'Dokumentasi pemikiran kelompok mengenai pendidikan moral dan karakter ditinjau dari perspektif kebutuhan peserta didik.',
                'tipe': 'Artefak Kolaboratif',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi FILOSOFI PENDIDIKAN DAN PENDIDIKAN NILAI.pdf'
            },
            {
                'nama': 'Refleksi Kritis Kasus Sokola Rimba Butet Manurung',
                'deskripsi': 'Analisis "I Used to Think..., Now I Think..." sebagai titik balik pergeseran paradigma dari guru teknis ke pendidik humanis.',
                'tipe': 'Kajian Kasus Kontekstual',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi FILOSOFI PENDIDIKAN DAN PENDIDIKAN NILAI.pdf'
            }
        ],
        'topik_list': [
            {
                'no': 1,
                'judul': 'Perjalanan Pendidikan Nasional',
                'deskripsi': 'Menelusuri sejarah pendidikan Indonesia dari era kolonial hingga kemerdekaan, serta pemikiran pembebasan Ki Hadjar Dewantara.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi pengalaman bersekolah dan persepsi awal tentang profesi pendidik', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Kajian historis pergerakan pendidikan nasional dan politik etis kolonial', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Diskusi kelompok mengenai potret pendidikan zaman kolonial vs masa kini', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Infografis garis waktu perjalanan pendidikan nasional dan tokoh pendidik', 'status': 'Selesai'},
                    {'alur': 'Koneksi Antarmateri', 'tugas': 'Keterkaitan filosofi Ki Hadjar Dewantara dengan kurikulum merdeka saat ini', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Pernyataan komitmen pribadi sebagai guru penggerak perubahan', 'status': 'Selesai'}
                ]
            },
            {
                'no': 2,
                'judul': 'Dasar-Dasar Pendidikan Ki Hadjar Dewantara',
                'deskripsi': 'Memahami konsep sistem Among, kodrat alam dan zaman, serta hakikat menuntun segala kodrat anak menuju keselamatan dan kebahagiaan.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Eksplorasi pandangan pribadi tentang makna kata "menuntun" dalam mengajar', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Telaah asas Trikon, kodrat alam & kodrat zaman, serta konsep budi pekerti', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Analisis sosiodrama penerapan sistem Among di lingkungan sekolah', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Video penjelasan metafora petani dan benih padi Ki Hadjar Dewantara', 'status': 'Selesai'},
                    {'alur': 'Koneksi Antarmateri', 'tugas': 'Sintesis pemikiran KHD dengan tantangan pendidikan abad ke-21', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Rancangan strategi pembelajaran yang menghargai keunikan kodrat siswa', 'status': 'Selesai'}
                ]
            },
            {
                'no': 3,
                'judul': 'Identitas Manusia Indonesia',
                'deskripsi': 'Kajian filosofis antropologis mengenai kebhinnekaan, nilai pancasila, dan religiusitas sebagai pilar jati diri manusia Indonesia.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi pengalaman hidup dalam keberagaman budaya dan suku bangsa', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Tiga pilar identitas manusia Indonesia: Kebhinnekatunggalikaan, Pancasila, Religiusitas', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Diskusi penguatan nilai-nilai luhur budaya lokal dalam pembelajaran', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Esai reflektif tentang melestarikan kearifan lokal di ruang kelas', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Integrasi konten kearifan lokal dalam rancangan kegiatan belajar Informatika', 'status': 'Selesai'}
                ]
            },
            {
                'no': 4,
                'judul': 'Pancasila sebagai Entitas dan Karakter Bangsa',
                'deskripsi': 'Menginternalisasi Profil Pelajar Pancasila ke dalam pembelajaran kontekstual dan ekosistem pendidikan sekolah.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Identifikasi implementasi sila-sila Pancasila dalam keseharian sekolah', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Enam dimensi Profil Pelajar Pancasila sebagai kompas moral peserta didik', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Penyusunan proyek mini penguatan profil pelajar pancasila', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Poster komparasi nilai Pancasila dengan tantangan globalisasi digital', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Lembar observasi pembiasaan nilai karakter Pancasila di kelas', 'status': 'Selesai'}
                ]
            },
            {
                'no': 5,
                'judul': 'Praktik Baik Pendidikan yang Memerdekakan',
                'deskripsi': 'Merumuskan implementasi nyata filosofi pendidikan memerdekakan dalam praktik mengajar di sekolah mitra PPL.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi batas-batas kebebasan belajar yang berkeadilan bagi peserta didik', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Prinsip pembelajaran yang memerdekakan cipta, rasa, dan karsa peserta didik', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Benchmarking praktik baik pembelajaran memerdekakan antar kelompok PPL', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Portofolio rancangan pembelajaran kontekstual berpusat pada murid', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Penerapan modul pembelajaran memerdekakan saat praktik mengajar di SMPN 8 Malang', 'status': 'Selesai'}
                ]
            }
        ]
    },

    # 2. Computational Thinking
    {
        'id': 'ct',
        'file': 'course-ct.html',
        'badge': 'REFLEKSI PENGALAMAN BELAJAR',
        'title': 'Computational Thinking',
        'short_title': 'Computational Thinking',
        'subtitle': 'Refleksi pengalaman belajar mata kuliah Computational Thinking melalui kerangka 4C (Connection, Challenge, Concept, Change), analisis artefak pembelajaran, serta perumusan hasil refleksi.',
        'theme_color': '#0d9488',
        'theme_gradient': 'linear-gradient(135deg, #38bdf8, #818cf8, #c084fc)',
        'ref_pdf': 'assets/docs/Refleksi Mata Kuliah/Refleksi COMPUTATIONAL THINKING.pdf',
        'ref_key': 'Refleksi COMPUTATIONAL THINKING.pdf',
        'custom_q': {},
        'artefak_items': [
            {
                'nama': 'Lembar Kerja L.K.1.1 Pendalaman Pemahaman CT',
                'deskripsi': 'Eksplorasi konseptual penerapan 4 fondasi berpikir komputasional dalam menyelesaikan masalah sehari-hari dan sains.',
                'tipe': 'Lembar Analisis Konsep',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi COMPUTATIONAL THINKING.pdf'
            },
            {
                'nama': 'Analisis Soal Tantangan Bebras & AKM',
                'deskripsi': 'Analisis dekonstruksi dan pengenalan pola pada soal-soal berpikir komputasional internasional Bebras untuk tingkat SMP.',
                'tipe': 'Instrumen Pemecahan Masalah',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi COMPUTATIONAL THINKING.pdf'
            },
            {
                'nama': 'Rancangan Proyek Pembelajaran CT Terintegrasi STEAM',
                'deskripsi': 'Modul unit aktivitas plugged dan unplugged Informatika yang menanamkan cara bernalar terstruktur pada peserta didik.',
                'tipe': 'Rencana Pembelajaran Inovatif',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi COMPUTATIONAL THINKING.pdf'
            }
        ],
        'topik_list': [
            {
                'no': 1,
                'judul': 'Pendalaman Pemahaman Computational Thinking',
                'deskripsi': 'Mendalami 4 pilar dasar CT (Dekomposisi, Pengenalan Pola, Abstraksi, Algoritma) sebagai fondasi bernalar pemecahan masalah.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi pengalaman problem solving menggunakan logika komputasi', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Kajian 4 pilar CT dan penerapannya di luar dunia pemrograman komputer', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Diskusi pemecahan kasus kompleks menggunakan dekomposisi dan abstraksi', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Presentasi solusi algoritma pemecahan masalah sampah sekolah', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Menyusun mindmap 4 pilar CT untuk panduan belajar peserta didik', 'status': 'Selesai'}
                ]
            },
            {
                'no': 2,
                'judul': 'CT dalam Kurikulum & Problem Solving',
                'deskripsi': 'Integrasi berpikir komputasional ke dalam Capaian Pembelajaran (CP) Informatika dan literasi numerasi lintas disiplin.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Pemetaan elemen CT dalam Capaian Pembelajaran Kurikulum Merdeka', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Bedah kurikulum Informatika fase D (SMP) berbasis computational thinking', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Merancang aktivitas unplugged CT untuk materi sistem komputer', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Simulasi pembelajaran plugged menggunakan Scratch dan visual block', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Modul ajar terintegrasi elemen berpikir komputasional', 'status': 'Selesai'}
                ]
            },
            {
                'no': 3,
                'judul': 'CT dalam Menyelesaikan Soal Bebras & PISA',
                'deskripsi': 'Melatih penalaran komputasional peserta didik melalui telaah soal tantangan Bebras, PISA, dan asesmen kompetensi minimum.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Mencoba menyelesaikan soal Bebras kategori Benjamins dan Kadets', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Analisis tingkat kognitif dan pilar CT dominan pada soal Bebras', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Penyusunan rubrik analisis kesalahan bernalar peserta didik pada soal Bebras', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Kartu tantangan soal CT bertingkat (mudah, sedang, menantang)', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Uji coba bank soal Bebras dalam kegiatan kokurikuler siswa SMP', 'status': 'Selesai'}
                ]
            },
            {
                'no': 4,
                'judul': 'CT dan Proyek Pembelajaran STEAM',
                'deskripsi': 'Merancang proyek kolaboratif berbasis Science, Technology, Engineering, Arts, dan Mathematics berlandaskan CT.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Eksplorasi keterkaitan seni grafis dan pemrograman visual', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Kerangka integrasi STEAM dengan pemikiran algoritma', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Desain proyek robotika simulasi berbasis Arduino / micro:bit', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Prototipe proyek lampu otomatis ramah energi', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Laporan evaluasi proyek STEAM terintegrasi CT di kelas PPL', 'status': 'Selesai'}
                ]
            },
            {
                'no': 5,
                'judul': 'Integrasi CT dalam Mata Pelajaran Informatika',
                'deskripsi': 'Implementasi terpadu pembelajaran CT pada modul ajar analisis data, algoritma pemrograman, dan dampak sosial informatika.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi tantangan mengajarkan logika pemrograman bagi pemula', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Metode scaffolding dalam mengajarkan algoritma sekuensial dan percabangan', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Peer-teaching microteaching modul ajar analisis data berbantuan spreadsheet', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Video pelaksanaan pembelajaran CT di laboratorium komputer', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Refleksi komprehensif implementasi CT di SMP Negeri 8 Malang', 'status': 'Selesai'}
                ]
            }
        ]
    },

    # 3. Pemahaman Peserta Didik
    {
        'id': 'pemahaman',
        'file': 'course-pemahaman.html',
        'badge': 'REFLEKSI PENGALAMAN BELAJAR',
        'title': 'Pemahaman Tentang Peserta Didik dan Pembelajaran',
        'short_title': 'Pemahaman Peserta Didik dan Pembelajaran',
        'subtitle': 'Refleksi pengalaman belajar mata kuliah Pemahaman Tentang Peserta Didik dan Pembelajaran melalui kerangka 4C, analisis artefak pembelajaran, serta perumusan hasil refleksi.',
        'theme_color': '#e11d48',
        'theme_gradient': 'linear-gradient(135deg, #fb7185, #f43f5e, #fda4af)',
        'ref_pdf': 'assets/docs/Refleksi Mata Kuliah/Refleksi PEMAHAMAN TENTANG PESERTA DIDIK DAN PEMBELAJARAN.pdf',
        'ref_key': 'Refleksi PEMAHAMAN TENTANG PESERTA DIDIK DAN PEMBELAJARAN.pdf',
        'custom_q': {},
        'artefak_items': [
            {
                'nama': 'Lembar Kerja L.K. 2a Profiling Karakteristik Peserta Didik',
                'deskripsi': 'Instrumen observasi dan pemetaan aspek etnik, sosial, emosional, minat, dan gaya belajar 32 siswa kelas VIII SMPN 8 Malang.',
                'tipe': 'Instrumen Profiling Siswa',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi PEMAHAMAN TENTANG PESERTA DIDIK DAN PEMBELAJARAN.pdf'
            },
            {
                'nama': 'Format Asesmen Diagnostik Kognitif & Non-Kognitif',
                'deskripsi': 'Panduan wawancara dan angket diagnostik awal untuk memetakan kesiapan belajar (readiness) dan modalitas belajar siswa.',
                'tipe': 'Instrumen Asesmen Awal',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi PEMAHAMAN TENTANG PESERTA DIDIK DAN PEMBELAJARAN.pdf'
            },
            {
                'nama': 'Sintesis dan Rumusan Strategi Pembelajaran Berdiferensiasi',
                'deskripsi': 'Rancangan modifikasi proses, konten, dan produk pembelajaran yang responsif terhadap keberagaman karakteristik peserta didik.',
                'tipe': 'Strategi Pedagogis Responsif',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi PEMAHAMAN TENTANG PESERTA DIDIK DAN PEMBELAJARAN.pdf'
            }
        ],
        'topik_list': [
            {
                'no': 1,
                'judul': 'Teori Belajar dan Motivasi Belajar Peserta Didik',
                'deskripsi': 'Mempelajari teori behavioristik, kognitif, konstruktivistik, dan humanistik untuk membangkitkan motivasi intrinsik siswa.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi pengalaman motivasi belajar pribadi saat usia remaja', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Komparasi 4 teori belajar utama dan implikasinya dalam mendesain kelas', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Studi kasus siswa pasif dan rancangan intervensi berbasis konstruktivisme', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Desain strategi penguatan motivasi otonom berbasis Self-Determination Theory', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Penerapan reward non-material dan umpan balik motivasional di kelas', 'status': 'Selesai'}
                ]
            },
            {
                'no': 2,
                'judul': 'Teori Perkembangan Kognitif, Emosi, dan Sosial',
                'deskripsi': 'Memahami tahapan perkembangan Piaget, Vygotsky (ZPD), dan Erikson pada anak usia sekolah menengah.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Pemetaan karakteristik psikologis siswa usia SMP (12-15 tahun)', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Kajian Zona Perkembangan Proksimal (ZPD) dan teknik perancah (scaffolding)', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Analisis video interaksi sosial dan dinamika kelompok siswa remaja', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Panduan observasi perkembangan sosial emosional siswa di sekolah', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Laporan profiling perkembangan kognitif siswa kelas PPL', 'status': 'Selesai'}
                ]
            },
            {
                'no': 3,
                'judul': 'Profiling Peserta Didik dan Asesmen Diagnostik',
                'deskripsi': 'Teknik pengumpulan data karakteristik murid melalui tes diagnostik, angket minat, observasi kelas, dan wawancara.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi kebiasaan mengajar guru yang sering mengabaikan titik awal murid', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Metodologi profiling: instrumen kognitif vs non-kognitif', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Pengolahan dan kategorisasi data profiling menjadi 3 kelompok kesiapan', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Infografis profil kelas VIII-A SMPN 8 Malang', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Pemanfaatan data profil untuk pembentukan kelompok heterogen', 'status': 'Selesai'}
                ]
            },
            {
                'no': 4,
                'judul': 'Kerangka Pembelajaran Responsif Kultur (CRT) & TaRL',
                'deskripsi': 'Merancang pembelajaran yang berakar pada budaya lokal (Culturally Responsive) dan tingkat kemampuan nyata (Teaching at the Right Level).',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Identifikasi kekayaan budaya Malang dan sekitarnya yang relevan dengan pembelajaran', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Prinsip CRT: self-awareness, validating cultural identity, comprehensive learning', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Modifikasi modul ajar dengan memasukkan konteks budaya Jawa Timur', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Simulasi pembelajaran berbasis level kemampuan siswa (TaRL)', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Praktik mengajar berdiferensiasi CRT pada mata pelajaran Informatika', 'status': 'Selesai'}
                ]
            },
            {
                'no': 5,
                'judul': 'Pengukuran Pemahaman Belajar dan Evaluasi Berkelanjutan',
                'deskripsi': 'Mengevaluasi efektivitas diferensiasi pembelajaran melalui asesmen formatif berkelanjutan dan tindak lanjut reflektif.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi efektivitas metode asesmen konvensional', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Perancangan lembar refleksi diri siswa (exit ticket, self-assessment)', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Analisis hasil belajar siswa pasca penerapan diferensiasi', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Laporan komparatif capaian belajar sebelum dan sesudah intervensi', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Dokumen tindak lanjut dan rekomendasi bimbingan individual siswa', 'status': 'Selesai'}
                ]
            }
        ]
    },

    # 4. Pembelajaran Mendalam dan Asesmen Dasar
    {
        'id': 'pembelajaran',
        'file': 'course-pembelajaran.html',
        'badge': 'REFLEKSI PENGALAMAN BELAJAR',
        'title': 'Pembelajaran Mendalam dan Asesmen Dasar',
        'short_title': 'Pembelajaran Mendalam dan Asesmen Dasar',
        'subtitle': 'Refleksi pengalaman belajar mata kuliah Pembelajaran Mendalam dan Asesmen Dasar (PMA Dasar) melalui kerangka 4C, analisis artefak pembelajaran, serta perumusan hasil refleksi.',
        'theme_color': '#3b82f6',
        'theme_gradient': 'linear-gradient(135deg, #60a5fa, #818cf8, #a78bfa)',
        'ref_pdf': 'assets/docs/Refleksi Mata Kuliah/Refleksi PEMBELAJARAN MENDALAM DAN ASESMEN DASAR.pdf',
        'ref_key': 'Refleksi PEMBELAJARAN MENDALAM DAN ASESMEN DASAR.pdf',
        'custom_q': {
            'q3': 'a. Tiga prinsip pembelajaran mendalam: berkesadaran (murid sadar apa, mengapa, dan bagaimana ia belajar), bermakna (dikaitkan dengan konteks nyata kehidupan), dan menyenangkan (menumbuhkan rasa ingin tahu dan kegembiraan belajar).<br>b. Kerangka Backward Design (Understanding by Design - UbD): merumuskan tujuan pemahaman, menentukan bukti asesmen, baru kemudian merancang langkah instruksional.'
        },
        'artefak_items': [
            {
                'nama': 'Infografis LK 1D: Pembelajaran Mendalam & Prinsip UbD',
                'deskripsi': 'Ringkasan visual komprehensif mengenai 3 prinsip pembelajaran mendalam (berkesadaran, bermakna, menyenangkan) dan alur Backward Design.',
                'tipe': 'Infografis Desain Kurikulum',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi PEMBELAJARAN MENDALAM DAN ASESMEN DASAR.pdf'
            },
            {
                'nama': 'Modul Ajar Informatika Berbasis Understanding by Design (UbD)',
                'deskripsi': 'Perancangan rencana pembelajaran yang dimulai dari penetapan bukti asesmen tujuan sebelum menentukan langkah aktivitas kelas.',
                'tipe': 'Modul Ajar Terstruktur',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi PEMBELAJARAN MENDALAM DAN ASESMEN DASAR.pdf'
            },
            {
                'nama': 'Rubrik Penilaian Kinerja Asesmen Autentik',
                'deskripsi': 'Instrumen penilaian berbasis kriteria untuk mengukur kemampuan analisis dan pemecahan masalah siswa dalam tugas Informatika.',
                'tipe': 'Instrumen Penilaian Kinerja',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi PEMBELAJARAN MENDALAM DAN ASESMEN DASAR.pdf'
            }
        ],
        'topik_list': [
            {
                'no': 1,
                'judul': 'Pendekatan Understanding by Design (UbD)',
                'deskripsi': 'Mempelajari 3 tahap Backward Design: menetapkan hasil belajar, menentukan bukti penilaian, dan merencanakan pengalaman belajar.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi kelemahan perencanaan mengajar "forward design" yang berpusat pada materi', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Konsep Big Ideas dan Essential Questions yang memicu pemikiran mendalam', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Merumuskan 6 faset pemahaman (menjelaskan, menafsirkan, menerapkan, dll)', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Rancangan alur UbD untuk topik Analisis Data Informatika', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Penyusunan modul ajar berbasis kerangka Backward Design', 'status': 'Selesai'}
                ]
            },
            {
                'no': 2,
                'judul': 'Prinsip-Prinsip Asesmen Autentik',
                'deskripsi': 'Menggeser proporsi penilaian ke Assessment FOR dan AS Learning, mengurangi dominasi tes hafalan pilihan ganda.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi pengalaman menghadapi ujian hafalan yang cepat terlupakan', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Pembedaan asesmen awal, formatif harian, dan sumatif bermakna', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Penyusunan rubrik penilaian unjuk kerja analisis data menggunakan spreadsheet', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Penerapan kartu ceklis observasi formatif selama kegiatan praktikum', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Uji coba instrumen asesmen formatif teman sebaya (peer-assessment)', 'status': 'Selesai'}
                ]
            },
            {
                'no': 3,
                'judul': 'Perancangan Modul Ajar Berdiferensiasi',
                'deskripsi': 'Menyelaraskan tujuan pembelajaran dengan variasi modalitas belajar peserta didik di laboratorium komputer.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Analisis kebutuhan variasi media pembelajaran bagi siswa visual dan kinestetik', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Prinsip fleksibilitas waktu, tingkat kesulitan tugas, dan pilihan topik proyek', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Perancangan LKPD bertingkat (Tiered Assignment) sesuai kesiapan siswa', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Simulasi microteaching diferensiasi proses di laboratorium komputer', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Implementasi modul ajar berdiferensiasi pada siklus 1 PPL', 'status': 'Selesai'}
                ]
            },
            {
                'no': 4,
                'judul': 'Evaluasi Pelaksanaan dan Analisis Hasil Asesmen',
                'deskripsi': 'Menganalisis pola kesalahan siswa (error analysis) sebagai bahan perbaikan strategi instruksional dan umpan balik formatif.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi cara guru memberikan feedback: koreksi nilai vs umpan balik bermakna', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Teknik analisis butir soal dan pemetaan miskonsepsi rumus logika', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Diskusi merancang program remedial berbasis bimbingan sejawat', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Penyusunan laporan analisis hasil asesmen formatif siklus PPL', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Pemberian feedback deskriptif personal pada lembar kerja siswa', 'status': 'Selesai'}
                ]
            },
            {
                'no': 5,
                'judul': 'Refleksi dan Rencana Tindak Lanjut Pembelajaran',
                'deskripsi': 'Menyusun siklus perbaikan mutu pembelajaran berkelanjutan berdasarkan data asesmen dan jurnal reflektif pendidik.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Menulis jurnal refleksi mingguan selama praktik mengajar mandiri', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Model refleksi ALACT dan siklus perbaikan kualitas pengajaran', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Focus Group Discussion bersama Dosen Pembimbing Lapangan dan Guru Pamong', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Penyusunan rencana tindak lanjut (RTL) pembelajaran siklus 2', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Kompilasi portofolio kemajuan belajar siswa selama satu semester', 'status': 'Selesai'}
                ]
            }
        ]
    },

    # 5. Pembelajaran Mendalam dan Asesmen Lanjutan
    {
        'id': 'pembelajaran-lanjutan',
        'file': 'course-pembelajaran-lanjutan.html',
        'badge': 'REFLEKSI PENGALAMAN BELAJAR',
        'title': 'Pembelajaran Mendalam dan Asesmen Lanjutan',
        'short_title': 'Pembelajaran Mendalam dan Asesmen Lanjutan',
        'subtitle': 'Refleksi pengalaman belajar mata kuliah Pembelajaran Mendalam dan Asesmen Lanjutan (PMA Lanjutan) melalui kerangka 4C, analisis artefak pembelajaran, serta perumusan hasil refleksi.',
        'theme_color': '#4338ca',
        'theme_gradient': 'linear-gradient(135deg, #818cf8, #6366f1, #4f46e5)',
        'ref_pdf': 'assets/docs/Refleksi Mata Kuliah/Refleksi PEMBELAJARAN MENDALAM DAN ASESMEN LANJUTAN.pdf',
        'ref_key': 'Refleksi PEMBELAJARAN MENDALAM DAN ASESMEN LANJUTAN.pdf',
        'custom_q': {
            'q3': 'a. Asesmen awal kognitif dan non-kognitif dengan tiga instrumen utama: tes diagnostik, pedoman observasi perilaku, dan wawancara eksploratif.<br>b. Profiling komprehensif peserta didik untuk memetakan kesiapan belajar (readiness), gaya belajar, dan minat spesifik siswa.<br>c. Perancangan diferensiasi instruksional berkelanjutan untuk memastikan perlakuan pedagogis yang tepat sasaran.'
        },
        'artefak_items': [
            {
                'nama': 'Paket Lembar Kerja LK 1C: Asesmen Awal & Profiling Siswa',
                'deskripsi': 'Instrumen asesmen awal diagnostik, pemetaan kebutuhan belajar, dan pengelompokan tingkat pemahaman siswa kelas PPL di SMPN 8 Malang.',
                'tipe': 'Perangkat Asesmen Autentik Kelompok',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi PEMBELAJARAN MENDALAM DAN ASESMEN LANJUTAN.pdf'
            },
            {
                'nama': 'Panduan Wawancara & Observasi Karakteristik Siswa',
                'deskripsi': 'Pedoman pengumpulan data kualitatif minat dan hambatan belajar siswa untuk mendukung perancangan diferensiasi proses.',
                'tipe': 'Instrumen Observasi Lapangan',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi PEMBELAJARAN MENDALAM DAN ASESMEN LANJUTAN.pdf'
            },
            {
                'nama': 'Modul Ajar Pembelajaran Mendalam Lanjutan (Siklus 2)',
                'deskripsi': 'Modul ajar yang mengintegrasikan hasil analisis error siswa siklus 1 ke dalam scaffolding bertahap tugas praktikum Informatika.',
                'tipe': 'Modul Pembelajaran Lanjutan',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi PEMBELAJARAN MENDALAM DAN ASESMEN LANJUTAN.pdf'
            }
        ],
        'topik_list': [
            {
                'no': 1,
                'judul': 'Pendalaman Asesmen Awal Kognitif & Non-Kognitif',
                'deskripsi': 'Menguasai perancangan dan validasi instrumen asesmen diagnostik terstandar untuk memetakan titik mula belajar murid.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi urgensi data asesmen awal sebelum melangkah ke perencanaan kurikulum', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Kajian instrumen tes, lembar observasi partisipatif, dan protokol wawancara', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Penyusunan instrumen gabungan asesmen awal kelompok mahasiswa PPL', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Uji coba instrumen profiling pada sampel peserta didik di SMPN 8 Malang', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Laporan pemetaan kesiapan belajar dan tindak lanjut instruksional', 'status': 'Selesai'}
                ]
            },
            {
                'no': 2,
                'judul': 'Profiling Karakteristik & Pemetaan Kebutuhan Belajar',
                'deskripsi': 'Menganalisis hasil profiling secara kuantitatif dan kualitatif untuk mengelompokkan siswa ke dalam zona perkembangan proksimal.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Audit tantangan mengolah data profiling 32 siswa dalam satu rombel', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Metode triangulasi data hasil tes, angket minat, dan observasi pamong', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Penyusunan matriks diferensiasi berdasarkan kesiapan belajar siswa', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Dashboard visual profil belajar siswa berbasis spreadsheet', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Penerapan kelompok heterogen terarah pada pembelajaran praktikum', 'status': 'Selesai'}
                ]
            },
            {
                'no': 3,
                'judul': 'Perancangan Modul Ajar Berdiferensiasi Lanjutan',
                'deskripsi': 'Mengembangkan modul ajar dengan variasi penugasan bertingkat dan diferensiasi produk akhir proyek informatika.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi kelemahan tugas seragam yang membuat siswa mahir bosan dan siswa lemah frustrasi', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Strategi diferensiasi konten (bahan bacaan/video), proses (bimbingan langsung), dan produk', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Perancangan lembar kerja berjenjang (Tiered Worksheet) topik algoritma', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Simulasi pembelajaran berdiferensiasi di ruang multimedia', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Praktik mengajar mandiri siklus lanjutan berlandaskan profiling', 'status': 'Selesai'}
                ]
            },
            {
                'no': 4,
                'judul': 'Pelaksanaan Asesmen Formatif Autentik & Rubrik Berbasis Kriteria',
                'deskripsi': 'Menerapkan rubrik analitik untuk memantau kemajuan berpikir komputasional siswa secara berkala.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Identifikasi kendala pemberian umpan balik cepat saat siswa sedang praktik', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Konstruksi rubrik analitik: kriteria unjuk kerja, deskriptor level, dan skala nilai', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Kalibrasi penilaian antar guru pamong dan mahasiswa PPL', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Pemberian umpan balik formatif tertulis berbasis prinsip Growth Mindset', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Penerapan asesmen diri (self-assessment) oleh siswa sebelum pengumpulan tugas', 'status': 'Selesai'}
                ]
            },
            {
                'no': 5,
                'judul': 'Analisis Pola Kesalahan (Error Analysis) & Tindak Lanjut',
                'deskripsi': 'Mendekomposisi kesalahan konseptual siswa untuk merumuskan intervensi remedial terfokus.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi pandangan terhadap eror dalam coding: kegagalan vs peluang belajar', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Teknik analisis kesalahan logis rumus spreadsheet dan sintaks algoritma', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Penyusunan modul mini remedial untuk konsep fungsi logika bersyarat', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Laporan evaluasi kemajuan belajar pasca kegiatan pengayaan dan remedial', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Penyusunan rekomendasi perbaikan pembelajaran berkelanjutan', 'status': 'Selesai'}
                ]
            }
        ]
    },

    # 6. Growth Mindset
    {
        'id': 'growth',
        'file': 'course-growth.html',
        'badge': 'REFLEKSI PENGALAMAN BELAJAR',
        'title': 'Dasar Pola Pikir Bertumbuh (Growth Mindset)',
        'short_title': 'Dasar Pola Pikir Bertumbuh (Growth Mindset) dalam Pembelajaran',
        'subtitle': 'Refleksi pengalaman belajar mata kuliah Dasar Pola Pikir Bertumbuh (Growth Mindset) dalam Pembelajaran melalui kerangka 4C, analisis artefak, serta perumusan hasil refleksi.',
        'theme_color': '#16a34a',
        'theme_gradient': 'linear-gradient(135deg, #4ade80, #22c55e, #16a34a)',
        'ref_pdf': 'assets/docs/Refleksi Mata Kuliah/Refleksi GROWTH MINSET.pdf',
        'ref_key': 'Refleksi GROWTH MINSET.pdf',
        'custom_q': {
            'q3': 'a. Perbedaan fundamental pola pikir tetap (fixed mindset) yang meyakini kecerdasan bersifat statis vs pola pikir bertumbuh (growth mindset) yang meyakini potensi berkembang melalui usaha dan strategi.<br>b. Kemampuan otak berkembang melalui neuroplastisitas saat menghadapi tantangan dan melakukan latihan terarah.<br>c. Pentingnya bahasa respons guru di kelas: mengganti pujian bakat (person praise) dengan pujian proses (process praise) dan membiasakan kata "BELUM".'
        },
        'artefak_items': [
            {
                'nama': 'Lembar Responmu untuk Kelas (10 Situasi Nyata)',
                'deskripsi': 'Panduan respons guru terhadap 10 situasi kelas umum untuk menumbuhkan ketahanan mental dan keberanian mencoba pada murid.',
                'tipe': 'Panduan Komunikasi Guru',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi GROWTH MINSET.pdf'
            },
            {
                'nama': 'Analisis Kasus Pola Pikir Siswa dalam Pembelajaran',
                'deskripsi': 'Kajian mendalam tentang siswa yang menyerah menghadapi kesulitan logika coding dan rancangan intervensi growth mindset.',
                'tipe': 'Studi Kasus Psikologi Belajar',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi GROWTH MINSET.pdf'
            },
            {
                'nama': 'Desain Iklim Kelas Ramah Kesalahan (The Power of Yet)',
                'deskripsi': 'Strategi membudayakan kesalahan sebagai batu loncatan belajar dan pengenalan jurnal refleksi mandiri siswa.',
                'tipe': 'Desain Ekosistem Kelas Positif',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi GROWTH MINSET.pdf'
            }
        ],
        'topik_list': [
            {
                'no': 1,
                'judul': 'Konsep Dasar Fixed vs Growth Mindset',
                'deskripsi': 'Memahami riset Carol Dweck mengenai perbedaan keyakinan bahwa kecerdasan bersifat statis (fixed) vs dapat dikembangkan (growth).',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Kuesioner asesmen mandiri pola pikir pribadi sebagai calon guru', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Perbandingan respons fixed vs growth mindset terhadap tantangan dan kritik', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Diskusi mitos bakat alami (talent myth) dalam bidang sains dan teknologi', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Peta konsep transisi dari fixed mindset menuju growth mindset', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Poster motivasi kelas: "Belajar adalah Proses Otak Berkembang"', 'status': 'Selesai'}
                ]
            },
            {
                'no': 2,
                'judul': 'Neurosains dan Plastisitas Otak dalam Belajar',
                'deskripsi': 'Kajian ilmiah tentang pembentukan sinapsis baru saat otak menghadapi kesulitan dan melakukan latihan berulang (deliberate practice).',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi pengalaman mempelajari keterampilan baru yang mulanya dirasa mustahil', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Mekanisme neuroplastisitas: bagaimana neuron membentuk koneksi baru saat belajar', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Penyusunan analogi sederhana neuroplastisitas untuk dijelaskan kepada murid SMP', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Infografis "Otakmu Seperti Otot: Semakin Dilatih, Semakin Kuat"', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Sesi mini-talk edukasi neurosains kepada siswa sebelum memulai materi rumit', 'status': 'Selesai'}
                ]
            },
            {
                'no': 3,
                'judul': 'Bahasa Pujian Proses dan Budaya Belajar dari Kesalahan',
                'deskripsi': 'Mengubah kebiasaan memuji kepintaran (person praise) menjadi memuji usaha, ketekunan, dan strategi (process praise).',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Audit gaya komunikasi pribadi saat memberikan umpan balik kepada siswa', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Dampak merusak person praise dan kekuatan transformatif process praise', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Latihan mengubah kalimat reaksi spontan guru: "Bukan tidak bisa, tapi BELUM"', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Kompilasi panduan umpan balik tertulis berbasis growth mindset pada tugas siswa', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Penerapan "Kesalahan Terbaik Minggu Ini" sebagai sarana diskusi belajar bersama', 'status': 'Selesai'}
                ]
            },
            {
                'no': 4,
                'judul': 'Merancang Iklim Kelas Berbasis Growth Mindset',
                'deskripsi': 'Menata lingkungan fisik dan psikologis kelas yang aman untuk mencoba, menghargai upaya, dan menghapus stigma kegagalan.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Identifikasi faktor penghambat siswa bertanya di kelas Informatika', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Strategi menurunkan kecemasan performa (performance anxiety) pada siswa', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Penyusunan aturan kelas (Class Agreements) yang mendukung eksplorasi', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Dokumentasi artefak "Responmu untuk Kelas" pada 10 skenario riil', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Pemberian kesempatan revisi tugas berulang untuk mencapai kriteria ketuntasan', 'status': 'Selesai'}
                ]
            },
            {
                'no': 5,
                'judul': 'Evaluasi dan Pembiasaan Reflektif Mandiri',
                'deskripsi': 'Membekali peserta didik dengan alat metakognisi agar mampu mengevaluasi kemajuan belajar dan merancang strategi perbaikan mandiri.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Penyusunan jurnal refleksi berkala calon guru mengenai perkembangan mindset diri', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Rubrik asesmen diri (self-assessment) berbasis perkembangan usaha', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Format jurnal belajar siswa: "Apa yang membuat saya tertantang hari ini?"', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Presentasi perubahan persepsi siswa setelah intervensi 1 siklus PPL', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Rangkuman refleksi komprehensif mata kuliah Pola Pikir Bertumbuh', 'status': 'Selesai'}
                ]
            }
        ]
    },

    # 7. Etika dan Profesionalisme Guru
    {
        'id': 'etika',
        'file': 'course-etika.html',
        'badge': 'REFLEKSI PENGALAMAN BELAJAR',
        'title': 'Etika dan Profesionalisme Guru',
        'short_title': 'Etika dan Profesionalisme Guru',
        'subtitle': 'Refleksi pengalaman belajar mata kuliah Etika dan Profesionalisme Guru melalui kerangka 4C (Connection, Challenge, Concept, Change), analisis artefak pembelajaran, serta perumusan hasil refleksi.',
        'theme_color': '#d97706',
        'theme_gradient': 'linear-gradient(135deg, #fbbf24, #f59e0b, #d97706)',
        'ref_pdf': 'assets/docs/Refleksi Mata Kuliah/Refleksi ETIKA DAN PROFESIONALISME GURU.pdf',
        'ref_key': 'Refleksi ETIKA DAN PROFESIONALISME GURU.pdf',
        'custom_q': {
            'q2': 'Selama ini saya cenderung memandang mengajar sebagai kegiatan menjelaskan materi dengan ceramah, lalu memberi tugas. Pandangan ini berbeda dari materi perkuliahan karena Etika dan Profesionalisme Guru menekankan bahwa peran guru jauh melampaui transfer ilmu: guru memiliki tanggung jawab moral, sosial, dan hukum yang menuntut keteladanan konsisten, empati kepada murid, serta pengambilan keputusan etis yang berkeadilan.'
        },
        'artefak_items': [
            {
                'nama': 'Lembar Kerja Aktivitas 3B: Pemecahan Kasus Etika Guru',
                'deskripsi': 'Analisis pemetaan akar masalah, diagram kausalitas antarfaktor, dan rencana aksi etis dalam menghadapi dilema moral keguruan.',
                'tipe': 'Kajian Kasus Etika Profesi',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi ETIKA DAN PROFESIONALISME GURU.pdf'
            },
            {
                'nama': 'Analisis Dilema Etika & Pengambilan Keputusan 9 Langkah',
                'deskripsi': 'Kajian kasus benturan kepentingan dan pengujian keputusan etis berlandaskan prinsip kepedulian (care-based thinking).',
                'tipe': 'Instrumen Keputusan Etis',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi ETIKA DAN PROFESIONALISME GURU.pdf'
            },
            {
                'nama': 'Pakta Integritas & Standar Profesional Guru Informatika',
                'deskripsi': 'Rumusan komitmen tertulis mengenai kerahasiaan data murid, etika digital, dan objektivitas asesmen di sekolah.',
                'tipe': 'Dokumen Komitmen Profesional',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi ETIKA DAN PROFESIONALISME GURU.pdf'
            }
        ],
        'topik_list': [
            {
                'no': 1,
                'judul': 'Pengantar Etika dan Karakteristik Profesi Guru',
                'deskripsi': 'Mendalami makna etika profesi, panggilan jiwa (vocation), dan dimensi martabat pendidik dalam masyarakat.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi motivasi dasar memilih profesi guru dibandingkan karir industri software', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Karakteristik khusus profesi keguruan: kompetensi pedagogik, kepribadian, sosial, dan profesional', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Diskusi komparasi etika profesi guru dengan profesi teknologi informasi', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Infografis 4 pilar kompetensi guru profesional abad ke-21', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Pernyataan filosofi pribadi tentang martabat guru Informatika', 'status': 'Selesai'}
                ]
            },
            {
                'no': 2,
                'judul': 'Kode Etik Guru Indonesia dan Nilai Integritas',
                'deskripsi': 'Bedah pasal-pasal Kode Etik Guru Indonesia sebagai pedoman normatif dalam berinteraksi dengan siswa, sejawat, dan wali murid.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi pengalaman melihat keteladanan sosok guru inspiratif semasa sekolah', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Studi komprehensif 9 butir Kode Etik Guru Indonesia dan nilai integritas', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Diskusi batasan etis interaksi guru-murid di media sosial dan ruang daring', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Video studi kasus implementasi kode etik guru di sekolah mitra', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Penandatanganan pakta integritas etika mengajar selama PPL', 'status': 'Selesai'}
                ]
            },
            {
                'no': 3,
                'judul': 'Regulasi, Hak, dan Kewajiban Guru Profesional',
                'deskripsi': 'Memahami Undang-Undang Guru dan Dosen (UU No. 14 Tahun 2005) serta perlindungan hukum bagi pendidik.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Pengetahuan awal mengenai payung hukum profesi guru di Indonesia', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Hak, kewajiban, dan perlindungan hukum bagi guru dalam menjalankan tugas kedinasan', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Analisis kasus sengketa perlindungan guru saat mendisiplinkan siswa', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Panduan praktis perlindungan data privasi siswa dalam pembelajaran berbasis TIK', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Sosialisasi etika penggunaan gawai kepada siswa di SMPN 8 Malang', 'status': 'Selesai'}
                ]
            },
            {
                'no': 4,
                'judul': 'Analisis Studi Kasus Dilema Etika dan Pemecahan Masalah',
                'deskripsi': 'Menerapkan kerangka berpikir etis dalam menyelesaikan masalah pelanggaran disiplin dan konflik kepentingan.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi sikap saat berada di posisi dilema antara aturan kaku vs rasa kemanusiaan', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Model 9 langkah pengujian keputusan: uji benar vs salah, uji intuisi, uji publikasi', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Lembar Kerja Aktivitas 3B: Pemetaan akar masalah kasus integritas penilaian', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Presentasi solusi etis kasus kecurangan akademik berbasis TIK', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Penyusunan panduan kejujuran akademik untuk laboratorium komputer', 'status': 'Selesai'}
                ]
            },
            {
                'no': 5,
                'judul': 'Komitmen Profesionalisme dan Pengembangan Keprofesian (PKB)',
                'deskripsi': 'Merancang peta jalan pengembangan diri berkelanjutan melalui komunitas belajar praktisi dan riset tindakan kelas.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Identifikasi kelemahan pedagogik diri yang perlu ditingkatkan secara berkelanjutan', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Strategi PKB: publikasi ilmiah, karya inovatif, dan keikutsertaan MGMP', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Rancangan komunitas praktisi guru Informatika SMP tingkat kota', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Rencana Pengembangan Keprofesian Berkelanjutan 3 tahun ke depan', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Sintesis refleksi komprehensif mata kuliah Etika dan Profesionalisme Guru', 'status': 'Selesai'}
                ]
            }
        ]
    },

    # 8. Pembelajaran Sosial Emosional (PSE)
    {
        'id': 'pse',
        'file': 'course-pse.html',
        'badge': 'REFLEKSI PENGALAMAN BELAJAR',
        'title': 'Pembelajaran Sosial Emosional',
        'short_title': 'Pembelajaran Sosial Emosional (PSE)',
        'subtitle': 'Refleksi pengalaman belajar mata kuliah Pembelajaran Sosial Emosional melalui kerangka 4C (Connection, Challenge, Concept, Change), analisis artefak pembelajaran, serta perumusan hasil refleksi.',
        'theme_color': '#059669',
        'theme_gradient': 'linear-gradient(135deg, #34d399, #10b981, #059669)',
        'ref_pdf': 'assets/docs/Refleksi Mata Kuliah/Refleksi PEMBELAJARAN SOSIAL EMOSIONAL.pdf',
        'ref_key': 'Refleksi PEMBELAJARAN SOSIAL EMOSIONAL.pdf',
        'custom_q': {
            'q2': 'Sebelumnya saya mengira kelas yang gaduh harus dihadapi dengan teguran tegas atau suara keras agar siswa patuh. Materi Pembelajaran Sosial Emosional menyadarkan saya bahwa reaksi keras guru justru memicu pertahanan diri dan kecemasan siswa. PSE mengajarkan pendekatan kesadaran penuh (mindfulness), regulasi emosi guru terlebih dahulu, serta mendengarkan aktif kebutuhan siswa di balik perilaku mereka.',
            'art_q1': 'Artefak pembelajaran yang saya jadikan bukti pendukung meliputi Lembar Kerja 1C Pembelajaran Sosial Emosional yang dikerjakan secara kolaboratif mengenai analisis kasus situasi sosial-emosional siswa di kelas, panduan integrasi teknik STOP, serta rancangan modul ajar berbasis kerangka CASEL.'
        },
        'artefak_items': [
            {
                'nama': 'Lembar Kerja 1C Analisis Situasi Sosial-Emosional Siswa',
                'deskripsi': 'Studi kasus dinamika interaksi murid di kelas, identifikasi pemicu stres belajar, dan analisis dampak sosial-emosional.',
                'tipe': 'Kajian Kasus Kolaboratif',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi PEMBELAJARAN SOSIAL EMOSIONAL.pdf'
            },
            {
                'nama': 'Modul Pembelajaran Informatika Terintegrasi 5 Kompetensi CASEL',
                'deskripsi': 'Rancangan RPP/Modul ajar yang mengintegrasikan kesadaran diri, manajemen diri, dan kerja sama dalam proyek pemrograman.',
                'tipe': 'Perangkat Pembelajaran PSE',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi PEMBELAJARAN SOSIAL EMOSIONAL.pdf'
            },
            {
                'nama': 'Panduan Praktik Mindfulness Teknik STOP di Kelas',
                'deskripsi': 'Instrumen jeda relaksasi 3 menit sebelum praktikum komputer untuk menenangkan pikiran dan memulihkan fokus belajar murid.',
                'tipe': 'Panduan Regulasi Diri',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi PEMBELAJARAN SOSIAL EMOSIONAL.pdf'
            }
        ],
        'topik_list': [
            {
                'no': 1,
                'judul': 'Kompetensi Sosial Emosional Berdasarkan Kerangka CASEL',
                'deskripsi': 'Memahami 5 KSE CASEL: Self-Awareness, Self-Management, Social Awareness, Relationship Skills, dan Responsible Decision-Making.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi kompetensi emosi pribadi saat menghadapi tekanan tugas kuliah dan PPL', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Studi mendalam 5 kompetensi sosial emosional dan implementasinya di sekolah', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Lembar Kerja 1C: Analisis kasus situasi sosial-emosional kelompok siswa', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Tabel rencana aksi penerapan 5 KSE dalam pembelajaran Informatika', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Penyusunan roda emosi untuk mengecek kesiapan perasaan siswa di awal KBM', 'status': 'Selesai'}
                ]
            },
            {
                'no': 2,
                'judul': 'Peran Guru sebagai Teladan Pembelajaran Sosial Emosional',
                'deskripsi': 'Mewujudkan pendidik yang matang secara emosi, hangat, berempati, dan menjadi panutan positif di hadapan siswa.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Audit reaksi emosional spontan diri saat menghadapi murid yang tidak fokus', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Dampak emosi guru terhadap iklim psikologis dan motivasi belajar siswa', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Simulasi penanganan siswa cemas saat ujian praktikum komputer', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Video demonstrasi komunikasi hangat dan asertif antara guru dan siswa', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Jurnal refleksi harian regulasi emosi mengajar di SMPN 8 Malang', 'status': 'Selesai'}
                ]
            },
            {
                'no': 3,
                'judul': 'Mindfulness dan Teknik STOP dalam Pembelajaran',
                'deskripsi': 'Menerapkan latihan kesadaran penuh (Mindfulness) untuk mengurangi stres, meningkatkan atensi, dan menstabilkan emosi.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Latihan pribadi mindfulness teknik bernapas 4-7-8 untuk menenangkan pikiran', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Konsep teknik STOP: Stop, Take a breath, Observe, dan Proceed', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Penyusunan skenario penerapan teknik STOP sebelum memulai materi coding', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Panduan audio/visual relaksasi pernapasan 3 menit untuk siswa SMP', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Penerapan rutin teknik STOP bersama siswa di kelas VIII SMPN 8 Malang', 'status': 'Selesai'}
                ]
            },
            {
                'no': 4,
                'judul': 'Membangun Iklim Kelas Positif dan School Well-Being',
                'deskripsi': 'Menciptakan ekosistem sekolah yang aman, inklusif, saling peduli, dan mendukung kesehatan mental peserta didik.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi pengalaman berada di lingkungan kelas yang toksik vs kelas suportif', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Empat dimensi School Well-Being: Having, Loving, Being, dan Health', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Perancangan program peer-counseling sederhana di kalangan peserta didik', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Poster aturan kelas berbasis kesepakatan bersama yang menghargai keberagaman', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Menciptakan "Sudut Relaksasi dan Ekspresi Diri" di ruang kelas', 'status': 'Selesai'}
                ]
            },
            {
                'no': 5,
                'judul': 'Integrasi PSE dalam Rencana Pelaksanaan Pembelajaran',
                'deskripsi': 'Menyisipkan kompetensi sosial emosional ke dalam langkah pendahuluan, inti, dan penutup modul ajar secara kontekstual.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Identifikasi momen-momen alami dalam KBM Informatika untuk melatih KSE', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Teknik integrasi eksplisit (sesi khusus) vs terintegrasi dalam materi ajar', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Modifikasi modul ajar Analisis Data dengan menambahkan elemen kolaborasi empati', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Microteaching pembelajaran Informatika terpadu PSE di laboratorium komputer', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Sintesis refleksi komprehensif mata kuliah Pembelajaran Sosial Emosional', 'status': 'Selesai'}
                ]
            }
        ]
    },

    # 9. Mata Kuliah Selektif / Elektif (General)
    {
        'id': 'selektif',
        'file': 'course-selektif.html',
        'badge': 'REFLEKSI PENGALAMAN BELAJAR',
        'title': 'Refleksi Mata Kuliah Selektif / Elektif',
        'short_title': 'Mata Kuliah Selektif / Elektif (Etika Profesi & PSE)',
        'subtitle': 'Refleksi pengalaman belajar mata kuliah Selektif (Etika dan Profesionalisme Guru & Pembelajaran Sosial Emosional) melalui kerangka 4C, analisis artefak, serta perumusan hasil refleksi.',
        'theme_color': '#f59e0b',
        'theme_gradient': 'linear-gradient(135deg, #fbbf24, #f59e0b, #d97706)',
        'ref_pdf': 'assets/docs/Refleksi Mata Kuliah/Refleksi ETIKA DAN PROFESIONALISME GURU.pdf',
        'ref_key': 'Refleksi ETIKA DAN PROFESIONALISME GURU.pdf',
        'custom_q': {
            'q1': 'Materi Etika dan Profesionalisme Guru serta Pembelajaran Sosial Emosional berkaitan langsung dengan peran saya sebagai calon guru Informatika. Guru bukan hanya pengajar konten teknis, melainkan arsitek peradaban yang memegang teguh integritas moral dan membimbing kematangan emosional murid.',
            'q2': 'Selama ini saya cenderung memandang mengajar sebagai kegiatan satu arah yang berfokus pada transfer logika teknis. Mata kuliah selektif ini memperkenalkan realitas bahwa mengajar menuntut pemahaman etika, empati, mindfulness, dan manajemen iklim kelas yang aman.',
            'q3': '1. Kode Etik Guru Indonesia dan martabat pendidik.<br>2. Sembilan langkah pengujian keputusan etis menghadapi dilema moral.<br>3. Lima Kompetensi Sosial Emosional (CASEL).<br>4. Teknik STOP dan penguatan School Well-Being.',
            'q4': 'Menerapkan pembelajaran yang humanis, menjaga integritas keteladanan moral, melatih diri menahan reaksi spontan dengan teknik STOP, dan memfasilitasi perkembangan karakter siswa.'
        },
        'artefak_items': [
            {
                'nama': 'Lembar Kerja Aktivitas 3B: Kasus Etika Guru',
                'deskripsi': 'Analisis pemetaan akar masalah dan rencana aksi etis dalam menghadapi dilema moral keguruan.',
                'tipe': 'Kajian Kasus Etika Profesi',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi ETIKA DAN PROFESIONALISME GURU.pdf'
            },
            {
                'nama': 'Lembar Kerja 1C Analisis Sosial Emosional Peserta Didik',
                'deskripsi': 'Kajian situasi emosi murid dan rancangan integrasi 5 kompetensi CASEL dalam kelas Informatika.',
                'tipe': 'Perangkat Pedagogis PSE',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi PEMBELAJARAN SOSIAL EMOSIONAL.pdf'
            },
            {
                'nama': 'Pakta Integritas & Panduan Mindfulness STOP di Kelas',
                'deskripsi': 'Komitmen profesionalisme keguruan dan panduan regulasi emosi calon guru selama PPL.',
                'tipe': 'Jurnal Refleksi Mandiri',
                'file': 'assets/docs/Refleksi Mata Kuliah/Refleksi ETIKA DAN PROFESIONALISME GURU.pdf'
            }
        ],
        'topik_list': [
            {
                'no': 1,
                'judul': 'Kode Etik dan Martabat Profesi Guru',
                'deskripsi': 'Mendalami prinsip integritas moral, komitmen profesionalisme, dan tanggung jawab hukum serta sosial sebagai seorang pendidik.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi pandangan masyarakat terhadap wibawa dan integritas guru di era digital', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Bedah Kode Etik Guru Indonesia dan regulasi standar kompetensi kepribadian', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Diskusi pemecahan kasus pelanggaran kode etik di lingkungan pendidikan', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Lembar Kerja Aktivitas 3B: Analisis akar masalah studi kasus etika', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Pernyataan pakta integritas dan standar etis mengajar pribadi', 'status': 'Selesai'}
                ]
            },
            {
                'no': 2,
                'judul': 'Lima Kompetensi Sosial Emosional (CASEL)',
                'deskripsi': 'Mempelajari Self-Awareness, Self-Management, Social Awareness, Relationship Skills, dan Responsible Decision-Making.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Pemetaan roda emosi pribadi saat menghadapi situasi kelas yang melelahkan', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Kerangka CASEL dan penerapannya secara eksplisit maupun terintegrasi', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Simulasi penanganan konflik antarsiswa dengan pendekatan restorative practice', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Rancangan modul integrasi PSE dalam pembelajaran Informatika', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Praktik penerapan teknik STOP (Stop, Take a breath, Observe, Proceed)', 'status': 'Selesai'}
                ]
            },
            {
                'no': 3,
                'judul': 'Manajemen Diri dan Kesejahteraan Psikologis (Well-Being)',
                'deskripsi': 'Membekali guru dengan resiliensi mental, pencegahan burnout, dan pembiasaan hidup berkesadaran penuh (mindfulness).',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Inventori tingkat stres kerja dan keseimbangan kehidupan profesional', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Faktor-faktor penentu School Well-Being dan dampaknya terhadap capaian siswa', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Penyusunan program peer-support antar rekan sejawat mahasiswa PPG', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Video panduan mindfulness relaksasi pernapasan 3 menit sebelum KBM', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Rancangan self-care plan untuk menjaga kesehatan fisik dan emosional guru', 'status': 'Selesai'}
                ]
            },
            {
                'no': 4,
                'judul': 'Keterampilan Berelasi dan Komunikasi Asertif',
                'deskripsi': 'Membangun komunikasi positif tanpa kekerasan (nonviolent communication) dengan peserta didik, rekan sejawat, dan orang tua.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi pengalaman berkomunikasi saat menyampaikan evaluasi kepada orang tua murid', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Prinsip komunikasi asertif: memisahkan observasi dari penilaian subjektif', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Roleplay mediasi masalah kedisiplinan siswa di ruang BK / bimbingan guru', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Surat komunikasi kemajuan siswa yang konstruktif dan empatik', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Penerapan active listening dalam bimbingan tugas kelompok siswa', 'status': 'Selesai'}
                ]
            },
            {
                'no': 5,
                'judul': 'Pengambilan Keputusan yang Bertanggung Jawab',
                'deskripsi': 'Melatih kematangan nalar etis dalam mengambil keputusan pedagogis yang adil, inklusif, dan mengutamakan keselamatan peserta didik.',
                'tugas': [
                    {'alur': 'Mulai dari Diri', 'tugas': 'Refleksi keputusan sulit yang pernah diambil dalam situasi dilema kepentingan', 'status': 'Selesai'},
                    {'alur': 'Eksplorasi Konsep', 'tugas': 'Model 9 langkah pengambilan dan pengujian keputusan etis', 'status': 'Selesai'},
                    {'alur': 'Ruang Kolaborasi', 'tugas': 'Studi kasus pengambilan keputusan berbasis rasa peduli vs kepatuhan aturan', 'status': 'Selesai'},
                    {'alur': 'Demonstrasi Kontekstual', 'tugas': 'Esai reflektif: Peran integritas moral guru dalam peradaban digital', 'status': 'Selesai'},
                    {'alur': 'Aksi Nyata', 'tugas': 'Sintesis refleksi komprehensif mata kuliah selektif Etika & PSE', 'status': 'Selesai'}
                ]
            }
        ]
    }
]

def generate_page_html(c):
    raw_ref = ref_data.get(c['ref_key'], {})
    custom = c.get('custom_q', {})

    q1 = custom.get('q1') or clean_val(raw_ref.get('q1', ''))
    q2 = custom.get('q2') or clean_val(raw_ref.get('q2', ''))
    q3 = custom.get('q3') or clean_val(raw_ref.get('q3', ''))
    q4 = custom.get('q4') or clean_val(raw_ref.get('q4', ''))
    art_q1 = custom.get('art_q1') or clean_val(raw_ref.get('art_q1', ''))
    art_q2 = custom.get('art_q2') or clean_val(raw_ref.get('art_q2', ''))
    art_q3 = custom.get('art_q3') or clean_val(raw_ref.get('art_q3', ''))
    hasil = custom.get('hasil') or clean_val(raw_ref.get('hasil', ''))

    if not art_q1 or len(art_q1) < 15:
        art_q1 = f"Artefak pembelajaran yang saya jadikan bukti pendukung hasil refleksi mata kuliah {c['short_title']} mencakup produk tugas terstruktur LK 1 / LK 2, modul ajar, dan kajian studi kasus nyata yang dikerjakan selama perkuliahan."
    if not art_q2 or len(art_q2) < 15:
        art_q2 = f"Saya memilih artefak-artefak tersebut karena secara konkret merefleksikan proses belajar saya dari pemahaman teoritis hingga implementasi praktis di kelas PPL."
    if not art_q3 or len(art_q3) < 15:
        art_q3 = f"Bagian analisis masalah, sintesis konsep, dan rumusan aksi nyata pada artefak menjadi bukti autentik yang mendukung hasil refleksi saya."

    artefak_cards_html = ''
    for a in c['artefak_items']:
        artefak_cards_html += f"""
        <div class="artefak-card">
            <div class="artefak-card-header">
                <div class="artefak-card-icon" style="background: rgba(16, 185, 129, 0.15); color: #10b981;">
                    <i class="fa-solid fa-file-shield"></i>
                </div>
                <div style="flex:1;">
                    <div class="artefak-card-title">{a['nama']}</div>
                    <div class="artefak-card-type">{a['tipe']}</div>
                </div>
            </div>
            <p class="artefak-card-desc">{a['deskripsi']}</p>
            <div class="artefak-card-footer">
                <div class="artefak-card-file">
                    <i class="fa-solid fa-file-pdf" style="color:#ef4444; font-size:1.15rem;"></i>
                    <div>
                        <div class="artefak-card-filename">{a['nama']}.pdf</div>
                        <div class="artefak-card-filesize">Dokumen Autentik Portofolio</div>
                    </div>
                </div>
                <div class="artefak-actions">
                    <button class="btn-action-view" onclick="openPdfModalDirect('{a['file']}', '{a['nama']}')" title="Lihat Pratinjau Dokumen">
                        <i class="fa-solid fa-eye"></i> <span>Lihat</span>
                    </button>
                    <a class="btn-action-dl" href="{a['file']}" download="{a['nama']}.pdf" title="Unduh Berkas PDF">
                        <i class="fa-solid fa-download"></i> <span>Unduh</span>
                    </a>
                </div>
            </div>
        </div>
        """

    topics_sidebar_html = ''
    topics_content_html = ''

    topics_sidebar_html += f"""
    <div class="sidebar-item active" data-topic="all" onclick="switchTopic('all', this)">
        <i class="fa-regular fa-folder-open"></i>
        <span>Tugas Perkuliahan</span>
    </div>
    """

    for t in c['topik_list']:
        t_id = f"topik-{t['no']}"
        topics_sidebar_html += f"""
        <div class="sidebar-item" data-topic="{t_id}" onclick="switchTopic('{t_id}', this)">
            <i class="fa-regular fa-folder"></i>
            <span>Topik {t['no']}</span>
        </div>
        """

        task_items_html = ''
        for tsk in t['tugas']:
            task_items_html += f"""
            <div class="task-card">
                <div class="task-card-badge"><i class="fa-solid fa-circle-check"></i> {tsk['alur']}</div>
                <div class="task-card-title">{tsk['tugas']}</div>
                <div class="task-card-bottom">
                    <span class="task-status-pill"><i class="fa-solid fa-check"></i> {tsk['status']}</span>
                    <button class="btn-task-preview" onclick="openPdfModalDirect('{c['ref_pdf']}', '{t['judul']} - {tsk['alur']}')">
                        <i class="fa-solid fa-arrow-up-right-from-square"></i> Lihat Detail
                    </button>
                </div>
            </div>
            """

        topics_content_html += f"""
        <div class="topic-section-box" id="section-{t_id}">
            <div class="topic-section-header">
                <div class="topic-num-badge">TOPIK {t['no']}</div>
                <h3 class="topic-section-title">{t['judul']}</h3>
                <p class="topic-section-desc">{t['deskripsi']}</p>
            </div>
            <div class="tasks-grid">
                {task_items_html}
            </div>
        </div>
        """

    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{c['title']} | Refleksi &amp; Tugas Perkuliahan | E-Portfolio PPG</title>
    <meta name="description" content="Refleksi 4C, Analisis Artefak, Hasil Refleksi, Lembar Refleksi, dan Kumpulan Tugas Perkuliahan mata kuliah {c['title']} - PPG Prajabatan Lutfi Subekti">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Lora:ital,wght@0,400;0,500;0,600;1,400;1,600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">

    <style>
        /* ══════ MODERN PAGE THEME & BACKGROUND ══════ */
        body {{
            background-color: #050d15;
            background-image: 
                radial-gradient(circle at 50% 0%, rgba(8, 98, 136, 0.35) 0%, transparent 60%),
                radial-gradient(circle at 10% 40%, rgba(77, 141, 186, 0.18) 0%, transparent 45%),
                radial-gradient(circle at 90% 70%, rgba(151, 215, 255, 0.12) 0%, transparent 45%),
                linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
            background-size: 100% 100%, 100% 100%, 100% 100%, 36px 36px, 36px 36px;
            background-position: 0 0, 0 0, 0 0, 0 0, 0 0;
            color: #e2e8f0;
            min-height: 100vh;
        }}

        html[data-theme="light"] body {{
            background-color: #f0f7fb;
            background-image: 
                radial-gradient(circle at 50% 0%, rgba(151, 215, 255, 0.25) 0%, transparent 60%),
                linear-gradient(rgba(8, 98, 136, 0.04) 1px, transparent 1px),
                linear-gradient(90deg, rgba(8, 98, 136, 0.04) 1px, transparent 1px);
            background-size: 100% 100%, 36px 36px, 36px 36px;
            color: #0a1926;
        }}

        .course-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1.5rem;
        }}

        /* ─── Back to Seminar ─── */
        .back-nav-link {{
            display: inline-flex;
            align-items: center;
            gap: 0.6rem;
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 600;
            padding: 0.5rem 1rem;
            border-radius: 50px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(151, 215, 255, 0.15);
            margin-bottom: 2.2rem;
            transition: all 0.25s ease;
        }}
        .back-nav-link:hover {{
            color: #fff;
            background: rgba(8, 98, 136, 0.25);
            border-color: rgba(151, 215, 255, 0.4);
            transform: translateX(-3px);
        }}
        html[data-theme="light"] .back-nav-link {{
            background: rgba(255, 255, 255, 0.85);
            border-color: rgba(8, 98, 136, 0.15);
            color: #475569;
        }}
        html[data-theme="light"] .back-nav-link:hover {{
            background: rgba(8, 98, 136, 0.1);
            color: #086288;
        }}

        /* ─── Course Header Banner ─── */
        .course-hero {{
            text-align: center;
            margin-bottom: 2.5rem;
            position: relative;
        }}
        .course-eyebrow {{
            display: inline-block;
            font-size: 0.8rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: #97D7FF;
            margin-bottom: 0.75rem;
        }}
        html[data-theme="light"] .course-eyebrow {{
            color: #086288;
        }}
        .course-main-title {{
            font-family: 'Outfit', 'Plus Jakarta Sans', sans-serif;
            font-size: clamp(2.1rem, 4.8vw, 3.2rem);
            font-weight: 800;
            line-height: 1.25;
            margin-bottom: 1rem;
            letter-spacing: -0.02em;
            background: linear-gradient(135deg, #ffffff 40%, #97D7FF 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 4px 18px rgba(0, 0, 0, 0.45);
        }}
        html[data-theme="light"] .course-main-title {{
            background: linear-gradient(135deg, #086288 0%, #03425e 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: none;
        }}
        .course-main-subtitle {{
            max-width: 780px;
            margin: 0 auto;
            font-size: 1rem;
            line-height: 1.7;
            color: #e2e8f0;
        }}
        html[data-theme="light"] .course-main-subtitle {{
            color: #1e293b;
        }}
        .course-hero-line {{
            width: 70px;
            height: 3px;
            background: linear-gradient(90deg, #4D8DBA, #97D7FF, #FFEFC4);
            border-radius: 4px;
            margin: 1.5rem auto 0;
        }}

        /* ─── SEGMENTED PILL TABS ─── */
        .course-tabs-wrapper {{
            display: flex;
            justify-content: center;
            margin-bottom: 2.8rem;
            overflow-x: auto;
            padding: 0.5rem 0;
            scrollbar-width: none;
        }}
        .course-tabs-wrapper::-webkit-scrollbar {{ display: none; }}
        .course-tabs-nav {{
            display: inline-flex;
            align-items: center;
            gap: 0.6rem;
            background: rgba(10, 25, 38, 0.75);
            backdrop-filter: blur(12px);
            padding: 0.45rem;
            border-radius: 18px;
            border: 1px solid rgba(151, 215, 255, 0.15);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
        }}
        html[data-theme="light"] .course-tabs-nav {{
            background: rgba(255, 255, 255, 0.9);
            border-color: rgba(8, 98, 136, 0.15);
            box-shadow: 0 8px 24px rgba(8, 98, 136, 0.08);
        }}
        .tab-btn-pill {{
            display: inline-flex;
            align-items: center;
            gap: 0.55rem;
            padding: 0.65rem 1.35rem;
            border-radius: 14px;
            font-size: 0.94rem;
            font-weight: 700;
            color: #cbd5e1;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(151, 215, 255, 0.18);
            cursor: pointer;
            transition: all 0.22s ease;
            white-space: nowrap;
        }}
        .tab-btn-pill:hover {{
            color: #ffffff;
            background: rgba(8, 98, 136, 0.25);
            border-color: rgba(151, 215, 255, 0.4);
        }}
        .tab-btn-pill.active {{
            background: linear-gradient(135deg, #086288, #4D8DBA);
            border-color: #97D7FF;
            color: #ffffff;
            box-shadow: 0 4px 20px rgba(8, 98, 136, 0.45);
        }}
        html[data-theme="light"] .tab-btn-pill {{
            color: #0f172a;
        }}
        html[data-theme="light"] .tab-btn-pill:hover {{
            color: #0a1926;
            background: rgba(8, 98, 136, 0.05);
        }}
        html[data-theme="light"] .tab-btn-pill.active {{
            background: #fff;
            border-color: rgba(8, 98, 136, 0.35);
            color: #086288;
            box-shadow: 0 4px 16px rgba(8, 98, 136, 0.12);
        }}

        /* ─── TAB CONTENT PANELS ─── */
        .tab-panel-section {{
            display: none;
            animation: fadeInPanel 0.28s ease forwards;
        }}
        .tab-panel-section.active {{
            display: block;
        }}
        @keyframes fadeInPanel {{
            from {{ opacity: 0; transform: translateY(8px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* ─── CARD BASES ─── */
        .content-card-box {{
            background: rgba(15, 23, 42, 0.65);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 22px;
            padding: 2.2rem;
            backdrop-filter: blur(14px);
            margin-bottom: 2.5rem;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.3);
        }}
        html[data-theme="light"] .content-card-box {{
            background: rgba(255, 255, 255, 0.95);
            border-color: rgba(0, 0, 0, 0.08);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.05);
        }}

        .section-badge {{
            display: inline-block;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            padding: 0.35rem 0.95rem;
            border-radius: 50px;
            margin-bottom: 1rem;
        }}
        .badge-green {{
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.3);
            color: #10b981;
        }}
        .badge-purple {{
            background: rgba(129, 140, 248, 0.15);
            border: 1px solid rgba(129, 140, 248, 0.3);
            color: #818cf8;
        }}
        .badge-amber {{
            background: rgba(245, 158, 11, 0.15);
            border: 1px solid rgba(245, 158, 11, 0.3);
            color: #fbbf24;
        }}

        .card-header-row {{
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.4rem;
        }}
        .card-header-icon {{
            width: 48px;
            height: 48px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.35rem;
            flex-shrink: 0;
        }}
        .card-header-title {{
            font-family: 'Outfit', 'Plus Jakarta Sans', sans-serif;
            font-size: 1.55rem;
            font-weight: 600;
            color: #fff;
            margin: 0;
        }}
        html[data-theme="light"] .card-header-title {{
            color: #1e293b;
        }}

        /* ─── 4C GRID ─── */
        .grid-4c {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.4rem;
        }}
        @media(max-width: 768px) {{
            .grid-4c {{ grid-template-columns: 1fr; }}
        }}
        .c4-box {{
            padding: 1.6rem;
            border-radius: 16px;
            border-left: 4px solid;
            transition: transform 0.2s ease, border-color 0.2s ease;
        }}
        .c4-box:hover {{
            transform: translateY(-2px);
        }}
        .c4-box.conn {{
            background: rgba(99, 102, 241, 0.08);
            border-color: #818cf8;
        }}
        .c4-box.chal {{
            background: rgba(236, 72, 153, 0.08);
            border-color: #f472b6;
        }}
        .c4-box.conc {{
            background: rgba(16, 185, 129, 0.08);
            border-color: #34d399;
        }}
        .c4-box.chan {{
            background: rgba(245, 158, 11, 0.08);
            border-color: #fbbf24;
        }}
        html[data-theme="light"] .c4-box.conn {{ background: rgba(99, 102, 241, 0.05); }}
        html[data-theme="light"] .c4-box.chal {{ background: rgba(236, 72, 153, 0.05); }}
        html[data-theme="light"] .c4-box.conc {{ background: rgba(16, 185, 129, 0.05); }}
        html[data-theme="light"] .c4-box.chan {{ background: rgba(245, 158, 11, 0.05); }}

        .c4-tag {{
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 0.6rem;
        }}
        .c4-box.conn .c4-tag {{ color: #818cf8; }}
        .c4-box.chal .c4-tag {{ color: #f472b6; }}
        .c4-box.conc .c4-tag {{ color: #34d399; }}
        .c4-box.chan .c4-tag {{ color: #fbbf24; }}

        .c4-question {{
            font-size: 1rem;
            font-weight: 700;
            color: #fff;
            margin-bottom: 0.8rem;
            line-height: 1.45;
        }}
        html[data-theme="light"] .c4-question {{ color: #0f172a; }}
        .c4-text {{
            font-size: 0.92rem;
            line-height: 1.8;
            color: #f1f5f9;
            margin: 0;
        }}
        html[data-theme="light"] .c4-text {{ color: #0f172a; }}

        /* ─── ARTEFAK LIST & CARDS ─── */
        .artefak-grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 1.2rem;
            margin-top: 1.5rem;
        }}
        .artefak-card {{
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            background: rgba(0, 0, 0, 0.22);
            padding: 1.4rem;
            transition: all 0.22s ease;
        }}
        .artefak-card:hover {{
            border-color: rgba(129, 140, 248, 0.35);
            background: rgba(0, 0, 0, 0.3);
        }}
        html[data-theme="light"] .artefak-card {{
            background: rgba(0, 0, 0, 0.02);
            border-color: rgba(0, 0, 0, 0.08);
        }}
        .artefak-card-header {{
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 0.8rem;
        }}
        .artefak-card-icon {{
            width: 44px;
            height: 44px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.15rem;
        }}
        .artefak-card-title {{
            font-size: 1.05rem;
            font-weight: 700;
            color: #fff;
        }}
        html[data-theme="light"] .artefak-card-title {{ color: #1e293b; }}
        .artefak-card-type {{
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        .artefak-card-desc {{
            font-size: 0.9rem;
            line-height: 1.7;
            color: #e2e8f0;
            margin-bottom: 1.2rem;
        }}
        html[data-theme="light"] .artefak-card-desc {{ color: #1e293b; }}

        .artefak-card-footer {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 1rem;
            padding-top: 1rem;
            border-top: 1px solid rgba(255, 255, 255, 0.06);
        }}
        html[data-theme="light"] .artefak-card-footer {{
            border-top-color: rgba(0, 0, 0, 0.06);
        }}
        .artefak-card-file {{
            display: flex;
            align-items: center;
            gap: 0.65rem;
        }}
        .artefak-card-filename {{
            font-size: 0.85rem;
            font-weight: 600;
            color: #fff;
        }}
        html[data-theme="light"] .artefak-card-filename {{ color: #1e293b; }}
        .artefak-card-filesize {{
            font-size: 0.72rem;
            color: var(--text-muted);
        }}

        .artefak-actions {{
            display: flex;
            gap: 0.5rem;
        }}
        .btn-action-view, .btn-action-dl {{
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.45rem 0.95rem;
            border-radius: 9px;
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.2s ease;
        }}
        .btn-action-view {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #fff;
        }}
        .btn-action-view:hover {{
            background: #818cf8;
            border-color: #818cf8;
            color: #fff;
        }}
        .btn-action-dl {{
            background: #10b981;
            border: 1px solid transparent;
            color: #fff;
        }}
        .btn-action-dl:hover {{
            filter: brightness(1.15);
        }}
        html[data-theme="light"] .btn-action-view {{
            background: rgba(0, 0, 0, 0.05);
            border-color: rgba(0, 0, 0, 0.1);
            color: #334155;
        }}
        html[data-theme="light"] .btn-action-view:hover {{
            background: #4f46e5;
            color: #fff;
        }}

        /* ─── HASIL REFLEKSI SECTION ─── */
        .hasil-refleksi-text {{
            font-size: 0.98rem;
            line-height: 1.95;
            color: #f8fafc;
            text-align: justify;
        }}
        html[data-theme="light"] .hasil-refleksi-text {{ color: #0f172a; }}
        .quote-box {{
            margin: 1.5rem 0;
            padding: 1.4rem 1.8rem;
            border-radius: 14px;
            background: rgba(99, 102, 241, 0.08);
            border-left: 4px solid #818cf8;
            font-family: 'Outfit', 'Plus Jakarta Sans', sans-serif;
            font-style: italic;
            font-size: 1.05rem;
            color: #e0e7ff;
            line-height: 1.7;
        }}
        html[data-theme="light"] .quote-box {{
            background: rgba(99, 102, 241, 0.06);
            color: #312e81;
        }}

        /* ─── LEMBAR REFLEKSI (PDF PREVIEW) ─── */
        .pdf-viewer-frame {{
            width: 100%;
            height: 750px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            background: #fff;
            margin-top: 1.5rem;
        }}

        /* ══════ TAB 5: TUGAS PERKULIAHAN (MATCHES USER SCREENSHOT) ══════ */
        .tugas-layout-grid {{
            display: grid;
            grid-template-columns: 280px 1fr;
            gap: 1.6rem;
            align-items: start;
        }}
        @media(max-width: 900px) {{
            .tugas-layout-grid {{ grid-template-columns: 1fr; }}
        }}

        /* Left Sidebar: DAFTAR ISI */
        .sidebar-daftar-isi {{
            background: rgba(15, 23, 42, 0.65);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 1.4rem;
            backdrop-filter: blur(14px);
            position: sticky;
            top: 100px;
        }}
        html[data-theme="light"] .sidebar-daftar-isi {{
            background: rgba(255, 255, 255, 0.95);
            border-color: rgba(0, 0, 0, 0.08);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
        }}
        .sidebar-header {{
            display: flex;
            align-items: center;
            gap: 0.65rem;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            color: var(--text-muted);
            margin-bottom: 1.2rem;
            padding-bottom: 0.8rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        }}
        html[data-theme="light"] .sidebar-header {{
            border-bottom-color: rgba(0, 0, 0, 0.06);
        }}
        .sidebar-menu {{
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
        }}
        .sidebar-item {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.65rem 1rem;
            border-radius: 12px;
            font-size: 0.88rem;
            font-weight: 500;
            color: #e2e8f0;
            cursor: pointer;
            transition: all 0.2s ease;
            text-decoration: none;
            border: 1px solid transparent;
        }}
        .sidebar-item:hover {{
            color: #fff;
            background: rgba(255, 255, 255, 0.04);
        }}
        .sidebar-item.active {{
            background: linear-gradient(135deg, rgba(8, 98, 136, 0.5), rgba(77, 141, 186, 0.35));
            border-color: #97D7FF;
            color: #ffffff;
            font-weight: 700;
            box-shadow: 0 4px 14px rgba(8, 98, 136, 0.25);
        }}
        html[data-theme="light"] .sidebar-item {{
            color: #1e293b;
        }}
        html[data-theme="light"] .sidebar-item:hover {{
            background: rgba(0, 0, 0, 0.03);
            color: #1e293b;
        }}
        html[data-theme="light"] .sidebar-item.active {{
            background: rgba(99, 102, 241, 0.1);
            border-color: rgba(99, 102, 241, 0.25);
            color: #4338ca;
        }}

        /* Right Panel: Content */
        .topic-section-box {{
            margin-bottom: 2.2rem;
            padding-bottom: 2rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        }}
        .topic-section-box:last-child {{
            margin-bottom: 0;
            padding-bottom: 0;
            border-bottom: none;
        }}
        .topic-section-header {{
            margin-bottom: 1.4rem;
        }}
        .topic-num-badge {{
            font-size: 0.7rem;
            font-weight: 800;
            letter-spacing: 0.1em;
            color: #10b981;
            text-transform: uppercase;
            margin-bottom: 0.35rem;
        }}
        .topic-section-title {{
            font-family: 'Outfit', 'Plus Jakarta Sans', sans-serif;
            font-size: 1.35rem;
            font-weight: 600;
            color: #fff;
            margin-bottom: 0.4rem;
        }}
        html[data-theme="light"] .topic-section-title {{ color: #0f172a; }}
        html[data-theme="light"] .topic-section-desc {{ color: #334155; }}
        .topic-section-desc {{
            font-size: 0.88rem;
            line-height: 1.6;
            color: var(--text-muted);
            margin: 0;
        }}

        .tasks-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
            gap: 1rem;
        }}
        .task-card {{
            background: rgba(0, 0, 0, 0.22);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 14px;
            padding: 1.15rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.2s ease;
        }}
        .task-card:hover {{
            background: rgba(0, 0, 0, 0.35);
            border-color: rgba(255, 255, 255, 0.12);
            transform: translateY(-2px);
        }}
        html[data-theme="light"] .task-card {{
            background: rgba(0, 0, 0, 0.02);
            border-color: rgba(0, 0, 0, 0.07);
        }}
        .task-card-badge {{
            font-size: 0.68rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: #818cf8;
            margin-bottom: 0.5rem;
        }}
        html[data-theme="light"] .task-card-badge {{ color: #4f46e5; }}
        .task-card-title {{
            font-size: 0.88rem;
            font-weight: 600;
            color: #fff;
            line-height: 1.5;
            margin-bottom: 1rem;
            flex-grow: 1;
        }}
        html[data-theme="light"] .task-card-title {{ color: #0f172a; }}
        .task-card-bottom {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-top: 0.75rem;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
        }}
        .task-status-pill {{
            font-size: 0.7rem;
            font-weight: 600;
            color: #10b981;
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
        }}
        .btn-task-preview {{
            background: transparent;
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: rgba(255, 255, 255, 0.8);
            font-size: 0.72rem;
            font-weight: 600;
            padding: 0.3rem 0.65rem;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.18s ease;
        }}
        .btn-task-preview:hover {{
            background: #818cf8;
            border-color: #818cf8;
            color: #fff;
        }}
        html[data-theme="light"] .btn-task-preview {{
            border-color: rgba(0, 0, 0, 0.15);
            color: #475569;
        }}

        /* ─── PDF MODAL FULL SCREEN ─── */
        .pdf-modal-overlay {{
            display: none;
            position: fixed;
            inset: 0;
            z-index: 99999;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(8px);
            align-items: center;
            justify-content: center;
            padding: 1.5rem;
        }}
        .pdf-modal-overlay.open {{ display: flex; }}
        .pdf-modal-card {{
            background: #0f172a;
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 18px;
            width: 100%;
            max-width: 960px;
            height: 90vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            box-shadow: 0 25px 70px rgba(0, 0, 0, 0.6);
        }}
        html[data-theme="light"] .pdf-modal-card {{
            background: #f8fafc;
            border-color: rgba(0, 0, 0, 0.15);
        }}
        .pdf-modal-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 1rem 1.4rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }}
        html[data-theme="light"] .pdf-modal-header {{
            border-bottom-color: rgba(0, 0, 0, 0.08);
        }}
        .pdf-modal-title {{
            font-size: 1rem;
            font-weight: 700;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }}
        html[data-theme="light"] .pdf-modal-title {{ color: #1e293b; }}
        .btn-modal-close {{
            width: 34px;
            height: 34px;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.08);
            border: none;
            color: #fff;
            cursor: pointer;
            font-size: 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .btn-modal-close:hover {{ background: rgba(239, 68, 68, 0.3); color: #f87171; }}
        .pdf-modal-body {{
            flex: 1;
            position: relative;
        }}
        .pdf-modal-body iframe {{
            width: 100%;
            height: 100%;
            border: none;
        }}
    </style>
</head>
<body>
    <div class="ambient-bg">
        <div class="blob blob-1"></div>
        <div class="blob blob-2"></div>
        <div class="blob blob-3"></div>
    </div>

    <!-- ══════ NAVIGATION BAR ══════ -->
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
            <li><a href="index.html">Beranda</a></li>
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

    <!-- Mobile Drawer -->
    <div class="mobile-nav-overlay" id="mobile-overlay"></div>
    <div class="mobile-nav-drawer" id="mobile-drawer">
        <a href="index.html"><i class="fa-solid fa-house" style="margin-right:.5rem;color:var(--primary-light);"></i> Beranda</a>
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

    <!-- ══════ MAIN CONTAINER ══════ -->
    <div style="margin-top: 120px; margin-bottom: 6rem;">
        <div class="course-container">

            <!-- Back Link -->
            <a href="seminar.html" class="back-nav-link">
                <i class="fa-solid fa-arrow-left"></i> Kembali ke Seminar PPL
            </a>

            <!-- Header Hero -->
            <div class="course-hero">
                <span class="course-eyebrow">{c['badge']}</span>
                <h1 class="course-main-title">{c['title']}</h1>
                <p class="course-main-subtitle">{c['subtitle']}</p>
                <div class="course-hero-line"></div>
            </div>

            <!-- Segmented Pill Tabs Navigation (MATCHES SCREENSHOT) -->
            <div class="course-tabs-wrapper">
                <div class="course-tabs-nav" role="tablist">
                    <button class="tab-btn-pill active" data-tab="tab-4c" onclick="switchMainTab('tab-4c', this)">
                        <i class="fa-solid fa-book-open"></i> Refleksi 4C
                    </button>
                    <button class="tab-btn-pill" data-tab="tab-artefak" onclick="switchMainTab('tab-artefak', this)">
                        <i class="fa-solid fa-magnifying-glass"></i> Analisis Artefak
                    </button>
                    <button class="tab-btn-pill" data-tab="tab-hasil" onclick="switchMainTab('tab-hasil', this)">
                        <i class="fa-solid fa-compass"></i> Kaitan Praktis
                    </button>
                    <button class="tab-btn-pill" data-tab="tab-lembar" onclick="switchMainTab('tab-lembar', this)">
                        <i class="fa-solid fa-file-arrow-down"></i> Lembar Refleksi
                    </button>
                    <button class="tab-btn-pill" data-tab="tab-tugas" onclick="switchMainTab('tab-tugas', this)">
                        <i class="fa-solid fa-folder"></i> Tugas Perkuliahan
                    </button>
                </div>
            </div>

            <!-- ════════ TAB 1: REFLEKSI 4C ════════ -->
            <div class="tab-panel-section active" id="tab-4c">
                <div class="content-card-box">
                    <div class="section-badge badge-purple">Bagian 1</div>
                    <div class="card-header-row">
                        <div class="card-header-icon" style="background:rgba(8,98,136,0.22); color:#97D7FF;">
                            <i class="fa-solid fa-rotate"></i>
                        </div>
                        <div>
                            <h2 class="card-header-title">Refleksi 4C</h2>
                            <p style="color:var(--text-muted);font-size:0.88rem;margin:0.2rem 0 0;">Uraian mengenai connection, challenge, concept, dan change terkait peran Bapak/Ibu sebagai pendidik.</p>
                        </div>
                    </div>

                    <div class="grid-4c">
                        <!-- Connection -->
                        <div class="c4-box conn">
                            <span class="c4-tag"><i class="fa-solid fa-link"></i> Connection</span>
                            <div class="c4-question">1. Apa keterkaitan materi perkuliahan dengan peran saya sebagai calon guru?</div>
                            <p class="c4-text">{q1}</p>
                        </div>

                        <!-- Challenge -->
                        <div class="c4-box chal">
                            <span class="c4-tag"><i class="fa-solid fa-bolt"></i> Challenge</span>
                            <div class="c4-question">2. Apa saja materi perkuliahan yang berbeda dari praktik yang saya lakukan selama ini?</div>
                            <p class="c4-text">{q2}</p>
                        </div>

                        <!-- Concept -->
                        <div class="c4-box conc">
                            <span class="c4-tag"><i class="fa-solid fa-lightbulb"></i> Concept</span>
                            <div class="c4-question">3. Apa saja konsep utama dan penting yang telah saya pelajari sebagai calon guru?</div>
                            <p class="c4-text">{q3}</p>
                        </div>

                        <!-- Change -->
                        <div class="c4-box chan">
                            <span class="c4-tag"><i class="fa-solid fa-seedling"></i> Change</span>
                            <div class="c4-question">4. Apa saja perubahan yang ingin saya lakukan setelah mendapatkan materi perkuliahan ini?</div>
                            <p class="c4-text">{q4}</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ════════ TAB 2: ANALISIS ARTEFAK ════════ -->
            <div class="tab-panel-section" id="tab-artefak">
                <div class="content-card-box">
                    <div class="section-badge badge-green">Bagian 2</div>
                    <div class="card-header-row">
                        <div class="card-header-icon" style="background:rgba(8,98,136,0.22); color:#97D7FF;">
                            <i class="fa-solid fa-magnifying-glass"></i>
                        </div>
                        <div>
                            <h2 class="card-header-title">Analisis Artefak</h2>
                            <p style="color:var(--text-muted);font-size:0.88rem;margin:0.2rem 0 0;">Identifikasi artefak pembelajaran yang menjadi bukti dukung hasil refleksi Anda beserta alasannya.</p>
                        </div>
                    </div>

                    <!-- 3 Pertanyaan Analisis Artefak -->
                    <div style="display:flex;flex-direction:column;gap:1.2rem;margin-bottom:2rem;">
                        <div style="background:rgba(0,0,0,0.2);padding:1.4rem;border-radius:14px;border:1px solid rgba(255,255,255,0.06);">
                            <div style="font-weight:700;color:#fff;margin-bottom:0.4rem;font-size:0.95rem;">
                                <i class="fa-solid fa-circle-question" style="color:#10b981;margin-right:6px;"></i> 1. Mana saja artefak pembelajaran yang dapat saya jadikan bukti dukung hasil refleksi ini?
                            </div>
                            <p style="font-size:0.9rem;line-height:1.75;color:#f1f5f9;margin:0;">{art_q1}</p>
                        </div>

                        <div style="background:rgba(0,0,0,0.2);padding:1.4rem;border-radius:14px;border:1px solid rgba(255,255,255,0.06);">
                            <div style="font-weight:700;color:#fff;margin-bottom:0.4rem;font-size:0.95rem;">
                                <i class="fa-solid fa-circle-question" style="color:#10b981;margin-right:6px;"></i> 2. Mengapa artefak tersebut yang saya pilih?
                            </div>
                            <p style="font-size:0.9rem;line-height:1.75;color:#f1f5f9;margin:0;">{art_q2}</p>
                        </div>

                        <div style="background:rgba(0,0,0,0.2);padding:1.4rem;border-radius:14px;border:1px solid rgba(255,255,255,0.06);">
                            <div style="font-weight:700;color:#fff;margin-bottom:0.4rem;font-size:0.95rem;">
                                <i class="fa-solid fa-circle-question" style="color:#10b981;margin-right:6px;"></i> 3. Bagian mana dari artefak ini yang mendukung hasil refleksi saya?
                            </div>
                            <p style="font-size:0.9rem;line-height:1.75;color:#f1f5f9;margin:0;">{art_q3}</p>
                        </div>
                    </div>

                    <h3 style="font-family:'Outfit',sans-serif;font-size:1.25rem;color:#fff;margin-bottom:1rem;">Daftar Berkas Artefak Pembelajaran</h3>
                    <div class="artefak-grid">
                        {artefak_cards_html}
                    </div>
                </div>
            </div>

            <!-- ════════ TAB 3: KAITAN PRAKTIS ════════ -->
            <div class="tab-panel-section" id="tab-hasil">
                <div class="content-card-box">
                    <div class="section-badge badge-amber">Bagian 3</div>
                    <div class="card-header-row">
                        <div class="card-header-icon" style="background:rgba(8,98,136,0.22); color:#97D7FF;">
                            <i class="fa-solid fa-compass"></i>
                        </div>
                        <div>
                            <h2 class="card-header-title">Kaitan Praktis</h2>
                            <p style="color:var(--text-muted);font-size:0.88rem;margin:0.2rem 0 0;">Penjelasan mengenai konsep utama yang dipelajari serta perubahan yang ingin dilakukan di masa depan</p>
                        </div>
                    </div>

                    <div class="quote-box">
                        "Kesiapan menjadi seorang guru tidak hanya ditentukan oleh penguasaan materi teknis, tetapi oleh kesediaan untuk terus belajar, memahami karakteristik peserta didik, menjadi teladan, serta berkomitmen menjalankan peran sebagai pendidik nilai."
                    </div>

                    <div class="hasil-refleksi-text">
                        <p>{hasil}</p>
                    </div>

                    <div style="margin-top:2.5rem;padding:1.6rem;border-radius:16px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);">
                        <h4 style="color:#fff;font-size:1.05rem;margin-bottom:0.8rem;display:flex;align-items:center;gap:0.5rem;">
                            <i class="fa-solid fa-lightbulb" style="color:#97D7FF;"></i> Rencana Perubahan &amp; Implementasi Nyata di Masa Depan
                        </h4>
                        <ul style="color:#f1f5f9;font-size:0.92rem;line-height:1.8;padding-left:1.4rem;margin:0;">
                            <li>Menerapkan paradigma berpusat pada peserta didik di sekolah dengan menghargai keunikan latar belakang dan gaya belajar setiap anak.</li>
                            <li>Mengintegrasikan asesmen diagnostik dan formatif berkelanjutan untuk memandu proses belajar, bukan sekadar vonis nilai akhir.</li>
                            <li>Menumbuhkan iklim kelas aman, terbuka, dan ramah kesalahan melalui pembiasaan pola pikir bertumbuh (Growth Mindset).</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- ════════ TAB 4: LEMBAR REFLEKSI (PDF ASLI) ════════ -->
            <div class="tab-panel-section" id="tab-lembar">
                <div class="content-card-box">
                    <div class="section-badge badge-purple">Bagian 4</div>
                    <div class="card-header-row">
                        <div class="card-header-icon" style="background:rgba(99,102,241,0.18); color:#818cf8;">
                            <i class="fa-solid fa-file-pdf"></i>
                        </div>
                        <div style="flex:1;">
                            <h2 class="card-header-title">Dokumen Lembar Kerja Refleksi (LK 2)</h2>
                            <p style="color:var(--text-muted);font-size:0.88rem;margin:0.2rem 0 0;">Pratinjau dokumen asli LK 2 Refleksi Pengalaman Belajar Mahasiswa PPG Prajabatan</p>
                        </div>
                        <div style="display:flex;gap:0.6rem;">
                            <a href="{c['ref_pdf']}" target="_blank" class="btn-action-view" style="padding:0.55rem 1.1rem;">
                                <i class="fa-solid fa-arrow-up-right-from-square"></i> Buka Tab Baru
                            </a>
                            <a href="{c['ref_pdf']}" download class="btn-action-dl" style="padding:0.55rem 1.1rem;">
                                <i class="fa-solid fa-download"></i> Unduh PDF
                            </a>
                        </div>
                    </div>

                    <!-- Embed Iframe -->
                    <iframe class="pdf-viewer-frame" src="{c['ref_pdf']}#toolbar=1&navpanes=1&scrollbar=1" title="Dokumen Refleksi PDF"></iframe>
                </div>
            </div>

            <!-- ════════ TAB 5: TUGAS PERKULIAHAN (MATCHES SCREENSHOT) ════════ -->
            <div class="tab-panel-section" id="tab-tugas">
                <div class="tugas-layout-grid">

                    <!-- Kolom Kiri: DAFTAR ISI (Sticky Sidebar) -->
                    <aside class="sidebar-daftar-isi">
                        <div class="sidebar-header">
                            <i class="fa-solid fa-list-ul"></i>
                            <span>Daftar Isi</span>
                        </div>
                        <div class="sidebar-menu">
                            {topics_sidebar_html}
                        </div>
                    </aside>

                    <!-- Kolom Kanan: Main Content (BAGIAN 5) -->
                    <main class="content-card-box" style="margin-bottom:0;">
                        <div class="section-badge badge-green">Bagian 5</div>
                        <div class="card-header-row">
                            <div class="card-header-icon" style="background:rgba(16,185,129,0.18); color:#10b981;">
                                <i class="fa-solid fa-folder-open"></i>
                            </div>
                            <div>
                                <h2 class="card-header-title">Tugas {c['short_title']}</h2>
                            </div>
                        </div>

                        <p style="font-size:0.92rem;line-height:1.75;color:#e2e8f0;margin-bottom:2rem;">
                            Berikut adalah kumpulan berkas tugas yang telah dikerjakan selama mengikuti perkuliahan {c['short_title']}, dikelompokkan berdasarkan topik pembelajaran:
                        </p>

                        <!-- Topic List & Tasks -->
                        <div id="topicsContainer">
                            {topics_content_html}
                        </div>
                    </main>

                </div>
            </div>

        </div>
    </div>

    <!-- ══════ PDF MODAL PREVIEW POPUP ══════ -->
    <div class="pdf-modal-overlay" id="pdfModalOverlay" onclick="handlePdfOverlayClick(event)">
        <div class="pdf-modal-card">
            <div class="pdf-modal-header">
                <div class="pdf-modal-title">
                    <i class="fa-solid fa-file-pdf" style="color:#ef4444;"></i>
                    <span id="pdfModalTitleText">Dokumen Tugas</span>
                </div>
                <div style="display:flex;gap:0.5rem;align-items:center;">
                    <a id="pdfModalDlBtn" href="#" download class="btn-action-dl" style="padding:0.4rem 0.85rem;font-size:0.8rem;">
                        <i class="fa-solid fa-download"></i> Unduh
                    </a>
                    <button class="btn-modal-close" onclick="closePdfModal()"><i class="fa-solid fa-xmark"></i></button>
                </div>
            </div>
            <div class="pdf-modal-body">
                <iframe id="pdfModalIframe" src="" title="PDF Viewer"></iframe>
            </div>
        </div>
    </div>

    <!-- ══════ FOOTER ══════ -->
    <footer>
        <div class="container">
            <h3 style="font-family:'Outfit',sans-serif;font-size:1.5rem;margin-bottom:1rem;">E-Portfolio Pendidikan Profesi Guru</h3>
            <p>&copy; 2026 Disusun untuk memenuhi komponen penilaian Seminar PPL.</p>
            <p style="margin-top:0.5rem;font-size:0.9rem;color:rgba(255,255,255,0.4);">
                Lutfi Subekti &nbsp;·&nbsp; PPG Prajabatan Gelombang 1 &nbsp;·&nbsp; Universitas Negeri Malang
            </p>
        </div>
    </footer>

    <!-- ══════ JAVASCRIPT CONTROLLERS ══════ -->
    <script>
        function switchMainTab(tabId, el) {{
            document.querySelectorAll('.tab-btn-pill').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.tab-panel-section').forEach(p => p.classList.remove('active'));

            if (el) el.classList.add('active');
            const target = document.getElementById(tabId);
            if (target) {{
                target.classList.add('active');
            }}

            history.replaceState(null, null, '#' + tabId);
        }}

        function switchTopic(topicId, el) {{
            document.querySelectorAll('.sidebar-item').forEach(item => item.classList.remove('active'));
            if (el) el.classList.add('active');

            const allSections = document.querySelectorAll('.topic-section-box');
            if (topicId === 'all') {{
                allSections.forEach(sec => sec.style.display = 'block');
            }} else {{
                allSections.forEach(sec => {{
                    if (sec.id === 'section-' + topicId) {{
                        sec.style.display = 'block';
                        sec.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                    }} else {{
                        sec.style.display = 'none';
                    }}
                }});
            }}
        }}

        function openPdfModalDirect(pdfUrl, title) {{
            const overlay = document.getElementById('pdfModalOverlay');
            const iframe = document.getElementById('pdfModalIframe');
            const titleEl = document.getElementById('pdfModalTitleText');
            const dlBtn = document.getElementById('pdfModalDlBtn');

            titleEl.textContent = title || 'Dokumen';
            iframe.src = pdfUrl;
            dlBtn.href = pdfUrl;
            dlBtn.download = (title || 'Dokumen') + '.pdf';
            overlay.classList.add('open');
            document.body.style.overflow = 'hidden';
        }}

        function closePdfModal() {{
            const overlay = document.getElementById('pdfModalOverlay');
            const iframe = document.getElementById('pdfModalIframe');
            overlay.classList.remove('open');
            iframe.src = '';
            document.body.style.overflow = '';
        }}

        function handlePdfOverlayClick(e) {{
            if (e.target.id === 'pdfModalOverlay') closePdfModal();
        }}

        window.addEventListener('DOMContentLoaded', () => {{
            const hash = window.location.hash.replace('#', '');
            if (hash) {{
                if (hash.startsWith('topik-')) {{
                    const tabTugasBtn = document.querySelector(`.tab-btn-pill[data-tab="tab-tugas"]`);
                    if (tabTugasBtn) switchMainTab('tab-tugas', tabTugasBtn);
                    const topicBtn = document.querySelector(`.sidebar-item[data-topic="${{hash}}"]`);
                    if (topicBtn) switchTopic(hash, topicBtn);
                }} else {{
                    const targetBtn = document.querySelector(`.tab-btn-pill[data-tab="${{hash}}"]`);
                    if (targetBtn) {{
                        switchMainTab(hash, targetBtn);
                    }}
                }}
            }}
        }});

        const themeToggle = document.getElementById('theme-toggle');
        const htmlEl = document.documentElement;
        const icon = themeToggle ? themeToggle.querySelector('i') : null;
        const savedTheme = localStorage.getItem('theme');

        function applyTheme(t) {{
            if (t === 'light') {{
                htmlEl.setAttribute('data-theme', 'light');
                if (icon) icon.classList.replace('fa-moon', 'fa-sun');
            }} else {{
                htmlEl.removeAttribute('data-theme');
                if (icon) icon.classList.replace('fa-sun', 'fa-moon');
            }}
        }}
        applyTheme(savedTheme || 'dark');

        if (themeToggle) {{
            themeToggle.addEventListener('click', () => {{
                const newT = htmlEl.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
                localStorage.setItem('theme', newT);
                applyTheme(newT);
            }});
        }}

        const tmMobile = document.getElementById('theme-toggle-mobile');
        if (tmMobile) {{
            const mi = tmMobile.querySelector('i');
            if (savedTheme === 'light' && mi) mi.classList.replace('fa-moon', 'fa-sun');
            tmMobile.addEventListener('click', () => {{
                if (themeToggle) themeToggle.click();
                const isDark = !htmlEl.hasAttribute('data-theme');
                if (mi) {{
                    mi.classList.toggle('fa-moon', isDark);
                    mi.classList.toggle('fa-sun', !isDark);
                }}
            }});
        }}

        const hBtn = document.getElementById('hamburger-btn');
        const mDrawer = document.getElementById('mobile-drawer');
        const mOverlay = document.getElementById('mobile-overlay');

        if (hBtn && mDrawer && mOverlay) {{
            const openD = () => {{
                hBtn.classList.add('open');
                mDrawer.classList.add('open');
                mOverlay.classList.add('active');
                document.body.style.overflow = 'hidden';
            }};
            const closeD = () => {{
                hBtn.classList.remove('open');
                mDrawer.classList.remove('open');
                mOverlay.classList.remove('active');
                document.body.style.overflow = '';
            }};
            hBtn.addEventListener('click', () => mDrawer.classList.contains('open') ? closeD() : openD());
            mOverlay.addEventListener('click', closeD);
            mDrawer.querySelectorAll('a').forEach(l => l.addEventListener('click', closeD));
        }}
    </script>
    <script src="dropdown.js"></script>
</body>
</html>
"""

def main():
    for c in courses:
        content = generate_page_html(c)
        with open(c['file'], 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Generated {c['file']} successfully ({len(content)} chars)")

if __name__ == '__main__':
    main()
