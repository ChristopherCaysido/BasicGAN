#Process of Creating a simple GAN
#Scenario:
#We want to generate a sad face 5x5 matrix
import numpy as np
from numpy import random
from matplotlib import pyplot as plt

#Plotting Function
def view_samples(samples,m,n):
    fig, axes = plt.subplots(figsize=(10,10), nrows=m, ncols=n, sharey=True, sharex=True)
    for ax, img in zip(axes.flatten(),samples):
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        im = ax.imshow(1-img.reshape((5,5)), cmap='Grey_r')
    return fig, axes

faces = [np.array([0,0,0,0,0,
                   0,1,0,1,0,
                   0,0,0,0,0,
                   0,1,1,1,0,
                   1,0,0,0,1]),
         np.array([0,0,0,0,0,
                   0,1,0,1,0,
                   0,0,0,0,0,
                   0,1,1,1,0,
                   1,0,0,0,1]),
         np.array([0,0,0,0,0,
                   0,1,0,1,0,
                   0,0,0,0,0,
                   0,1,1,1,0,
                   1,0,0,0,1]),
         np.array([0,0,0,0,0,
                   0,1,0,1,0,
                   0,0,0,0,0,
                   0,1,1,1,0,
                   1,0,0,0,1])]

_ = view_samples(faces, 1,5)



