import tensorflow as tf 
form tensorflow import keras 
form tensorflow.keras.layers import Dense, Embeding, Bidirectional, LSTM
from tensorfolw.keras.datasets import imbd


num_words = 1000 #nombre de mots à utiliser
maxlen = 100 # longueur maximale de chaque avis
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=num_words)