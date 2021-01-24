from matplotlib import pyplot

from data.visuals import x, y, results

pyplot.contourf(x, y, results, levels=50, cmap='jet')
optima_x = [0.0, 0.0]
pyplot.plot([optima_x[0]], [optima_x[1]], '*', color='white')
pyplot.show()
