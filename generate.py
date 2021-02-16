import pyrosim.pyrosim as pyrosim
length = 1.0
width = 1.0
height = 1.0
x = 0
y = 0
z = 0.5
pyrosim.Start_SDF("boxes.sdf")
for p in range(6):
	for q in range (6):
		for r in range(10):
			currBox = "Box" + str(q) + str(q) + str(r)
			pyrosim.Send_Cube(name= currBox, pos=[x,y,z] , size=[length, width, height])
			z += (0.9 * height + height) / 2.0
			length *= 0.9
			width *= 0.9
			height *= 0.9
		length = 1.0
		width = 1.0
		height = 1.0
		z = 0.5
		y += width
	length = 1.0
	width = 1.0
	height = 1.0
	y = 0
	x += length
pyrosim.End()