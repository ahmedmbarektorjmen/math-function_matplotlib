from matplotlib.pyplot import *
from numpy import *

# Unit vectors i and j
vecteurs = array([[100, 0],[0, 100],[-100, 0],[0, -100]])
origin = array([[0, 0],[0, 0],[0, 0],[0, 0]]) # origin point for vectors i and j
scatter(0, 0,color="black") # origin point

quiver(origin[:,0], origin[:,1], vecteurs[:,0], vecteurs[:,1], color=["black"], scale=21)


# points for a parabole in + :
for x in range (-100,100) :
    if (x != 0)  :
        scatter(x, ((50 * (x ** 2)) + 23),color="cyan")
        print(f"epochs : {x+101}/200")

savefig("parabole.png")

show()