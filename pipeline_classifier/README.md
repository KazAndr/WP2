# Single-pulse Recognition Pipeline

This repository contains a high-performance pipeline for transient recognition, designed to process pulsar data, run inference models, and handle data buffers efficiently. The pipeline leverages **TransientX** and TensorFlow-based machine learning models to classify single-pulse candidates in astronomical data, specifically in the DM-time plane format. At its current stage, the model is optimized for detecting individual pulses from the Crab Pulsar (B5031+21) within a dispersion measure (DM) range of 0 to 128, with a step size of 0.5.

## Directory Structure

- **`data/`**: Contains filterbank files for processing.
- **`models/`**: Holds trained TensorFlow models used for inference.
- **`singularity_images/`**: Includes Singularity image files for running various components of the pipeline in a containerized environment.

## Requirements

The pipeline requires the following dependencies:

- **Python** (≥3.6)
- **Singularity** for containerized execution.
- **TensorFlow** (for running ML models)
- **TransientX**: High-performance transient search software.  
  GitHub: [https://github.com/ypmen/TransientX](https://github.com/ypmen/TransientX)  

## Pipeline Overview

### Configuration Files
- **Pipeline Configuration (`config.json`)**: Specifies parameters like buffer size, model paths, and data keys.
- **TransientX Configuration (`dbdedispdb_config.json`)**: Defines parameters for transient search.

### Workflow

1. **Buffer Setup**:  
   Using `dada_db`, the pipeline initializes input and output buffers with specified sizes and keys.

2. **Data Processing**:
   - **`dada_fildb`**: Handles raw data from filterbank files.
   - **`dada_dbdedispdb`**: Performs dedispersion and creates DM-time planes using parameters from the TransientX configuration file (`dbdedispdb_config.json`).

3. **Inference**:
   Runs a TensorFlow model (`run_inference.py`) to classify the generated spectrograms. Predictions are stored in a `.npy` file for further analysis.

4. **Cleanup**:  
   Stops all running processes and deallocates buffers.

### Key Components
- **`main_pipeline.py`**: Orchestrates the entire workflow, from buffer creation to inference.
- **`run_inference.py`**: Loads the TensorFlow model and processes DM-time images for classification.
- **`utils.py`**: Provides helper functions for command execution, buffer management, and data normalization.

## Example Usage

1. **Prepare the Environment**:
   Ensure that all dependencies and Singularity images are properly installed.

2. **Run the Pipeline**:
   ```bash
   python main_pipeline.py -c config.json
   ```

3. **Output**:
   - Predictions are saved as `predictions.npy`.
   - Logs for processing and errors are printed to the console.

## Citation

- **TransientX**:  
  [https://arxiv.org/abs/2401.13834](https://arxiv.org/abs/2401.13834)

## Acknowledgments

Special thanks to the authors of **TransientX** and contributors to the pulsar research community. Their work on tools like TransientX and its dependencies made this pipeline possible.
