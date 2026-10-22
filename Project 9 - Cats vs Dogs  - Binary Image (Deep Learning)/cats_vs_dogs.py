# Task 1 - Load the Image Dataset from Folders
# Step 1: Import Required Libraries
import keras
from keras.models import Sequential
from keras.layers import Input, Rescaling, Conv2D, MaxPooling2D, Flatten, Dense

# Step 2: Load Training Images
training_dataset = keras.utils.image_dataset_from_directory(
    "dataset/training_set",
    image_size=(64, 64),
    batch_size=32
)

# Step 3: Load Testing Images
testing_dataset = keras.utils.image_dataset_from_directory(
    "dataset/test_set",
    image_size=(64, 64),
    batch_size=32
)

# Task 2 - Build the Convolutional Neural Network (CNN)
# Step 1: Assemble CNN Layers
model = Sequential([
    Input(shape=(64, 64, 3)),
    Rescaling(1.0 / 255.0),
    Conv2D(32, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation="relu"),
    Dense(1, activation="sigmoid")
])

# Task 3 - Compile the Model
# Step 1: Compile Model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Task 4 - Train the Model
# Step 1: Fit the Model
model.fit(training_dataset, validation_data=testing_dataset, epochs=3)

# Task 5 - Evaluate Model Accuracy
# Step 1: Evaluate on Test Images
loss, accuracy = model.evaluate(testing_dataset)
print(f"Test Accuracy: {accuracy * 100:.2f}%")
