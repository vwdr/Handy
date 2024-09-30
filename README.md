# Handy

## 💡 Story and Motivation

At an FTC robotics outreach event, I met a young kid fascinated by our robots, but there was a barrier—I quickly realized that they could only communicate in sign language, and I didn’t know it. While I tried my best to connect with gestures, it was clear that something more was needed. That moment sparked an idea: **Handy**, an app that transcribes sign language into spoken words and text in real time, breaking down the communication barriers between the deaf and hearing communities.

Today, more than 5% of the world’s population (~432 million adults and 34 million children) live with disabling hearing loss. By 2050, that number is expected to grow to over 700 million (1 in every 10 people) globally (WHO, 2020). With this in mind, **Handy** aims to leverage modern technology to promote inclusivity, allowing more people to connect and communicate without learning a new language first.

## 🕹️ Technologies Used

- **OpenCV**: Used to capture real-time data from the device’s camera, allowing for dynamic analysis of hand movements and gestures.
- **Mediapipe (Hand Module)**: A powerful machine learning solution developed by Google that tracks and infers 21 3D hand landmarks from each camera frame.

## 🔬 Underlying Research

Handy’s hand detection and transcription are built using Google’s Mediapipe, which was first introduced in the research paper *“MediaPipe Hands: On-device Real-time Hand Tracking.”* This module allows the app to accurately detect and interpret hand signs, turning them into actionable data for transcription. Mediapipe also powers solutions such as face detection, face mesh, and pose estimation, expanding the app’s future capabilities.

## 📥 Installation

To set up Handy on your device:

1. Clone the repository in your chosen directory:
   ```bash
   git clone https://github.com/YourRepo/Handy.git
   ```

2. Navigate into the project folder and install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application locally:
   ```bash
   python app.py
   ```

## 🖥️ Usage

To use Handy:

1. Open the app on a device equipped with a camera.
2. Position yourself comfortably, ensuring the camera has a clear view of your hands (about 0.5 meters from the camera).
3. Start signing, and the app will detect your gestures in real time and transcribe them into text or spoken words.
4. **Handy** will display:
   - Current word being formed from your signing
   - Individual letters or signs as they are detected
   - A preview of the translated sentence or word being formed

Ensure good lighting and that your hands are fully visible to the camera for the most accurate results.

## 🔮 Future Directions

The potential for Handy is limitless! Here are some of the exciting directions we plan to take this project:

- **Improved Hand Detection**: Expanding beyond static signs to detect motion-based gestures.
- **Auto-Complete Feature**: Suggesting words or phrases as users sign to make conversations faster and more fluid.
- **Multilingual Transcription**: Translating ASL not only to English but also to other languages like French and Spanish.
- **Emotion Recognition**: Using face mesh technology to identify the emotions accompanying signs, improving the app’s contextual understanding.
