from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

import os, sys, glob, re

app = Flask(__name__)

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
        print("./templates/Alluvial.html")
        
        return "Alluvial","./templates/Alluvial.html"
    elif result == 1:
        print("./templates/regular_soil.html")
        
        return "Regular Soil", "./templates/Regular_soil.html"
    elif result == 2:
        print("./templates/Clay_soil.html")
        
        return "Clay Soil" , "./templates/Clay_soil.html"
    elif result == 3:
        print("./templates/Laterite_soil.html")
        
        return "Laterite Soil" , "./templates/Laterite_soil.html"

@app.route('/',methods=['GET'])
def index():
    return render_template('./templates/index.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    print("Entered")
    if request.method == 'POST':
        print("Entered here")
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = model_predict(file_path,SoilNet)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)
    


if __name__ == '__main__':
    app.run(debug=True,threaded=False)
    
