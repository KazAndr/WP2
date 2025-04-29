import os
import argparse
import numpy as np
import tensorflow as tf
from tqdm import trange
from tensorflow.keras.models import load_model
from psrdada import Reader
from utils import load_config, normalize_image_to_255

# Set up argument parser to accept configuration file path
parser = argparse.ArgumentParser(description="Inference pipeline")
parser.add_argument('-c', '--config', type=str, required=True, 
                   help="Path to configuration file")
args = parser.parse_args()

# Load configuration parameters from specified file
config = load_config(args.config)

# Load pre-trained model from specified path
model = load_model(f'{config["path_to_models"]}{config["name_of_the_model"]}')

# Initialize DADA reader with hexadecimal key from config
reader = Reader(int(str(config["key_output"]), 16))

# Generate output filename by removing extension from filterbank name
output_filename = f"predictions_{config['name_of_the_filterbank'].split('.')[0]}.npy"

# Create memory-mapped array for efficient disk-backed storage
# This allows incremental saving without loading full array in memory
predictions_array = np.lib.format.open_memmap(
    output_filename,       # Output file path
    dtype=np.int32,          # Data type (can handle variable-length sequences)
    mode='w+',             # Read/write mode, creates new file
    shape=(config["n_spectra"],)  # Pre-allocate array size
)

# Process each spectrum in the input data
for i in trange(config["n_spectra"]):
    # Get next data page from DADA buffer
    page = reader.getNextPage()
    
    # Convert raw bytes to float32 numpy array
    data = np.frombuffer(page, dtype=np.float32)
    
    # Calculate dimensions for reshaping
    total_size = data.size
    num_dms = 256          # Fixed number of DM trials
    num_dumps = total_size // num_dms
    
    # Reshape 1D array into 2D (DM trials × time samples)
    data = data.reshape((num_dms, num_dumps))
    
    # Normalize and flip the image vertically
    normalized_image = normalize_image_to_255(data[::-1])
    
    # Add batch and channel dimensions for model input
    reshaped_data = normalized_image.reshape(1, *normalized_image.shape, 1)
    
    # Run model inference (disable training-specific ops)
    prediction = model(reshaped_data, training=False)
    
    # Get class with highest probability
    max_index = tf.argmax(prediction, axis=-1)
    
    # Store prediction in memory-mapped array
    predictions_array[i] = int(max_index.numpy()[0])
    
    # Mark buffer page as processed
    reader.markCleared()
    
    # Periodically flush writes to disk (every 100 spectra)
    if (i + 1) % 100 == 0:
        predictions_array.flush()

# Final flush to ensure all data is written
predictions_array.flush()

# Clean up DADA reader connection
reader.disconnect()
