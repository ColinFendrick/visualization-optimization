from numpy import meshgrid
from matplotlib import pyplot

from data.results import objective
from data.constants import r_min, r_max, x_axis, y_axis
from data.visuals import result, results, x, y

print('f(%.3f, %.3f) = %.3f' % (4.0, 3.0, result))
print('\n')

print(x[:5, :5])
print('\n')

print(results[:5, :5])
print('\n')

for i in range(5):
  print('f(%.3f, %.3f) = %.3f' % (x[i, 0], y[i, 0], results[i, 0]))

pyplot.contour(x, y, results, 50, alpha=1.0, cmap='jet')
pyplot.show()
