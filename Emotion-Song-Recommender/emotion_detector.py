import cv2
from fer import FER
from song_recommender import recommend_song

cap = cv2.VideoCapture(0)

detector = FER(mtcnn=True)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    emotions = detector.detect_emotions(frame)

    if emotions:

        emotion_data = emotions[0]["emotions"]

        detected_emotion = max(
            emotion_data,
            key=emotion_data.get
        )

        song = recommend_song(detected_emotion)

        cv2.putText(
            frame,
            f"Emotion: {detected_emotion}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        cv2.putText(
            frame,
            f"Song: {song}",
            (20,80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255,0,0),
            2
        )

    cv2.imshow(
        "Emotion Song Recommender",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()