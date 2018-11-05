import requests
import os


class Song:
    endpoint = 'https://api.lyrics.ovh/v1/{}/{}'
    all_lyrics_path = os.path.join(os.getcwd(), 'Artists_lyrics')

    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        self.artist_lyrics_path = os.path.join(Song.all_lyrics_path, self.artist)

    def search_lyrics(self):
        """
        Returns the song lyrics as str
        or None if request status code <> 200.
        """
        url = self.endpoint.format(self.artist, self.title)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['lyrics']
        else:
            return None

    def save_lyrics(self):
        """
        Saves the lyrics in the artist's folder.
        Filename = song title.
        Returns True if file has been saved, False if not.
        """
        song_lyrics = self.search_lyrics()
        if song_lyrics is not None:
            Song.create_folder_if_not_exists(self.artist_lyrics_path)
            song_path = os.path.join(self.artist_lyrics_path, Song.remove_chars(self.title))
            with open(song_path, 'w', encoding='utf-8') as new_file:
                new_file.write(song_lyrics)
            return True
        else:
            return False

    @staticmethod
    def create_folder_if_not_exists(path):
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def remove_chars(text: str) -> str:
        """
        Removes '/', '\', '?', '*', ':', '"', '<', '>', '|' chars
        from given text
        to ensure that the returned string can be used as the file name.
        """
        string = ''.join(e for e in text if e not in ['/', '\\', '?', '*', ':', '"', '<', '>', '|'])
        return string
