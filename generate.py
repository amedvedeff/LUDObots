import pyrosim.pyrosim as pyrosim
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5
pyrosim.Start_SDF("boxes.sdf")
for r in range(10):
	currBox = "Box" + str(x)
	pyrosim.Send_Cube(name= currBox, pos=[x,y,z] , size=[length, width, height])
	z += 1
pyrosim.End()