import os

# read mp3 files from the audio directory and list them
def read_mp3_files():
    audio_files = []
    for file in os.listdir("audio"):
        if file.endswith(".mp3"):
            audio_files.append(file)
    return audio_files

print(read_mp3_files())