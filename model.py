import tensorflow as tf
import numpy as np
import pandas as pd
import pickle


df= pd.read_csv('data.csv')
df.replace('Yes',1,inplace=True)
df.replace('No',0,inplace=True)
narray= df.to_numpy()

Y_train=narray[:,-1:].astype(np.float32)
X_train= np.delete(narray,-1,axis=1).astype(np.float32)

model = tf.keras.models.Sequential([
    
    tf.keras.layers.Dense(units=20, activation='relu'),
    tf.keras.layers.Dense(units=13, activation='relu'),
    tf.keras.layers.Dense(units=1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, Y_train, epochs=6)

sample=np.array([[1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0]])

pred =model.predict(sample)
if(pred[0][0]>0.5):
    print("Likely to have covid")
else:
    print("Unlikely to get covid")

pickle.dump(model, open('model.json', 'wb'))