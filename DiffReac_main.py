"""  
Simulate the coupled diffusion reaction system on a square

        u(t+1) = u(t) + d_u*Laplace u(t) + f*u(t)*v(t),
        v(t+1) = v(t) + d_v*Laplace u(t) + g*u(t)*v(t),

with 0 Dirichlet boundary conditions, leading to pattern formation.

"""
import matplotlib.pyplot as plt
import random as rnd
from functions import Laplace, Laplace2, Laplace3, cmap, bounds, norm


# Key parameters
d_u = .85
d_v = .85
g = .05
f = -.08
# COMMENTS;
# Diffusion at .8 more stable clear pattern+grid. At .9 it burns in the center
# u =.8, v=.9 a hot grid starts to appear for v. Swap this and it burns in some spots
# Using Laplace2 or Laplace3 only a trivial pattern appears! 


steps = 200 #time steps simulated
gs = 200 #gridsize
E = 10 #If this is less than 9 the is not stable pattern (same inital condition)

Grid_u = [[rnd.randint(0,E) for i in range(0,gs)]
        for i in range(0,int(gs))] 
Grid_v = [[rnd.randint(0,E) for i in range(0,gs)]
        for i in range(0,int(gs))] 
# Comments:
# Different white noise-like initial condiitons do not matter as long as E \ge 8 
# Deterministic initial condition 10 gives a funny result with singularities
# developping at the corners  (try combine with D1, D2 =  20,20).


System = {'u': Grid_u, 'v': Grid_v }

D1, D2 =  0,0
# This enforces a  Dirichlet boundary conditions D as the D's on 
# the boundary never change.
# D1, D2 =  -100, 100 looks like burning paper with 
# still pattern inside 
Grid_u_next = [[D1 for i in range(0,gs)]
        for i in range(0,gs)]
Grid_v_next = [[D2 for i in range(0,gs)]
        for i in range(0,gs)]



max_u, min_u, max_v, min_v = 5, 5, 5, 5

for s in range(0,steps):
        #print(Grid_next == Grid)
        fig, ax = plt.subplots(1,2)
        ax[0].imshow(System['u'])
        ax[0].set_title('u: t = ' + str(s+1))
        ax[1].imshow(System['v'])
        ax[1].set_title('v: t = ' + str(s+1))
        plt.show()
        for i in range(0,gs-1):
            for j in range(0,gs-1):
                Grid_u_next[i][j] = System['u'][i][j]+ d_u*Laplace(System['u'],i,j)+f*System['u'][i][j]*System['v'][i][j]
                Grid_v_next[i][j] = System['v'][i][j] + d_v*Laplace(System['v'],i,j) +g*System['v'][i][j]*System['u'][i][j]
        System['u'], Grid_u_next = Grid_u_next, System['u'] #swap lists
        System['v'], Grid_v_next = Grid_v_next, System['v']#swap lists
        """if s > int(steps/2):
            if max(max(System['u'], key=max)) > max_u:
                max_u = max(max(System['u'], key=max))
            if min(min(System['u'], key=min)) < min_u:
                min_u = min(min(System['u'], key=min))
            if max(max(System['v'], key=max)) > max_v:
                max_v = max(max(System['v'], key=max))
            if min(min(System['v'], key=min)) < min_v:
                min_v = min(min(System['v'], key=min))
print('Max and mins after ',int(steps/2),' steps:')         
print('(max_u, min_u)=',[max_u,min_u])
print('(max_v, min_v)=',[max_v,min_v]) """
plt.imshow([bounds], cmap=cmap, norm=norm)
plt.show()

 
        


   