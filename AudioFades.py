import os
from pydub import AudioSegment

# the fade duration in milliseconds
fade_duration = 25  # 50ms, adjust as needed

# directory where you have your wav files
dir_path = '/Users/Samples/'  # replace this with your actual path

# create a subdirectory for the processed files
output_dir = os.path.join(dir_path, 'processed')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# list all files in the directory
files = os.listdir(dir_path)

# process each file
for filename in files:
    # only process .wav files
    if filename.endswith('.wav'):
        # full path to the file
        file_path = os.path.join(dir_path, filename)
        
        # load the song
        song = AudioSegment.from_file(file_path)

        # add fade in and out
        song = song.fade_in(fade_duration).fade_out(fade_duration)
            
        # save the song to the output directory
        output_path = os.path.join(output_dir, filename)
        
        print("Saving to:", output_path)
        song.export(output_path, format="wav")
