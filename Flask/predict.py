import json
import tensorflow as tf
import os
import numpy as np
import base64
# from keras.preprocessing import image

model = tf.keras.models.load_model('./mobilenetv3_edit_v1')
class_names = ['freshapples', 'freshbanana', 'freshlemon', 'freshoranges',
               'rottenapples', 'rottenbanana', 'rottenlemon', 'rottenoranges']


def do_predict(data):
    prediction = model.predict(data)
    new_prediction = prediction.tolist()
    result = int(np.argmax(prediction))
    class_name = class_names[result]
    percent = float(np.max(prediction * 100))
    if percent < 70.0:
        jsonDict = {
            'predClass': -1,
            'className': 'unknown',
            'percentage': 0,
            'prediction': new_prediction,
        }
    else:
        jsonDict = {
            'predClass': result,
            'className': class_name,
            'percentage': percent,
            'prediction': new_prediction,
        }
    return json.dumps(jsonDict)
