import json
import os

# Create a class named Song, with 3 attributes: index, song_title, artist.
# Each song from the file is one of the objects of the song class
class Song:

    def __init__(self, song_title, artist):
        self.song_title = song_title
        self.artist = artist

    def __repr__(self):
        return f"Song<song title: {self.song_title}, artist: {self.artist}>"


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
        return [Song(song[0], song[1]) for song in self.song_data]

    def get_artists(self):
        return [song.artist for song in self.song_objects]

    def get_song_titles(self):
        return [song.song_title for song in self.song_objects]

    def print(self):
        for song in self.song_objects:
            print(song)

# Create a class named DataHandler that handle the data from the file and remove duplicates
class DataHandler:

    # Class variables belong to the class
    # When objects are created from the class, they also have the class variables.
    SHAZAM_FILE_NAME = 'shazam2.txt'
    OLD_SONGS_FILE_NAME = 'old_songs.json'

    def __init__(self):
        self.raw_lines = self.read_file_to_get_raw_lines()
        self.indices = self.get_indices()
        self.song_raw_list = self.get_songs_raw_data()
        self.songs = self.get_songs()
        self.remove_duplicates_and_indices()
        self.filter_old_songs()

    # This is a method which read a file and transfer it into a list of every line in the file
    def read_file_to_get_raw_lines(self):
        with open(file=self.SHAZAM_FILE_NAME, mode='r', encoding='utf-8') as f:
            # Create a list named raw_lines to store the lines without space or line break surrounding:
            raw_lines = []
            for line in f.readlines():
                # Remove the surrounding space and line break of each line in f
                strip_string = line.strip()
                if strip_string:
                    raw_lines.append(strip_string)

        return raw_lines

    # From the method: read_file_to_get_raw_lines(), we get the list of every line in the file.
    # We need to remove the unnecessary lines, and only keep the index, song titles and artists.
    # In order to do that, firstly we need to get all the song index numbers and put them into a list.
    # This is a function that create a list called index_list to store all the index numbers in raw_data:
    def get_indices(self):
        return [index_num for index_num in self.raw_lines if index_num.isdigit()]

    # From the method:get_indices(), we get the list of index numbers from the file.
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

    # From the method get_songs_raw_data(), we get a list of index number, song title and artist.
    # Based on this, we can create a method named get_song_tuple_list() to put the index, song title and artist
    # of every song into a tuple and then put all the tuples into a list.
    def get_songs(self):
        return [tuple(self.song_raw_list[i:i + 3]) for i in range(0, len(self.song_raw_list), 3)]

    # From the method get_song_tuple_list(), we get the list of tuple of song.
    # But it may have duplicates in this list, so we need to remove duplicates.
    # method remove_duplicates() is the function to get the unique tuple of the song title and artist
    def remove_duplicates_and_indices(self):
        self.songs = list(
            set([(index_title_artist[1], index_title_artist[2]) for index_title_artist in self.songs])
        )

    def print(self):
        for song in self.songs:
            print(song)

    # We save the songs into a json file
    def save_json(self):
        with open(file=self.OLD_SONGS_FILE_NAME, mode='w', encoding='utf-8') as f:
            json.dump(self.songs, f, ensure_ascii=False, indent=2)

    # We load the content of the songs in 'old_songs.json'
    def load_json(self):
        with open(file=self.OLD_SONGS_FILE_NAME, mode='r', encoding='utf-8') as f:
            return set(tuple(song) for song in json.load(f))

    def filter_old_songs(self):
        #  If the songs in the file are being saved for the first time,
        #  we create a json file named 'old_songs.json' which contains the songs that just have been saved.
        if not os.path.exists(self.OLD_SONGS_FILE_NAME):
            print('The songs are being loaded for the first time, and old_songs.json is created!')
            self.save_json()
            # This return statement means "exit the method without doing anything else"
            # Methods and functions only need to return something if it is going to be used later on in the code
            return

        self.songs = set(self.songs) - self.load_json()
        if not self.songs:
            print('There is no extra new song to be downloaded.')
            quit()

        print('New songs which need to be downloaded: \n', self.songs)








