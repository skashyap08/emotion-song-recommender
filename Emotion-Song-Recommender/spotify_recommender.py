import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "2b3592c7b9a34d78978e7d27aad930a4"
CLIENT_SECRET = "8d44e30d12e438dabebead8a1f68577"

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
)

emotion_queries = {
    "happy": "happy playlist",
    "sad": "sad songs",
    "angry": "rock workout",
    "fear": "calm relaxing music",
    "neutral": "chill hits",
    "surprise": "party songs",
    "disgust": "motivational songs"
}

def recommend_playlist(emotion):

    query = emotion_queries.get(
        emotion,
        "top hits"
    )

    results = sp.search(
        q=query,
        type="playlist",
        limit=5
    )

    playlists = []

    for item in results["playlists"]["items"]:
        playlists.append({
            "name": item["name"],
            "url": item["external_urls"]["spotify"]
        })

    return playlists