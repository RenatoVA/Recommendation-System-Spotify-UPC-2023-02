from pprint import pprint
import json
import pandas as pd
path="./data/spotify_dataset.json"


if __name__=="__main__":
    data=json.loads(open(path).read())["playlists"]
    playlistdf=pd.json_normalize(data, record_path=None, meta=['name','collaborative','num_tracks','num_albums','num_followers','num_edits','duration_ms','num_artists'])
    tracksdf = pd.json_normalize(data, record_path='tracks', meta=['name'])
    playlistdf=playlistdf.drop("tracks",axis=1)
    playlistdf.to_csv("./data/raw_playlists.csv")
    tracksdf.to_csv("./data/raw_tracks.csv")
