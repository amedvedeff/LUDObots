import time
import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import numpy
import pathlib

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
bodyId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")
backLegSensorValues = numpy.zeros(1000)

for x in range(0, 1000):
	p.stepSimulation()
	backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	time.sleep(1/60)
p.disconnect()

print(backLegSensorValues)

numpy.save(r'C:\Users\Administrator\Documents\LUDObots\data\backLegValues.npy', backLegSensorValues)