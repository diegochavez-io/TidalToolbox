# TidalToolBox

This repository provides tools for chopping up audio files into segments based on the BPM and applying a fade in and fade out to each segment to prevent pops or clicks. 

## Installation

1. Make sure you have Python installed, preferably version 3.8 or later.
2. Install the necessary Python libraries with pip:

    ```
    pip install pydub
    ```

## Usage

### OctaveSplit.py

Based on the provided BPM, the script chops up an audio file into bar-length segments. It then applies a fade in and fade out to each segment and saves the segments as individual files, split into two folders, representing a lower and higher octave numbered 1-12, and 13-24.

Replace the directory path, 'dir_path', with your own directory path where your .wav files are located.

### BeatSlicer.py

Chops up an audio file into bar-length segments based on the provided BPM. It then applies a fade in and fade out to each segment and saves the segments as individual files in one folder.

Replace the directory path, 'dir_path', with your own directory path where your .wav files are located.

### DrumKit.py

Automates the process of generating drum samples from drum kit audio files. Segments the audio data into chunks between successive onsets. Each segment corresponds to a drum hit or sample. Applies a linear fade-in and fade-out effect to each segment. Fade durations can be adjusted. Saves each processed segment as a separate .wav file in a corresponding subdirectory.

### AudioFades.py

Applies a fade in and fade out to a given audio file to prevent pops or clicks and saves the treated audio in a 'processed' subfolder.

To use the script, simply replace the directory path, 'dir_path', with your own directory path where your .wav files are located.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss the changes you'd like to make.
