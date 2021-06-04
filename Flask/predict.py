import json
import tensorflow as tf
import os
import numpy as np
import base64
# from keras.preprocessing import image

model = tf.keras.models.load_model('./mobilenetv3_edit_v2')
class_names = ['Fresh Apple', 'Fresh Banana', 'Fresh Lemon', 'Fresh Orange',
               'Rotten Apple', 'Rotten Banana', 'Rotten Lemon', 'Rotten Orange',
               'Uncategorized']


def do_predict(data):
    prediction = model.predict(data)
    new_prediction = prediction.tolist()
    result = int(np.argmax(prediction))
    class_name = class_names[result]
    percent = float(np.max(prediction * 100))
    jsonDict = {
        'predClass': result,
        'className': class_name,
        'percentage': percent,
        'prediction': new_prediction,
    }
    return json.dumps(jsonDict)
