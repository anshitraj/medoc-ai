# medoc-ai

Project containing the **Face Authentication Attendance System** (Medoc assignment) and related app structure.

## Face Authentication Attendance System

Biometric attendance using face recognition: register faces via webcam, then punch in/out with live face detection and basic spoof prevention.

**Location:** [`attendance_system/`](attendance_system/)

### Quick start

1. **Install dependencies**
   ```bash
   cd attendance_system
   pip install -r requirements.txt
   ```
   *(If `face_recognition` fails on Windows, install [CMake](https://cmake.org/) and add to PATH, then `pip install dlib face_recognition`.)*

2. **Register a face**
   ```bash
   python register_face.py
   ```
   Enter name → look at camera → press **s** to save → **q** to quit.

3. **Take attendance**
   ```bash
   python recognize_face.py
   ```
   Look at camera → press **1** to Punch in, **2** to Punch out → **q** to quit.  
   Attendance is saved in `attendance_system/attendance.csv`.

### Full documentation

See **[attendance_system/README.md](attendance_system/README.md)** for overview, model details, accuracy, spoof prevention, and troubleshooting.

## Repository structure

- **attendance_system/** – Face registration, recognition, spoof check, CSV attendance
- **client/** – Frontend (React/Vite)
- **server/** – Backend
