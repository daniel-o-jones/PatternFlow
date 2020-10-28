"""
Laterality classification of the OAI AKOA knee data set.

@author Jonathan Godbold, s4533974.

Usage of this file is strictly for The University of Queensland.
Date: 27/10/2020.

Description:
Builds a model of the OASIS OKOA dataset.

"""
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Input, Conv2D, Dense, Activation, Flatten, Dropout, MaxPooling2D, BatchNormalization, ReLU, LeakyReLU, Conv2D, Conv2DTranspose, BatchNormalization, Flatten, Dense, Reshape
from tensorflow.keras.models import Sequential, Model, load_model
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import regularizers, optimizers
from tensorflow.keras.callbacks import EarlyStopping

print('TensorFlow version:', tf.__version__)

def addLayer(model, input_shape, weight_decay, n_filters, kernel_size, padding, kernel_regularizer, batch_norm, activation_func):
    model.add(Conv2D(filters=n_filters, kernel_size=kernel_size, padding=padding, kernel_regularizer=kernel_regularizer, input_shape=input_shape))
    if (batch_norm == True):
        model.add(BatchNormalization())
    model.add(Activation(activation_func))
    print(model.summary())
    return model

def buildNetwork():
    model = Sequential()
    shape = 228, 260, 1
    weight_decay = 1e-4
    k_size = (3, 3)
    reg = regularizers.l2(weight_decay)
    model = addLayer(model, shape, weight_decay, 32, k_size, "same", reg, True, 'relu')
    model = addLayer(model, shape, weight_decay, 64, k_size, "same", reg, True, 'relu')
    model = addLayer(model, shape, weight_decay, 128, k_size, "same", reg, True, 'relu')
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))
    return model