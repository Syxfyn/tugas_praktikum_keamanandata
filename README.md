# tugas_praktikum_keamanandata
implementasi program GUI (Graphical User Interface) menggunakan **Tkinter** di Python untuk melakukan **enkripsi** dan **dekripsi teks** dengan menggunakan algoritma Caesar Cipher. Berikut adalah cara kerjanya:

---

### **Fungsi Utama**

1. **Fungsi `enkripsi(plain_text, shift)`**
   - Melakukan enkripsi teks biasa (plain text) menjadi teks terenkripsi (cipher text) menggunakan Caesar Cipher.
   - **Prosesnya:**
     - Setiap huruf di `plain_text` digeser sejauh `shift` posisi dalam alfabet.
     - Huruf besar dan kecil diproses secara terpisah untuk menjaga kapitalisasi.
     - Karakter non-alfabet (misalnya spasi atau tanda baca) tidak berubah.

2. **Fungsi `dekripsi(chiper_text, shift)`**
   - Mengembalikan teks terenkripsi menjadi teks asli.
   - **Prosesnya:**
     - Huruf pada `chiper_text` digeser mundur sejauh `shift` posisi.
     - Sama seperti fungsi enkripsi, kapitalisasi huruf tetap dijaga, dan karakter non-alfabet tidak berubah.

3. **Fungsi `encrypt_text()`**
   - Di-trigger saat tombol **Encrypt** ditekan.
   - **Prosesnya:**
     - Membaca teks dari input field `entry_plain_text`.
     - Membaca nilai `shift` dari input field `entry_shift` (harus integer antara 1-25).
     - Memanggil fungsi `enkripsi()` untuk melakukan enkripsi.
     - Menampilkan hasil enkripsi di `entry_chiper_text`.
     - Jika `shift` tidak valid, menampilkan pesan error.

4. **Fungsi `decrypt_text()`**
   - Di-trigger saat tombol **Decrypt** ditekan.
   - **Prosesnya:**
     - Membaca teks dari input field `entry_chiper_text`.
     - Membaca nilai `shift` dari input field `entry_shift`.
     - Memanggil fungsi `dekripsi()` untuk melakukan dekripsi.
     - Menampilkan hasil dekripsi di `entry_plain_text`.
     - Jika `shift` tidak valid, menampilkan pesan error.

---

### **Tampilan GUI**

1. **Komponen Utama:**
   - **Plain Text Input:** Tempat untuk memasukkan teks asli.
   - **Shift Input:** Tempat untuk memasukkan nilai pergeseran (1-25).
   - **Chiper Text Input:** Tempat untuk menampilkan teks terenkripsi atau menerima input untuk didekripsi.
   - **Encrypt Button:** Tombol untuk mengenkripsi teks.
   - **Decrypt Button:** Tombol untuk mendekripsi teks.

2. **Styling:**
   - Latar belakang aplikasi berwarna biru muda (`#add8e6`).
   - Teks label berwarna biru navy dengan font tebal.

3. **Alur Penggunaan:**
   - Masukkan teks di kolom **Plain Text**.
   - Masukkan nilai shift (1-25).
   - Tekan tombol **Encrypt** untuk mengenkripsi.
   - Teks hasil enkripsi muncul di kolom **Chiper Text**.
   - Masukkan teks di kolom **Chiper Text** dan tekan tombol **Decrypt** untuk mendekripsi kembali.

---

### **Flow Kerja Program**
1. **Input Validation:**
   - Program memastikan nilai `shift` berada dalam rentang 1-25.
   - Jika input tidak valid, pesan error ditampilkan.

2. **Enkripsi dan Dekripsi:**
   - Menggunakan operasi modular (`% 26`) untuk memastikan pergeseran tetap berada dalam alfabet.
   - ASCII digunakan untuk menghitung karakter baru berdasarkan pergeseran.

3. **Event Handling:**
   - Setiap tombol (Encrypt/Decrypt) memiliki fungsi yang dipanggil ketika ditekan.

---

### **Cara Menjalankan Program**
1. Simpan kode ke file Python, misalnya `caesar_cipher_gui.py`.
2. Jalankan program dengan Python:
   ```
   python caesar_cipher_gui.py
   ```
3. GUI akan muncul, dan Anda dapat mulai memasukkan teks untuk dienkripsi atau didekripsi.

Program ini memberikan cara sederhana untuk memahami Caesar Cipher melalui antarmuka grafis!


--------------------------------------------------------------------------------------------------------

aplikasi GUI untuk melakukan **enkripsi** dan **dekripsi** teks menggunakan algoritma **DES (Data Encryption Standard)** dengan antarmuka berbasis **Tkinter**. Berikut adalah cara kerja program ini:

---

#### 1. **Fungsi Pendukung**
- **`pad(text)`**
  - Fungsi untuk menambahkan padding pada teks sehingga panjangnya menjadi kelipatan 8 byte, karena DES hanya dapat memproses data dalam blok 8 byte.
  - Menambahkan spasi (`' '`) di akhir teks jika panjang teks tidak sesuai.

- **`encrypt(plain_text, key)`**
  - Melakukan enkripsi teks dengan algoritma DES menggunakan mode **ECB (Electronic Codebook)**.
  - **Prosesnya:**
    1. Membuat objek DES dengan kunci (`key`) sepanjang 8 byte.
    2. Melakukan padding pada teks jika diperlukan.
    3. Mengenkripsi teks yang sudah dipad menjadi data biner.
    4. Data biner dienkode ke format Base64 untuk mempermudah penyimpanan dan pengiriman.
  - **Return:** Teks terenkripsi dalam format Base64.

- **`decrypt(encrypted_text, key)`**
  - Melakukan dekripsi teks terenkripsi dengan algoritma DES.
  - **Prosesnya:**
    1. Membuat objek DES dengan kunci yang sama.
    2. Mendekode teks terenkripsi dari Base64 ke biner.
    3. Mendekripsi data biner.
    4. Menghapus padding tambahan di akhir teks.
  - **Return:** Teks asli setelah dekripsi.

---

#### 2. **Fungsi untuk Tombol GUI**
- **`perform_encryption()`**
  - Dipanggil ketika tombol **Encrypt** ditekan.
  - **Prosesnya:**
    1. Mengambil teks dari kolom **Input Text** dan kunci dari kolom **Key**.
    2. Memastikan panjang kunci adalah 8 karakter.
    3. Melakukan enkripsi teks dengan fungsi `encrypt`.
    4. Menampilkan hasil enkripsi di kolom **Output Text**.
    5. Jika panjang kunci tidak sesuai, menampilkan pesan error.

- **`perform_decryption()`**
  - Dipanggil ketika tombol **Decrypt** ditekan.
  - **Prosesnya:**
    1. Mengambil teks terenkripsi dari kolom **Input Text** dan kunci dari kolom **Key**.
    2. Memastikan panjang kunci adalah 8 karakter.
    3. Melakukan dekripsi teks dengan fungsi `decrypt`.
    4. Menampilkan hasil dekripsi di kolom **Output Text**.
    5. Jika terjadi kesalahan (misalnya kunci salah atau data tidak valid), menampilkan pesan error.

---

#### 3. **Antarmuka GUI**
- **Input Text:**
  - Tempat untuk memasukkan teks yang akan dienkripsi atau teks terenkripsi yang akan didekripsi.
- **Key:**
  - Kolom untuk memasukkan kunci DES. Kunci harus memiliki panjang **8 karakter**.
- **Output Text:**
  - Tempat untuk menampilkan hasil enkripsi atau dekripsi.
- **Tombol Encrypt dan Decrypt:**
  - Mengaktifkan fungsi `perform_encryption` atau `perform_decryption`.

---

### **Alur Kerja Program**
1. **Enkripsi:**
   - Masukkan teks di kolom **Input Text**.
   - Masukkan kunci (8 karakter) di kolom **Key**.
   - Klik tombol **Encrypt**.
   - Hasil enkripsi akan muncul di kolom **Output Text**.

2. **Dekripsi:**
   - Masukkan teks terenkripsi di kolom **Input Text**.
   - Masukkan kunci yang sama (8 karakter) di kolom **Key**.
   - Klik tombol **Decrypt**.
   - Teks asli akan muncul di kolom **Output Text**.

---

### **Catatan Penting**
1. **DES dan Kunci:**
   - DES menggunakan kunci sepanjang **8 byte** (64 bit). Jika panjang kunci tidak sesuai, enkripsi/dekripsi tidak akan berjalan.
   - Mode ECB yang digunakan dalam kode ini tidak aman untuk data sensitif karena pola teks asli dapat terlihat dalam hasil enkripsi. Mode yang lebih aman seperti **CBC** disarankan untuk penggunaan nyata.

2. **Base64:**
   - Format Base64 digunakan untuk menyandikan data biner hasil enkripsi agar dapat disimpan atau dikirim dengan mudah.

3. **Kesalahan Umum:**
   - **Kunci tidak 8 karakter:** Menampilkan pesan error.
   - **Data tidak valid untuk dekripsi:** Menampilkan pesan error dengan deskripsi masalah.

---

### **Cara Menjalankan Program**
1. Simpan kode ke file Python, misalnya `des_gui.py`.
2. Instal pustaka **pycryptodome** untuk mendukung algoritma DES:
   ```
   pip install pycryptodome
   ```
3. Jalankan program:
   ```
   python des_gui.py
   ```
4. Gunakan antarmuka untuk mengenkripsi dan mendekripsi teks.

--------------------------------------------------------------------------------------------------------

**aplikasi GUI** berbasis Python untuk **steganografi**, yaitu menyembunyikan pesan rahasia dalam sebuah gambar atau menampilkan pesan tersembunyi dari gambar menggunakan pustaka `stegano` (khususnya metode **LSB (Least Significant Bit)**). Berikut adalah cara kerja aplikasi:

---

#### 1. **Antarmuka Utama**
- Aplikasi dimulai dengan menu utama yang memberikan tiga opsi:
  - **Sembunyikan Pesan:** Untuk menyisipkan pesan ke dalam gambar.
  - **Tampilkan Pesan:** Untuk mengambil pesan tersembunyi dari gambar.
  - **Keluar:** Menutup aplikasi.

#### 2. **Mode Sembunyikan Pesan**
- Memungkinkan pengguna untuk:
  1. Memilih gambar asal (format `.png` atau `.jpg`) yang akan digunakan untuk menyimpan pesan rahasia.
  2. Memasukkan pesan rahasia yang ingin disisipkan.
  3. Memilih lokasi dan nama file baru untuk menyimpan gambar yang sudah berisi pesan.
- Proses:
  - Fungsi `process_hide`:
    1. Memastikan semua input (path gambar, pesan, dan path penyimpanan) diisi.
    2. Menggunakan `lsb.hide` dari pustaka `stegano` untuk menyisipkan pesan ke dalam gambar.
    3. Menyimpan gambar hasil dengan pesan tersembunyi ke path yang dipilih.
    4. Menampilkan notifikasi keberhasilan atau kesalahan.

#### 3. **Mode Tampilkan Pesan**
- Memungkinkan pengguna untuk:
  1. Memilih gambar yang diduga berisi pesan tersembunyi.
- Proses:
  - Fungsi `process_reveal`:
    1. Memastikan path gambar valid.
    2. Menggunakan `lsb.reveal` dari pustaka `stegano` untuk mengambil pesan tersembunyi.
    3. Menampilkan pesan jika ditemukan, atau memberi tahu pengguna bahwa tidak ada pesan tersembunyi.

#### 4. **Pengelolaan File**
- Fungsi `select_file`: Membuka dialog untuk memilih file gambar dari sistem.
- Fungsi `select_save_path`: Membuka dialog untuk menentukan lokasi penyimpanan file hasil.
- Format gambar yang didukung adalah **PNG** dan **JPG**.

---

### **Komponen Program**

#### 1. **Kelas `SteganografiApp`**
- **Konstruktor `__init__`**:
  - Menginisialisasi aplikasi, membuat jendela utama, dan menampilkan menu utama.

- **`create_main_menu`**:
  - Menampilkan menu utama dengan opsi untuk memilih mode operasi atau keluar dari aplikasi.

- **`load_menu`**:
  - Menampilkan formulir dan opsi sesuai mode (sembunyikan atau tampilkan pesan).

- **`process_hide`**:
  - Menangani penyisipan pesan ke dalam gambar menggunakan metode LSB.

- **`process_reveal`**:
  - Menangani pengambilan pesan tersembunyi dari gambar menggunakan metode LSB.

- **`select_file`** dan **`select_save_path`**:
  - Membantu pengguna memilih file input atau lokasi penyimpanan output.

- **`clear_frame`**:
  - Membersihkan elemen dalam frame sebelum menampilkan antarmuka baru.

#### 2. **Fungsi `lsb.hide` dan `lsb.reveal`**
- Bagian dari pustaka `stegano`:
  - **`lsb.hide(img_path, message)`**:
    - Menyisipkan pesan ke dalam gambar pada bit paling tidak signifikan.
  - **`lsb.reveal(img_path)`**:
    - Mengambil pesan tersembunyi dari gambar.

---

### **Alur Kerja Program**

1. **Pengguna Memilih Mode**:
   - Dari menu utama, pengguna memilih apakah ingin menyembunyikan pesan atau menampilkan pesan.

2. **Mode Sembunyikan Pesan**:
   - Pengguna memilih gambar asal, memasukkan pesan, dan menentukan lokasi penyimpanan.
   - Klik tombol "Sembunyikan":
     - Program menyisipkan pesan ke dalam gambar menggunakan `lsb.hide`.
     - Gambar baru dengan pesan tersembunyi disimpan ke lokasi yang dipilih.

3. **Mode Tampilkan Pesan**:
   - Pengguna memilih gambar yang ingin diperiksa.
   - Klik tombol "Tampilkan Pesan":
     - Program mengambil pesan dari gambar menggunakan `lsb.reveal`.
     - Pesan ditampilkan dalam dialog jika ditemukan.

4. **Notifikasi**:
   - Program menampilkan dialog keberhasilan atau kesalahan untuk setiap proses.

---

### **Cara Menjalankan Program**

1. **Instalasi Pustaka `stegano`**:
   ```
   pip install stegano
   ```

2. **Jalankan Program**:
   - Simpan kode dalam file Python (misalnya `steganografi_app.py`).
   - Jalankan:
     ```
     python steganografi_app.py
     ```

3. **Gunakan Antarmuka**:
   - Pilih mode operasi (Sembunyikan/Tampilkan).
   - Ikuti langkah-langkah yang diminta pada antarmuka.

---

### **Catatan Penting**

1. **Format Gambar**:
   - Steganografi bekerja paling baik dengan format **PNG** karena kompresi lossless.
   - Format **JPG** dapat digunakan, tetapi hasilnya mungkin kurang andal.

2. **Keterbatasan Pesan**:
   - Panjang pesan yang dapat disisipkan bergantung pada ukuran gambar. Gambar kecil hanya dapat menyisipkan pesan pendek.

3. **Keamanan**:
   - Metode ini sederhana dan dapat dideteksi dengan alat analisis gambar. Tidak cocok untuk aplikasi yang membutuhkan keamanan tinggi.

4. **Kesalahan Umum**:
   - Jika gambar tidak valid atau format salah, program akan menampilkan pesan error.
