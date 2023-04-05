#find librarys that import excel files into a format the computer can read
#import random
#count number of songs in list
#create a randomizer 
#user input where user chooses what genres/songs they want to exclude from the queue

import random
#import openpyxl

#Define all the songs and their respected genres, this is where i would import my entire file of songs and their respected genres

song_list = [("song 1", "Rock"),("song 2", "Pop"),("song 3", "Rap"),("song 4", "EDM"),("song 5", "Jazz")]

#Define a dictionary to keep track of the count of songs by genre
genre_count = { "Rock": 0,"Pop": 0,"Rap": 0,"EDM": 0, "Jazz": 0}

#Randomly select 5 songs from the list
for i in range(10):
    song = random.choice(song_list)
    print(f"Playing {song[0]} ({song[1]})")
    genre_count[song[1]] += 1

# Print the count of songs by genre
print(f"Number of Rock songs played: {genre_count['Rock']}")
print(f"Number of Pop songs played: {genre_count['Pop']}")
print(f"Number of Pop songs played: {genre_count['Rap']}")
print(f"Number of Pop songs played: {genre_count['EDM']}")
print(f"Number of Pop songs played: {genre_count['Jazz']}")