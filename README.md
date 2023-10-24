# Exotic Pet Detection App

## Introduction

The Exotic Pet detection App is a Streamlit application designed for predicting the type of an exotic pet based on an uploaded image. Whether you're an enthusiast or simply curious about your exotic pet's category, this app can provide you with the answer.

## Features

- **Pet Type Prediction**: Upload an image of your exotic pet, and the app will predict the most likely type from a list of 10 different categories.
- **User-Friendly**: The app's intuitive interface ensures that it is accessible and easy to use.

## Demo

You can experience a live demonstration of the app [here](https://exoticpetdetection.streamlit.app/).

## Installation

To run the Exotic Pet detection App locally, please follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/harichselvamc/Exotics_Pets_Detection/


2. Change the directory to the project folder:

   ```bash
    cd Exotics_Pets_Detection
   
3. Install the required dependencies using pip:

   ```bash
    pip install -r requirements.txt


4. Run the Streamlit app:

   ```bash
    streamlit run app.py

### The app will open in your web browser, allowing you to upload Pets images for detection.





# Folder Structure
### The model has been trained on a dataset organized in the following folder structure:

    
        ./exotic_pet
    │
    ├── Chameleon
    │   ├── 001.jpg
    │   ├── 002.jpg
    │   ...
    │
    ├── Crocodile_Alligator
    │   ├── 001.jpg
    │   ├── 002.jpg
    │   ...
    ...

        
  Each Pets has its own folder containing multiple images.


# Model Details
The Exotics Pets Detection App uses a pre-trained machine learning model based on the InceptionV3 architecture. The model has been fine-tuned on a dataset of 10 different Pets Types.

   
