# 🧠 Khai phá dữ liệu - Dự án môn học

Đây là repo tổng hợp các bài thực hành, bài kiểm tra và bài tập lớn trong môn học **Khai phá dữ liệu**. Các nội dung được triển khai bằng **Python** (Jupyter Notebook) và một phần thực hiện bằng **ngôn ngữ C# (.NET)** cho bài kiểm tra ứng dụng.

---

## 📁 Cấu trúc thư mục chính


## 📁 Cấu trúc thư mục

```plaintext
Data-mining/
├── Exercises/                         # Các bài notebook chính về khai phá dữ liệu
│   ├── Clustering.ipynb              # Phân cụm: K-Means, Hierarchical
│   ├── Classification.ipynb         # Phân loại: Decision Tree, KNN, Random Forest
│   ├── Association.ipynb            # Luật kết hợp: Apriori, FP-Growth
│   ├── Regression.ipynb             # Hồi quy tuyến tính và đa thức
│   ├── Dimensionality.ipynb         # Giảm chiều: PCA, t-SNE
│   ├── Preprocessing.ipynb          # Tiền xử lý dữ liệu: xử lý thiếu, mã hóa, chuẩn hóa
│   └── Logistic_Regression.ipynb    # Hồi quy Logistic
│
├── datamining/                       # Thư mục bài tập lớn nhóm và ứng dụng
│   ├── ConsoleApp1/                 # Bài kiểm tra thực hành viết bằng C# (.NET)
│   │   ├── Program.cs
│   │   ├── ConsoleApp1.sln
│   │   └── obj/...
│   ├── EmpSal.ipynb                 # Dự đoán lương nhân viên
│   ├── mall_customers.ipynb        # Phân cụm khách hàng (KMeans)
│   ├── marketing.ipynb             # Phân tích dữ liệu marketing
│   ├── Mall_Customers.csv          # Dataset khách hàng
│   ├── Ktra1/                      # Bài kiểm tra số 1 (có cả file .rar)
│
├── KHAI_THÁC_CHUỖI_KÍ_HIỆU_VÀ_SINH_HỌC.ipynb
├── KHAI_THÁC_CHUỖI_THỜI_GIAN.ipynb
├── KHAI_THÁC_ĐỒ_THỊ_VÀ_MẠNG.ipynb
├── KHAI_THÁC_DỮ_LIỆU_THỐNG_KÊ_VÀ_KHAI_THÁC_DỮ_LIỆU_HÌNH_ẢNH,_ÂM_THANH.ipynb
├── ỨNG_DỤNG_KHAI_THÁC_DỮ_LIỆU.ipynb

├── Nhóm 6- Khai phá dữ liệu.docx     # Báo cáo bài tập lớn
├── Nhóm 6- Khai phá dữ liệu.pdf      # Bản PDF báo cáo
├── README.md                         # Tài liệu này

---
```
## 🎯 Mục tiêu dự án

- Thực hành triển khai các kỹ thuật khai phá dữ liệu:
  - Phân cụm, phân loại, luật kết hợp, hồi quy, giảm chiều
- Ứng dụng thư viện Python như: `pandas`, `scikit-learn`, `mlxtend`, `seaborn`
- Áp dụng vào bài toán thực tế như: phân tích khách hàng, lương nhân viên, marketing
- Làm việc nhóm và trình bày báo cáo cuối kỳ

---

## 📦 Yêu cầu môi trường

- Python 3.8 trở lên
- Các thư viện:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`
  - `mlxtend`

💡 Bạn có thể cài nhanh qua:
```bash
pip install -r requirements.txt
```
# ▶️ Hướng dẫn sử dụng
1. Tải repo
```bash
git clone https://github.com/quynhphuong1209/Data-mining.git
cd Data-mining
```
2. Mở Jupyter Notebook để chạy các file .ipynb:
```bash
jupyter notebook
```
3. Hoặc chạy trực tiếp trên Google Colab nếu không cài Python cục bộ.

# 👩‍💻 Tác giả
- Đinh Lê Quỳnh Phương
- GitHub: @quynhphuong1209
- Môn học: Khai phá dữ liệu
- Trường: [Trường Đại học Y tế Công cộng / hoặc bạn tự điền]

# 📎 Tài liệu đính kèm
- 📄 Báo cáo nhóm: Nhóm 6 - Khai phá dữ liệu.pdf
- 🧾 Các bài tập, kiểm tra, ứng dụng đầy đủ bằng Python và C#
- 📊 Dữ liệu thực tế: Mall_Customers.csv, EmpSal.ipynb, v.v.

# 💡 Gợi ý mở rộng: Bạn có thể tích hợp đồ thị tương tác với Plotly, xuất báo cáo tự động bằng nbconvert, hoặc triển khai mô hình đơn giản với Streamlit để nâng cao repo này hơn nữa.
