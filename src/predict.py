import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from data_utils import load_data

# Load model
model = keras.models.load_model('model/mnist_cnn.h5')

# Load data
(X_train, y_train), (X_test, y_test) = load_data('mnist')

# Make predictions on test data
predictions = model.predict(X_test)

# Print example predictions
for i in range(10):
    print('Example', i+1, 'prediction:', np.argmax(predictions[i]))
    print('True label:', np.argmax(y_test[i]))
