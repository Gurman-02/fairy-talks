
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing import text
import numpy as np
from tensorflow.keras.utils import pad_sequences

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

with open('max_final.pickle', 'rb') as handle:
    max_len = pickle.load(handle)

# Load the saved model
loaded_model = tf.keras.models.load_model('final_model.h5')





def sentPrediction(text):
    new_text=text
    new_text_seq = tokenizer.texts_to_sequences([new_text])
    new_text_padded = pad_sequences(new_text_seq, maxlen=max_len, padding='post')
    
    predictions = loaded_model.predict(new_text_padded)
    predicted_class_index = predictions.argmax(axis=-1)
    if predicted_class_index[0] == 0:
        return "positive"
    elif predicted_class_index[0] == 1:
        return "negative"
    else:
         return "neutral"

















