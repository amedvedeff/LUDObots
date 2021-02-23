import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load(r'C:\Users\Administrator\Documents\LUDObots\data\backLegValues.npy')
frontLegSensorValues = numpy.load(r'C:\Users\Administrator\Documents\LUDObots\data\frontLegValues.npy')
line1 = matplotlib.pyplot.plot(backLegSensorValues, linewidth=3, label = 'Back leg')
line2 = matplotlib.pyplot.plot(frontLegSensorValues, label = 'Front leg')
matplotlib.pyplot.legend()

matplotlib.pyplot.show()