import string
import random
import re
import os
from graph import Graph
import lyrics


def get_words_from_text(text_path):
    with open(text_path, 'rb') as file:
        text = file.read().decode("utf-8")

        text = re.sub(r'\[(.+)\]', ' ', text)

    # turns the text into all lowercase separated by only spaces
    text = ' '.join(text.split())
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()
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


def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.word)
        word = g.get_next_word(word)

    return composition


def main():
    artist = input("Enter artist name: ")
    songs = input("Enter song names separated by comma: ").split(", ")
    lyrics.save_lyrics(songs, artist)
    words = []

    for song in os.listdir('songs/{}'.format(artist)):
        if song == '.DS_Store':
            continue
        words.extend(get_words_from_text('songs/{artist}/{song}'.format(artist=artist, song=song)))

    g = make_graph(words)
    composition = compose(g, words, 100)
    print(' '.join(composition))


if __name__ == '__main__':
    main()

