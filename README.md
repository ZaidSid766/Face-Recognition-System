
# 👤 Face Recognition System

This is a simple yet effective **Face Recognition System** using Python and OpenCV. It captures, trains, and recognizes human faces using Haar Cascade and LBPH Face Recognizer.

## 📂 Project Structure

```
Face_recognition/
│
├── dataset/                      # Stores captured face images
├── main.py                       # Main program to detect and recognize faces
├── train.py                      # Trains the face recognition model
├── test.py                       # Optional: Used for testing
├── haarcascade_frontalface_default.xml  # Haar cascade classifier
├── requirements.txt              # Required Python packages
└── README.md                     # Project overview (this file)
```

## 🚀 Features

- Face detection using Haar Cascades
- Face dataset creation and image storage
- Model training using LBPH algorithm
- Real-time face recognition via webcam
- Easy-to-understand and modular code

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Face_recognition.git
   cd Face_recognition
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🧑‍💻 Usage

1. **Capture face data:**
   ```bash
   python main.py
   ```

2. **Train the model:**
   ```bash
   python train.py
   ```

3. **Test/Run Recognition:**
   ```bash
   python test.py
   ```

## ✅ Requirements

- Python 3.x
- OpenCV
- NumPy

## 📸 Demo

> Add screenshots or a demo GIF of your application here!

## 🙌 Credits

- [OpenCV](https://opencv.org/)
- Haar Cascade Classifiers
- Developed by **[Your Name]**

## 📜 License

This project is licensed under the MIT License. Feel free to use and modify it!
