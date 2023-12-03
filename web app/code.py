from flask import*
import tensorflow as tf
from tensorflow import keras
from keras import layers

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict",methods = ["POST","GET"])
def savedetails():
    msg = "Cancerous Image"  
    if request.method == "POST":  
        uploaded_file = request.files["imageUpload"]
        img_path = "static/uploaded_image.jpeg"
        uploaded_file.save(img_path)
        loaded_model = tf.keras.models.load_model('model.h5')
        new_image_path = 'static/uploaded_image.jpeg'
        new_image = tf.keras.preprocessing.image.load_img(new_image_path, target_size=(256, 256,3))
        new_image = tf.keras.preprocessing.image.img_to_array(new_image)
        new_image = tf.expand_dims(new_image, axis=0)
        result = loaded_model.predict(new_image)


        print(result[0][1])

        if result[0][1] >= 1:
            prediction = 'Cancerous'
        else:
            prediction = 'Non-Cancerous'
            
        # print(f'The prediction for the new image is: {prediction}')

        return render_template("result.html", msg=prediction, img_path="static/uploaded_image.jpeg")
    

    
app.run(host='0.0.0.0', port=5000)

