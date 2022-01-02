import lyricsgenius
import os


# generate an api key and paste it
# https://genius.com/api-clients
genius = lyricsgenius.Genius("api-key-here")

def save_lyrics(songs, artist_name):
    parent_dir = "./songs/"
    path = os.path.join(parent_dir, artist_name)
    os.mkdir(path)

    for i in range(len(songs)):
        song_title = songs[i]
        song = genius.search_song(song_title, artist_name)
        lyrics = song.lyrics
        # with open('songs/{}/{}_{}_{}.txt'.format('_'.join(artist_name.split(' ')), i+1, '-'.join(''.join(song_title.split('\'')).split(' '))), 'w') as f:
            # f.writelines(lyrics.split('\\n'))

        lines = lyrics.split("\\n")
        file_name = path + '/' + songs[i] + '.txt'
        with open(file_name, 'w+', encoding='utf-8') as f:
            for line in lines:
                line = line.replace("347EmbedShare", "")
                line = line.replace("URLCopyEmbedCopy", "")
                line = line.replace(" ", " ")
                f.write(line)

if __name__ == '__main__':
    songs = [
        'the box',
        'down below',
        'project dreams',
        'die young',
        'boom boom room',
        'high fashion',
        'roll dice',
        'war baby',
        'every season'
    ]
    songs2 = [
        'vent'
    ]
    save_lyrics(songs2, 'baby keem')
