# main.py
# This script creates a local web server to host your trained sustainability model.

import tensorflow as tf
import numpy as np
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import io
from PIL import Image

# --- 1. Initialize the FastAPI App ---
# This creates the main application instance.
app = FastAPI(title="Sustainability Scoring API", version="1.0")

# Add CORS middleware to allow requests from any origin (useful for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 2. Load Your Trained Model ---
MODEL_PATH = 'sustainability_model_v1.keras'
model = None
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print(f"--- ✅ Model loaded successfully from {MODEL_PATH} ---")
except Exception as e:
    print(f"--- ❌ ERROR: Model could not be loaded. Error: {e} ---")
    model = None

# --- 3. Define Class Names ---
# IMPORTANT: This list MUST match the alphabetical order printed by the training script.
CLASS_NAMES = ['10_high_sustainability', '1_low_sustainability', '5_medium_sustainability']

def preprocess_image(image: Image.Image) -> np.ndarray:
    """Prepares an image for the model."""
    image = image.resize((224, 224)).convert('RGB')
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    return np.expand_dims(image_array, axis=0) # Add batch dimension

# --- 4. Create the Prediction Endpoint ---
# This defines the API endpoint that will receive image uploads.
@app.post("/predict")
async def predict_sustainability(file: UploadFile = File(...)):
    """
    Receives an image, runs prediction, and returns the score.
    """
    if model is None:
        raise HTTPException(status_code=500, detail="Model is not loaded or has failed.")

    # Read the image file from the request
    contents = await file.read()
    
    try:
        image = Image.open(io.BytesIO(contents))
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image file.")

    processed_image = preprocess_image(image)
    
    # Run the prediction
    predictions = model.predict(processed_image)
    
    # Process the result
    predicted_class_index = np.argmax(predictions[0])
    predicted_class_name = CLASS_NAMES[predicted_class_index]
    confidence = float(np.max(predictions[0]))
    
    # Extract the score from the class name (e.g., '5' from '5_medium_sustainability')
    score = int(predicted_class_name.split('_')[0])
    
    return {
        "predicted_class": predicted_class_name,
        "sustainability_score": score,
        "confidence": round(confidence, 4)
    }

@app.get("/")
def read_root():
    return {"message": "Welcome to the Local Sustainability Scoring API. Go to /docs to test."}
