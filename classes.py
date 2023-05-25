import pandas as pd
import os

class Song:

    def __init__(self, song_title, artist):
        self.song_title = song_title
        self.artist = artist

    def __repr__(self):
        return f"Song<song title: {self.song_title}, artist: {self.artist}>"


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

# Create a class named DataHandler that handle the data from the file and build a data frame
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
        self.df = self.build_dataframe()
        self.remove_duplicates()
        self.filter_old_songs()

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

    def get_indices(self):
        return [index_num for index_num in self.raw_lines if index_num.isdigit()]

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

    def get_songs(self):
        return [tuple(self.song_raw_list[i:i + 2]) for i in range(1, len(self.song_raw_list), 3)]

    def build_dataframe(self):
        return pd.DataFrame(self.songs, columns=['Title', 'Artist'])

    def remove_duplicates(self):
        if self.df.duplicated().any():
            self.df = self.df.drop_duplicates()

    def print(self):
        print(self.df.reset_index(drop=True))

    def save_json(self):
        self.df.to_json(self.OLD_SONGS_FILE_NAME)

    # We load the content of the songs in 'old_songs.json'
    def load_json(self):
        return pd.read_json(self.OLD_SONGS_FILE_NAME)

    def filter_old_songs(self):
        #  If the songs in the file are being saved for the first time,
        #  we create a json file named 'old_songs.json' which contains the songs that just have been saved.
        if not os.path.exists(self.OLD_SONGS_FILE_NAME):
            print('The songs are being loaded for the first time to old_songs.json!')
            self.save_json()
            # This return statement means "exit the method without doing anything else"
            # Methods and functions only need to return something if it is going to be used later on in the code
            return

        # Load the content of 'old_songs.json' into a dataframe named df2
        loaded_df = self.load_json()
        print('Totally {} songs are downloaded!'.format(len(loaded_df)))
        if self.df.equals(loaded_df):
            print('There is no extra new song to be downloaded.')
            quit()

        self.extra_df = self.df[~self.df.isin(loaded_df)].dropna()
        print('Number of new songs to be downloaded: {}'.format(len(self.extra_df)))
        print('List of new songs:')
        print(self.extra_df.to_string(index=False))











