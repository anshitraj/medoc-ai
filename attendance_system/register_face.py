import cv2
import face_recognition
import pickle
import os

# Create faces directory if not exists
if not os.path.exists("faces"):
    os.makedirs("faces")

def register():
    # 1. Ask for name
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    # 2. Open Webcam
    video_capture = cv2.VideoCapture(0)
    
    print("Please look at the camera...")
    print("Press 's' to save face, 'q' to quit.")

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Show feed
        cv2.imshow("Register Face", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            # 3. Capture and Save
            img_path = f"faces/{name}.jpg"
            cv2.imwrite(img_path, frame)
            print(f"Image saved to {img_path}")
            
            # 4. Generate and Store Encoding
            # Convert to RGB for face_recognition
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(rgb_frame)
            encodings = face_recognition.face_encodings(rgb_frame, boxes)

            if len(encodings) > 0:
                encoding = encodings[0]
                encoding_path = f"faces/{name}.pkl"
                with open(encoding_path, "wb") as f:
                    pickle.dump(encoding, f)
                print(f"Encoding saved for {name}")
            else:
                print("No face detected! Please try again.")
                os.remove(img_path) # Cleanup
                continue
            
            break

        elif key == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    register()
