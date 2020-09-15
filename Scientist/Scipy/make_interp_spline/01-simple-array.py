# Thanks to S.O question: https://es.stackoverflow.com/questions/388280/importerror-cannot-import-name-spline-from-scipy-interpolate/388289


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Create two numpy arrays:
x = np.array([1,2,3,4])
y = np.array([1,2,8,12])

# Smooth every one:
x_smooth = np.linspace(x.min(),x.max(),300)
y_smooth = make_interp_spline(x,y)(x_smooth)

# Plot x and y smoothed
plt.plot(x_smooth,y_smooth)

# Show graph
plt.show()
