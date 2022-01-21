'''This was added as a guide to working with MatplotLib.colors in order to later
convert the sine waveform into visible light. I intend to later use parameters
that will access colors via RGB'''


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize


class PiecewiseNorm(Normalize):
    def __init__(self, levels, clip=False):
        self.levels = np.sort(levels)
        self.normed = np.linspace(0, 1, len(levels))
        Normalize.__init__(self, None, None, clip)

    def __call__(self, value, clip=None):
        return np.ma.masked_array(np.interp(value, self.levels, self.normed))


x = np.linspace(-3, 3, 101)
y = np.linspace(-3, 3, 101)
xx, yy = np.meshgrid(x, y)

field = 500.0 * np.exp(-(xx**2 + yy**2) / 2.0)

levels = [0, 20, 40, 60, 80, 100, 200, 300, 400, 450, 500]

norm_levels = PiecewiseNorm(levels)

print(norm_levels.levels)
print(norm_levels.normed)
print(norm_levels(levels))

clim = [0, 500]

cmap = "jet"

plt.figure()

plt.subplot(2, 2, 1)
plt.contourf(xx, yy, field, cmap=cmap)
plt.title("Default Setting - no user control")
plt.colorbar()

plt.tight_layout()
plt.show()
