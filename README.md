# SDF05 Task 10 — Kelompok 7

Tugas praktik unit testing dan pengujian mutasi pada modul `pricing.py`.
Kode acuan mengikuti soal Sesi 10 tanpa mengubah aturan bisnisnya.

## Anggota

| Nama | NIM | Bagian |
| --- | --- | --- |
| Izhar Rahman Dwiputra | 25120300032 | Test total, mutasi, analisis 3–4, dan integrasi |
| Deva Agriani | 25120300026 | Test subtotal dan diskon, analisis 1 dan 6 |
| Muhammad Miftahhul Fauzi | 25120300009 | Test pajak dan struk, analisis 2 dan 5 |

## Isi tugas

- `pricing.py`: kode acuan dari soal.
- `tests/`: unit test menggunakan PyTest.
- `docs/`: jawaban analisis dan hasil pengujian mutasi.
- `bukti/`: keluaran pengujian.

## Hasil akhir

Seluruh bagian anggota sudah digabung. Pengujian menghasilkan **14 fungsi test
/ 29 kasus lulus**, dan ketiga mutasi berhasil terdeteksi.
`pricing.py` tetap sama dengan kode acuan awal.

| Artefak | Berkas |
| --- | --- |
| Kode acuan | [pricing.py](pricing.py) |
| Unit test | [tests/](tests/) |
| Keluaran `pytest -v` seluruh test | [bukti/pytest-v.txt](bukti/pytest-v.txt) |
| Tabel dan bukti tiga mutasi | [docs/hasil-mutasi.md](docs/hasil-mutasi.md) |
| Analisis nomor 1 dan 6 | [docs/analisis-deva.md](docs/analisis-deva.md) |
| Analisis nomor 2 dan 5 | [docs/analisis-miftahhul.md](docs/analisis-miftahhul.md) |
| Analisis nomor 3 dan 4 | [docs/analisis-izhar.md](docs/analisis-izhar.md) |

Test mencakup subtotal, penolakan harga negatif dan kuantitas tidak valid,
diskon anggota, pajak, total, serta isi struk termasuk baris baru terakhir.
Fitur PyTest yang digunakan adalah `parametrize`, `raises`, `approx`, dan `tmp_path`.
Pengujian memakai Python 3.9.6 dan PyTest 8.4.2.

`bukti/pytest-izhar.txt` disimpan sebagai riwayat pengujian bagian Izhar.
Hasil akhir kelompok mengacu pada `bukti/pytest-v.txt` dan bukti mutasi terbaru.
