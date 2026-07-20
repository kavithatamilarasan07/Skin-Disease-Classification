# Skin Disease Classification using Deep Learning

A deep learning based web application that classifies skin diseases from uploaded skin images using an EfficientNetB0 model and provides prediction results through a Flask web interface.

## Project Overview

This project uses Convolutional Neural Network (CNN) techniques with transfer learning to identify different types of skin lesions. The trained model can classify skin images into 7 different categories.

## Features

- Upload skin image through web interface
- AI-based skin disease prediction
- Displays predicted disease name
- Shows prediction confidence score
- User-friendly Flask web application

## Technologies Used

### Deep Learning
- TensorFlow
- Keras
- EfficientNetB0
- Transfer Learning

### Backend
- Python
- Flask

### Image Processing
- OpenCV
- Pillow
- NumPy

### Data Analysis
- Pandas
- Scikit-learn
- Matplotlib

## Dataset

The model is trained using the HAM10000 Skin Lesion Dataset.

Classes:

- AKIEC - Actinic Keratosis
- BCC - Basal Cell Carcinoma
- BKL - Benign Keratosis
- DF - Dermatofibroma
- MEL - Melanoma
- NV - Melanocytic Nevus
- VASC - Vascular Lesions

## Project Structure


Skin-Disease-Classification
│
├── app
│ ├── app.py
│ ├── routes.py
│ └── templates
│
├── src
│ ├── train.py
│ ├── evaluate.py
│ ├── predict.py
│ ├── model.py
│ └── preprocessing.py
│
├── dataset
├── models
│ └── skin_disease_model.keras
│
├── requirements.txt
└── README.md


## Installation

Clone the repository:

```bash
git clone https://github.com/kavithatamilarasan07/Skin-Disease-Classification.git
