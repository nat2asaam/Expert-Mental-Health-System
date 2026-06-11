import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Input
import warnings
import pandas as pd
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
# This script is for medical diagnosis of bi-polar disorder with the symptoms below which are commonly associated with manic episodes in bipolar disorder:
# The symptoms are the features or inputs to the neural network and the output is the likelihood of having bipolar disorder based on these symptoms.
# Below are the 7 symptoms:
# Feeling overly happy or high
# Having a decreased need for sleep
# Talking fast
# Feeling extremely restless or impulsive
# Being easily distracted
# Having over confidence in your abilities
# Engaging in risky activities
# This scripts uses the Keras Library to build a neural network model for regression. The model is trained on a dataset of 128 samples, where each sample represents a combination of the 7 symptoms and the corresponding likelihood of having bipolar disorder. The dataset is generated using numpy, where the input features are binary (0 or 1) indicating the presence or absence of each symptom, and the target variable is the mean of the input features, representing the likelihood of having bipolar disorder. The model is trained for 100 epochs with a validation split of 30%.

def regression_model(n_cols):
    # create model
    model = Sequential()
    model.add(Input(shape=(n_cols,)))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(1))
    # compile model
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model
def train_model():
    # Generate the input dataset
    X=np.indices((2,)*7).reshape(7,-1).T
    X=X.astype(np.float32)
    # Generate the target dataset
    d=np.mean(X, axis=1)
    d=d.reshape(1,-1)
    predictors_norm=(X-X.mean())/X.std()
    target=d.T
    n_cols=predictors_norm.shape[1]
    model=regression_model(n_cols)
    history=model.fit(predictors_norm, target, validation_split=0.3, epochs=100, verbose=2)
    model.evaluate(predictors_norm, target)
    #predict the likelihood of having bipolar disorder based on the symptoms
    new_data=np.array([[1.0,1.0,1.0,1.0,1.0,1.0,1.0]])
    prediction=model.predict(new_data)
    print("The likelihood of having bipolar disorder based on the symptoms is: ", prediction)
    # 2. Extract loss and validation loss values
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(1, len(loss) + 1)

    # 3. Create the plot
    plt.figure(figsize=(8, 5))
    plt.plot(epochs, loss, 'bo-', label='Training Loss')       # Blue line with dots
    plt.plot(epochs, val_loss, 'ro-', label='Validation Loss') # Red line with dots

    # 4. Add labels, title, and styling
    plt.title('Training and Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)

    # 5. Display the plot
    plt.show()
    save_model(model)
def save_model(model):
    model.save('bipolar_model.keras')
def load_model():
    loaded_model = keras.models.load_model('bipolar_model.keras')
    return loaded_model
def predict_bipolar_disorder(symptoms):
    loaded_model = load_model()
    prediction = loaded_model.predict(symptoms)
    return prediction