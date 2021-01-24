from numpy import meshgrid

from .results import objective
from .constants import r_min, r_max, x_axis, y_axis

result = objective(4.0, 3.0)

x, y = meshgrid(x_axis, y_axis)

results = objective(x, y)

