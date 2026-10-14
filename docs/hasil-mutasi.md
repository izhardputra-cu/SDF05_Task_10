# Hasil pengujian mutasi — tahap Izhar

Pengujian ini menggunakan empat fungsi test pada `tests/test_total.py` (sembilan
kasus setelah parameterisasi). Ini belum merupakan pengujian gabungan kelompok.
Kode benar lulus seluruh kasus; keluaran tersedia di `bukti/pytest-izhar.txt`.

Setiap mutasi dijalankan secara berurutan pada salinan sementara yang baru dari
`pricing.py` acuan. Mutasi tidak ditumpuk dan kode acuan tidak diubah.

| Kerusakan buatan | Test yang gagal | Kesimpulan daya deteksi |
| --- | --- | --- |
| Diskon anggota dihilangkan | `tests/test_total.py::test_total_member[100-1-99.9]`<br>`tests/test_total.py::test_total_member[12500-2-24975]`<br>`tests/test_total.py::test_total_member[19.99-3-59.91003]` | Terdeteksi: assertion/pengecualian tidak terpenuhi |
| Pajak diubah menjadi 12% | `tests/test_total.py::test_total_member[100-1-99.9]`<br>`tests/test_total.py::test_total_member[12500-2-24975]`<br>`tests/test_total.py::test_total_member[19.99-3-59.91003]`<br>`tests/test_total.py::test_total_non_member` | Terdeteksi: assertion/pengecualian tidak terpenuhi |
| Validasi kuantitas dihapus | `tests/test_total.py::test_total_invalid_input[100-0-quantity must be positive]`<br>`tests/test_total.py::test_total_invalid_input[100--2-quantity must be positive]` | Terdeteksi: assertion/pengecualian tidak terpenuhi |

Keluaran lengkap masing-masing percobaan tersedia di `bukti/mutasi-01.txt`,
`bukti/mutasi-02.txt`, dan `bukti/mutasi-03.txt`.
Ketiga mutasi terdeteksi oleh test total. Hasil ini tidak membuktikan semua jenis
kesalahan pasti terdeteksi. Setelah bagian anggota lain digabung, pengujian
normal dan mutasi perlu dijalankan ulang dengan seluruh test.
