import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re
id="7453e3eb94b843389849d0bc7cb2c596"
sid="08d1459247b340738283ee670a5e9039"
client_credentials_manager = SpotifyClientCredentials(client_id=id, client_secret=sid)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def features_track(code):
    #audio features
    features=sp.audio_features(code)[0]
    #general features
    artist = sp.track(code)["artists"][0]["id"]
    artist_pop = sp.artist(artist)["popularity"]
    artist_genres = sp.artist(artist)["genres"]
    #track popularity
    track_pop = sp.track(code)["popularity"]
    features["artist_pop"] = artist_pop
    if artist_genres:
        features["genres"] = " ".join([re.sub(' ','_',i) for i in artist_genres])
    else:
        features["genres"] = "unknown"
    features["track_pop"] = track_pop
    
    return features

if __name__ == "__main__":
    result = features_track("6I9VzXrHxO9rA9A5euc8Ak")
    print(result)


