# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:34:06 2021

@author: Mas
"""


from matplotlib import colors

def Laplace(grid,i,j):
    return (grid[i][j-1]+grid[i-1][j]+grid[i+1][j]+grid[i][j+1]-4*grid[i][j])/4 
def Laplace2(grid,i,j):
    return .2*grid[i][j-1]+.2*grid[i-1][j]+.2*grid[i+1][j]+.2*grid[i][j+1]+.05*grid[i+1][j+1]+.05*grid[i-1][j+1]+.05*grid[i-1][j-1]+.05*grid[i+1][j-1]-grid[i][j] 
def Laplace3(grid,i,j):
    return (1/8)*grid[i][j-1]+(1/8)*grid[i-1][j]+(1/8)*grid[i+1][j]+(1/8)*grid[i][j+1]+(1/8)*grid[i+1][j+1]+(1/8)*grid[i-1][j+1]+(1/8)*grid[i-1][j-1]+(1/8)*grid[i+1][j-1]-grid[i][j] 
def subtract(list1,list2):
    res = [list1[i]-list2[i] for i in  range(0,len(list1))]
    return res
        

cmap = colors.ListedColormap(['white','ivory','moccasin', 'khaki', 
                              'gold','goldenrod',
                              'orange', 'orangered', 'red','darkred'])

bounds = [i for i in range(0,9)]
#bounds = [-100,-50,-30,0,3,5,7,10,30,50,100]
norm = colors.BoundaryNorm(bounds, cmap.N)

"""
cmap = colors.ListedColormap(['black','white'])

bounds = [-1,0,1]
norm = colors.BoundaryNorm(bounds, cmap.N)




cmap = colors.ListedColormap(['blue','blue','blue', 'khaki', 
                              'gold','goldenrod',
                              'orange', 'black', 'black','black'])

bounds = [-100,-50,-30,0,3,5,7,10,30,50,100]





cmap = colors.ListedColormap(['white','ivory','moccasin', 'khaki', 
                              'gold','goldenrod',
                              'orange', 'orangered', 'red','darkred'])

bounds = [1+i/10 for i in range(0,9)]
norm = colors.BoundaryNorm(bounds, cmap.N)
"""