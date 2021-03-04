import time
import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import numpy
import math
import random
import pathlib

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

numSteps = 1000

frontLeg_amplitude = numpy.pi / 10
frontLeg_frequency = 10
frontLeg_phaseOffset = numpy.pi

frontLeg_targetAgles = frontLeg_amplitude * numpy.sin(frontLeg_frequency * numpy.linspace(-numpy.pi, numpy.pi, numSteps) + frontLeg_phaseOffset)

backLeg_amplitude = numpy.pi / 4
backLeg_frequency = 10
backLeg_phaseOffset = 0

backLeg_targetAgles = backLeg_amplitude * numpy.sin(backLeg_frequency * numpy.linspace(-numpy.pi, numpy.pi, numSteps) + backLeg_phaseOffset)
#backLeg_targetAgles = numpy.sin(numpy.linspace(-numpy.pi, numpy.pi, 1000)) * numpy.pi / 4

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")
backLegSensorValues = numpy.zeros(numSteps)
frontLegSensorValues = numpy.zeros(numSteps)

numpy.save(r'C:\Users\Administrator\Documents\LUDObots\data\backLegAngleValues.npy', backLeg_targetAgles)
numpy.save(r'C:\Users\Administrator\Documents\LUDObots\data\frontLegAngleValues.npy', frontLeg_targetAgles)


for x in range (0, 1000):
	p.stepSimulation()
	backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	pyrosim.Set_Motor_For_Joint(
    	bodyIndex = robot,
    	jointName = "BackLeg_Torso",
    	controlMode = p.POSITION_CONTROL,
    	targetPosition = backLeg_targetAgles[x],
    	maxForce = 50)
	pyrosim.Set_Motor_For_Joint(
		bodyIndex = robot,
		jointName = "Torso_FrontLeg",
		controlMode = p.POSITION_CONTROL,
		targetPosition = frontLeg_targetAgles[x],
		maxForce = 50)
	time.sleep(1/60)
p.disconnect()


numpy.save(r'C:\Users\Administrator\Documents\LUDObots\data\backLegValues.npy', backLegSensorValues)
numpy.save(r'C:\Users\Administrator\Documents\LUDObots\data\frontLegValues.npy', frontLegSensorValues)
