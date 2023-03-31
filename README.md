How to Use the MoI Project
Installation
Clone the project from the GitHub repository: https://github.com/your-username/your-project-name

Install the necessary packages by running the following command in the project root directory:

Copy code
pip install -r requirements.txt
Usage
Place any images you want to classify into the data/test_images/ folder.

In the root directory, run the following command to classify the images:

css
Copy code
python main.py predict --image_path=<path-to-image>
For example, if you want to classify an image called test_image.jpg in the data/test_images/ folder, you would run:

css
Copy code
python main.py predict --image_path=data/test_images/test_image.jpg
The predicted class and the confidence score will be printed to the console.

To train the model, run the following command:

css
Copy code
python main.py train
The model will be trained on the data in the data/train_data.npy and data/train_labels.npy files. The training progress will be printed to the console, and the resulting model will be saved as model/MoI_model.h5 and the training history will be saved as model/history.pickle.

To test the accuracy of the model, run the following command:

bash
Copy code
python main.py test
The model will be tested on the data in the data/test_data.npy and data/test_labels.npy files, and the accuracy score will be printed to the console.

To generate a confusion matrix for the model, run the following command:

css
Copy code
python main.py confusion_matrix
The confusion matrix will be generated based on the predictions made by the model on the data in the data/test_data.npy and data/test_labels.npy files, and will be saved as model/confusion_matrix.png.

Conclusion
That's it! These instructions should help you get started with using the MoI project. Feel free to modify the code and experiment with different parameters to improve the accuracy of the model.