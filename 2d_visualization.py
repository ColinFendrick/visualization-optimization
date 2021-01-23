from numpy import meshgrid

from data.results import objective
from data.constants import r_min, r_max, x_axis, y_axis

result = objective(4.0, 3.0)
print('f(%.3f, %.3f) = %.3f' % (4.0, 3.0, result))
print('\n')

x, y = meshgrid(x_axis, y_axis)

print(x[:5, :5])
print('\n')

results = objective(x, y)
print(results[:5, :5])
print('\n')

for i in range(5):
  print('f(%.3f, %.3f) = %.3f' % (x[i, 0], y[i, 0], results[i, 0]))
