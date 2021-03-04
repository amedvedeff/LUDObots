import time
import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import numpy
import constants as c
import math
import random
import pathlib

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# numSteps = 1000
#
# frontLeg_amplitude = numpy.pi / 10
# frontLeg_frequency = 10
# frontLeg_phaseOffset = numpy.pi

frontLegTargetAngles = c.frontLegAmplitude * numpy.sin(c.frontLegFrequency * numpy.linspace(-numpy.pi, numpy.pi,
																						   c.numSteps) +
													  									c.frontLegPhaseOffset)

# backLeg_amplitude = numpy.pi / 4
# backLeg_frequency = 10
# backLeg_phaseOffset = 0

backLegTargetAngles = c.backLegAmplitude * numpy.sin(c.backLegFrequency * numpy.linspace(-numpy.pi, numpy.pi,
																						 c.numSteps) +
													 									c.backLegPhaseOffset)
#backLeg_targetAgles = numpy.sin(numpy.linspace(-numpy.pi, numpy.pi, 1000)) * numpy.pi / 4

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")
backLegSensorValues = numpy.zeros(c.numSteps)
frontLegSensorValues = numpy.zeros(c.numSteps)

numpy.save(r'C:\Users\Administrator\Documents\LUDObots\data\backLegAngleValues.npy', backLegTargetAngles)
numpy.save(r'C:\Users\Administrator\Documents\LUDObots\data\frontLegAngleValues.npy', frontLegTargetAngles)


for x in range (0, c.numSteps):
	p.stepSimulation()
	backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	pyrosim.Set_Motor_For_Joint(
    	bodyIndex = robot,
    	jointName = "BackLeg_Torso",
    	controlMode = p.POSITION_CONTROL,
    	targetPosition = backLegTargetAngles[x],
    	maxForce = c.forceAmount)
	pyrosim.Set_Motor_For_Joint(
		bodyIndex = robot,
		jointName = "Torso_FrontLeg",
		controlMode = p.POSITION_CONTROL,
		targetPosition = frontLegTargetAngles[x],
		maxForce = c.forceAmount)
	time.sleep(1/60)
p.disconnect()


numpy.save(r'C:\Users\Administrator\Documents\LUDObots\data\backLegValues.npy', backLegSensorValues)
numpy.save(r'C:\Users\Administrator\Documents\LUDObots\data\frontLegValues.npy', frontLegSensorValues)
