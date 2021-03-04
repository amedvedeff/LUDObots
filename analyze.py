import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load(r'C:\Users\Administrator\Documents\LUDObots\data\backLegAngleValues.npy')
frontLegSensorValues = numpy.load(r'C:\Users\Administrator\Documents\LUDObots\data\frontLegAngleValues.npy')
line1 = matplotlib.pyplot.plot(backLegSensorValues,  label = 'Back leg')
line2 = matplotlib.pyplot.plot(frontLegSensorValues, label = 'Front leg')
matplotlib.pyplot.legend()

matplotlib.pyplot.show()