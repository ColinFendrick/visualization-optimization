from numpy.random import seed, rand
from matplotlib import pyplot

from data.constants import inputs, r_min, r_max
from data.results import objective, optima_x, optima_y, results

seed(1)
sample = r_min + rand(10) * (r_max - r_min)
sample_eval = objective(sample)
pyplot.plot(inputs, results)
pyplot.axvline(x=optima_x, ls='--', color='r')
pyplot.plot(sample, sample_eval, 'o', color='b')
pyplot.show()
