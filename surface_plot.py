from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

from data.constants import x_axis, y_axis
from data.visuals import x, y, results

figure = pyplot.figure()
axis = figure.gca(projection='3d')
axis.plot_surface(x, y, results, cmap='jet')

pyplot.show()