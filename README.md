# Smart Fruit Analyzer - B21-CAP0354 (ML - CC)

## Team

Adam Ramadhan - A1511725  
Muharroman Attoriq Zayzda - A0080846  
Juandito Batara Kuncoro - M0080845  

## Capstone Project Introduction

In this age of Industry 4.0, industries are beginning to implement digital integration to boost their production efficiency. According to Anton Setiyawan, Director of Digital Economy Protection of Badan Siber dan Sandi Negara (BSSN) of Indonesia, there will be more Internet of Things (IoT) ecosystem users than the number of smartphones users in Indonesia.

Currently, some of the fruit and vegetable industry in Indonesia are still lacking digital integration and automation for quality checks. By developing a Machine Learning model for fruit / vegetable quality classification in a mobile dashboard, we hope that this will be the first step for the development of IoT implementation in the fruit and vegetable industry, especially in Indonesia.  

This app is able to identify a number of fruits and determine its quality with a Machine Learning model. And then it will insert the data into a database, which will save all the fruit info which is saved into it. Currently the classifications are limited to:

- Apple,
- Banana,
- Lemon,
- Orange, and
- Uncategorized

And the app will also tell us whether the fruit is fresh or rotten. The similarity percentage we got from the machine learning model will also be identified.

This app works by getting pictures from the user’s gallery, and then sending those pictures to the machine learning model deployed on Virtual Machine Instance with Cloud Computing, where the app will fetch the result of the classification.

## Repository

- [Android](https://github.com/adamramadhn/B21-CAP0354)  
- [ML - CC](https://github.com/JurgenStr/B21-CAP0354-ML-CC)  

## Steps

- Image Augmentation
  - Mount to Drive, and unzip raw dataset
  - Make sure that all categories are listed as a directory in the dataset folder
  - Create ImageDataGenerator with augmentation parameters
  - Apply *flow_from_directory* to each of the dataset categories, and save as PNG
  - Zip the augmented images, and download  

- Model Building
  - Mount your Google Drive, download dataset from Kaggle (requires Kaggle API), and unzip additional datasets
  - Make sure that all categories are listed as a directory in the dataset folder
  - Shuffle and split train data into train and validation
  - Create ImageDataGenerator for train, validation and test data
  - Build the model architecture, and set callbacks
  - Fit the model, and evaluate it
  - Visualize the result, and convert model into SavedModel and TFLite format  

- Model Deployment
  - Set up a Compute Engine VM and a Cloud Storage Bucket
  - Upload SavedModel to the Bucket
  - Open VM SSH, and clone a repository containing Flask scripts
  - Install virtual environment and necessary libraries
  - Download SavedModel from Cloud Storage Bucket
  - Set up NginX and Gunicorn to set up web server
