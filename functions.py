# This is a function which read the content of a file
# and transfer it into a list of every line in the file
def read_file_to_get_raw_lines(filename):
    with open(file=filename, mode='r', encoding='utf-8') as f:
        # Create a list named raw_lines to store the lines without space or line break surrounding:
        raw_lines = []
        for line in f.readlines():
            # Remove the surrounding space and line break of each line in file1
            strip_string = line.strip()
            if strip_string:
                raw_lines.append(strip_string)

    return raw_lines


# From the function: read_file_to_get_raw_lines, we get the list of every line in the file.
# We need to remove the unnecessary lines, and only keep the index, song titles and artists.
# In order to do that, firstly we need to get all the song index numbers and put them into a list.
# This is a function that create a list called index_list to store all the index numbers in raw_data:
def get_indices(raw_lines):
    index_list = []
    for index_num in raw_lines:
        if index_num.isdigit():
            index_list.append(index_num)

    return index_list


# From the function:get_indices, we get the list of index numbers from the file.
# Based on this, we can create a function named get_songs_raw_data to
# generate a list of all index, song names and artists from the indices and raw_lines.
def get_songs_raw_data(indices, raw_lines):
    # Get the first index and last index value:
    first_index_value = indices[0]
    last_index_value = indices[-1]

    # Find the location of the first_index_value and last_index_value in the raw_lines
    first_song_index = raw_lines.index(first_index_value)
    last_song_index = raw_lines.index(last_index_value)

    # Generate the music list based on the first_song_index and last_song_index:
    song_raw_list = raw_lines[first_song_index:last_song_index + 3]
    return song_raw_list


# From the function:get_songs_raw_data, we get a list of index number, song title and artist.
# Based on this, we can create a function named get_song_tuple_list to put the index, song title and artist
# of every song into a tuple and then put all the tuples into a list.
def get_song_tuple_list(song_raw_list):
    song_tuple_list = [tuple(song_raw_list[i:i+3]) for i in range(0, len(song_raw_list), 3)]
    return song_tuple_list


from wordcloud import WordCloud

# This is the function to generate the image of word cloud from the given text
def get_wordcloud(text):

    wordcloud = WordCloud(
        background_color='white',
        width=800,
        height=600,
        margin=2,
        stopwords={'feat', 'remix', 'Radio', 'Edit', 'The', 'I', 'You'}
    ).generate(text)

    return wordcloud

