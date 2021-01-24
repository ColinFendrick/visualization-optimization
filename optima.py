from matplotlib import pyplot

from data.constants import inputs
from data.results import optima_y, results

pyplot.scatter(inputs, results)
pyplot.plot([0.0], [optima_y], 's', color='r')
pyplot.axvline(x=0.0, ls='--', color='r')
pyplot.show()
