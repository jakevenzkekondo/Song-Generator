import lyricsgenius
import os

# TODO:
# get rid of the "EmbedShare" token at the end of the lyrics file

# generate an api key and paste it
# https://genius.com/api-clients
genius = lyricsgenius.Genius("api-key-here")

def save_lyrics(songs, artist_name):
    parent_dir = "./songs/"
    path = os.path.join(parent_dir, artist_name)
    os.mkdir(path)

    for i in range(len(songs)):
        song_title = songs[i]
        try:
            song = genius.search_song(song_title, artist_name)
        except TimeoutError:
            print("API failed to find lyrics")
            exit()

        if song is not None:
            lyrics = song.lyrics

            lines = lyrics.splitlines(keepends=True)
            file_name = path + '/' + songs[i] + '.txt'
            with open(file_name, 'w+', encoding='utf-8') as f:
                for line in lines:
                    line = line.replace("EmbedShare", "")
                    line = line.replace("URLCopyEmbedCopy", "")
                    line = line.replace(" ", " ")
                    f.write(line)
        else:
            print(songs[i] + " by " + artist_name + " cannot be found\n")
            print("Please try again")
            exit()
