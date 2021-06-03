import os
import cv2
import json
import base64
import numpy as np

# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf
from keras.preprocessing import image
from flask import Flask, request


app = Flask(__name__)

model = tf.keras.models.load_model('model_keras_200.h5')
# print(model.summary())
print("----------------model loaded----------------------")

@app.route("/")
def hello():
  return "Hello, World!"

@app.route("/predict", methods=["POST"])
def predict():
  request_json = request.json
  print("data: {}".format(request_json))
  print("type: {}".format(type(request_json)))

  dataInBase64 = request_json.get('data')

  dataInBase64 = dataInBase64.encode('utf-8')
  print(dataInBase64)
  print(type(dataInBase64))

  with open("deploy2.png", "wb") as fh:
    fh.write(base64.decodebytes(dataInBase64))
  
  img = image.load_img("deploy2.png", target_size=(100, 100))
  # img = image.load_img('bondi_beach.jpg', grayscale=True)

  img_array = image.img_to_array(img)

  image.save_img('deploy2resized.png', img_array)
  img_array = np.expand_dims(img_array, axis=0)
  images = np.vstack([img_array])

  prediction = model.predict(images)
  print(prediction)
  # prediction_string = [str(d) for d in prediction]
  
  response_json = {
    "data" : request_json.get("data"),
    "prediction" : "wakwaw"
    # "prediction" : list(prediction_string)
  }

  return json.dumps(response_json)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)