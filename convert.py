import os

# Create a function that reads audio files in the mp3 format from 
# the 'audio' directory and returns a list of them.
def get_audio_files():
    audio_files = []
    for file in os.listdir('audio'):
        if file.endswith('.mp3'):
            audio_files.append(file)
    return audio_files

print(get_audio_files())