import lyricsgenius
import os


# generate an api key and paste it
# https://genius.com/api-clients
genius = lyricsgenius.Genius("api-key-here")


def save_lyrics(songs, artist_name):
    parent_dir = "./songs/"
    path = os.path.join(parent_dir, artist_name)
    try:
        os.mkdir(path)
    except FileExistsError:
        print(artist_name + " was already used")

    for i in range(len(songs)):
        song_title = songs[i]
        try:
            song = genius.search_song(song_title, artist_name)
        except Exception:
            print("Lyrics Genius API failed to find lyrics")
            exit()

        if song is not None:
            lyrics = song.lyrics

            lines = lyrics.splitlines(keepends=True)
            file_name = path + '/' + songs[i] + '.txt'
            with open(file_name, 'w+', encoding='utf-8') as f:
                for line in lines:
                    line = line.replace("EmbedShare", "")
                    line = line.replace("URLCopyEmbedCopy", "")
                    f.write(line)
        else:
            print(songs[i] + " by " + artist_name + " cannot be found\n")
            print("Please try again")
            exit()
