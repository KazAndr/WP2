import sys
import os
import json
import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from training_models import models_htable


# Function to load the configuration file
def load_config(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)


# Function to dynamically select the file based on resolution
def get_filename(config, resolution):
    files_by_res = config["files_by_resolution"]
    # Check if a specific file is mapped to the resolution
    if str(resolution) in files_by_res:
        filename = files_by_res[str(resolution)]
    else:
        # Use default format with the resolution substituted in the filename
        filename = files_by_res["default"].format(res=resolution)
    return os.path.join(config["path_to_files"], filename)


# Function to set up callbacks for model training
def get_callbacks(config, resolution, model_name):
    checkpoint_path = os.path.join(
        config["path_to_checkpoints"],
        f'ch_point_{model_name}_{resolution}',
        'prot-{epoch:03d}-{accuracy:.3f}-{val_accuracy:.3f}.h5'
    )

    callbacks = [
        ModelCheckpoint(
            checkpoint_path,
            mode='max',
            monitor='accuracy',
            save_freq='epoch',
            save_weights_only=False,
            save_best_only=True,
            verbose=1
        ),
        ModelCheckpoint(
            checkpoint_path,
            mode='max',
            monitor='val_accuracy',
            save_freq='epoch',
            save_weights_only=False,
            save_best_only=True,
            verbose=1
        ),
        EarlyStopping(monitor='accuracy', patience=config["patience"])
    ]
    return callbacks


# Function to encode labels into numeric format
def label_encoding(labels):
    map_dict = {
        'Artefact': 0,
        'Pulse': 1
    }
    return np.array([map_dict[i] for i in labels])


def main():
    # Load configuration file
    config_path = sys.argv[1]
    config = load_config(config_path)

    # Extract parameters from the configuration
    resolution = config["resolution"]
    model_name = config["model_name"]

    # Dynamically select the data file based on resolution
    filename = get_filename(config, resolution)
    labels_file = os.path.join(config["path_to_files"], config["labels"])

    # Load the data and labels
    data = np.load(filename)
    labels = np.load(labels_file)

    # Add an additional dimension to the data
    data = data[..., tf.newaxis]
    labels = label_encoding(labels)

    # Split the dataset into training and validation sets
    x_train, x_val, y_train, y_val = train_test_split(data, labels, test_size=0.2, random_state=42)

    # Initialize the model
    model = models_htable[model_name](resolution)
    callbacks = get_callbacks(config, resolution, model_name)
    opt = Adam(learning_rate=config["learning_rate"])

    # Compile the model
    model.compile(optimizer=opt,
                  loss=SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    # Train the model
    history = model.fit(
        x_train,
        y_train,
        epochs=config["num_epochs"],
        validation_data=(x_val, y_val),
        callbacks=callbacks
    )

    # Plot training and validation loss and accuracy
    plt.clf()
    plt.figure(figsize=(12, 4))

    # Loss plot
    plt.subplot(1, 2, 1)
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title(f'Model Loss: {resolution}x{resolution}')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.grid(True, ls='--')
    plt.legend(['Train', 'Validation'], loc='upper right')

    # Accuracy plot
    plt.subplot(1, 2, 2)
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title(f'Model Accuracy: {resolution}x{resolution}')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.grid(True, ls='--')
    plt.legend(['Train', 'Validation'], loc='lower right')

    # Add a common title
    plt.suptitle(f'Model {model_name} performance for {resolution}x{resolution} resolution', fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(
        os.path.join(config["path_to_images"], f'accuracy_across_epochs_for_{model_name}_{resolution}x{resolution}.jpg'),
        format='jpg',
        dpi=300
    )

    # Evaluate the model on the validation set
    test_loss, test_acc = model.evaluate(x_val, y_val, verbose=2)
    print(f'Test Accuracy: {test_acc}')


if __name__ == "__main__":
    main()
