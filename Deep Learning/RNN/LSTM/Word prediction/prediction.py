import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
from tensorflow.keras.models import load_model 

# same  steps form notebook
with open('RNN/LSTM/Word prediction/tokenizer.pickle','rb') as handle:
    mytokenizer = pickle.load(handle)

# print(mytokenizer)
    
model = load_model('RNN/LSTM/Word prediction/word_prediction_model.h5')

input_text = 'prime minister'
predict_next_words = 5

for i in range(predict_next_words):
    #tokenizing
    token_list = mytokenizer.texts_to_sequences([input_text])[0]
    # padding
    token_list = pad_sequences([token_list],maxlen=model.input_shape[1],padding = 'pre')
    # model prediction
    predicted = model.predict(token_list)
    # print(predicted)
    predicted = np.argmax(predicted, axis=-1)
    print(predicted) # here we get predited values key
    # so we need to take value of key
    predicted_word = mytokenizer.index_word[predicted[0]]
    # print(predicted_word)
    # join predicted words
    input_text +=" " + predicted_word
print(input_text)