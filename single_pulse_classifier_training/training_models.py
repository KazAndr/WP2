from tensorflow.keras import layers, models

def model_DM_time_binary_classificator_241002_1(resol):
    model = models.Sequential()

    if resol == 256:
        model.add(layers.Conv2D(16, (5, 5), activation='relu', input_shape=(resol, resol, 1)))
        model.add(layers.Flatten())
        model.add(layers.Dense(256, activation='relu'))
    elif resol == 128:
        model.add(layers.Conv2D(8, (5, 5), activation='relu', input_shape=(resol, resol, 1)))
        model.add(layers.Flatten())
        model.add(layers.Dense(128, activation='relu'))
    elif resol == 64:
        model.add(layers.Conv2D(8, (5, 5), activation='relu', input_shape=(resol, resol, 1)))
        model.add(layers.Flatten())
        model.add(layers.Dense(256, activation='relu'))
    elif resol == 32:
        model.add(layers.Conv2D(16, (5, 5), activation='relu', input_shape=(resol, resol, 1)))
        model.add(layers.Flatten())
        model.add(layers.Dense(256, activation='relu'))

    model.add(layers.Dense(2, activation='softmax'))
    return model


def model_DM_time_binary_classificator_241002_2(resol):
    model = models.Sequential()

    if resol == 256:
        model.add(layers.Conv2D(16, (5, 5), activation='relu', input_shape=(resol, resol, 1)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(16, (5, 5), activation='relu'))
        model.add(layers.Flatten())
        model.add(layers.Dense(512, activation='relu'))
    elif resol == 128:
        model.add(layers.Conv2D(16, (5, 5), activation='relu', input_shape=(resol, resol, 1)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(16, (5, 5), activation='relu'))
        model.add(layers.Flatten())
        model.add(layers.Dense(128, activation='relu'))
    elif resol == 64:
        model.add(layers.Conv2D(16, (5, 5), activation='relu', input_shape=(resol, resol, 1)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(16, (5, 5), activation='relu'))
        model.add(layers.Flatten())
        model.add(layers.Dense(128, activation='relu'))
    elif resol == 32:
        model.add(layers.Conv2D(16, (5, 5), activation='relu', input_shape=(resol, resol, 1)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(16, (5, 5), activation='relu'))
        model.add(layers.Flatten())
        model.add(layers.Dense(512, activation='relu'))

    model.add(layers.Dense(2, activation='softmax'))
    return model


def model_DM_time_binary_classificator_241002_3(resol):
    model = models.Sequential()

    if resol == 256:
        model.add(layers.Conv2D(8, (5, 5), activation='relu', input_shape=(resol, resol, 1)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(8, (5, 5), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(12, (5, 5), activation='relu'))
        model.add(layers.Flatten())
        model.add(layers.Dense(256, activation='relu'))
    elif resol == 128:
        model.add(layers.Conv2D(8, (5, 5), activation='relu', input_shape=(resol, resol, 1)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(12, (5, 5), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(12, (5, 5), activation='relu'))
        model.add(layers.Flatten())
        model.add(layers.Dense(256, activation='relu'))
    elif resol == 64:
        model.add(layers.Conv2D(8, (5, 5), activation='relu', input_shape=(resol, resol, 1)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(12, (5, 5), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(8, (5, 5), activation='relu'))
        model.add(layers.Flatten())
        model.add(layers.Dense(512, activation='relu'))
    elif resol == 32:
        model.add(layers.Conv2D(8, (5, 5), activation='relu', input_shape=(resol, resol, 1)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(12, (5, 5), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(12, (5, 5), activation='relu'))
        model.add(layers.Flatten())
        model.add(layers.Dense(512, activation='relu'))

    model.add(layers.Dense(2, activation='softmax'))
    return model

models_htable = {
    'DM_time_binary_classificator_241002_1': model_DM_time_binary_classificator_241002_1,
    'DM_time_binary_classificator_241002_2': model_DM_time_binary_classificator_241002_2,
    'DM_time_binary_classificator_241002_3': model_DM_time_binary_classificator_241002_3
}

