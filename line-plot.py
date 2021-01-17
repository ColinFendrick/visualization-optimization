from matplotlib import pyplot

from data.constants import inputs
from data.results import results, objective

pyplot.plot(inputs, results)
pyplot.show()
