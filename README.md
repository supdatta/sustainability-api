# AI Sustainability Scoring API

This repository contains the complete end-to-end solution for building, training, and deploying a production-ready, cloud-hosted API that analyzes an image of an object and returns a sustainability score from 1-10.

![Project Workflow](https://i.imgur.com/8QzXJ2C.png)

## Table of Contents
1.  [Project Objective](#project-objective)
2.  [Technology Stack](#technology-stack)
3.  [Project Workflow](#project-workflow)
    * [Part 1: Data Processing & Model Training (Google Colab)](#part-1-data-processing--model-training-google-colab)
    * [Part 2: Local API Development (FastAPI)](#part-2-local-api-development-fastapi)
    * [Part 3: Cloud Deployment (Render)](#part-3-cloud-deployment-render)
4.  [API Documentation for Frontend](#api-documentation-for-frontend)

---

## Project Objective
The goal of this project is to create a web API that can accept an image of an object (like a can, bottle, or carton) and return a sustainability score. This involves processing a dataset, training a deep learning model, building an API server, and deploying it to the cloud for public access.

---

## Technology Stack
* **Data Processing & Modeling**: Python, TensorFlow, Keras, Google Colab, Pandas
* **API Framework**: FastAPI
* **Server**: Uvicorn
* **Cloud Platform**: Render (Free Tier)
* **Version Control**: Git & GitHub

---

## Project Workflow

### Part 1: Data Processing & Model Training (Google Colab)
This phase is handled entirely within a Google Colab notebook, which is divided into two main tasks.

#### 1.1 Dataset Processing
* **Input**: A `.zip` file containing 771 images with labels in their filenames (e.g., `BOTTLE-123.jpg`, `CAN-456.jpg`).
* **Process**:
    1.  The Colab notebook mounts the user's Google Drive.
    2.  It unzips the dataset.
    3.  A script iterates through each image, extracts the object type (e.g., "BOTTLE") from the filename.
    4.  A predefined rulebook maps the object type to a sustainability score:
        * Cans = 4
        * Bottles = 2
        * Cartons = 1
    5.  Images are automatically moved into a new, structured dataset folder in Google Drive with subdirectories named after their score (e.g., `1_low_sustainability`, `2_low_sustainability`, `4_medium_sustainability`).
* **Output**: A sorted dataset folder in Google Drive, ready for model training.

#### 1.2 Model Training
* **Process**:
    1.  The second part of the Colab notebook uses the sorted dataset created above.
    2.  It builds a model using **TensorFlow** and **Keras**.
    3.  **Transfer learning** is employed using the pre-trained **MobileNetV2** as the base model.
    4.  A new classification head is added and trained on our custom dataset.
* **Output**: A final, trained model saved as `sustainability_model_v1.keras` in the user's Google Drive.

---

### Part 2: Local API Development (FastAPI)
This phase involves creating a local server on a Windows PC to test the model's functionality before deployment.

#### Project Structure
/project-folder
|-- venv/
|-- main.py
|-- sustainability_model_v1.keras
|-- requirements.txt
|-- .gitignore
#### 2.1 Setup Instructions (Windows)
1.  **Clone the repository and navigate into the directory.**
2.  **Create a Python virtual environment:**
    ```bash
    python -m venv venv
    ```
3.  **Activate the virtual environment:**
    ```bash
    .\venv\Scripts\activate
    ```
4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Place the trained `sustainability_model_v1.keras` file in the root directory.**

#### 2.2 Running the Local Server
Execute the following command in your terminal:
```bash
uvicorn main:app --reload
Of course. Here is the complete README content formatted as a single Markdown code block, ready for you to copy and paste into a .md file.

Markdown

# AI Sustainability Scoring API

This repository contains the complete end-to-end solution for building, training, and deploying a production-ready, cloud-hosted API that analyzes an image of an object and returns a sustainability score from 1-10.

![Project Workflow](https://i.imgur.com/8QzXJ2C.png)

## Table of Contents
1.  [Project Objective](#project-objective)
2.  [Technology Stack](#technology-stack)
3.  [Project Workflow](#project-workflow)
    * [Part 1: Data Processing & Model Training (Google Colab)](#part-1-data-processing--model-training-google-colab)
    * [Part 2: Local API Development (FastAPI)](#part-2-local-api-development-fastapi)
    * [Part 3: Cloud Deployment (Render)](#part-3-cloud-deployment-render)
4.  [API Documentation for Frontend](#api-documentation-for-frontend)

---

## Project Objective
The goal of this project is to create a web API that can accept an image of an object (like a can, bottle, or carton) and return a sustainability score. This involves processing a dataset, training a deep learning model, building an API server, and deploying it to the cloud for public access.

---

## Technology Stack
* **Data Processing & Modeling**: Python, TensorFlow, Keras, Google Colab, Pandas
* **API Framework**: FastAPI
* **Server**: Uvicorn
* **Cloud Platform**: Render (Free Tier)
* **Version Control**: Git & GitHub

---

## Project Workflow

### Part 1: Data Processing & Model Training (Google Colab)
This phase is handled entirely within a Google Colab notebook, which is divided into two main tasks.

#### 1.1 Dataset Processing
* **Input**: A `.zip` file containing 771 images with labels in their filenames (e.g., `BOTTLE-123.jpg`, `CAN-456.jpg`).
* **Process**:
    1.  The Colab notebook mounts the user's Google Drive.
    2.  It unzips the dataset.
    3.  A script iterates through each image, extracts the object type (e.g., "BOTTLE") from the filename.
    4.  A predefined rulebook maps the object type to a sustainability score:
        * Cans = 4
        * Bottles = 2
        * Cartons = 1
    5.  Images are automatically moved into a new, structured dataset folder in Google Drive with subdirectories named after their score (e.g., `1_low_sustainability`, `2_low_sustainability`, `4_medium_sustainability`).
* **Output**: A sorted dataset folder in Google Drive, ready for model training.

#### 1.2 Model Training
* **Process**:
    1.  The second part of the Colab notebook uses the sorted dataset created above.
    2.  It builds a model using **TensorFlow** and **Keras**.
    3.  **Transfer learning** is employed using the pre-trained **MobileNetV2** as the base model.
    4.  A new classification head is added and trained on our custom dataset.
* **Output**: A final, trained model saved as `sustainability_model_v1.keras` in the user's Google Drive.

---

### Part 2: Local API Development (FastAPI)
This phase involves creating a local server on a Windows PC to test the model's functionality before deployment.

#### Project Structure
/project-folder
|-- venv/
|-- main.py
|-- sustainability_model_v1.keras
|-- requirements.txt
|-- .gitignore


#### 2.1 Setup Instructions (Windows)
1.  **Clone the repository and navigate into the directory.**
2.  **Create a Python virtual environment:**
    ```bash
    python -m venv venv
    ```
3.  **Activate the virtual environment:**
    ```bash
    .\venv\Scripts\activate
    ```
4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Place the trained `sustainability_model_v1.keras` file in the root directory.**

#### 2.2 Running the Local Server
Execute the following command in your terminal:
```bash
uvicorn main:app --reload
The API will now be running locally at http://127.0.0.1:8000.

2.3 main.py Code
The main.py script loads the Keras model and defines a /predict endpoint.


'''
art 3: Cloud Deployment (Render)
This section guides you through deploying the FastAPI application to a free, public URL using Render.

3.1 Preparation
Create requirements.txt: This file lists all the Python libraries your project needs.

Bash

pip freeze > requirements.txt
Important: Manually review this file and remove any Windows-specific packages (like pywin32) to avoid deployment errors.

Create .gitignore: Create a .gitignore file to exclude unnecessary files (like the venv folder and .pyc files) from your GitHub repository.

Host the Model File: The .keras model is too large for a standard GitHub repository. Upload sustainability_model_v1.keras to a free file hosting service that provides a direct public download link (e.g., Google Drive with public sharing, or GitHub LFS). Copy this public URL.

3.2 Version Control
Initialize a Git repository in your project folder.

Add all necessary files (main.py, requirements.txt, .gitignore).

Commit your changes and push the repository to GitHub.

3.3 Deploying on Render
Sign up for a Render account and connect your GitHub.

On the dashboard, click "New +" and select "Web Service".

Connect the GitHub repository you just created.

Configure the service with the following settings:

Name: Choose a unique name (e.g., sustainability-api).

Root Directory: Leave blank if your main.py is in the root.

Environment: Python 3

Region: Choose your preferred region.

Branch: main (or your default branch).

Build Command: pip install -r requirements.txt

Start Command: This command first downloads the hosted model and then starts the server. Replace YOUR_PUBLIC_MODEL_URL with the link you copied in step 3.1.

Bash

wget -O sustainability_model_v1.keras YOUR_PUBLIC_MODEL_URL && uvicorn main:app --host 0.0.0.0 --port $PORT
Click "Create Web Service". Render will now build and deploy your application.

API Documentation for Frontend
This section contains the final documentation for the frontend team to integrate the deployed API.

Live Endpoint URL: https://your-service-name.onrender.com/predict (replace your-service-name with the name you chose on Render).

HTTP Method: POST

Request Format: The request must be multipart/form-data and contain a file field named file.

Success Response (200 OK)
A successful request will return a JSON object with the following structure:

JSON

{
  "sustainability_score": 4,
  "predicted_class": "4_medium_sustainability",
  "confidence": 0.9875
}
Error Response
If the file is missing or in an invalid format, the API will return a standard FastAPI error response (e.g., 422 Unprocessable Entity).

JavaScript fetch Example
Here is a sample code snippet for making a request from a browser.

JavaScript

async function getSustainabilityScore(imageFile) {
  const apiUrl = '[https://your-service-name.onrender.com/predict](https://your-service-name.onrender.com/predict)';
  const formData = new FormData();
  formData.append('file', imageFile);

  try {
    const response = await fetch(apiUrl, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    console.log('API Response:', data);
    // Use the data in your application
    // e.g., displayScore(data.sustainability_score);
    return data;

  } catch (error) {
    console.error('Error fetching sustainability score:', error);
  }
}

// How to use it with an HTML file input:
// <input type="file" id="imageInput" accept="image/*">
const imageInput = document.getElementById('imageInput');
imageInput.addEventListener('change', (event) => {
  const file = event.target.files[0];
  if (file) {
    getSustainabilityScore(file);
  }
});
⭐ Important Note on Free Tier Usage
The free web service on Render will spin down due to inactivity. The first request after a period of inactivity will take longer to process (15-30 seconds) as the service starts up. It is crucial to implement a loading indicator or a spinner in the user interface to provide feedback to the user during this initial delay.
'''
