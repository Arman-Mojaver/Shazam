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
