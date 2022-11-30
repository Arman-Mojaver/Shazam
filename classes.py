# Create a class named Song, with 3 attributes: index, song_title, artist.
# Each song from the file is one of the objects of the song class
class Song:

    def __init__(self, index, song_title, artist):
        self.index = index
        self.song_title = song_title
        self.artist = artist

    def __repr__(self):
        return f"Song<index: {self.index}, song title: {self.song_title}, artist: {self.artist}>"


# Create a class named Songs that handle the list of song objects
class Songs:
    def __init__(self, song_data):
        # song_data is the list of tuples of songs
        self.song_data = song_data
        # song_objects is the list of Song objects
        self.song_objects = self.get_song_objects()
        # artists is the list of artists
        self.artists = self.get_artists()
        # song_titles is the list of song_titles
        self.song_titles = self.get_song_titles()

    # This method creates a list of objects of type Song.
    # We use Song class here so that we can convert the tuples into Song objects
    def get_song_objects(self):
        return [Song(song[0], song[1], song[2]) for song in self.song_data]

    def get_artists(self):
        return [song.artist for song in self.song_objects]

    def get_song_titles(self):
        return [song.song_title for song in self.song_objects]

    def print(self):
        for song in self.song_objects:
            print(song)

# Create a class named DataHandler that handle the data from the file and remove duplicates
class DataHandler:
    def __init__(self, file):
        self.file = file
        self.raw_lines = self.read_file_to_get_raw_lines()
        self.indices = self.get_indices()
        self.song_raw_list = self.get_songs_raw_data()
        self.song_tuple_list = self.get_song_tuple_list()
        self.unique_songs = self.remove_duplicates()
        self.reindexed_songs = self.reindex()

    # This is a function which read a file and transfer it into a list of every line in the file
    def read_file_to_get_raw_lines(self):
        with open(file=self.file, mode='r', encoding='utf-8') as f:
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
    def get_indices(self):
        index_list = []
        for index_num in self.raw_lines:
            if index_num.isdigit():
                index_list.append(index_num)

        return index_list

    # From the function:get_indices, we get the list of index numbers from the file.
    # Based on this, we can create a function named get_songs_raw_data to
    # generate a list of all index, song names and artists from the indices and raw_lines.
    def get_songs_raw_data(self):
        # Get the first index and last index value:
        first_index_value = self.indices[0]
        last_index_value = self.indices[-1]

        # Find the location of the first_index_value and last_index_value in the raw_lines
        first_song_index = self.raw_lines.index(first_index_value)
        last_song_index = self.raw_lines.index(last_index_value)

        # Generate the music list based on the first_song_index and last_song_index:
        song_raw_list = self.raw_lines[first_song_index:last_song_index + 3]

        return song_raw_list

    # From the function:get_songs_raw_data, we get a list of index number, song title and artist.
    # Based on this, we can create a function named get_song_tuple_list to put the index, song title and artist
    # of every song into a tuple and then put all the tuples into a list.
    def get_song_tuple_list(self):
        return [tuple(self.song_raw_list[i:i + 3]) for i in range(0, len(self.song_raw_list), 3)]

    # From the function: get_song_tuple_list, we get the list of tuple of song.
    # But it may have duplicates in this list, so we need to remove duplicates.
    # Function: remove_duplicates is the function to get the unique tuple of the song title and artist
    def remove_duplicates(self):
        return list(set([(index_title_artist[1], index_title_artist[2]) for index_title_artist in self.song_tuple_list]))

    # From the function: remove_duplicates, we get the list of unique tuple of the song title and artist
    # Based on this, we create a function named reindex to add the index into every tuple
    # In this function, we also sort the songs by artist name.
    def reindex(self):
        sorted_songs = sorted(self.unique_songs, key=lambda unique_songs: unique_songs[1])
        return [(index, song[0], song[1]) for index, song in enumerate(sorted_songs, 1)]

    def print(self):
        for song in self.reindexed_songs:
            print(song)

