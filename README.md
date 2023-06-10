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

To use the script, simply replace the directory path, 'dir_path', with your own directory path where your .wav files are located.

### BeatSlicer.py

Chops up an audio file into bar-length segments based on the provided BPM. It then applies a fade in and fade out to each segment and saves the segments as individual files in one folder.

To use the script, simply replace the directory path, 'dir_path', with your own directory path where your .wav files are located.

### AudioFades.py

Applies a fade in and fade out to a given audio file to prevent pops or clicks and saves the treated audio in a 'processed' subfolder.

To use the script, simply replace the directory path, 'dir_path', with your own directory path where your .wav files are located.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss the changes you'd like to make.
