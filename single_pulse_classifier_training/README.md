# Model Training Pipeline

This repository contains the training pipeline for binary classification of single-pulse candidates in DM-time plane data. The pipeline is designed to preprocess data, train convolutional neural networks (CNNs), and save the results, including model checkpoints and performance plots.

## Directory Structure

- **`data/`**: Contains the training datasets and label files.
- **`checkpoints/`**: Stores the model checkpoints saved during training.
- **`images/`**: Contains plots of training and validation performance metrics.

## Requirements

The training pipeline requires the following dependencies:

- **Python** (≥3.6)
- **TensorFlow/Keras**
- **Matplotlib**
- **NumPy**
- **scikit-learn**

Install these dependencies using `pip`:
```bash
pip install tensorflow matplotlib numpy scikit-learn
```

## Configuration File

The training process is controlled using a JSON configuration file. Below is an example:

```json
{
    "path_to_files": "data/",
    "path_to_checkpoints": "checkpoints/",
    "path_to_images": "images/",
    "resolution": 256,
    "model_name": "DM_time_binary_classificator_241002_3",
    "files_by_resolution": {
        "256": "B0531+21_59000_48386_DM_time_dataset_realbased_training.npy",
        "default": "B0531+21_59000_48386_DM_time_dataset_realbased_training_{res}x{res}.npy"
    },
    "labels": "B0531+21_59000_48386_DM_time_dataset_realbased_labels_training.npy",
    "learning_rate": 0.0001,
    "num_epochs": 100,
    "patience": 5
}
```

### Key Parameters
- **`path_to_files`**: Path to the directory containing the training data and labels.
- **`path_to_checkpoints`**: Path where model checkpoints will be saved.
- **`path_to_images`**: Path to save training and validation performance plots.
- **`resolution`**: Resolution of the DM-time data (e.g., 256x256).
- **`model_name`**: Name of the model architecture to use.
- **`files_by_resolution`**: Mapping of resolution to dataset filenames.
- **`labels`**: Filename of the label file.
- **`learning_rate`**: Learning rate for model optimization.
- **`num_epochs`**: Maximum number of training epochs.
- **`patience`**: Number of epochs without improvement to trigger early stopping.

## Models

The training pipeline supports multiple CNN architectures, implemented in `training_models.py`. Each model is designed to handle different DM-time data resolutions.

### Supported Models
- **`DM_time_binary_classificator_241002_1`**: A simple CNN with one convolutional layer.
- **`DM_time_binary_classificator_241002_2`**: A deeper CNN with max pooling.
- **`DM_time_binary_classificator_241002_3`**: A more complex CNN with multiple convolutional and pooling layers.

## Workflow

1. **Load Configuration**: The pipeline loads training parameters and paths from the configuration file.

2. **Prepare Data**:
   - Dynamically selects the dataset file based on resolution.
   - Loads the DM-time data and corresponding labels.
   - Splits the data into training and validation sets (80% training, 20% validation).

3. **Train the Model**:
   - Initializes the selected model architecture.
   - Compiles the model with the Adam optimizer and sparse categorical cross-entropy loss.
   - Trains the model with early stopping and checkpoint saving.

4. **Save Results**:
   - Saves the best-performing model as a checkpoint.
   - Plots training and validation loss/accuracy over epochs and saves the plot in the `images/` directory.

## Example Usage

1. **Prepare the Environment**:
   Ensure the data, configuration file, and required dependencies are set up.

2. **Run the Training Script**:
   ```bash
   python training_pipeline.py config.json
   ```

3. **Output**:
   - Checkpoints saved in `checkpoints/`.
   - Training and validation performance plots saved in `images/`.

## Outputs

- **Model Checkpoints**: Saved with filenames indicating epoch, training accuracy, and validation accuracy.
- **Performance Plots**: Visualizations of training/validation loss and accuracy across epochs.

## Directory Structure After Training

```
project/
├── data/
│   ├── B0531+21_59000_48386_DM_time_dataset_realbased_training.npy
│   ├── B0531+21_59000_48386_DM_time_dataset_realbased_labels_training.npy
├── checkpoints/
│   ├── ch_point_DM_time_binary_classificator_241002_3_256/
│   │   ├── prot-001-0.900-0.850.h5
├── images/
│   ├── accuracy_across_epochs_for_DM_time_binary_classificator_241002_3_256x256.jpg
├── training_pipeline.py
├── training_models.py
├── config.json
```

## Future Enhancements

- Support for additional architectures.
- Integration with hyperparameter tuning libraries for automated optimization.