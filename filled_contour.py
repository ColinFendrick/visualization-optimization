from matplotlib import pyplot
from numpy.random import seed, rand

from data.constants import r_max, r_min, x_axis, y_axis
from data.results import optima_x
from data.visuals import x, y, results

seed(1)
sample_x = r_min + rand(10) * (r_max - r_min)
sample_y = r_min + rand(10) * (r_max - r_min)

pyplot.contourf(x, y, results, levels=50, cmap='jet')

pyplot.plot([optima_x[0]], [optima_x[1]], '*', color='white')
pyplot.plot(sample_x, sample_y, 'o', color='black')
pyplot.show()