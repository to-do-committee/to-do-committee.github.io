import numpy as np
import matplotlib.pyplot as plt


def make_plots(results1, results2, xlabels, cat1, cat2, output_file_name): 
    X = np.arange(len(results1))
    fig = plt.figure(dpi=100)
    ax = fig.add_subplot(111)
    ax.bar(X, results1, color = 'black', width = 0.25,label=cat1 ) 
    ax.bar(X + 0.25, results2, color = 'orangered', width = 0.25,label=cat2)
    ax.set_facecolor("silver")

    xticks = [x+0.25 if results1[i]==0 else x if results2[i]==0 else x+0.125 for i, x in enumerate(X)] # checks whether any of the values is zero to center x-ticks under bar(s)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels,rotation=45, ha='right', rotation_mode='anchor')
    ax.tick_params(axis='x', colors='grey') 
    ax.spines['bottom'].set_color('grey') 

    yticks = np.arange(0,max(results1+results2)+5,5)
    ax.set_yticks(yticks)
    ax.tick_params(axis='y', colors='grey')  #setting up Y-axis tick color to black
    ax.spines['left'].set_color('grey')        # setting up Y-axis tick color to grey

    plt.legend(prop={'size': 9})
    plt.tight_layout() # make labels fit on figure

    plt.rcParams['axes.facecolor']='silver'
    plt.rcParams['savefig.facecolor']='#171819' # matching fig backgroudn with website colour 
    plt.savefig(f'{output_file_name}.png', dpi=500, transparent=False)

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

# week 2
# X = np.arange(5)
# fig = plt.figure(dpi=100)
# # ax = fig.add_axes([0,0,1,1])
# ax = fig.add_subplot(111)
# ax.bar(X, [14,12,24,21,17], color = 'black', width = 0.25,label='Will probably stay the same' ) # ,tick_label=['Vegan', 'Between Vegan and Vegetarian', 'Vegetarian', 'Flexiterian', 'Omnivore']
# ax.bar(X + 0.25, [1,2,4,7,0], color = 'orangered', width = 0.25,label='Will probably change next year')
# ax.set_facecolor("silver")
# ax.set_xticks(X)
# ax.set_xticklabels(['Vegan', 'Between Vegan & Vegetarian', 'Vegetarian', 'Flexitarian', 'Omnivore'],rotation=15, ha='right', rotation_mode='anchor')
# ax.tick_params(axis='x', colors='grey') 
# ax.spines['bottom'].set_color('grey') 

# ax.set_yticks([0,5,10,15,20, 25])
# ax.tick_params(axis='y', colors='grey')  #setting up Y-axis tick color to black
# ax.spines['left'].set_color('grey')        # setting up Y-axis tick color to grey

# plt.legend(prop={'size': 9})
# plt.tight_layout() # make labels fit on figure

# plt.rcParams['axes.facecolor']='silver'
# plt.rcParams['savefig.facecolor']='#171819'
# plt.savefig('results_week2.png', dpi=500, transparent=False)

# week 4

# X = np.arange(5)
# fig = plt.figure(dpi=100)
# # ax = fig.add_axes([0,0,1,1])
# ax = fig.add_subplot(111)
# ax.bar(X, [30,4,31,2,0], color = 'black', width = 0.25,label='Travel time <30min' ) # ,tick_label=['Vegan', 'Between Vegan and Vegetarian', 'Vegetarian', 'Flexiterian', 'Omnivore']
# ax.bar(X + 0.25, [0,0,0,9,4], color = 'orangered', width = 0.25,label='Travel time >30min')
# ax.set_facecolor("silver")
# ax.set_xticks(X)
# ax.set_xticklabels(['Walking', 'Cycling/Walking', 'The Dutch way (cycling)', "Public transport", 'Other'],rotation=45, ha='right', rotation_mode='anchor')
# ax.tick_params(axis='x', colors='grey') 
# ax.spines['bottom'].set_color('grey') 

# ax.set_yticks([0,5,10,15,20, 25])
# ax.tick_params(axis='y', colors='grey')  #setting up Y-axis tick color to black
# ax.spines['left'].set_color('grey')        # setting up Y-axis tick color to grey

# plt.legend(prop={'size': 9})
# plt.tight_layout() # make labels fit on figure

# plt.rcParams['axes.facecolor']='silver'
# plt.rcParams['savefig.facecolor']='#171819'
# plt.savefig('results_week4.png', dpi=500, transparent=False)

# week 5
# make_plots(results1=[29,5,35,4,9], results2=[12,0,14,17,8], xlabels=['Home Office', 'Both', 'Beurs', 'Tresoar', 'Dbieb'], 
#     cat1='Basically always there', cat2='Only there when shit hits the fan', output_file_name='results_week5')

# week 6 

make_plots(results1=[0,3,8,19,13], results2=[1,5,13,25,14], xlabels=['I hate it', 'I dislike it', 'Neutral', 'I like it', 'I love it'], 
    cat1='Mostly live in places <100k inhabitants', cat2='Mostly live in places >100k inhabitants', output_file_name='results_week6')

# week 7 

make_plots(results1=[3,3,0,3,50], results2=[66,27,16,3,5], xlabels=['Non-existent', 'Basic', 'Conversational', 'Proficient', 'Fluent'], 
    cat1="I'm Dutch", cat2="I'm not Dutch", output_file_name='results_week7')

# week 8

make_plots(results1=[6,27,17,33,6, 0], results2=[2,41,7,24,6,3], xlabels=['Asexual', 'Straight', 'Gay/Lesbian', 'Multisexual', 'Queer', 'Not listed here'], 
    cat1="Single and (not) ready to mingle", cat2="Seeing someone/in a relationship", output_file_name='results_week8')
