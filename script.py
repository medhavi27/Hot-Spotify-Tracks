import spotipy
import json
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials(client_id='892032ace0be417288450d053972970f',
                                                      client_secret='a89a7fa1ce9f4b90aa2d7be97ec57148')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
def write_tracks(text_file, tracks):
    json_list = []
    with open(text_file, 'a') as file_out:
        while True:
            for item in tracks['items']:
                if 'track' in item:
                    track = item['track']
                else:
                    track = item
                try:
                    print(track['popularity'])
                    track_url = track['external_urls']['spotify']
                    features = spotify.audio_features([track['id']])[0]
                    features['song_id'] = track['id']
                    features['name'] = track['name']
                    features['date'] = track['album']['release_date']
                    features['year'] = track['album']['release_date'].split('-')[0]
                    features['popularity'] = track['popularity']
                    json_list.append(features)
                    # file_out.write(json.dumps(features) + '\n')
                except KeyError:
                    print(u'Skipping track {0} by {1} (local only?)'.format(
                            track['name'], track['artists'][0]['name']))
            # 1 page = 50 results
            # check if there are more pages
            if tracks['next']:
                tracks = spotify.next(tracks)
            else:
                pd.read_json(json.dumps(json_list))
                open('data0.csv', 'a').write(pd.read_json(json.dumps(json_list)).to_csv())
                break
def write_playlist(username, playlist_id):
    results = spotify.user_playlist(username, playlist_id)
    text_file = u'{0}.txt'.format(results['name'], ok='-_()[]{}')
    print(u'Writing {0} tracks to {1}'.format(
            results['tracks']['total'], text_file))
    tracks = results['tracks']
    write_tracks(text_file, tracks)
def main():
    # small playlist
    # write_playlist('cwang.txt', '2YRe7HRKNRvXdJBp9nXFza')
    #big playlist
    write_playlist('cwang.txt', '2sRZldX6n9oaII70OoO3zB')
if __name__ == "__main__":
    main()
