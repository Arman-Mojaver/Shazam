from functions import (
    read_file_to_get_raw_lines,
    get_indices,
    get_songs_raw_data,
    get_song_tuple_list,
    get_wordcloud
)
from classes import Songs
import matplotlib.pyplot as plt

# Open the file which is named shazam.txt and read the content of this file
my_file = 'shazam.txt'
# We convert the content from the shazam.txt into a list of tuple of a song
# including index, song title and artist step by step.
raw_lines = read_file_to_get_raw_lines(my_file)
indices = get_indices(raw_lines)
song_raw_list = get_songs_raw_data(indices, raw_lines)
song_tuple_list = get_song_tuple_list(song_raw_list)

# songs is the list of tuples of songs from the original file
songs = Songs(song_data=song_tuple_list)
# print all the song objects
for song in songs.song_objects:
    print(song)

# We create the word cloud of the artists
text = ' '.join(songs.artists)
wordcloud_1 = get_wordcloud(text)
plt.imshow(wordcloud_1)
plt.axis('off')
plt.show()

wordcloud_1.to_file('shazam_artist_wordcloud.png')
