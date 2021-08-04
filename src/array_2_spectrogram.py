# imports
from glob import glob

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# set plotting params
plt.rcParams['font.serif'] = 'Ubuntu'
plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 32
plt.rcParams['axes.labelsize'] = 32
plt.rcParams['axes.titlesize'] = 32
plt.rcParams['xtick.labelsize'] = 24
plt.rcParams['ytick.labelsize'] = 24
plt.rcParams['legend.fontsize'] = 32
plt.rcParams['figure.titlesize'] = 48

# get paths
train_left = sorted(glob('data/train/left/*'))
train_none = sorted(glob('data/train/none/*'))
train_right = sorted(glob('data/train/right/*'))
test_left = sorted(glob('data/test/left/*'))
test_none = sorted(glob('data/test/none/*'))
test_right = sorted(glob('data/test/right/*'))

paths = [train_left, train_none, train_right,
         test_left, test_none, test_right]


def make_spectro(in_path, out_path):
    # load data
    data = np.load(in_path)

    # make spectrogram
    fig = plt.figure(figsize=(16, 16))
    ax = [fig.add_subplot(16, 1, i+1) for i in range(16)]

    for i, a in enumerate(ax):
        slice = data[:, i, :]
        a.imshow(slice.T)
        a.set_axis_off()

    fig.subplots_adjust(wspace=0, hspace=0)
    plt.savefig(out_path)


def silly_crop(path):
    # load image
    im = Image.open(path)

    # set size
    h, w = im.size
    left = 660
    top = 192
    right = w - 660
    bottom = h - top

    # crop and save
    crop_im = im.crop((left, top, right, bottom))
    crop_im.save(path)


def make_image_path(path):
    # path_list = path.split('/')
    new_path = 'img/' + path.split('.')[0] + '.png'

    return new_path


if __name__ == '__main__':
    # iterate through all paths, convert to spectrogram, and crop
    for sub_paths in paths:
        for path in sub_paths:
            new_path = make_image_path(path)
            make_spectro(path, new_path)
            silly_crop(new_path)
