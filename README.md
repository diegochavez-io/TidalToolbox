# TidalToolBox

This repository contains Python scripts designed to assist with preparing audio files for live coding sessions in TidalCycles.

## Introduction

TidalToolBox provides tools for chopping up audio files into segments based on the BPM and applying a fade in and fade out to each segment to prevent pops or clicks. The scripts are designed to be flexible and can be adapted to fit your specific needs.

## Installation

1. Make sure you have Python installed, preferably version 3.8 or later.
2. Install the necessary Python libraries with pip:

    ```
    pip install pydub
    ```

## Usage

### OctaveSplit.py

The OctaveSplit script chops up an audio file into bar-length segments based on the provided BPM. It then applies a fade in and fade out to each segment and saves the segments as individual files, split into two folders, each representing an octave.

To use the script, simply replace the directory path, 'dir_path', with your own directory path where your .wav files are located.

### BeatSlicer.py

The BeatSlicer script chops up an audio file into bar-length segments based on the provided BPM. It then applies a fade in and fade out to each segment and saves the segments as individual files in one folder.

To use the script, simply replace the directory path, 'dir_path', with your own directory path where your .wav files are located.

### AudioFades.py

The AudioFades script applies a fade in and fade out to a given audio file to prevent pops or clicks and saves the treated audio in a 'processed' subfolder.

To use the script, simply replace the directory path, 'dir_path', with your own directory path where your .wav files are located.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss the changes you'd like to make.
