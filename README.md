# 🤖 AI Face Recognition System

An AI-powered Face Recognition System built using **Python, DeepFace, FastAPI, Streamlit, TensorFlow, and OpenCV**. The application detects, registers, and recognizes human faces by generating facial embeddings and comparing them with stored data.

This project demonstrates the practical implementation of Artificial Intelligence and Computer Vision for real-world applications such as attendance systems, identity verification, and security solutions.

---

## ✨ Features

- 👤 Face Registration
- 🧠 AI-based Face Recognition using DeepFace
- 📷 Image Upload Support
- 🔍 Multiple Face Detection
- ⚡ FastAPI REST API Backend
- 🎨 Interactive Streamlit Dashboard
- 📊 Facial Embedding Generation
- 📈 Recognition Confidence Score
- 🚀 Fast and Efficient Processing
- 🖥️ Easy-to-Use Interface

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| AI Framework | DeepFace |
| Machine Learning | TensorFlow |
| Computer Vision | OpenCV |
| Backend | FastAPI |
| Frontend | Streamlit |
| Data Processing | NumPy, Pandas |
| API Server | Uvicorn |

---

## 📂 Project Structure

```
face_recognition_project/
│
├── app/
│   ├── main.py
│   ├── services.py
│   ├── models.py
│   ├── utils.py
│   └── ...
│
├── demo/
│   └── streamlit_app.py
│
├── data/
│
├── tests/
│
├── requirements.txt
│
└── README.md
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/Anuragsu57/Face-Recognition.git
```

### Navigate to the Project

```bash
cd Face-Recognition
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Start FastAPI Backend

```bash
python -m uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

---

## Start Streamlit Frontend

```bash
streamlit run demo/streamlit_app.py
```

Frontend URL

```
http://localhost:8501
```

---

# 🔄 Project Workflow

1. Upload or register a face image.
2. Detect face(s) using OpenCV.
3. Generate facial embeddings using DeepFace.
4. Store embeddings for registered users.
5. Compare uploaded image embeddings with stored embeddings.
6. Display the matched identity along with confidence score.

---

# 📸 Screenshots

### Home Page

> Add screenshot here

```
images/home.png
```

---

### Face Registration

> Add screenshot here

```
images/register.png
```

---

### Recognition Result

> Add screenshot here

```
images/result.png
```

---

# 🎯 Applications

- Smart Attendance System
- Identity Verification
- Office Access Control
- Visitor Management
- Security Surveillance
- Employee Authentication
- AI-powered Face Recognition Systems

---

# 💡 Key Skills Demonstrated

- Artificial Intelligence
- Computer Vision
- Face Recognition
- Deep Learning Fundamentals
- FastAPI Development
- Streamlit Development
- TensorFlow Integration
- OpenCV Image Processing
- REST API Development
- Python Programming
- Data Processing
- Problem Solving

---

# 🔮 Future Enhancements

- 🎥 Live Webcam Face Recognition
- 🗄️ Database Integration (MySQL / PostgreSQL)
- ☁️ Cloud Deployment
- 🔐 JWT Authentication
- 👥 Multi-user Support
- 📱 Mobile Application
- 📊 Recognition Analytics Dashboard
- 🧾 Attendance Report Generation

---

# 📦 Requirements

Main Libraries Used

- DeepFace
- TensorFlow
- OpenCV
- FastAPI
- Streamlit
- NumPy
- Pandas
- Uvicorn
- Pillow

Complete dependencies are available in **requirements.txt**.

---

# 👨‍💻 Author

## Anurag Kashyap

B.Tech Computer Science Engineering

🔗 GitHub

https://github.com/Anuragsu57

🔗 LinkedIn

https://www.linkedin.com/in/anurag-kashyap/

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

## 📄 License

This project is licensed under the MIT License.