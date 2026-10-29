/**
 * Dropdown Click Toggle — E-Portfolio PPG
 * Perilaku:
 *   - Klik pertama pada "Semester 1/2" → buka dropdown pilihan sub-halaman
 *   - Klik kedua pada tombol yang sama  → navigasi ke halaman semester tersebut
 *   - Klik item di dalam dropdown       → navigasi langsung ke sub-halaman
 *   - Klik di luar / Escape            → tutup dropdown
 */
(function () {
    'use strict';

    document.addEventListener('DOMContentLoaded', function () {
        const dropdowns = document.querySelectorAll('.nav-links li.dropdown');

        dropdowns.forEach(function (dropdown) {
            const btn = dropdown.querySelector('a.dropbtn');
            if (!btn) return;

            btn.addEventListener('click', function (e) {
                const isOpen = dropdown.classList.contains('dropdown-open');

                if (!isOpen) {
                    // Klik pertama → buka dropdown, jangan navigasi
                    e.preventDefault();
                    e.stopPropagation();

                    // Tutup semua dropdown lain
                    dropdowns.forEach(function (d) {
                        d.classList.remove('dropdown-open');
                    });

                    dropdown.classList.add('dropdown-open');
                } else {
                    // Klik kedua (dropdown sudah terbuka) → navigasi ke href
                    // Biarkan e.preventDefault() TIDAK dipanggil → link berjalan normal
                    dropdown.classList.remove('dropdown-open');
                    // navigasi berjalan secara alami via href
                }
            });
        });

        // Klik di luar navbar → tutup semua dropdown
        document.addEventListener('click', function () {
            dropdowns.forEach(function (d) {
                d.classList.remove('dropdown-open');
            });
        });

        // Klik pada navbar sendiri (bukan dropbtn) tidak menutup dropdown
        const navbar = document.getElementById('navbar');
        if (navbar) {
            navbar.addEventListener('click', function (e) {
                // Hanya stop propagation jika bukan link sub-menu
                const isSubLink = e.target.closest('.dropdown-content a');
                if (!isSubLink) {
                    e.stopPropagation();
                }
            });
        }

        // Tekan Escape → tutup semua dropdown
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') {
                dropdowns.forEach(function (d) {
                    d.classList.remove('dropdown-open');
                });
            }
        });
    });
})();
