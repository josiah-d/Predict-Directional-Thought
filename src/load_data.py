# imports
import os

import numpy as np

# set directories to get data from
train_dir = '../data/train'
test_dir = '../data/test'

# establish labels for the differing thoughts
actions = ['left', 'right', 'none']


def shuffle(data_dct):
    '''
    shuffle the data to prevent overfitting 

    params
    ======
    data_dct (dict): FFT EEG data keys are labeled targets, values are the
        features

    attrs
    =====
    none

    returns
    =======
    data_dct (dict): FFT EEG data keys are labeled targets, values are the
        features
    '''
    lengths = [len(data_dct[action]) for action in actions]
    for action in actions:
        np.random.shuffle(data_dct[action])
        data_dct[action] = data_dct[action][:min(lengths)]

    return data_dct


def load_data(actions, data_dir):
    '''
    loads the data from the .npy files and convert it to a dictionary

    params
    ======
    actions (list): strings of labels that correspond to the directories of each
        .npy file
    data_dir (str): path to the beginning of the data

    attrs
    =====
    none

    returns
    =======
    data_dct (dict): shuffled FFT EEG data keys are labeled targets, values are
        the features
    '''
    data_dct = {}
    for action in actions:
        if action not in data_dct:
            data_dct[action] = []

        data_sub_dir = os.path.join(data_dir, action)
        for item in os.listdir(data_sub_dir):
            data = np.load(os.path.join(data_sub_dir, item))
            for datum in data:
                data_dct[action].append(datum)

    return shuffle(data_dct)


def combine_data(data_dct):
    '''
    sets a array of ints as the target

    params
    ======
    data_dct (dict): shuffled FFT EEG data keys are labeled targets, values are
        the features

    attrs
    =====
    none

    returns
    =======
    combined_data (list): shuffled data in 0 index, array of ints as the target
        in 1 index
    '''
    combined_data = []
    for action in actions:
        for data in data_dct[action]:

            if action == "left":
                combined_data.append([data, [1, 0, 0]])
            elif action == "right":
                combined_data.append([data, [0, 0, 1]])
            elif action == "none":
                combined_data.append([data, [0, 1, 0]])

    np.random.shuffle(combined_data)

    return combined_data


def split_data(data_dct):
    '''
    performs an X, y split

    params
    ======
    data_dct (dict): shuffled FFT EEG data keys are labeled targets, values are
        the features

    attrs
    =====
    none

    returns
    =======
    X (list): shuffled data
    y (list): array of ints as the target in 1 index
    '''
    X = []
    y = []
    data = combine_data(data_dct)
    for feature, target in data:
        X.append(feature)
        y.append(target)

    return X, y


def master_load():
    '''
    performs an train, test split

    params
    ======
    none

    attrs
    =====
    none

    returns
    =======
    X_train (list): shuffled data
    X_test (list): shuffled data
    y_train (list): array of ints as the target in 1 index
    y_test (list): array of ints as the target in 1 index
    '''
    train = load_data(actions, train_dir)
    test = load_data(actions, test_dir)

    X_train, y_train = split_data(train)
    X_test, y_test = split_data(test)

    return X_train, X_test, y_train, y_test


if __name__ == '__main__':
    X_train, X_test, y_train, y_test = master_load()
