import pyrosim.pyrosim as pyrosim
length = 1.0
width = 1.0
height = 1.0
x = 0
y = 0
z = 0.5
pyrosim.Start_SDF("boxes.sdf")
pyrosim.Send_Cube(name= "Box", pos=[x,y,z] , size=[length, width, height])
pyrosim.End()