# MoI (ModelOIntelligence)

MoI is a basic AI built using TensorFlow and Keras that uses a convolutional neural network (CNN) to classify images. This project serves as a starting point for anyone interested in building their own CNN using TensorFlow and Keras.

## Getting Started

To get started with MoI, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Set up the folder structure as described in the project prompt.
4. Load your own data into the `data` folder, or use the sample data provided.
5. Train the model using the `train.py` script.
6. Evaluate the performance of the model using the `predict.py` script.

## Folder Structure

The MoI folder should contain the following subfolders:

- `data`: Contains the dataset for training and testing the model.
- `model`: Contains the trained model and related files.
- `src`: Contains the source code for the project.

## Loading Data

To load data into MoI, follow these steps:

1. Create a new script in the `src` folder.
2. Import the necessary libraries, including `numpy`, `PIL`, and `cv2`.
3. Define a function to load your data into a `numpy` array.
4. Preprocess your data by resizing and normalizing it.
5. Save the preprocessed data to a `.npy` file in the `data` folder.

## Training the Model

To train the model, follow these steps:

1. Run the `train.py` script located in the `src` folder.
2. Set the appropriate hyperparameters for your model, including the number of epochs and the learning rate.
3. Train the model using the `fit()` method of your model object.
4. Save the trained model to the `model` folder using the `.h5` file format.
5. Save the training history to a `history.pickle` file in the `model` folder.

## Evaluating the Model

To evaluate the performance of the model, follow these steps:

1. Run the `predict.py` script located in the `src` folder.
2. Load the saved model using the `load_model()` function from Keras.
3. Load your test data into a `numpy` array using the same preprocessing steps used during training.
4. Use the `evaluate()` method of your model object to evaluate the performance of the model on the test data.

## Conclusion

MoI is a basic AI that serves as a starting point for anyone interested in building their own CNN using TensorFlow and Keras. Follow the instructions provided in this README to get started with MoI and start building your own AI today!