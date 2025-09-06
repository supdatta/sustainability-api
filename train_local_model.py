# train_local_model.py
# This script trains your sustainability model on your local PC.

import tensorflow as tf
import os

# --- Configuration ---
# The script expects your dataset to be in a folder named 'dataset'
DATASET_DIR = 'dataset'

# The final, trained model will be saved with this filename.
MODEL_SAVE_PATH = 'sustainability_model_v1.keras'

# --- Model Training Parameters ---
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 15

def train():
    """
    Main function to load data, build, train, and save the model.
    """
    print("--- Starting Local Model Training Process ---")

    # --- 1. Load the Local Dataset ---
    print(f"Loading and splitting the dataset from: '{DATASET_DIR}' folder")

    # This Keras utility is the key. It reads the folder structure and creates the dataset.
    # It splits the data into 80% for training and 20% for validation.
    train_dataset, validation_dataset = tf.keras.utils.image_dataset_from_directory(
        DATASET_DIR,
        validation_split=0.2,
        subset="both",
        seed=123,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE
    )

    class_names = train_dataset.class_names
    print(f" Dataset loaded. Found classes: {class_names}")
    print(f" (Note: TensorFlow sorts them alphabetically. Your API will need to know this order.)")

    # Optimize the data pipeline for performance
    AUTOTUNE = tf.data.AUTOTUNE
    train_dataset = train_dataset.cache().prefetch(buffer_size=AUTOTUNE)
    validation_dataset = validation_dataset.cache().prefetch(buffer_size=AUTOTUNE)

    # --- 2. Build the Model using Transfer Learning ---
    print("\nBuilding model using MobileNetV2 as a base...")

    # Load a powerful pre-trained model, but without its final layer.
    base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SIZE + (3,),
                                                   include_top=False,
                                                   weights='imagenet')
    # Freeze the base model layers. We will only train our new, small final layer.
    base_model.trainable = False

    # Create the full model architecture
    inputs = tf.keras.Input(shape=IMG_SIZE + (3,))
    x = tf.keras.applications.mobilenet_v2.preprocess_input(inputs) # Preprocessing layer
    x = base_model(x, training=False)
    x = tf.keras.layers.GlobalAveragePooling2D()(x) # Flattens the output
    x = tf.keras.layers.Dropout(0.2)(x)             # Regularization to prevent overfitting
    outputs = tf.keras.layers.Dense(len(class_names), activation='softmax')(x) # Our prediction layer

    model = tf.keras.Model(inputs, outputs)

    # --- 3. Compile the Model ---
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(),
                  metrics=['accuracy'])

    print(" Model built and compiled successfully.")
    model.summary()

    # --- 4. Train the Model ---
    print(f"\n--- Starting training for {EPOCHS} epochs ---")
    model.fit(train_dataset,
              epochs=EPOCHS,
              validation_data=validation_dataset)

    print("\n---  Training Complete! ---")

    # --- 5. Save the Final Model ---
    print(f"Saving the trained model to: {MODEL_SAVE_PATH}")
    model.save(MODEL_SAVE_PATH)
    print(" Model saved successfully!")
    print("\n Next Steps: You can now build the local API using the saved model file.")

if __name__ == '__main__':
    train()
