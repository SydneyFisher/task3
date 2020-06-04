import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rc


def calculate(df, df_header):
    size, intensity, age = np.array([df["Size"]]), np.array([df["Intensity"]]), df_header.iat[1,0]
    size_avg, intensity_avg = np.average(size), np.average(intensity)
    return size_avg, intensity_avg, age

def main():
    size, intensity, age = [], [], []
    with os.scandir("imgdata/") as files:
        for entry in files:
            df = pd.read_csv(entry, header=3, index_col=0)
            df_header = pd.read_csv(entry, index_col=0, nrows=2, header=None)
            result = calculate(df, df_header)
            size.append(result[0])
            intensity.append(result[1])
            age.append(result[2])
    print(age)
    plot = sns.regplot(age, size, color="#78b6ed")
    plot.set(xlabel="Age", ylabel="Size")
    plt.show()

if __name__ == "__main__":
    main()

