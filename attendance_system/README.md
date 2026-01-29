# Face Authentication Attendance System

**Student Name:** [Your Name]  
**University:** [Your University]  
**Course:** Machine Learning / Computer Vision Assignment  

---

## 1. Project Overview
This project is a **Face Authentication Attendance System** built using Python and OpenCV. Its purpose is to automate the attendance process by replacing manual signatures with biometric face recognition. The system captures a student's face via webcam, matches it against a registered database, and logs their entry (Punch-in) or exit (Punch-out) time in a CSV file.

The goal is to demonstrate practical application of Computer Vision (CV) concepts like face detection, feature encoding, and matching in a real-time environment.

## 2. Model and Approach Used

### Face Detection
We use the **Histogram of Oriented Gradients (HOG)** method provided by the `face_recognition` library (built on `dlib`) to locate faces in an image. This method is robust against lighting changes and faster than deep learning-based CNN detectors on CPU.

### Face Encoding
Once a face is detected, the system generates a **128-dimensional embedding** (a vector of 128 numbers). This encoding represents the unique features of the face (distance between eyes, nose shape, etc.). 
- We use a **pretrained model** (`dlib_face_recognition_resnet_model_v1`) which has been trained on millions of images to produce these embeddings.
- No manual training of a neural network is required; we simply use the pretrained weights.

### Matching
To identify a person, we calculate the **Euclidean distance** between the live face embedding and the stored embeddings. 
- If the distance is below a threshold (tolerance = 0.6), it is considered a match.
- The system returns the name of the person with the smallest distance.

## 3. Training Process
Since we utilize a **pretrained model**, there is no traditional "training" phase where we iterate over epochs. Instead, we have a **Registration Phase**:
1. The user inputs their name.
2. The webcam captures their face.
3. The system computes the 128-d encoding.
4. This encoding is saved to a `.pkl` file.

This "one-shot learning" approach allows us to add new users instantly without retraining the whole model.

## 4. Accuracy Expectations
- **Good Lighting:** 90–95% accuracy. The HOG detector works very well when facial features are clearly visible.
- **Poor Lighting:** 70–80% accuracy. Shadows can obscure features, leading to "Unknown" results or false negatives.
- **Side Profiles:** Accuracy drops significantly if the person turns their head more than 30 degrees.

## 5. Spoof Prevention Method
To prevent users from using a photo of another person, basic **liveness detection** is implemented.
- **Movement Detection:** The system expects slight changes in face position or size over frames. A completely static image (like a printed photo held still) can be flagged.
- **Blink Detection (Optional Logic):** By analyzing eye landmarks, we can require a blink to verify a live human. (Simplified implementation in `spoof_check.py`).

## 6. Known Failure Cases
- **Low Light:** The camera may introduce noise, preventing detection.
- **Twins:** The 128-d embeddings might be too similar for identical twins.
- **Printed Photo:** High-quality prints might bypass basic liveness checks if moved realistically.
- **Masks:** Face occlusion (like medical masks) hides key features (nose, mouth), causing detection failure.

## 7. How to Run

### Step 1: Install Requirements
Open your terminal and run:
```bash
pip install -r requirements.txt
```
*(Note: Requires CMake and Visual Studio build tools on Windows, or standard build-essential on Linux)*

### Step 2: Register a User
Run the registration script to add a new face:
```bash
python register_face.py
```
- Enter name when prompted.
- Press 's' to save the face.
- Press 'q' to quit.

### Step 3: Take Attendance
Run the main recognition system:
```bash
python recognize_face.py
```
- The webcam will open.
- When your face is recognized, press **'1'** to Punch In.
- Press **'2'** to Punch Out.
- Press **'q'** to exit.
- Attendance is saved in `attendance.csv`.

## 8. Evaluation Criteria Mapping
| Criteria | Implementation |
|----------|----------------|
| **Functional Accuracy** | Uses state-of-the-art dlib embeddings for high-precision matching. |
| **Reliability** | Handles "Unknown" faces gracefully; allows retries. |
| **ML Limitations** | Acknowledges issues with lighting and occlusion in this report. |
| **Practical Quality** | Simple CLI/Window interface, CSV export, works in real-time. |
