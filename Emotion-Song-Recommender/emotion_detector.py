import cv2
from fer import FER
from spotify_recommender import recommend_playlist

cap = cv2.VideoCapture(0)

detector = FER(mtcnn=True)

playlist_shown = False

while True:

    ret, frame = cap.read()

    if not ret:
        break

    emotions = detector.detect_emotions(frame)

    if emotions:

        emotion_scores = emotions[0]["emotionss"]

        detected_emotion = max(
            emotion_scores,
            key=emotion_scores.get
        )

        cv2.putText(
            frame,
            f"Emotion: {detected_emotion}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        if not playlist_shown:

            playlists = recommend_playlist(
                detected_emotion
            )

            print("\n========================")
            print("Detected Emotion:",
                  detected_emotion)
            print("========================\n")

            for i, playlist in enumerate(
                playlists,
                start=1
            ):
                print(
                    f"{i}. {playlist['name']}"
                )
                print(
                    playlist['link']
                )
                print()

            playlist_shown = True

    cv2.imshow(
        "Emotion Playlist Recommender",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord('r'):
        playlist_shown = False

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()