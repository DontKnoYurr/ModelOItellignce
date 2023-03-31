import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.utils import to_categorical
import os

def load_data(dataset_name):
    # Load data from file
    if dataset_name == 'mnist':
        (X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
    elif dataset_name == 'cifar10':
        (X_train, y_train), (X_test, y_test) = keras.datasets.cifar10.load_data()
    else:
        raise ValueError('Invalid dataset name')

    # Normalize pixel values to be between 0 and 1
    X_train = X_train.astype('float32') / 255.0
    X_test = X_test.astype('float32') / 255.0

    # Convert class labels to one-hot encoded vectors
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    return (X_train, y_train), (X_test, y_test)
