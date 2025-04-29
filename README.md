# Single Pulse Detection and Classification

This repository contains several elements for detecting and classifying individual pulses from the Crab pulsar in filterbank files:

1. **`DM_time_dataset_creator/`**: A module for generating DM-Time datasets from transient candidate data.
2. **`single_pulse_classifier_training/`**: Scripts for training machine learning models to classify single-pulse candidates.
3. **`pipeline_classifier/`**: A high-performance pipeline based on [TransientX](https://github.com/ypmen/TransientX) and minimalistic CNN model
 for processing pulsar data in filterbank format and identifying single-pulse candidates.
