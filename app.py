import spacy
import lyricsgenius

print('yes')
genius = lyricsgenius.Genius("cBFptPjIfCWpvKjqgMgXmOW24-D-Xfx9A4wa11p_GJ2JeM82HBsJidIAJCx4NbMs")
artist = genius.search_artist("Eminem", max_songs=3, sort="title")
print(artist.songs)