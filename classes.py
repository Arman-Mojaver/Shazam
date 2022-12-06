import json
from os.path import exists as file_exists

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
    def __init__(self, file):
        self.file = file
        self.raw_lines = self.read_file_to_get_raw_lines()
        self.indices = self.get_indices()
        self.song_raw_list = self.get_songs_raw_data()
        self.song_tuple_list = self.get_song_tuple_list()
        self.unique_songs = self.remove_duplicates()
        self.json_songs = self.filter_songs()

    # This is a method which read a file and transfer it into a list of every line in the file
    def read_file_to_get_raw_lines(self):
        with open(file=self.file, mode='r', encoding='utf-8') as f:
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
    def get_song_tuple_list(self):
        return [tuple(self.song_raw_list[i:i + 3]) for i in range(0, len(self.song_raw_list), 3)]

    # From the method get_song_tuple_list(), we get the list of tuple of song.
    # But it may have duplicates in this list, so we need to remove duplicates.
    # method remove_duplicates() is the function to get the unique tuple of the song title and artist
    def remove_duplicates(self):
        return list(set([(index_title_artist[1], index_title_artist[2]) for index_title_artist in self.song_tuple_list]))

    def print(self):
        for song in self.unique_songs:
            print(song)

    # We save the unique_songs into a json file
    def save_json(self):
        song_list = self.unique_songs
        # Transfer the list into json format
        json_songs = json.dumps(song_list, ensure_ascii=False, indent=2)
        with open(file='old_songs.json', mode='w', encoding='utf-8') as f1:
            f1.write(json_songs)
            f1.close()

    # We load the content of the songs in 'old_songs.json'
    def load_json(self):
        with open(file='old_songs.json', mode='r', encoding='utf-8') as f2:
            return set(tuple(song) for song in json.load(f2))

    def filter_songs(self):
        song_list = self.unique_songs
        #  If the songs in the file are being saved for the first time,
        #  we create a json file named 'old_songs.json' which contains the songs that just have been saved.
        if not file_exists('old_songs.json'):
            print('The songs are being loaded for the first time, and old_songs.json is created!')
            self.save_json()
        # When the file gets updated with a few extra songs,we return the new songs.
        else:
            new_songs = set(song_list) - self.load_json()
            if new_songs:
                print('New songs which need to be downloaded: ')
                return new_songs
            else:
                print('There is no extra new song to be downloaded.')







