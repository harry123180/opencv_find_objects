import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.gca(projection='3d')
P0, P1, P2 = np.array([ [0, 0,0],
                        [-2, 4,-10],
                        [5, 3,0] ])
# define bezier curve
P = lambda t: (1 - t)**2 * P0 + 2 * t * (1 - t) * P1 + t**2 * P2
# evaluate the curve on [0, 1] sliced in 50 points
points = np.array([P(t) for t in np.linspace(0, 1, 50)])
# get x and y coordinates of points separately
x, y,z = points[:,0], points[:,1],points[:,2] # plot
ax.plot(x, y, z, color='gray', label='My Curve')
print(len(x))
#ax.scatter(P0, P1, P2, c=z, cmap='jet', label='My Points')
# 顯示圖例
ax.legend()
for i in range(10,0,-1):
    print(i)
plt.show()

