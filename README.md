# COVID-19-Pneumonia-Detection-Web-Based-Managent-System

Till this day, there is still no treatment or cure for COVID-19. It still remains as the main threat to our human health. The global communities are still living under this severe pandemic. Reports are always showing the number of cases and deaths daily. Nobody could know when this nightmare would eventually end. On the other side, pneumonia has always been the main cause of death among children who are under the age of five. Many have lost their lost ones due to all these diseases.

The main aim of this project is to implement a CNN model which has the ability to diagnose COVID-19 & pneumonia from chest X-ray images in helping doctors in making much better decisions easily and at the same time provide high accuracy and speed. Moreover, a web-based system will be developed integrating with the CNN model to store and display the information and the result of the patients.

## Objectives:
1. To develop a COVID-19 & pneumonia detection by locating the information of the lesion on the X-rays
2. To find the best parameter for model tuning to detect COVID-19 & pneumonia
3. To design a user-friendly app web-based system to store and view the information and the result of patients.

## Datasets:
1. RSNA Pneumonia Detection Challenge: https://www.kaggle.com/c/rsna-pneumonia-detection-challenge
2. COVID-19 Chest X-ray Dataset: https://github.com/ieee8023/covid-chestxray-dataset
3. Figure1 COVID-19 Chest X-ray Dataset: https://github.com/agchung/Figure1-COVID-chestxray-dataset
4. Actualmed COVID-19 Chest X-ray Dataset Initiative: https://github.com/agchung/Actualmed-COVID-chestxray-dataset
5. COVID-19 Radiography Database: https://www.kaggle.com/tawsifurrahman/covid19-radiography-database

## Software & Programming Languages Used:
1. **IDE/ Code Editor for Model Development:** Jupyter Notebook </br>
2. **IDE/ Code Editor for Web-Based Management Development:** Visual Studio Code</br>
3. **Scripting Language for Model Development:** Python 3.10 </br>
4. **Scripting Language for Web-Based Management Development:** Django 4.0, HTML5, CSS3, JavaScript (ES2022)

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

## Result and Discussion

### Evaluation Metrics
#### 1. Validation & Learning Curve
<img src="https://user-images.githubusercontent.com/82216057/219871142-cf043f9a-aad3-446b-8e0f-c87c5363a3c1.png" width="1300" height="300">

For the accuracy model, it can be observed that the training accuracy gradually increases from epoch 0 to epoch 3. After the 12 epochs, it had reached a steady rate of accuracy throughout the 200 epochs within the range of accuracy from 90% to 94%. As for the validation accuracy, the accuracy was very low during the beginning. This was mainly due to the fact that the model was not fully capable to predict the outcomes yet as the model had only been trained with only a few epochs of datasets. More epochs are needed to train the model in order to enhance the performance of the model. This can be shown from the figure where the validation accuracy has begun to increase as the number of epochs increases. Although the validation accuracy was slightly fluctuating, nevertheless the accuracy was stable enough along the epochs within a range of 94% to 75%. Besides, the developer thinks that it is the most optimum parameter tuning for the model. Therefore, the developer is satisfied with 
the result.As for the model loss, it can be observed that the training loss had reached a steady rate of loss from the beginning throughout the 200 epochs within a range of 0.15 to 0.14. As for the validation loss, the model was fluctuating at the beginning. This was also due to the model not capable of predicting the outcome with only a few epochs of datasets. After 34 epochs, the validation loss had reached a steady rate of 0.8 to 0.5 until 200 epochs even though slight fluctuations occurred.

#### 2. Accuracy Score
<img src="https://user-images.githubusercontent.com/82216057/219871180-6b6e3a57-8d0f-4c7b-ab19-7f2d5075017b.png" width="400" height="150">

The accuracy of the model is able to achieve a satisfying accuracy score of 94.65%.

#### 3. Confusion Matrix
<img src="https://user-images.githubusercontent.com/82216057/219871193-31ade9aa-76f7-43d1-a6b1-2f0b2fd8d3cb.png" width="700" height="500">

The column values will serve as predicted values and the row values will serve as actual values. For the first row, which is NORMAL value, the model was able to predict 834 of X-ray images correctly and 52 of THE Xray incorrectly (48 PNEUMONIA & 4 COVID). For the second row, which is PNEUMONIA, the model is able to predict 571 of X-ray images correctly and 31 of the images were predicted as NORMAL. Lastly, which is COVID-19 on the third row, the model is able to predict 98 of the Xray images correctly and 2 of the images incorrectly (1 NORMAL & 1 PNEUMONIA).Looking at the NORMAL column, 866 of the X-ray images had been predicted as NORMAL. 
Among the 866 predicted values, 32 of them were incorrectly predicted (31 PNEUMONIA & COVID). For the PNEUMONIA column, 620 of the X-rays images had been predicted as 
PNEUMONIA. 571 images were predicted correctly and 49 were predicted incorrectly (48 NORMAL & 1 COVID). Last but not least, which is the COVID-19 column, 102 of the X-ray images had been predicted as COVID. 98 images were predicted correctly and 4 were predicted as NORMAL.

#### 4. Heatmap Generation
<img src="https://user-images.githubusercontent.com/82216057/219871208-b0d40923-6d44-40fe-8504-0bdc3a395d2e.png" width="700" height="350">
<img src="https://user-images.githubusercontent.com/82216057/219871227-47c429d5-e045-43a6-a1ab-06fad6b5cbb1.png" width="700" height="350">
<img src="https://user-images.githubusercontent.com/82216057/219871497-00f7bdbb-5916-44e9-8e43-2adf36f07b21.png" width="700" height="350">

## Web-Based System

#### 1. Visitor's Main Menu
<img src="https://user-images.githubusercontent.com/82216057/219871653-c4c091d9-e8a3-497e-8cfa-d87a56cdfc97.png" width="800" height="350">
<img src="https://user-images.githubusercontent.com/82216057/219871745-fd33fd10-5062-491a-a6ed-3134e523bffb.png" width="800" height="350">
<img src="https://user-images.githubusercontent.com/82216057/219871770-5ce9da0e-e298-4fad-9314-d85720875365.png" width="800" height="450">

#### 2. Dashboard
<img src="https://user-images.githubusercontent.com/82216057/219871846-92941ccf-8ab5-4358-9bec-5563dcac3f6d.png" width="800" height="350">

#### 3. Register Patient
<img src="https://user-images.githubusercontent.com/82216057/219871920-11ff810e-dcb2-42c4-868d-2536453dd70c.png" width="800" height="650">

#### 4. View Record
<img src="https://user-images.githubusercontent.com/82216057/219871991-c59863e6-55c7-4483-acb4-f23e03ea9e8b.png" width="800" height="400">

## Conclusion
In a nutshell, the main goal had been achieved by detecting COVID-19 and pneumonia through chest X-ray images. In addition, the three objectives had been accomplished as well. 
