# Gestura

### Vision-Based Gesture and Gaze Interaction System

Gestura is a computer vision-based human–computer interaction system that enables touchless computer control using hand gestures, eye gaze, virtual mouse actions, screen awareness, and customizable gesture commands.

The project is designed as a single modular platform using a webcam and local computer vision processing.

---

## 🚀 Features

### 1. Hand Gesture PC Controller
Control computer actions using predefined hand gestures such as:
- Pointing
- Pinching
- Open palm
- Fist
- Thumbs up/down
- Custom gestures

### 2. Eye-Gaze Mouse Controller
Use eye and gaze direction to control the mouse cursor.

Planned capabilities include:
- Gaze-based cursor movement
- Eye-based selection
- Blink-based interaction
- User calibration

### 3. Vision-Based Virtual Mouse
Use hand tracking and gestures as a replacement for a physical mouse.

Supported interactions can include:
- Cursor movement
- Left click
- Right click
- Drag and drop
- Click-and-hold

### 4. Smart Screen
Detect basic user presence and attention states.

Example states:
- User present
- User absent
- Looking at screen
- Looking away
- Unknown

### 5. Gesture Command Language
Create custom gesture sequences and map them to computer actions.

Example:

```text
Index + Pinch → Select
Two Fingers   → Next
Thumbs Up     → Confirm
Open Palm     → Stop
```

---

## 🏗️ System Architecture

```text
                    WEBCAM
                       |
                       v
              +----------------+
              | Vision Engine   |
              | OpenCV/MediaPipe|
              +--------+-------+
                       |
       +---------------+---------------+
       |               |               |
       v               v               v
   Hand Vision     Eye Vision     Screen Vision
       |               |               |
       v               v               v
   Gestures        Gaze Control    Presence/
       |               |            Attention
       +---------------+---------------+
                       |
                       v
              Interaction Engine
                       |
          +------------+------------+
          |            |            |
          v            v            v
        Mouse      Keyboard      System
        Control      Control      Actions
```

---

## 🛠️ Technology Stack

- **Python** – Core programming language
- **OpenCV** – Camera and image processing
- **MediaPipe** – Hand and face/landmark tracking
- **NumPy** – Numerical and geometric calculations
- **PyAutoGUI** – Mouse and keyboard automation
- **pynput** – Input control and monitoring

---

## 📁 Project Structure

```text
Gestura/
│
├── main.py
├── requirements.txt
├── README.md
│
├── config/
│   ├── settings.yaml
│   └── gestures.yaml
│
├── core/
│   ├── camera.py
│   ├── frame_processor.py
│   └── state_manager.py
│
├── hand/
│   ├── hand_detector.py
│   ├── landmark_tracker.py
│   ├── gesture_detector.py
│   └── gesture_language.py
│
├── eye/
│   ├── face_detector.py
│   ├── eye_detector.py
│   ├── iris_tracker.py
│   ├── gaze_estimator.py
│   └── calibration.py
│
├── mouse/
│   ├── virtual_mouse.py
│   ├── cursor_controller.py
│   ├── click_controller.py
│   └── smoothing.py
│
├── screen/
│   ├── presence_detector.py
│   ├── attention_detector.py
│   └── screen_state.py
│
├── interaction/
│   ├── command_engine.py
│   ├── action_executor.py
│   └── input_controller.py
│
├── ui/
│   ├── dashboard.py
│   └── overlay.py
│
└── utils/
    ├── logger.py
    └── geometry.py
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd Gestura
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Gestura

```bash
python main.py
```

---

## 🎮 Interaction Modes

Gestura is designed around multiple interaction modes:

```text
1. Hand Gesture Controller
2. Eye-Gaze Mouse
3. Virtual Mouse
4. Smart Screen
5. Gesture Command Language
6. Combined Mode
```

---

## 🎯 Project Objectives

- Develop a real-time vision-based interaction system.
- Reduce dependence on conventional mouse and keyboard input.
- Enable touchless computer interaction.
- Explore hand and eye tracking using computer vision.
- Provide customizable gesture-based commands.
- Build a modular and extensible computer vision platform.

---

## 🔒 Privacy

Gestura is designed for local processing. Camera frames are processed on the user's computer and are not required to be sent to external cloud services.

---

## ⚠️ Limitations

Performance and recognition accuracy may depend on:

- Camera quality
- Lighting conditions
- Camera position
- User distance from the camera
- Hand/face visibility
- Computer hardware
- Tracking and calibration accuracy

---

## 🗺️ Development Roadmap

- [ ] Camera and frame-processing pipeline
- [ ] Hand detection and landmark tracking
- [ ] Gesture recognition
- [ ] Hand gesture PC control
- [ ] Virtual mouse
- [ ] Eye and iris tracking
- [ ] Gaze calibration
- [ ] Eye-gaze mouse
- [ ] Smart screen presence detection
- [ ] Attention detection
- [ ] Gesture command language
- [ ] Combined interaction mode
- [ ] Performance optimization
- [ ] Testing and documentation

---

## 📌 Scope

Gestura focuses specifically on **computer vision-based human–computer interaction**.

It does **not** include:
- LLMs
- Voice assistants
- Cloud AI services
- JARVIS AI core
- Conversational AI

---

## 👨‍💻 Project

**Project Name:** Gestura  
**Full Title:** Vision-Based Gesture and Gaze Interaction System

Built as a standalone computer vision project for exploring touchless and multimodal human–computer interaction.
