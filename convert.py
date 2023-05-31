# read the audio folder and list the files inside it

import os

# path to the audio folder
path = 'audio'

def create_audio_list_from_files():
    # list all the files inside the audio folder
    files = os.listdir(path)
    # create a list of audio files
    audio_files = []
    # loop through all the files and add the audio files to the list
    for file in files:
        if file.endswith('.mp3'):
            audio_files.append(file)
    return audio_files

print(create_audio_list_from_files())