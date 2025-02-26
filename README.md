# Proyek Pengenalan Ekspresi Wajah 😃👀

Selamat datang di proyek **Pengenalan Ekspresi Wajah**! 🎉 Proyek ini menggunakan teknik **deep learning** dengan model **Convolutional Neural Network (CNN)** untuk mendeteksi emosi berdasarkan ekspresi wajah. Model ini dilatih menggunakan dataset **FER2013**, yang berisi gambar yang dilabeli dengan 7 emosi berbeda.

## 🛠️ Alat dan Perpustakaan yang Digunakan

- **TensorFlow** 🤖: Untuk membangun dan melatih model CNN.
- **Keras** 🧠: API tingkat tinggi untuk jaringan saraf.
- **OpenCV** 👁️: Untuk pemrosesan gambar dan deteksi wajah menggunakan webcam.
- **Pandas** 📊: Untuk manipulasi data dan membaca file CSV.
- **Scikit-learn** 📚: Untuk membagi data menjadi data latih dan data uji.
- **Kaggle** 🌐: Untuk mengunduh dataset FER2013.

## 📦 Instalasi

Untuk memulai, instal semua perpustakaan yang diperlukan dengan menjalankan perintah berikut:

```
!pip install tensorflow keras opencv-python pandas scikit-learn kaggle
```

### Langkah 1: Mount Google Drive 📂

Mount Google Drive untuk menyimpan model dan file lainnya:

```
from google.colab import drive
drive.mount('/content/drive')
```

### Langkah 2: Unduh dan Persiapkan Dataset 📥

1. **Unduh file `kaggle.json`** dan unggah ke Colab.
2. **Setel akses API Kaggle** dengan menyalin `kaggle.json` ke folder yang tepat dan mengatur izin akses.
3. **Unduh dataset FER2013** menggunakan perintah Kaggle:

```
!kaggle datasets download -d msambare/fer2013
!unzip fer2013.zip -d /content/fer2013
```

### Langkah 3: Pra-pemrosesan Data 📊

- Gambar akan diubah menjadi **grayscale** dan diubah ukurannya menjadi **48x48 piksel**.
- Nilai piksel akan dinormalisasi ke rentang [0, 1].
- Data akan dibagi menjadi **data latih** dan **data uji**.

### Langkah 4: Latih Model CNN 🧠

Model CNN digunakan untuk mengklasifikasikan ekspresi wajah ke dalam 7 kategori emosi:

- **Angry** 😠
- **Disgust** 🤢
- **Fear** 😱
- **Happy** 😃
- **Sad** 😔
- **Surprise** 😲
- **Neutral** 😐

Model dilatih menggunakan **TensorFlow** dan **Keras** dengan fungsi **sparse categorical crossentropy** dan **adam optimizer**.

### Langkah 5: Deteksi Ekspresi Wajah Menggunakan Webcam 🎥

Setelah model dilatih, Anda dapat menggunakan **webcam** untuk mendeteksi ekspresi wajah secara langsung. Program ini akan mendeteksi wajah menggunakan algoritma **Haar Cascade** dan memprediksi ekspresi wajah menggunakan model yang telah dilatih. Hasil prediksi ekspresi akan ditampilkan di layar dengan kotak di sekitar wajah yang terdeteksi.

- Program akan membuka webcam, mendeteksi wajah dalam setiap frame, dan memprediksi ekspresi wajah berdasarkan gambar yang terdeteksi.
- Ekspresi yang diprediksi akan ditampilkan di atas wajah yang terdeteksi.

### Langkah 6: Menyimpan dan Menggunakan Model

Model yang telah dilatih dapat disimpan ke **Google Drive** setelah proses pelatihan selesai untuk digunakan kembali di masa depan. Anda dapat memuat kembali model tersebut untuk melakukan prediksi pada gambar atau video baru.

```
model.save('/content/drive/MyDrive/face_analysis_project/models/emotion_model.h5')
```

Model yang telah dilatih dapat diakses di [Google Drive - emotion_model.h5](https://drive.google.com/drive/folders/1_uYLCplKCNf1ZW8ogVkdyAd4wVKUm-yO?usp=sharing).

## 🔧 Cara Menggunakan Model untuk Prediksi Ekspresi Wajah

Setelah model dilatih dan disimpan, Anda dapat menggunakannya untuk memprediksi ekspresi wajah pada gambar atau video lain. Cukup dengan memuat model yang telah disimpan dan memberikan gambar wajah untuk diprediksi.

## 📂 Struktur Folder

```
SensorWajah
├── face_analysis_project
│   ├── models
│   │   └── emotion_model.h5       # Model yang telah dilatih
│   ├── face.py                    # Skrip untuk deteksi ekspresi wajah
│   ├── model_training.ipynb       # Notebook untuk pelatihan model
│   └── requirements.txt           # Daftar dependensi untuk proyek
```

- **/content/fer2013/images**: Gambar-gambar wajah dalam dataset FER2013.
- **/content/fer2013/fer2013.csv**: File CSV yang berisi label ekspresi wajah.
- **/content/drive/MyDrive/face_analysis_project/models/emotion_model.h5**: Model yang telah dilatih.

## 📌 Catatan

- **Akurasi Model**: Akurasi model ini dapat bervariasi tergantung pada data yang digunakan. Berdasarkan data yang saya ambil, model ini mencapai akurasi sekitar **90%**.
- **Penggunaan Webcam**: Pastikan perangkat keras Anda mendukung penggunaan webcam untuk deteksi ekspresi wajah secara langsung.

---

## 📜 Lisensi

Proyek ini dilisensikan di bawah **MIT License**. Lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

---

Terima kasih! Semoga bermanfaat untuk aplikasi pengenalan ekspresi wajah di berbagai bidang seperti **keamanan**, **interaksi manusia-komputer**, dan **analisis sentimen**. 🎉
