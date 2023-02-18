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

## Result and Discussion

### Evaluation Metrics
1. Validation & Learning Curve

For the accuracy model, it can be observed that the training accuracy gradually increases from epoch 0 to epoch 3. After the 12 epochs, it had reached a steady rate of accuracy throughout the 200 epochs within the range of accuracy from 90% to 94%. As for the validation accuracy, the accuracy was very low during the beginning. This was mainly due to the fact that the model was not fully capable to predict the outcomes yet as the model had only been trained with only a few epochs of datasets. More epochs are needed to train the model in order to enhance the performance of the model. This can be shown from the figure where the validation accuracy has begun to increase as the number of epochs increases. Although the validation accuracy was slightly fluctuating, nevertheless the accuracy was stable enough along the epochs within a range of 94% to 75%. Besides, the developer thinks that it is the most optimum parameter tuning for the model. Therefore, the developer is satisfied with 
the result.As for the model loss, it can be observed that the training loss had reached a steady rate of loss from the beginning throughout the 200 epochs within a range of 0.15 to 0.14. As for the validation loss, the model was fluctuating at the beginning. This was also due to the model not capable of predicting the outcome with only a few epochs of datasets. After 34 epochs, the validation loss had reached a steady rate of 0.8 to 0.5 until 200 epochs even though slight fluctuations occurred.

2. Accuracy Score
The accuracy of the model is able to achieve a satisfying accuracy score of 94.65%.

3. Confusion Matrix

The column values will serve as predicted values and the row values will serve as actual values. For the first row, which is NORMAL value, the model was able to predict 834 of X-ray images correctly and 52 of THE Xray incorrectly (48 PNEUMONIA & 4 COVID). For the second row, which is PNEUMONIA, the model is able to predict 571 of X-ray images correctly and 31 of the images were predicted as NORMAL. Lastly, which is COVID-19 on the third row, the model is able to predict 98 of the Xray images correctly and 2 of the images incorrectly (1 NORMAL & 1 PNEUMONIA).Looking at the NORMAL column, 866 of the X-ray images had been predicted as NORMAL. 
Among the 866 predicted values, 32 of them were incorrectly predicted (31 PNEUMONIA & COVID). For the PNEUMONIA column, 620 of the X-rays images had been predicted as 
PNEUMONIA. 571 images were predicted correctly and 49 were predicted incorrectly (48 NORMAL & 1 COVID). Last but not least, which is the COVID-19 column, 102 of the X-ray images had been predicted as COVID. 98 images were predicted correctly and 4 were predicted as NORMAL.

4. Heatmap Generation



