import cv2

# Load the Haar cascade face detection model
face_cap = cv2.CascadeClassifier(
    "C:/Users/Zaidsid/PycharmProjects/Face_recognition/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"
)

# Open the webcam
video_cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not video_cap.isOpened():
    print("❌ Error: Could not open video stream from webcam.")
    exit()

while True:
    ret, frame = video_cap.read()

    if not ret:
        print("❌ Error: Failed to capture frame.")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Enhance contrast (optional but helpful in low light)
    gray = cv2.equalizeHist(gray)

    # Apply Gaussian blur to reduce noise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect faces with better-tuned parameters
    faces = face_cap.detectMultiScale(
        gray,
        scaleFactor=1.05,     # More precise scaling
        minNeighbors=6,       # Reduces false positives
        minSize=(40, 40),     # Avoids small noisy detections
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw rectangles and show face count
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show number of faces on screen
    cv2.putText(frame, f"Faces: {len(faces)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    # Display the output
    cv2.imshow("Live Face Detection", frame)

    # Exit on pressing 'a'
    if cv2.waitKey(10) & 0xFF == ord("a"):
        break

# Cleanup
video_cap.release()
cv2.destroyAllWindows()
