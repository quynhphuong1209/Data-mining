# -*- coding: utf-8 -*-
"""KHAI THÁC DỮ LIỆU THỐNG KÊ VÀ KHAI THÁC DỮ LIỆU HÌNH ẢNH, ÂM THANH.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19W77rpAyDHyBTwwEimNWl67zbhBfIbtO

**KHAI THÁC DỮ LIỆU THỐNG KÊ**

Sử dụng scikit-learn để phân tích và huấn luyện một mô hình học máy đơn giản:
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Tạo dữ liệu giả lập
data = pd.DataFrame({
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [5, 4, 3, 2, 1],
    'Target': [2, 3, 4, 5, 6]
})

# Tách dữ liệu thành X (features) và y (target)
X = data[['Feature1', 'Feature2']]
y = data['Target']

# Chia dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Khởi tạo và huấn luyện mô hình Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán và in kết quả
y_pred = model.predict(X_test)
print(f"Dự đoán: {y_pred}")

"""**KHAI THÁC DỮ LIỆU HÌNH ẢNH**

Mã sử dụng OpenCV để đọc và hiển thị một hình ảnh
"""

import cv2
from google.colab import files
from google.colab.patches import cv2_imshow

# Tải lên tệp hình ảnh
uploaded = files.upload()

# Đường dẫn tệp hình ảnh sau khi tải lên
image_path = 'cinqueterre.jpg'

# Đọc hình ảnh
image = cv2.imread(image_path)

# Kiểm tra nếu hình ảnh đã được đọc thành công
if image is not None:
    # Hiển thị hình ảnh
    cv2_imshow(image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Không thể đọc hình ảnh.")

"""**KHAI THÁC DỮ LIỆU ÂM THANH**

Mã sử dụng librosa để đọc và phân tích âm thanh
"""

!pip install pydub

!apt-get install ffmpeg

from google.colab import files
from pydub import AudioSegment
import librosa.display
import matplotlib.pyplot as plt

# Tải tệp âm thanh
uploaded = files.upload()

# Chuyển đổi m4a sang wav
audio_path = 'His.m4a'  # Đảm bảo tên tệp chính xác
audio = AudioSegment.from_file(audio_path, format="m4a")
audio.export("His_converted.wav", format="wav")

# Load tệp âm thanh đã chuyển đổi
y, sr = librosa.load("His_converted.wav")

# Hiển thị sóng âm
librosa.display.waveshow(y, sr=sr)
plt.title('Waveshow of Audio')
plt.show()