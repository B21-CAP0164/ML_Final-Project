import tensorflow as tf

model = tf.keras.models.load_model('model_keras_200.h5')
tf.saved_model.save(model, "savedModelImage")