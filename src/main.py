from src.data_utils import load_data
from src.model_utils import build_model
from src.train_utils import train_model
from src.predict_utils import predict

# Load the data
train_data, test_data = load_data()

# Build the model
model = build_model()

# Train the model
trained_model = train_model(model, train_data)

# Evaluate the model on test data
test_loss, test_acc = trained_model.evaluate(test_data)

# Make predictions on new data
predictions = predict(trained_model, test_data)

# Print the test accuracy and predicted labels
print("Test accuracy:", test_acc)
print("Predictions:", predictions)
