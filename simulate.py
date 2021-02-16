import time
import pybullet as p
physicsClient = p.connect(p.GUI)
p.setGravity(0,0,-9.8)
p.loadSDF("box.sdf")
for x in range (1000):
	p.stepSimulation()
	time.sleep(1.0/60.0)
p.disconnect()