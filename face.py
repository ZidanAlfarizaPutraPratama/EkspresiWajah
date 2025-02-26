import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Memuat model yang telah disimpan
model_path = 'face_analysis_project/models/emotion_model.h5'  # Path ke model
model = load_model(model_path)

# Daftar ekspresi wajah yang bisa diprediksi
emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Fungsi untuk memprediksi ekspresi wajah pada gambar
def predict_expression(image):
    if image is None:
        print("Gambar tidak ditemukan atau gagal dimuat.")
        return None
    
    # Mengubah gambar ke grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Ubah ukuran gambar menjadi 48x48
    gray = cv2.resize(gray, (48, 48))
    
    # Ubah bentuknya menjadi (1, 48, 48, 1) untuk prediksi
    gray = gray.reshape(1, 48, 48, 1)
    
    # Normalisasi gambar
    gray = gray / 255.0
    
    # Prediksi ekspresi wajah dengan model
    prediction = model.predict(gray)
    
    # Mengambil indeks kelas dengan probabilitas tertinggi
    emotion_index = np.argmax(prediction)
    
    return emotions[emotion_index], gray

# Membuka webcam untuk deteksi ekspresi wajah
cap = cv2.VideoCapture(0)  # Menggunakan webcam default

# Menggunakan pre-trained haarcascade untuk mendeteksi wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Membaca frame dari webcam
    ret, frame = cap.read()
    
    if not ret:
        print("Gagal membaca frame.")
        break
    
    # Mengubah gambar ke grayscale untuk deteksi wajah
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Deteksi wajah dalam gambar
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Melakukan prediksi untuk setiap wajah yang terdeteksi
    for (x, y, w, h) in faces:
        # Menambahkan kotak di sekitar wajah
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Memotong wajah yang terdeteksi untuk diprediksi
        face_roi = frame[y:y + h, x:x + w]
        
        # Prediksi ekspresi wajah pada wajah yang terdeteksi
        expression, _ = predict_expression(face_roi)
        
        # Menampilkan ekspresi pada gambar
        if expression is not None:
            cv2.putText(frame, f'Ekspresi: {expression}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # Menampilkan frame
    cv2.imshow('Deteksi Ekspresi Wajah', frame)
    
    # Menunggu tombol 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Melepaskan webcam dan menutup jendela
cap.release()
cv2.destroyAllWindows()
