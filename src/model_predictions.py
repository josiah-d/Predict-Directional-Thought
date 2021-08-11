from glob import glob

import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

from load_data import master_load

# load data
X_train, X_test, y_train, y_test = master_load()

# get best model
best_numpy_model = sorted(glob('../models/numpy/*.model'))[-1]
model_numpy = load_model(best_numpy_model)

# make predictions and reformat test data
y_pred = np.argmax(model_numpy.predict(X_test), axis=-1)
y_true = np.argmax(y_test, axis=-1)

# build dataframe to stow results
df = pd.DataFrame({'y_true': y_true, 'y_pred': y_pred})
df = df.sample(frac=1).reset_index()
df.drop('index', axis=1, inplace=True)


if __name__ == '__main__':
    # save results
    df.to_csv('../data/best_model_results.csv')
