from libpytunes import Library
import argparse
# import spotipy
# import spotipy.util as util

parser = argparse.ArgumentParser(description='Parse iTunes XML library and output useful things because Apple won\'t help you')
parser.add_argument('file', help='iTunes XML library file to process')
parser.add_argument('--lists', help='file with newline delimited lists to output')
parser.add_argument('--playlist', help='output playlist names only', action='store_true')
parser.add_argument('--spotify', help='transfer playlists to a spotify account')
args = parser.parse_args()

l = Library(args.file)
playlists = l.getPlaylistNames()

# remove first element; by default it's a list of all songs
del playlists[0]

if args.playlist == True:
    for listname in playlists:
        print(listname)
else:
    # if specific playlists desired, prepare array
    lists = []
    if args.lists:
        # lists = open(args.lists).readlines()
        listfile = open(args.lists)
        for line in listfile:
            line = line.rstrip()
            lists.append(line)

    # determine if playlist flag set, if so limit scope to specified lists
    for listname in playlists:
        if listname in lists or not args.lists:
            print('Playlist: ', listname)
            for song in l.getPlaylist(listname).tracks:
                print('  ',song.name,'-',song.artist,'-',song.album)
