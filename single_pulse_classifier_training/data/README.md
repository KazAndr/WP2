# DM-Time Datasets

The files and singularity images required for the work have been uploaded to the [Edmond](https://edmond.mpg.de/)
 system and can be found by the [identifier](https://doi.org/10.17617/3.HQYC8O).

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

2. **Labeling**:
   - Pulse events were labeled as **`Pulse`**.
   - Broadband RFI and other events were labeled as **`Artefact`**.

3. **Downsampling**:
   - The original 256x256 images were downsampled to resolutions of:
     - **128x128**
     - **64x64**
     - **32x32**

4. **Dataset Shuffling**:
   - The images and labels were shuffled to create randomized datasets for training and validation.
