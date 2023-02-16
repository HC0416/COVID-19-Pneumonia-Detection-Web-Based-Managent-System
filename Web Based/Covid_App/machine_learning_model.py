import os
import numpy as np
import pandas as pd 
import random
import cv2
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt,mpld3

# Deep learning libraries
import tensorflow as tf
from keras import backend as K
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile

from io import StringIO, BytesIO
import base64

# Setting seeds for reproducibility
seed = 232
np.random.seed(seed)
tf.random.set_seed(seed)

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True 
config.gpu_options.per_process_gpu_memory_fraction = 0.9
session = tf.compat.v1.InteractiveSession(config=config)

tf.compat.v1.disable_eager_execution()

from keras.models import load_model

def get_model():
    global model
    print("Loading model")
    model = load_model("C:/Users/Dell/Desktop/Hadrian_FYP/outputs/resnet") #change the file location
    model._make_predict_function()

    print("Model Loaded")

get_model()

conv_layer = "post_relu"

from skimage import data, color, io, img_as_float
from skimage import filters

def get_heatmap(processed_image, class_idx):
    
    class_output = model.output[:, class_idx]
    # choose the last conv layer in your model
    last_conv_layer = model.get_layer(conv_layer)
    # get the gradients wrt to the last conv layer
    grads = K.gradients(class_output, last_conv_layer.output)[0]
   # we pool the gradients over all the axes leaving out the channel dimension
    pooled_grads = K.mean(grads, axis=(0,1,2))
    # Define a function that generates the values for the output and gradients
    with session.as_default():
            with session.graph.as_default():
                iterate = K.function([model.input], [pooled_grads, last_conv_layer.output[0]])
                print("ghm6")
                grads_values, conv_ouput_values = iterate([processed_image])

   
    # get the values
    # iterate over each feature map in your conv output and multiply
    # the gradient values with the conv output values. This gives an 
    # indication of "how important a feature is"
    nv = grads_values.shape[0]
    for i in range(nv):
        conv_ouput_values[:,:,i] *= grads_values[i]
    # create a heatmap
    heatmap = np.mean(conv_ouput_values, axis=-1)
    # remove negative values
    heatmap = np.maximum(heatmap, 0)
    # normalize
    heatmap /= heatmap.max()
    
    return heatmap

graph = tf.compat.v1.get_default_graph()

def pre(sample_image,model):
    sample_image = cv2.resize(sample_image, (150,150))
    sample_image = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)
    sample_image = sample_image.astype(np.float32)/255.
    sample_label = 1
    sample_image_processed = np.expand_dims(sample_image, axis=0)
    pred_label =[]

    with session.as_default():
            with session.graph.as_default():
                with graph.as_default():
                    pred_label = model.predict(sample_image_processed)
    pred_label = list(pred_label[0]).index(max(pred_label[0]))
    return pred_label,sample_image,sample_image_processed

def heatm(pred_label,sample_image,sample_image_processed):
    # get the heatmap for class activation map(CAM)
    heatmap = get_heatmap(sample_image_processed, pred_label)
    heatmap = cv2.resize(heatmap, (sample_image.shape[0], sample_image.shape[1]))
    heatmap = heatmap *255
    heatmap = np.clip(heatmap, 0, 255).astype(np.uint8)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_RAINBOW)
    #superimpose the heatmap on the image    

    sample_image_hsv = color.rgb2hsv(sample_image)
    heatmap = color.rgb2hsv(heatmap)

    alpha=.9
    sample_image_hsv[..., 0] = heatmap[..., 0]
    sample_image_hsv[..., 1] = heatmap[..., 1] * alpha

    img_masked = color.hsv2rgb(sample_image_hsv)
    return img_masked

def evaluate(X_Ray):
    dis = ["NORMAL","PNEUMONIA","COVID"]
    img = X_Ray
    count = 0
    f,ax = plt.subplots(1,2,figsize=(16,40))
    ax = ax.ravel()
    plt.tight_layout()
    i = 0

    sample_image = plt.imread(img)
    pred_label,sample_image1,sample_image_processed = pre(sample_image,model)
    img_masked = heatm(pred_label,sample_image1,sample_image_processed)

    if(dis[0] == dis[pred_label]):
        ax[i].imshow(sample_image1)
        ax[i].set_title(f"True label: {dis[0]} \n Predicted label: {dis[pred_label]}")
        ax[i].axis('off')
        i+=1
        ax[i].imshow(img_masked)
        ax[i].set_title("Class Activation Map")
        ax[i].axis('off')
        i+=1
        
    elif(dis[1] == dis[pred_label]):
        ax[i].imshow(sample_image1)
        ax[i].set_title(f"True label: {dis[1]} \n Predicted label: {dis[pred_label]}")
        ax[i].axis('off')
        i+=1
        ax[i].imshow(img_masked)
        ax[i].set_title("Class Activation Map")
        ax[i].axis('off')
        i+=1        

    elif(dis[2] == dis[pred_label]):
        ax[i].imshow(sample_image1)
        ax[i].set_title(f"True label: {dis[2]} \n Predicted label: {dis[pred_label]}")
        ax[i].axis('off')
        i+=1
        ax[i].imshow(img_masked)
        ax[i].set_title("Class Activation Map")
        ax[i].axis('off')
        i+=1

    # plt.savefig("C:\\Users\\Dell\\Desktop\\django\\Pneumonia\\Images\\Results\\"+ str(X_Ray), bbox_inches = 'tight')

    f = StringIO()
    plt.savefig("C:\\Users\\Dell\\Desktop\\FYP_Web\\Pneumonia_Web\Images\\Heatmap\\"+ str(X_Ray), bbox_inches = 'tight')

    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches = 'tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    data = base64.b64encode(image_png)
    data = data.decode('utf-8')

    return data, dis[pred_label]

