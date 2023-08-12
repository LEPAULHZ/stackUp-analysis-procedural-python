# Libraries
import statistics as st
import numpy as np
from numpy.random import normal
# from matplotlib import pyplot
# import matplotlib.pyplot as plt


def normal_dist(data_frame):
    # Preallocate arrays
    sample_size = 1000
    sample_ave = []
    sample_stdev = []
    sample_random = []
# Interate through each row
    for i in range(len(data_frame)):
        ave = data_frame.loc[i, 'Nominal']
        std_dev = data_frame.loc[i, 'SD']
# Creating a normal distribution of each body
        sample = normal(ave, std_dev, sample_size)
# Choosing a random value within the normal distribution
        random_value = np.random.choice(sample)
# Plot
    # pyplot.hist(sample, bins=20)
    # pyplot.title('%d Samples'%sample_size)
    # pyplot.show()
# Collecting mean and sigma from sample
        sample_ave.append(st.mean(sample))
        sample_stdev.append(st.stdev(sample))
        sample_random.append(random_value)
    return [sample_ave, sample_stdev, sample_random]


def main():
    print('Running get_sample module directly')


if __name__ == '__main__':
    main()
