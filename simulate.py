import pybullet_data
import time
import pybullet as p
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("box.sdf")
for x in range (1000):
	p.stepSimulation()
	time.sleep(1.0/60.0)
p.disconnect()