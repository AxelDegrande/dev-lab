import numpy as np


class PerlinNoise:
    def __init__(self, seed=None):
        rng = np.random.default_rng(seed)

        # Generate random gradients (+1 or -1)
        self.gradients = rng.choice([-1, 1], size=256)

    def fade(self, t):
        # Quintic smoothing function
        return 6*t**5 - 15*t**4 + 10*t**3

    def lerp(self, a, b, t):
        # Linear interpolation
        return a + t * (b - a)

    def noise(self, x):
        # Find integer grid points
        x0 = int(np.floor(x))
        x1 = x0 + 1

        # Position within the grid cell
        t = x - x0

        # Gradient values at grid points
        g0 = self.gradients[x0 % 256]
        g1 = self.gradients[x1 % 256]

        # Calculate dot products
        n0 = g0 * (x - x0)
        n1 = g1 * (x - x1)

        # Smooth interpolation
        u = self.fade(t)

        return self.lerp(n0, n1, u)