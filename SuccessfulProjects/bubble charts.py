import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

N=6
province=['nim','Ontario','Quebec','BritishColumbia','Manitoba','NovaScoti']
size = [0,908.607,1356.547,922.509,552.329,651.036]
population = [0,12851821,7903001,4400057,1208268,4160000]
injuries = [0,625*3,752*3,629*3,1255*3,630*3]

# Choose some random colors
colors=['purple','red','blue','green', 'yellow','black']
#colors=cm.rainbow(np.random.rand(N))

# Use those colors as the color argument
plt.scatter(size,population,s=injuries,color=colors)
for i in range(N):
    plt.annotate(province[i],xy=(size[i],population[i]))
plt.xlabel('Size(*1000km2)')
plt.ylabel('Population(ten million)')

# Move title up with the "y" option
plt.title('The Car Accidents Injuries Rate in 5 Canada Provinces',y=1.05)
plt.show()
