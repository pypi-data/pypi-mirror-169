import imp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


def plot_regression(dep_var, pred_var):

    plt.figure(figsize=[20, 10], facecolor='lightsteelblue')

    plt.subplot(2, 2, 1)
    ax1 = sn.regplot(x=pred_var, y=dep_var)
    plt.title('Regression IC 95%')

    plt.subplot(2, 2, 2)
    ax2 = sn.residplot(x=pred_var,y= dep_var)
    plt.title('Plot Residuals')

    return ax1, ax2
