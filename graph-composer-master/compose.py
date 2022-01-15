import string
import random
import re
import os
from graph import Graph
import lyrics

SONG_LENGTH = 200


def get_words_from_text(text_path):
    with open(text_path, 'rb') as file:
        text = file.read().decode("utf-8")
        text = re.sub(r'\[(.+)\]', ' ', text)

    # gets rid of punctuation and makes lowercase
    text = text.replace('\r', '')
    text = text.replace('\n', ' \n ')
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = list(filter(bool, text.split(' ')))

    words = words[:1000]
    return words


def make_graph(words):
    g = Graph()
    prev_word = None
    # for each word
    for word in words:
        # check that word is in graph, and if not then add it
        word_vertex = g.get_vertex(word)

        # if there was a previous word, then add an edge if does not exist
        # if exists, increment weight by 1
        if prev_word:  # prev word should be a Vertex
            # check if edge exists from previous word to current word
            prev_word.increment_edge(word_vertex)
        prev_word = word_vertex
    g.generate_probability_mappings()

    return g


def compose(g, words, length):
    composition = []
    curr_word = g.get_vertex(random.choice(words))

    # we don't want the initial seed word to be the last lyric or a newline
    while len(curr_word.neighbors) == 0 or curr_word == '\n':
        curr_word = g.get_vertex(random.choice(words))

    for _ in range(length):
        composition.append(curr_word.word)
        curr_word = g.get_next_word(curr_word)
        while len(curr_word.neighbors) == 0:
            curr_word = g.get_vertex(random.choice(words))

    # capitalizes lyrics
    composition[0] = composition[0].capitalize()
    for i in range(length - 1):
        if composition[i] == '\n':
            composition[i+1] = composition[i+1].capitalize()
        elif composition[i] == 'i':
            composition[i] = composition[i].capitalize()

    return composition


def main():
    print("If you wish to quit the program, enter QUIT for artist name.")

    while True:
        artist = input("Enter artist name: ")
        if artist == 'QUIT':
            exit()
        songs = input("Enter song names separated by comma: ").split(", ")
        lyrics.save_lyrics(songs, artist)
        words = []

        for song in os.listdir('songs/{}'.format(artist)):
            if song == '.DS_Store':
                continue
            words.extend(get_words_from_text('songs/{artist}/{song}'.format(artist=artist, song=song)))

        g = make_graph(words)
        composition = compose(g, words, SONG_LENGTH)
        print()
        print("Generated song:")

        # removes unicode characters that cannot be printed
        generated_song = ' ' + ' '.join(composition)
        generated_song = generated_song.encode("ascii", "ignore")
        print(generated_song.decode())


if __name__ == '__main__':
    main()
