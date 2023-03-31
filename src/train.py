import os
import tensorflow as tf
from tensorflow import keras
from model.cnn import CNN
from data_utils import load_data

# Set hyperparameters
batch_size = 64
epochs = 10
learning_rate = 0.001

# Load data
(X_train, y_train), (X_test, y_test) = load_data('mnist')

# Create CNN model
model = CNN.build(width=28, height=28, depth=1, classes=10)

# Compile model
opt = keras.optimizers.Adam(lr=learning_rate)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=batch_size, epochs=epochs)

# Evaluate model
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print('Test accuracy:', test_acc)

# Save model
if not os.path.exists('model'):
    os.makedirs('model')
model.save('model/mnist_cnn.h5')
