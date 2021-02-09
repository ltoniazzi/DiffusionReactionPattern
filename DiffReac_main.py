# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 23:10:41 2021

@author: Mas
"""
import numpy as np
import matplotlib.pyplot as plt
import random as rnd
from matplotlib import colors
from functions import Laplace

# create discrete colormap
"""cmap = colors.ListedColormap(['white','ivory','moccasin', 'khaki', 
                              'gold','goldenrod',
                              'orange', 'orangered', 'red','darkred'])
"""
cmap = colors.ListedColormap(['blue','blue','khaki', 'khaki', 
                              'gold','goldenrod',
                              'orange', 'red', 'black','black'])

bounds = [i for i in range(0,9)]
#bounds = [-100,-50,-30,0,3,5,7,10,30,50,100]
norm = colors.BoundaryNorm(bounds, cmap.N)

#diffusion at 4.2/5 less stable but still pattern 
d_u = 4/5
d_v = 4/5
g = .05
f = -.08

steps = 100
gridsize1 = 100
gridsize2 = 100
gridsize = gridsize1 + gridsize2
E = 10 #If this is less than 9 the is not stable pattern (same inital condition)

Grid1 = [[rnd.randint(0,E) for i in range(0,gridsize)]
        for i in range(0,int(gridsize1))]
for i in range(0,int(gridsize2)):
    Grid1.append([rnd.randint(0,E) for j in range(0,gridsize)]) 
 
Grid2 = [[rnd.randint(0,E) for i in range(0,gridsize)]
        for i in range(0,int(gridsize1))]
for i in range(0,int(gridsize2)):
    Grid2.append([rnd.randint(0,E) for j in range(0,gridsize)]) 
# Different initial condiitons do not matter much? (Same E)

System = {'u': Grid1, 'v': Grid2 }

Grid_next1 = [[0 for i in range(0,gridsize)]
        for i in range(0,gridsize)]
Grid_next2 = [[0 for i in range(0,gridsize)]
        for i in range(0,gridsize)]

for s in range(0,steps):
        #print(Grid_next == Grid)
        fig, ax = plt.subplots(1,2)
        ax[0].imshow(System['u'], cmap=cmap, norm=norm)
        ax[0].set_title('u: t = ' + str(s+1))
        ax[1].imshow(System['v'], cmap=cmap, norm=norm)
        ax[1].set_title('v: t = ' + str(s+1))
        plt.show()
        for i in range(0,gridsize-1):
            for j in range(0,gridsize-1):
                Grid_next1[i][j] = System['u'][i][j]+ d_u*Laplace(System['u'],i,j)+f*System['u'][i][j]*System['v'][i][j]
                Grid_next2[i][j] = System['v'][i][j] + d_v*Laplace(System['v'],i,j) +g*System['v'][i][j]*System['u'][i][j]
        System['u'], Grid_next1 = Grid_next1, System['u'] #swap lists
        System['v'], Grid_next2 = Grid_next2, System['v'] #swap lists
 
        
""" #Discrete: u(t+1) = u(t) + d_a Delta u(t) + u(t)(c -f v(x))
    #PDE:    u_t = d_a Delta u(t) + 
  
   
    """

   