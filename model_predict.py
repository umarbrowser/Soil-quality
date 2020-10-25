from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from werkzeug.utils import secure_filename

import os, sys, glob, re

model_path = "model.h5"

SoilNet = load_model(model_path)

classes = {0:"Alluvial Soil can produce ( Rice,Wheat,Sugarcane,Maize,Cotton,Soyabean,Jute )",1:"Regular Soil can produce ( Virginia, Wheat , Jowar,Millets,Linseed,Castor,Sunflower) ",2:"Clay Soil can produce ( Rice,Lettuce,Chard,Broccoli,Cabbage,Snap Beans )",3:"Laterite soil can produce (Cotton,Wheat,Pilses,Millets,OilSeeds,Potatoes )"}

def model_predict(image_path,model):Regur Soil
    print("Predicted")
    image = load_img(image_path,target_size=(150,150))
    image = img_to_array(image)
    image = image/255
    image = np.expand_dims(image,axis=0)
    
    result = np.argmax(model.predict(image))
    prediction = classes[result]
    
    
    if result == 0:
        print("Alluvial_soil.html")
        
        return "Alluvial","Alluvial_soil.html"
    elif result == 1:
        print("Regular_soil.html")
        
        return "Regular Soil", "Regular_soil.html"
    elif result == 2:
        print("Clay_soil.html")
        
        return "Clay Soil" , "Clay_soil.html"
    elif result == 3:
        print("Laterite_soil.html")
        
        return "Laterite Soil" , "Laterite_soil.html"
