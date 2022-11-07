from classes import Song

# Function 1: read_shazam_to_get_raw_lines
# read_shazam_to_get_raw_lines is a function which read the content of a file
# and transfer it into a list of each line in the file
def read_shazam_to_get_raw_lines(file1):
    with open(file=file1, mode='r', encoding='utf-8') as f1:
        # Create a list named raw_lines to store the lines without space or line break surrounding:
        raw_lines = []
        for line in f1.readlines():
            # Remove the surrounding space and line break of each line in file1
            strip_string = line.strip()
            if strip_string:
                raw_lines.append(strip_string)

    return raw_lines


# Function 2: get_indices
# get_indices is a function that create a list called index_list to store all the index numbers in raw_data:
def get_indices(raw_lines):
    index_list = []
    for index_num in raw_lines:
        if index_num.isdigit():
            index_list.append(index_num)

    return index_list


# Function 3: get_songs_raw_data
# From the raw_lines and index_list to get the music list
def get_songs_raw_data(indices, raw_lines):
    # Get the first index and last index value:
    first_index_value = indices[0]
    last_index_value = indices[-1]

    # Find the location of the first_index_value and last_index_value in the raw_lines
    first_song_index = raw_lines.index(first_index_value)
    last_song_index = raw_lines.index(last_index_value)

    # Generate the music list based on the first_song_index and last_song_index:
    music_list = raw_lines[first_song_index:last_song_index + 3]
    return music_list


# Function 4: get_song_tuple_list
# Spilt the music form music_list to a list of tuple
# In this case, we spilt the list in every step 3:
def get_song_tuple_list(music_list):
    tuple_list = [tuple(music_list[i:i+3]) for i in range(0, len(music_list), 3)]
    return tuple_list


# Function 5: get_song_objects
# Create the function to pass all the songs into the object of Class Song:
def get_song_objects(tuple_list):
    return [Song(song[0], song[1], song[2]) for song in tuple_list]
