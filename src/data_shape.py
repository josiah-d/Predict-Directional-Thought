# imports
import numpy as np
from glob2 import glob

# get paths
train_paths = ['data/train/left/*.npy',
               'data/train/none/*.npy',
               'data/train/right/*.npy']

test_paths = ['data/test/left/*.npy',
              'data/test/none/*.npy',
              'data/test/right/*.npy']


def shape_retriever(path):
    """Obtain the shape of each numpy.ndarray

    params
        path: relative file path

    returns
        shape: tuple containing array shape
    """
    arr = np.load(path)
    return arr.shape


def observ_data_number(paths):
    """Obtain the number of observations and datapoints

    params
        paths: array of file paths

    returns
        observations: number of observations
        data_points: number of data points
    """
    observations = 0
    data_points = 0

    for dir in paths:
        for path in glob(dir):
            x, y, z = shape_retriever(path)
            observations += x  # observations
            data_points += x * y * z  # data points

    return observations, data_points


# compute number of observation or datapoints
train_observations, train_data_points = observ_data_number(train_paths)
print('train')
print(f'observations: {train_observations}, datapoints: {train_data_points}')

test_observations, test_data_points = observ_data_number(test_paths)
print('test')
print(f'observations: {test_observations}, datapoints: {test_data_points}')


'''
RESULTS
=======

train
observations: 284625, datapoints: 273240000

test
observations: 35250, datapoints: 33840000
'''
