from libpytunes import Library
import argparse

parser = argparse.ArgumentParser(description='Parse iTunes XML library and output useful things because Apple won\'t help you')
parser.add_argument('file', help='iTunes XML library file to process')
parser.add_argument('lists', help='space separated names of playlists to output', nargs='*')
parser.add_argument('--playlist', help='output playlist names only', action='store_true')
args = parser.parse_args()

l = Library(args.file)
playlists = l.getPlaylistNames()

# remove first element; by default it's a list of all songs
del playlists[0]

if args.playlist == True:
    for listname in playlists:
        print(listname)
else:
    for listname in playlists:
        print('Playlist: ',listname)
        for song in l.getPlaylist(listname).tracks:
            print('  ',song.name,'-',song.artist,'-',song.album)
