This program was written by Jakob Venzke-Kondo and Uzay Takil


USAGE: 
Thank you for using our Song Generator.
The program will prompt you for the name of a musical artist and some of their songs. It will then generate
a 200 word song based on the songs that you inputted. If you use the same artist multiple times the new songs
will be considered as well as the previous ones you entered. 

You can exit the program by typing in QUIT when prompted for the artist name.

If the Genius Lyrics API is unable to find a requested song by the artist, the program will notify you. If
none of the requested songs could be found, the program will notify you and quit.


HOW IT WORKS:
Our program makes use of the Genius Lyrics API to pull the lyrics of songs off of the website genius.com.
Once the user inputs the requested songs by an artist, those songs' lyrics are pulled from genius.com and
written to text files in a newly created directory. 

Then a graph is created, with each unique word in all of the lyrics as a vertex. Each vertex points to other
vertices that represent unique words that immediately follow that word. The weights of the edges are how many
times that word follows the other word.

The song is generated via a Markov chain. First a initial word vertex is selected from the graph. The next word
in the generated song is one of the words that vertex points to, and the likelihood of the vertex being chosen
is porportional to the edge weights. This continues until the 200 word song was been written, and is then
printed.
