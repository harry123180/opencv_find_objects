import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create figure.
fig = plt.figure()
ax = fig.gca(projection = '3d')

# Generate example data.
R, Y = np.meshgrid(np.arange(0, 500, 0.5), np.arange(0, 40, 0.5))
z = 0.1 * np.abs(np.sin(R/40) * np.sin(Y/6))

# Plot the data.
surf = ax.plot_surface(R, Y, z, cmap=cm.jet, linewidth=0)
fig.colorbar(surf)

# Set viewpoint.
ax.azim = -160
ax.elev = 30

# Label axes.
ax.set_xlabel('Along track (m)')
ax.set_ylabel('Range (m)')
ax.set_zlabel('Height (m)')

# Save image.
#fig.savefig('data.png')
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

us = np.linspace(0, 2 * np.pi, 32)
zs = np.linspace(0, 10, 2)

us, zs = np.meshgrid(us, zs)

xs = 10 * np.cos(us)
ys = 10 * np.sin(us)
ax.plot_surface(xs, ys, zs, color='b')

plt.show()