import numpy

numSteps = 1000
frontLegAmplitude = numpy.pi / 10
frontLegFrequency = 10
frontLegPhaseOffset = numpy.pi
backLegAmplitude = numpy.pi / 4
backLegFrequency = 10
backLegPhaseOffset = 0

forceAmount = 50
sleepAmount = 1/60

numberOfGenerations = 1
populationSize = 10
numberOfIndividualsAddedEachGeneration = 1

numSensorNeurons = 8
numMotorNeurons = 4

motorJointRange = 0.2