import os
import eyed3

# Create a function that reads audio files in the mp3 format from 
# the 'audio' directory and returns a list of dictionaries containing
# the title and comments for each file.
def get_audio_files():
    audio_files = []
    for file in os.listdir('audio'):
        if file.endswith('.mp3'):
            audio_file = eyed3.load(os.path.join('audio', file))
            audio_files.append({
                'title': audio_file.tag.title,
                'comments': audio_file.tag.comments
            })
    return audio_files

print(get_audio_files())