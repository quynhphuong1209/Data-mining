# -*- coding: utf-8 -*-
"""KHAI THÁC CHUỖI KÍ HIỆU VÀ SINH HỌC.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oz6nT_tLT2AbRQ021QcXIkfWzfJpnfcf
"""

!pip install hmmlearn

"""Ví dụ về việc sử dụng Hidden Markov Models (HMM) để phân tích chuỗi DNA."""

from hmmlearn.hmm import MultinomialHMM
import numpy as np

# Chuỗi DNA giả lập (A, T, G, C)
sequence = ['A', 'C', 'G', 'T', 'A', 'A', 'T', 'C', 'G', 'T']

# Đặt chỉ mục cho các ký tự trong chuỗi DNA
unique_chars = ['A', 'T', 'G', 'C']
char_to_index = {char: idx for idx, char in enumerate(unique_chars)}
indexed_sequence = [char_to_index[char] for char in sequence]

# Chuyển đổi chuỗi ký tự thành dạng ma trận (mỗi ký tự là một số nguyên)
X = np.array(indexed_sequence).reshape(-1, 1)

# Khởi tạo mô hình MultinomialHMM
model = MultinomialHMM(n_components=2, random_state=42)  # Giả sử có 2 trạng thái ẩn

# Huấn luyện mô hình với dữ liệu chuỗi ký tự
model.fit(X)

# Dự đoán chuỗi trạng thái ẩn
hidden_states = model.predict(X)

# Hiển thị kết quả
print("Chuỗi trạng thái ẩn dự đoán:", hidden_states)