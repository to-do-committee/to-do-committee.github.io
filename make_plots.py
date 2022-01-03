import numpy as np
import matplotlib.pyplot as plt

X = np.arange(5)
fig = plt.figure(dpi=100)
ax = fig.add_axes([0,0,1,1])
ax.bar(X, [59,40,4,0,7], color = 'black', width = 0.25,label='hope to stick around' ,tick_label=['< 1 year', '< 2 year', '< 3 year', '< 4 year', 'basically furniture'])
ax.bar(X + 0.25, [9,7,0,3,3], color = 'orangered', width = 0.25,label='cannot wait to leave')
ax.set_facecolor("silver")
ax.tick_params(axis='x', colors='grey')    #setting up X-axis tick color to red
ax.tick_params(axis='y', colors='grey')  #setting up Y-axis tick color to black

ax.spines['left'].set_color('grey')        # setting up Y-axis tick color to red
ax.spines['bottom'].set_color('grey') 
plt.legend()
plt.savefig('results_week1.png', dpi=500)