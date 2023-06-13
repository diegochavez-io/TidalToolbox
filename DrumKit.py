import os
import librosa
import numpy as np
from scipy.io import wavfile

# Define fade in and fade out durations in milliseconds
fade_in_ms = 10
fade_out_ms = 100

# Function to create the fade in and fade out window
def create_fade_in_out_window(n_samples, sr, fade_in_ms, fade_out_ms):
    window = np.ones(n_samples)
    fade_in_samples = min(int(sr * fade_in_ms / 1000), n_samples)
    fade_out_samples = min(int(sr * fade_out_ms / 1000), n_samples)
    fade_in_window = np.linspace(0, 1, fade_in_samples)
    fade_out_window = np.linspace(1, 0, fade_out_samples)
    window[:fade_in_samples] = fade_in_window
    window[-fade_out_samples:] = fade_out_window
    return window

# Directory containing audio files
audio_dir = '/Samples/'

for filename in os.listdir(audio_dir):
    if filename.endswith(('.aif', '.wav', '.mp3')):
        base_filename = os.path.splitext(filename)[0]
        samples_dir = os.path.join(audio_dir, f'{base_filename}')
        if not os.path.exists(samples_dir):
            os.makedirs(samples_dir)

        filepath = os.path.join(audio_dir, filename)
        audio_data, sr = librosa.load(filepath, sr=None)
        o_env = librosa.onset.onset_strength(y=audio_data, sr=sr)
        onsets = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr, backtrack=True)
        onset_samples = librosa.frames_to_samples(onsets)
        onset_samples = np.append(onset_samples, [len(audio_data)])
        
        for i in range(len(onset_samples) - 1):
            start_sample = onset_samples[i]
            end_sample = onset_samples[i+1]
            segment = audio_data[start_sample:end_sample]
            window = create_fade_in_out_window(len(segment), sr, fade_in_ms, fade_out_ms)
            segment = segment * window
            
            # Save the processed segment as a WAV file in the created directory
            output_filepath = os.path.join(samples_dir, f'{base_filename}_{i}.wav')
            wavfile.write(output_filepath, sr, segment)
