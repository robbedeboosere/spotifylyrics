import requests
from lyricsgenius import Genius

SPOTIFY_ACCESS_TOKEN = 'BQCrpG5OSFcayHkj4EEx0D2OQHxhy6apPJUrJQCiDreM4vBrk8w2NaPqpT8KAHhUTYdGq4dqACW7x5gC-ciNWmDcerv1_62Q5jmJJ7mVcGG0rn9YZjj71NwCFn4WZjQJZK6dROGzk7A0EocHs2SP'
SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'

GENIUS_ACCESS_TOKEN = 'oHUhSDrfKhedVIIWkYSToMuWs6D6BYtlqfpikzczQDRu2K9Knm0TKjek554RIhOH'
genius = Genius(GENIUS_ACCESS_TOKEN)

def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers = {
            'Authorization': f'Bearer {access_token}'
            }
        )
    resp_json = response.json()
    current_track_info = {
        "name": resp_json['item']['name'],
        "artists":[artist['name'] for artist in resp_json['item']['artists']]
    }
    return current_track_info

def get_current_lyrics():
    current_track = get_current_track(SPOTIFY_ACCESS_TOKEN)
    name = current_track.get('name').split('(')[0].rstrip()
    artist = genius.search_artist(current_track.get('artists')[0],max_songs=0)
    artist.add_song(name)
    song = genius.search_song(name,artist.name)
    return song.lyrics

if __name__ == '__main__':
    print(get_current_lyrics())
    #print(get_current_track(SPOTIFY_ACCESS_TOKEN))