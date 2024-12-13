# Single Pulse Detection and Classification

This repository contains two key components for detecting and classifying single pulses in radio astronomy data:

1. **`pipeline_classifier/`**: A high-performance pipeline for processing pulsar data and identifying single-pulse candidates.
2. **`single_pulse_classifier_training/`**: Tools and scripts for training machine learning models to classify single-pulse candidates.

## Directory Overview

### `pipeline_classifier/`

This directory contains the complete pipeline for single-pulse detection. It includes:

- **Data Preprocessing**: Handles raw radio data in filterbank format.
- **Candidate Detection**: Uses **TransientX** to find potential single pulses.
- **Classification**: Applies machine learning models to identify real pulses vs. artifacts.

See the [README in `pipeline_classifier/`](pipeline_classifier/README.md) for details on setup and usage.

### `single_pulse_classifier_training/`

This directory contains the code and resources for training classification models. It includes:

- **Data Preparation**: Converts raw filterbank data and TransientX outputs into DM-time images.
- **Model Training**: Trains convolutional neural networks (CNNs) for binary classification of single pulses.
- **Evaluation Tools**: Validates model performance with visualizations and accuracy metrics.

See the [README in `single_pulse_classifier_training/`](single_pulse_classifier_training/README.md) for details on model training.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url.git
   cd single_pulse_detection
   ```

2. Set up the environment:
   - Install dependencies listed in the respective READMEs for each directory.
   - Ensure that all required data files are in place.

3. Follow the instructions in each directory's README to run the pipeline or train models.

## Contributions

Contributions to improve the pipeline or classification models are welcome. Please submit issues or pull requests in the appropriate directory.

## License

This project is licensed under the [MIT License](LICENSE).