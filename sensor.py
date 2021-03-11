import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
import pathlib

class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.numSteps)


    def Get_Value(self, x):
        self.values[x] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Value (self):
        numpy.save(r'C:\Users\Administrator\Documents\LUDObots\data\sensorValues.npy', self.values)