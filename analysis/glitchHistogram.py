import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('evanstyle.mplstyle')
import numpy as np
import math

glitch_df = pd.read_pickle('glitches_df.p')
ratio = 254/1350
glitch_df['diameter'] = ratio*2*((glitch_df['area'].div(np.pi))**(1/2))
min_width = ratio*30
n = math.ceil((glitch_df['diameter'].max() - glitch_df['diameter'].min())/min_width)

hist = glitch_df.hist(column='diameter', bins = n, figsize = (12,8))
for ax in hist.flatten():
    ax.grid(False)
    ax.set_xlabel('Diameter of glitch (μm)')
    ax.set_ylabel('Number of glitches')
    ax.set_title('Diameter of distinct glitches')
print("Histogram!")
plt.show()
