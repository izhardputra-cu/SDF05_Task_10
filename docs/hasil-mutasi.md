# Hasil pengujian mutasi

Pengujian akhir menggunakan seluruh bagian Izhar, Deva, dan Miftahhul: **14 fungsi
test dengan 29 kasus setelah parameterisasi**. Pada kode benar, semuanya lulus.
Keluaran `pytest -v` tersedia di [bukti pengujian](../bukti/pytest-v.txt).

Setiap kerusakan berikut diterapkan secara berurutan pada salinan sementara yang
baru dari `pricing.py` acuan. Seluruh test disalin dan dijalankan dengan
`pytest -v` untuk setiap mutasi. Mutasi tidak ditumpuk; kode acuan di repository
tetap sama dengan versi awal dari soal.

| Kerusakan buatan | Test yang gagal | Kesimpulan daya deteksi |
| --- | --- | --- |
| Penerapan diskon dihapus | `tests/test_subtotal_discount.py::test_member_discount[200-True-180]`<br>`tests/test_subtotal_discount.py::test_member_discount[59.97-True-53.973]`<br>`tests/test_total.py::test_total_member[100-1-99.9]`<br>`tests/test_total.py::test_total_member[12500-2-24975]`<br>`tests/test_total.py::test_total_member[19.99-3-59.91003]` | Terdeteksi: 5 kasus gagal |
| Tarif pajak diubah dari 11% menjadi 12% | `tests/test_tax_receipt.py::test_add_tax[100-111]`<br>`tests/test_tax_receipt.py::test_add_tax[180-199.8]`<br>`tests/test_tax_receipt.py::test_add_tax[53.973-59.91003]`<br>`tests/test_total.py::test_total_member[100-1-99.9]`<br>`tests/test_total.py::test_total_member[12500-2-24975]`<br>`tests/test_total.py::test_total_member[19.99-3-59.91003]`<br>`tests/test_total.py::test_total_non_member` | Terdeteksi: 7 kasus gagal |
| Validasi kuantitas dihapus | `tests/test_subtotal_discount.py::test_subtotal_invalid_quantity[0]`<br>`tests/test_subtotal_discount.py::test_subtotal_invalid_quantity[-1]`<br>`tests/test_subtotal_discount.py::test_subtotal_invalid_quantity[-5]`<br>`tests/test_total.py::test_total_invalid_input[100-0-quantity must be positive]`<br>`tests/test_total.py::test_total_invalid_input[100--2-quantity must be positive]` | Terdeteksi: 5 kasus gagal |

Keluaran lengkap:

- [Mutasi 1: diskon dihapus](../bukti/mutasi-01.txt)
- [Mutasi 2: pajak diubah](../bukti/mutasi-02.txt)
- [Mutasi 3: validasi kuantitas dihapus](../bukti/mutasi-03.txt)

Ketiga kerusakan terdeteksi. Test diskon dan total mendeteksi perubahan diskon;
test pajak dan total mendeteksi tarif pajak yang salah; test subtotal dan total
mendeteksi validasi kuantitas yang hilang karena ValueError tidak muncul.
Kasus dengan nilai nol tetap lulus pada mutasi tarif, sehingga perlu dilengkapi
kasus bernilai positif. Hasil ini menunjukkan daya deteksi terhadap tiga
kerusakan yang dicoba, bukan jaminan bahwa seluruh kemungkinan bug sudah tercakup.
