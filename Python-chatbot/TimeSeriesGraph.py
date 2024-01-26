import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv 
import random
from itertools import count

with open('TimeSeries.csv') as File:
    Line_reader = csv.reader(File)


x_vals = [10,12,14,16,18,20,22,24]
y_vals = [5,10,30,25,35,15,20,40]

plt.plot(x_vals, y_vals)

plt.plot(x_vals,y_vals)
plt.yticks(y_vals)
plt.xticks(x_vals)

#create the plot 
plt.plot( linestyle =  'dotted')

# add title and axis label
plt.title('Time Series plot')
plt.xlabel('2 hour intervals')
plt.ylabel('Number of interactions')

plt.tight_layout()
plt.show()