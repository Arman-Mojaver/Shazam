# Create a class named Song, with 3 attributes: index, song, artist:
class Song:

    def __init__(self, index, song, artist):
        self.index = index
        self.song = song
        self.artist = artist

    def __repr__(self):
        return f"{self.index}, Song:{self.song}, Artist:{self.artist}"
