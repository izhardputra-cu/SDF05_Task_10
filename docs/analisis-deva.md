# Analisis — Deva Agriani

## 1. Mengapa menggunakan pytest.approx?

Bilangan pecahan desimal tidak selalu dapat disimpan secara tepat dalam bentuk
biner. Akibatnya, hasil operasi bisa sedikit berbeda dari angka desimal yang
kita harapkan. `pytest.approx` membandingkan angka dengan toleransi kecil,
sehingga test tidak gagal hanya karena selisih representasi floating point.
Nilai harapan tetap dihitung dari aturan soal, bukan disalin dari rumus fungsi.

## 6. Apakah total anggota selalu lebih besar daripada subtotal?

Tidak. Setelah diskon 10% dan pajak 11%, hasilnya adalah
`subtotal × 0,90 × 1,11 = subtotal × 0,999`.
Untuk subtotal 100, nilai setelah diskon adalah 90 dan totalnya 99,9.
Jadi total anggota sedikit lebih kecil daripada subtotal jika subtotal positif.
Jika subtotal nol, totalnya juga nol. Contoh ini diperiksa pada test total anggota.
