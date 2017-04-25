#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 22:30:02 2017

@author: T. Swayne
"""

# Do not import anything. Do not leave any debugging print statements

# Goal is to maximize the duration of the playlist 
# but the problem does not mention this in details, only prescribes
# taking the lowest filesize

# If the first song doesn't fit on disk, return an empty list. 

# sorted using python docs sorting HOWTO example
# sorting a list of tuples by the 3rd element

# this is an 0/1 knapsack problem
# asking for a greedy algorithm

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen
    """
    
    playlist = []
    playlist_size = 0
    
    # clone songs list
    songs_remaining = songs[:]
    
    # check if first song is too big
    if songs_remaining[0][1] > max_size:
        return playlist # it will be empty
    else:
        playlist.append(songs_remaining[0][0]) # the song title
        playlist_size += songs_remaining[0][2]
        del songs_remaining[0]
    
    # sort the remaining songs
    list.sort(songs_remaining, key=lambda song: song[2]) 
    
    for song in songs_remaining:
        if playlist_size + song[2] > max_size:
            return playlist # up until now
        else:
            playlist.append(song[0]) # the song title
            playlist_size += song[2]
            
    # now we have added all available songs
    return playlist

# --- testing --- 

a = [('a',1.0,1.0),('b',2.0,1.0),('c',1.0,2.0)]

#len1 = 0.5
#print("for a filesize of",str(len1),"we have:")
#print(song_playlist(a, len1))

len2 = 2.0
len2 = 10.0
len2 = 0.5

print("for a filesize of",str(len2),"we have:")
print(song_playlist(a, len2))


