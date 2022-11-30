from classes import Songs, DataHandler
#import matplotlib.pyplot as plt

# Open the file which is named shazam.txt and read the content of this file
my_file = 'shazam.txt'
data_handler = DataHandler(my_file)
# Print all the reindexed songs in the class of DataHandler
data_handler.print()

# songs is the list of tuples of songs from the original file
songs = Songs(song_data=data_handler.reindexed_songs)
# Print all the reindexed songs in the class of Songs
songs.print()

# We create the word cloud of the artists
#text = ' '.join(songs.artists)
#wordcloud_1 = get_wordcloud(text)
#plt.imshow(wordcloud_1)
#plt.axis('off')
#plt.show()

#wordcloud_1.to_file('shazam_artist_wordcloud.png')