from matplotlib import pyplot

from data.results import results
from data.constants import inputs

pyplot.scatter(inputs, results)
pyplot.show()
