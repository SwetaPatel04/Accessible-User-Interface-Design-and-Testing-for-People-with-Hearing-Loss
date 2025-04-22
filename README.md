# 🧏 Accessible User Interface Design and Testing for People with Hearing Loss

An innovative solution that bridges the communication gap for people with hearing impairments using **Speech-to-ASL Conversion**, **Text-to-ASL Visualization**, and **3D Sign Language Modeling**. This system leverages **Python**, **Google Speech Recognition**, **Tkinter GUI**, **Unity**, and **Blender** to deliver a rich, accessible experience.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Results & Usability](#results--usability)
- [Team Members](#team-members)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## 🧠 Overview

This project was designed using the **User-Centered Design (UCD)** methodology following **ISO** and **Nielsen Norman Group (NNG)** standards. It helps users:
- Convert **text to ASL symbols**
- Translate **spoken language into ASL**
- Display **3D ASL hand signs** using Unity and Blender
- Conduct real-time speech-to-3D model translation

---

## ✨ Features

- 🔠 **Text to ASL Conversion** using image-based sign representation
- 🎙️ **Speech to Text Recognition** via Google’s Speech API
- 🤖 **Speech to ASL Converter** (text-to-image ASL transition)
- 🧱 **3D Modeling of ASL signs (0-9)** in Blender
- 🕹️ **Unity-based 3D ASL Translator**
- 👂 **Voice-Activated ASL Display**

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** (for GUI)
- **Google Speech Recognition API**
- **PIL / OpenCV** for image rendering
- **Blender** for 3D hand modeling
- **Unity** for real-time 3D interaction
- **Numpy**, **Pyaudio**, **SpeechRecognition**

---

## 💾 Installation

1. Clone this repository:
```bash
git clone https://github.com/USERNAME/accessible-ui-hearing-loss.git
cd accessible-ui-hearing-loss
```

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 1. **Text to ASL (Run in Python)**
```bash
python text_to_asl.py
```

### 2. **Speech to ASL (Run in Python)**
```bash
python speech_to_asl.py
```

### 3. **3D ASL Translator (Blender + Unity)**
- Open Blender files to view or modify 3D hand signs
- Use Unity to map recognized speech to Blender-based 3D models

---

## 🗂️ Project Structure

```bash
Project/
│
├── asl_3d model translator.py       # Main translator script
├── text_to_asl.py                   # Text to ASL GUI
├── speech_to_asl.py                 # Speech to ASL translator
├── speech_to_text.py                # Speech recognition standalone
├── *.jpg / *.png                    # ASL image mappings
├── hand0.png - hand9.png            # 3D hand sign images
├── Blender Models/                  # 3D ASL symbols (0-9)
├── Unity Project/                   # Unity-based interaction
└── README.md                        # This file!
```

---

## ✅ Results & Usability

- 🔊 **Speech Recognition Accuracy:** ~90%
- ✋ **Real-time ASL Feedback** on speech input
- 🧩 **High Satisfaction** from usability test participants
- 🧘‍♂️ **Easy to Use** with minimal learning curve
- 🎯 **ISO/NNG compliant** user interface

---

## 👨‍👩‍👧‍👦 Team Members

- **Sweta Patel** – 📄 Documentation, Reporting
- **Vaishal Shah** – 🧱 Blender 3D Modeling
- **Ujash Thakkar** – 🎤 Speech Recognition Integration
- **Dikshaben Patel** – 🕹️ Unity & Translator UI Testing
- **Nisha Raval** – 🔍 Research & 3D Modeling Support

---

## 🚀 Future Enhancements

- 🧠 Integrate **Machine Learning** for gesture prediction
- 🌐 Real-time web deployment
- 📚 Add **ASL learning modules** (quizzes & lessons)
- 📱 Build **mobile-friendly** versions

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to use, modify, and enhance it with attribution.

