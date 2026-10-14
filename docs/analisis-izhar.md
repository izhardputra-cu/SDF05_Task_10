# Analisis — Izhar Rahman Dwiputra

## 3. Test yang paling lemah

Di bagian saya, `test_total_zero_price` paling lemah untuk memeriksa tarif diskon
dan pajak. Hasil nol tetap nol meskipun tarif salah, sehingga test ini tidak
mendeteksi dua mutasi tarif/perhitungan. Namun, test ini tetap berguna untuk
memastikan harga nol diterima. Perbaikannya adalah melengkapinya dengan nilai
positif dan pecahan, seperti pada `test_total_member`, serta kasus non-anggota.
Dengan begitu, nilai harapan yang konkret bisa membedakan rumus benar dan salah.

## 4. Pengaruh hasil mutasi terhadap penilaian kualitas test

Test yang lulus pada kode benar belum tentu bisa menemukan kesalahan. Dalam
percobaan ini, diskon yang dihapus dan tarif pajak yang diganti membuat test total
gagal. Validasi kuantitas yang dihapus juga menyebabkan kasus kuantitas nol dan
negatif gagal karena ValueError tidak muncul. Artinya test tersebut menjaga
perilaku yang diperiksa, bukan hanya menjalankan fungsi. Kasus harga nol masih
lulus pada mutasi diskon dan pajak; karena itu diperlukan variasi kasus yang
saling melengkapi. Tiga mutasi terdeteksi tidak berarti semua bug sudah tercakup.
