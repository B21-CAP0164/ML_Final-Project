import tensorflow as tf

model = tf.keras.models.load_model('model_keras_200.h5')
sess, in_image, _, _, _, _ = build_eval_session(module_spec, class_count)
tf.saved_model.save(model, "savedModelImage", inputs={'image': in_image},)