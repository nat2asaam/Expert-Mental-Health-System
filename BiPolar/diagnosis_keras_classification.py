import keras
from keras.models import Sequential
from keras.layers import Dense,Input
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np
# This script is for medical diagnosis of bi-polar disorder with the symptoms below which are commonly associated with manic episodes in bipolar disorder:
# The symptoms are the features or inputs to the neural network and the output is an output  of categorical data showing that a patient has or does not have the disorder
# 1 for has and 0 for does not have.
# Below are the 7 symptoms:
# Feeling overly happy or high
# Having a decreased need for sleep
# Talking fast
# Feeling extremely restless or impulsive
# Being easily distracted
# Having over confidence in your abilities
# Engaging in risky activities
# This scripts uses the Keras Library to build a neural network model for regression. The model is trained on a dataset of 128 samples, where each sample represents a combination of the 7 symptoms and the corresponding likelihood of having bipolar disorder. The dataset is generated using numpy, where the input features are binary (0 or 1) indicating the presence or absence of each symptom, and the target variable is the mean of the input features, representing the likelihood of having bipolar disorder. The model is trained for 100 epochs with a validation split of 30%.
def classification_model(n_cols):
    model = Sequential()
    model.add(Input(shape=(n_cols,)))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(100, activation='sigmoid'))
    model.add(Dense(2, activation='softmax'))  
    model.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy','precision'])
    return model
def train_model():
    # Generate the input dataset
    X=np.indices((2,)*7).reshape(7,-1).T
    X=X.astype(np.float32)
    # Generate the random target dataset
    #d=np.random.randint(0, 2, size=128) 
    # d = np.random.randint(0, 3, size=128) for 3 classes
    # Genrate the target dataset based on the when any of the input symptooms is present then the target is 1 and when all the symptoms are absent then the target is 0
    d=np.where(X.sum(axis=1) > 0, 1, 0) 
    target=to_categorical(d,2)
    d=d.reshape(1,-1)

    n_cols=X.shape[1]
    print("Number of classes: ", n_cols)
    model=classification_model(n_cols)  
    history=model.fit(X,target,validation_split=0.2,epochs=100,verbose=2)
    scores=model.evaluate(X, target, verbose=0)
    print('Accuracy: {} \n Error: {}'.format(scores[1], 1 - scores[1]))   

    random_index = np.random.randint(0, len(X))
    # Using a slice [index:index+1] keeps the required 2D shape (1, 7)
    #random_sample = X[random_index:random_index+1]
    random_sample=np.array([[0,1,0,0,0,0,0]])
    prediction=model.predict(random_sample)
    print('Prediction: {} and sample: {}'.format(prediction, random_sample))
    model.save('bipolar_classification_model.keras')
def load_model():
    loaded_model = keras.models.load_model('bipolar_classification_model.keras')
    return loaded_model
def predict_bipolar_disorder(symptoms):
    loaded_model = load_model()
    prediction = loaded_model.predict(symptoms)
    return prediction