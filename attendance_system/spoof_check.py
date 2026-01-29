"""
Basic spoof prevention: head movement detection.
Rejects static images (e.g. printed photo held still).
Returns True if live face (movement detected), False if static.
"""
import cv2
import numpy as np

# Store recent face centers for movement check (module-level state)
_face_center_history = []
_HISTORY_SIZE = 10
_MOVEMENT_THRESHOLD = 3.0   # min std (pixels) to consider "moved"
_STATIC_THRESHOLD = 2.0     # if std below this over many frames, treat as static


def check_liveness(frame, face_location):
    """
    Basic liveness: require head movement to reject static images.
    face_location: (top, right, bottom, left) in same scale as frame.
    Returns True if live (movement seen), False if static (possible spoof).
    """
    global _face_center_history

    if face_location is None or len(face_location) < 4:
        return False

    top, right, bottom, left = face_location
    center_x = (left + right) // 2
    center_y = (top + bottom) // 2

    _face_center_history.append((center_x, center_y))
    if len(_face_center_history) > _HISTORY_SIZE:
        _face_center_history.pop(0)

    # Need enough samples to decide
    if len(_face_center_history) < 5:
        return True   # Assume live until we have enough data

    xs = [c[0] for c in _face_center_history]
    ys = [c[1] for c in _face_center_history]
    std_x = float(np.std(xs))
    std_y = float(np.std(ys))

    # Movement detected -> live
    if std_x >= _MOVEMENT_THRESHOLD or std_y >= _MOVEMENT_THRESHOLD:
        return True
    # Many samples and no movement -> static (spoof)
    if len(_face_center_history) >= _HISTORY_SIZE and std_x < _STATIC_THRESHOLD and std_y < _STATIC_THRESHOLD:
        return False
    # Still collecting or borderline
    return True


def reset_liveness_history():
    """Call when starting a new check so history does not carry over."""
    global _face_center_history
    _face_center_history = []
