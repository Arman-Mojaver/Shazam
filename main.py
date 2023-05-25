from classes import Songs, DataHandler

my_file = 'shazam.txt'
data_handler = DataHandler()
data_handler.remove_duplicates()
data_handler.print()
data_handler.filter_old_songs()

