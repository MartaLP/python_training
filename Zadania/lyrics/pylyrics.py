# import sys
# sys.path.append('C:\\Users\\mlys\\Desktop\\My_stuff\\PYTHON_KURS\\PyCharm_Projekt')
from Zadania.lyrics.Song import Song
from Zadania.lyrics.Artist import Artist


while True:
    user_input = input("Enter the artist name or type q to exit.\n ").strip()
    if user_input.lower() == "q":
        print("Exiting")
        break
    else:
        artist = Artist(user_input)
        artist_songs = artist.search_titles()
        if artist_songs is None:
            print(f"{artist.name} songs not found.")
        else:
            print(f"The following songs found for '{artist.name}':")
            for title in artist_songs:
                print(title)
            option = input('Try to find lyrics? y - yes, other - no\n').strip().lower()
            if option == 'y':
                for title in artist_songs:
                    song = Song(artist.name, title)
                    if song.save_lyrics():
                        print(f'Lyrics for {title} saved.')
                    else:
                        print(f'Lyrics for {title} not found.')
            else:
                print("Exiting")
                continue
