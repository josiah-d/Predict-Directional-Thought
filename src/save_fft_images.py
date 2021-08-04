# imports
import matplotlib.pyplot as plt
import numpy as np

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

# load data
path = 'data/train/right/1572815379.npy'
data = np.load(path)


def save_images(data):
    '''iterate through observations and save as images'''
    for i in range(len(data)):
        fig, ax = plt.subplots(figsize=(16, 9))
        for channel in data[i]:
            plt.plot(channel)
        ax.set_title('All Leads')
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel('Frequency (µV)')
        ax.set_ylim(0, 35)

        if i < 10:
            plt.savefig(f'img/animate/00{i}.png')
        elif i < 100:
            plt.savefig(f'img/animate/0{i}.png')
        else:
            plt.savefig(f'img/animate/{i}.png')


if __name__ == '__main__':
    save_images(data)
