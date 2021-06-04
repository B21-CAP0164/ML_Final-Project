import os
import cv2
import json
import base64
import numpy as np

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf
from keras.preprocessing import image
from flask import Flask, request

IMAGE_PATH = "../img/deploy.png"
RESIZED_PATH = "../img/deployResized.png"
MODEL_PATH = '../model_keras_200.h5'
label = ["good", "poor", "very_poor"]

app = Flask(__name__)

model = tf.keras.models.load_model(MODEL_PATH)
# print(model.summary())
print("----------------model loaded----------------------")

@app.route("/")
def hello():
  return "Hello, World!"

@app.route("/predict", methods=["POST"])
def predict():
  request_json = request.json
  # print("data: {}".format(request_json))
  print("type: {}".format(type(request_json)))

  dataInBase64 = request_json.get('data')

  dataInBase64 = dataInBase64.encode('utf-8')
  # print(dataInBase64)
  print(type(dataInBase64))

  with open(IMAGE_PATH, "wb") as fh:
    fh.write(base64.decodebytes(dataInBase64))
  
  img = image.load_img(IMAGE_PATH, target_size=(100, 100))
  img_array = image.img_to_array(img)

  image.save_img(RESIZED_PATH, img_array)
  img_array = np.expand_dims(img_array, axis=0)
  images = np.vstack([img_array])

  prediction = model.predict(images)
  # print(prediction)
  # print(type(prediction))
  print(prediction[0])
  # print(prediction[0][0])
  # print(prediction[0][1])
  # print(prediction[0][2])

  response = []
  response.append(prediction[0][0])
  response.append(prediction[0][1])
  response.append(prediction[0][2])
  
  max_value = max(response)
  max_index = response.index(max_value)
  print("prediction :", label[max_index])
  
  response_json = {
    "prediction" : label[max_index],
  }

  return json.dumps(response_json)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)