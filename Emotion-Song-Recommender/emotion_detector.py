import cv2
from song_recommender import recommend_song

cap = cv2.VideoCapture(0)

emotion = "happy"
song = recommend_song(emotion)

while True:
    ret, frame = cap.read()

    cv2.putText(
        frame,
        f"Emotion: {emotion}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Song: {song}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    cv2.imshow("Emotion Song Recommender", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()