# DM-Time Datasets


These datasets contain DM-time images derived from radio astronomy observations of the pulsar **B0531+21** (the Crab Pulsar). They are structured for use in machine learning tasks such as pulse detection and classification. The datasets are available for download at the following link: [Download DM-Time Datasets](https://keeper.mpdl.mpg.de/d/f61c63e113ca40a5a476/).

## Overview of the Data

The datasets consist of DM-time images, which are visual representations of dedispersed radio signals across a range of dispersion measures (DMs) and time. Each image corresponds to a segment of the observation where potential transient events were detected or suspected.

## Data Categories

1. **Pulse Events**: 
   - Events with DMs in the range of **56–58**, corresponding to the Crab Pulsar.
   - These are labeled as **`Pulse`**.
2. **Broadband RFI**:
   - Events with **DM = 0**, often caused by terrestrial radio frequency interference (RFI).
   - These are labeled as **`Artefact`**.
3. **Other Events**:
   - Events outside the range of 56–58 DM and not at DM = 0.
   - These are also labeled as **`Artefact`**.

## How the Data Was Created

The datasets were generated from raw filterbank data and candidate files produced by **TransientX**. The steps for creating the datasets are as follows:

1. **Input Data**:
   - **Filterbank File**: Raw radio observations in the `.fil` format.
   - **TransientX Candidate File**: List of candidate events detected by the TransientX software.
   - **DM-Time Data Files**: Dedispersed data for various DM values, stored in `.dat` files.

2. **Candidate Event Processing**:
   - Candidate events were categorized based on their DM values.
   - The positions of each candidate in the filterbank file were calculated using its Modified Julian Date (MJD).

3. **Image Generation**:
   - For each candidate, a **256x256** DM-time image was created.
   - The images were normalized to a scale of 0–255.

4. **Labeling**:
   - Pulse events were labeled as **`Pulse`**.
   - Broadband RFI and other events were labeled as **`Artefact`**.

5. **Downsampling**:
   - The original 256x256 images were downsampled to resolutions of:
     - **128x128**
     - **64x64**
     - **32x32**

6. **Dataset Shuffling**:
   - The images and labels were shuffled to create randomized datasets for training and validation.

## Dataset Files

The following files are generated:

1. **Main Dataset**:
   - **`*_DM_time_dataset_realbased.npy`**: Combined DM-time images.
   - **`*_DM_time_dataset_realbased_labels.npy`**: Labels corresponding to the images.

2. **Resolution-Specific Datasets**:
   - **`*_DM_time_dataset_realbased_128x128.npy`**
   - **`*_DM_time_dataset_realbased_64x64.npy`**
   - **`*_DM_time_dataset_realbased_32x32.npy`**

3. **Category-Specific Datasets**:
   - **Pulse-Only Dataset**: Contains only pulse events.
   - **Broadband RFI Dataset**: Contains only zero-DM events.

## Summary

The DM-time datasets provide a labeled collection of radio astronomy data, formatted for machine learning. They represent a mix of pulse events, broadband RFI, and other transient phenomena. The datasets are structured to support tasks like training binary classifiers and testing new algorithms in radio transient detection.