import cv2
from song_recommender import recommend_song

# Start webcam
cap = cv2.VideoCapture(0)

# Initialize FER detector
detector = FER(mtcnn=True)

last_emotion = None
song_name = ""

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = detector.detect_emotions(frame)

    if results:

        emotions = results[0]["emotions"]

        detected_emotion = max(
            emotions,
            key=emotions.get
        )

        confidence = emotions[detected_emotion]

        # Recommend a new song only when emotion changes
        if detected_emotion != last_emotion:

            song_name = recommend_song(
                detected_emotion
            )

            last_emotion = detected_emotion

            print("\n====================")
            print("Emotion :", detected_emotion)
            print("Confidence :", round(confidence * 100, 2), "%")
            print("Recommended Song :", song_name)
            print("====================")

        # UI Panel
        cv2.rectangle(
            frame,
            (10, 10),
            (650, 140),
            (0, 0, 0),
            -1
        )

        # Display Emotion
        cv2.putText(
            frame,
            f"Emotion: {detected_emotion}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        # Display Confidence
        cv2.putText(
            frame,
            f"Confidence: {round(confidence * 100, 2)}%",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        # Display Song
        cv2.putText(
            frame,
            f"Song: {song_name}",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 0, 0),
            2
        )

    cv2.imshow(
        "AI Emotion Based Music Recommendation System",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()