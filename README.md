# COVID-19-Pneumonia-Detection-Web-Based-Managent-System

Till this day, there is still no treatment or cure for COVID-19. It still remains as the main threat to our human health. The global communities are still living under this severe pandemic. Reports are always showing the number of cases and deaths daily. Nobody could know when this nightmare would eventually end. On the other side, pneumonia has always been the main cause of death among children who are under the age of five. Many have lost their lost ones due to all these diseases.

The main aim of this project is to implement a CNN model which has the ability to diagnose COVID-19 & pneumonia from chest X-ray images in helping doctors in making much better decisions easily and at the same time provide high accuracy and speed. Moreover, a web-based system will be developed integrating with the CNN model to store and display the information and the result of the patients.

## Objectives:
1. To develop a COVID-19 & pneumonia detection by locating the information of the lesion on the X-rays
2. To find the best parameter for model tuning to detect COVID-19 & pneumonia
3. To design a user-friendly app web-based system to store and view the information and the result of patients.

## Datasets:
1. RSNA Pneumonia Detection Challenge
2. COVID-19 Chest X-ray Dataset
3. Figure1 COVID-19 Chest X-ray Dataset
4. Actualmed COVID-19 Chest X-ray Dataset Initiative
5. COVID-19 Radiography Database

## Data Preprocessing Steps:
1. Training & Validation Split </br>
a) COVID-19 Dataset: 1st to last 100 images for training & last 100 for validation </br>
b) COVID-19 Dataset: 1st to last 100 images for training & last 100 for validation 

2. Resizing: </br>
a) Convert the image to 155 x 155 pixel size 

3. Normalization </br>
    a) Input data divided by 255 </br>
    
4. Data Augmentation

## CNN Model:
| Parameter     | Value         |
| ------------- | ------------- |
| Number of hidden layer | 4 |
| Number of neurons for the input layer| 2048 |
| Number of neurons for the first hidden layer| 1024 |
| Number of neurons for the second hidden layer| 512 |
| Number of neurons for the third hidden layer| 64 |
| Number of neurons for the fourth hidden layer| 32 |
| Number of neurons for the output layer| 3 |
| Activation Function (Input & Hidden layer) | ReLU |
| Activation Function (Output) | softmax |
| Optimizer | SGD |
| Batch Size | 32 |
| Epochs | 200 |





