# Analisis — Muhammad Miftahhul Fauzi

## 2. Mengapa menggunakan tmp_path?

File tetap di direktori proyek bisa menimpa data, meninggalkan file sisa, atau
membuat test bergantung pada hasil test sebelumnya. `tmp_path` menyediakan
direktori sementara yang unik untuk setiap test. Kita bisa memeriksa isi struk
secara nyata tanpa mengganggu file proyek dan tanpa berebut path antar-test.

## 5. Padanan fitur PyTest dan JUnit 5

| PyTest | JUnit 5 | Kegunaan |
| --- | --- | --- |
| `pytest.raises` | `assertThrows` | Memastikan pengecualian yang diharapkan muncul |
| `pytest.mark.parametrize` | `@ParameterizedTest` bersama `@CsvSource` atau `@ValueSource` | Menjalankan test dengan beberapa input |
| Fixture untuk penyiapan | `@BeforeEach` | Menyiapkan kebutuhan sebelum setiap test |
| Fixture `tmp_path` | `@TempDir` | Menyediakan direktori sementara |

Fixture PyTest lebih luas daripada `@BeforeEach`, karena dapat memberikan nilai
melalui parameter test dan mempunyai beberapa scope. Padanan di tabel menunjukkan
fungsi penyiapannya, bukan berarti semua perilakunya identik.
