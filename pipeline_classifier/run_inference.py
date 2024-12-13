import os
import argparse

import numpy as np
import tensorflow as tf

from tqdm import trange
from tensorflow.keras.models import load_model
from psrdada import Reader

from utils import load_config, normalize_image_to_255

parser = argparse.ArgumentParser(description="Inference pipeline")
parser.add_argument('-c', '--config', type=str, required=True, help="Config file")
args = parser.parse_args()

config = load_config(args.config)

model = load_model(f'{config["path_to_models"]}{config["name_of_the_model"]}')

reader = Reader(int(str(config["key_output"]), 16))

predictions_array = np.empty([config["n_spectra"]], dtype=object) 

for i in trange(config["n_spectra"]):
    page = reader.getNextPage()
    data = np.frombuffer(page, dtype=np.float32)
    total_size = data.size
    num_dms = 256
    block_size = 256
    num_dumps = total_size // num_dms
    data = data.reshape((num_dms, num_dumps))
    normalized_image = normalize_image_to_255(data[::-1])
    reshaped_data = data.reshape(1, *normalized_image.shape, 1)
    prediction = model(reshaped_data, training=False)
    max_index = tf.argmax(prediction, axis=-1)
    predictions_array[i] =  max_index.numpy()[0]
    reader.markCleared()

reader.disconnect()
np.save("predictions.npy", predictions_array)
