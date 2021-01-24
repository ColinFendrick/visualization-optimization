from matplotlib import pyplot

from data.results import optima_x
from data.visuals import x, y, results

pyplot.contourf(x, y, results, levels=50, cmap='jet')
pyplot.plot([optima_x[0]], [optima_x[1]], '*', color='white')
pyplot.show()
