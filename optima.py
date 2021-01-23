from matplotlib import pyplot

from data.constants import inputs
from data.results import optima_x, optima_y, results

pyplot.scatter(inputs, results)
pyplot.plot([optima_x], [optima_y], 's', color='r')
pyplot.axvline(x=optima_x, ls='--', color='r')
pyplot.show()
