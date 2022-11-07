from functions import (
    read_shazam_to_get_raw_lines,
    get_indices,
    get_songs_raw_data,
    get_song_tuple_list,
    get_song_objects
)

file1 = 'shazam.txt'

raw_lines = read_shazam_to_get_raw_lines(file1)
indices = get_indices(raw_lines)

music_result = get_songs_raw_data(indices, raw_lines)
music_tuple = get_song_tuple_list(music_result)

songs = get_song_objects(music_tuple)

for song in songs:
    print(song)
