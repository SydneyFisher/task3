import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rc




def get_data():
    """Collect the data from files in the imgdata directory."""

    size, intensity, age = [], [], []
    def calculate(data, data_top):
        """Return age and the averages of size and intensity."""
        size, intensity, age = np.array([data["Size"]]), np.array([data["Intensity"]]), data_top.iat[1,0]
        size_avg, intensity_avg = np.average(size), np.average(intensity)
        return size_avg, intensity_avg, age
   
    with os.scandir("imgdata/") as files:
        for entry in files:
            data = pd.read_csv(entry, header=3, index_col=0)
            data_top = pd.read_csv(entry, index_col=0, nrows=2, header=None)
            result = calculate(data, data_top)
            size.append(result[0])
            intensity.append(result[1])
            age.append(result[2])
    return size, intensity, age
    
if __name__ == "__main__":
    size, intensity, age = get_data()
    sns.set()
    plt.rc('font', size=14)
    #plt.rc('figure', dpi=200)
    fig, ax = plt.subplots(1,2)
    p1 = sns.regplot(age, size, ax=ax[0])
    p2 = sns.regplot(age, intensity, ax=ax[1])
    p1.set(xlabel='Age', ylabel='Size')
    p2.set(xlabel='Age', ylabel='Intensity')
    plt.show()

