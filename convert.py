import os
import yaml
import eyed3
import time

def get_audio_files():
    audio_files = []
    for file in os.listdir('audio'):
        if file.endswith('.mp3'):
            audio_file = eyed3.load(os.path.join('audio', file))
            comments = ''
            if audio_file.tag.comments:
                for comment in audio_file.tag.comments:
                    comments += comment.text + '\n'
            duration = time.strftime('%H:%M:%S', time.gmtime(audio_file.info.time_secs))
            audio_files.append({
                'title': audio_file.tag.title,
                'comments': comments,
                'filename': '/audio/' + file,
                'duration': duration
            })
    return audio_files

def convert_to_yaml():
    data = get_audio_files()
    yaml_data = yaml.dump(data, sort_keys=False)
    return yaml_data

print(convert_to_yaml())