import numpy as np
import matplotlib.pyplot as plt

# X = np.arange(5)
# fig = plt.figure(dpi=100)
# ax = fig.add_axes([0,0,1,1])
# ax.bar(X, [59,40,4,0,7], color = 'black', width = 0.25,label='hope to stick around' ,tick_label=['< 1 year', '< 2 year', '< 3 year', '< 4 year', 'basically furniture'])
# ax.bar(X + 0.25, [9,7,0,3,3], color = 'orangered', width = 0.25,label='cannot wait to leave')
# ax.set_facecolor("silver")
# ax.tick_params(axis='x', colors='grey')    #setting up X-axis tick color to red
# ax.tick_params(axis='y', colors='grey')  #setting up Y-axis tick color to black

# ax.spines['left'].set_color('grey')        # setting up Y-axis tick color to red
# ax.spines['bottom'].set_color('grey') 
# plt.legend()
# plt.show()
# plt.savefig('results_week1.png', dpi=500)


X = np.arange(5)
fig = plt.figure(dpi=100)
# ax = fig.add_axes([0,0,1,1])
ax = fig.add_subplot(111)
ax.bar(X, [14,12,24,21,17], color = 'black', width = 0.25,label='Will probably stay the same' ) # ,tick_label=['Vegan', 'Between Vegan and Vegetarian', 'Vegetarian', 'Flexiterian', 'Omnivore']
ax.bar(X + 0.25, [1,2,4,7,0], color = 'orangered', width = 0.25,label='Will probably change next year')
ax.set_facecolor("silver")
ax.set_xticks(X)
ax.set_xticklabels(['Vegan', 'Between Vegan & Vegetarian', 'Vegetarian', 'Flexitarian', 'Omnivore'],rotation=15, ha='right', rotation_mode='anchor')
ax.tick_params(axis='x', colors='grey') 
ax.spines['bottom'].set_color('grey') 

ax.set_yticks([0,5,10,15,20, 25])
ax.tick_params(axis='y', colors='grey')  #setting up Y-axis tick color to black
ax.spines['left'].set_color('grey')        # setting up Y-axis tick color to red

plt.legend(prop={'size': 9})
plt.tight_layout() # make labels fit on page 
# plt.show()
plt.rcParams['axes.facecolor']='silver'
plt.rcParams['savefig.facecolor']='#171819'
plt.savefig('results_week2.png', dpi=500, transparent=False)
