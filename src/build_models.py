# imports
import time

import pandas as pd
from tensorflow.keras.layers import Activation, Conv1D, Dropout, Reshape
from tensorflow.keras.models import Sequential

from load_data import master_load

# build df to stow models
model_df = pd.DataFrame({'loss': [],
                         'accuracy': [],
                         'val_loss': [],
                         'val_accuracy': [],
                         'model_name': []})


def fit_model(model, X_train, y_train, X_test, y_test, epochs=5, batch_size=32, model_type='numpy'):
    # fit model and stow results
    global model_df

    fitted = model.fit(X_train, y_train, batch_size=batch_size,
                       epochs=epochs, validation_data=(X_test, y_test))
    score = fitted.model.evaluate(X_test, y_test, batch_size=batch_size)

    model_name = f'../models/{model_type}/acc_{round(score[1], 3)}-loss_{round(score[0], 2)}-{int(time.time())}.model'

    temp_df = pd.DataFrame.from_dict(fitted.history)
    temp_df['model_name'] = model_name
    model_df = pd.concat([model_df, temp_df])

    fitted.model.save(model_name)
    print('done')


# load data
X_train, X_test, y_train, y_test = master_load()

# best model structure
model = Sequential()

model.add(Conv1D(64, (5), padding='same', input_shape=X_train.shape[1:]))
model.add(Activation('relu'))

model.add(Conv1D(128, (5), padding='same'))
model.add(Activation('relu'))

model.add(Conv1D(256, (5), padding='same'))
model.add(Activation('relu'))

model.add(Conv1D(512, (5), padding='same'))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Conv1D(3, (16)))
model.add(Reshape((3,)))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.summary()

if __name__ == '__main__':
    # fit model
    fit_model(model, X_train, y_train, X_test, y_test,
              epochs=100, batch_size=32, model_type='numpy')
