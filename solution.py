import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time
class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = (numpy.random.rand(3,2) * 2) - 1
        self.myID = nextAvailableID

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        fitnessFloatValue = 0
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID))

        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)

        f = open("fitness" + str(self.myID) + ".txt")
        fitnessFloatValue = float(f.read())
        self.fitness = fitnessFloatValue
        f.close()

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        fitnessFloatValue = 0
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID))


    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)

        f = open("fitness" + str(self.myID) + ".txt")
        fitnessFloatValue = float(f.read())
        self.fitness = fitnessFloatValue
        f.close()

        os.system("rm fitness" + str(self.myID) + ".txt")

    def Create_World(self):
        length = 1.0
        width = 1.0
        height = 1.0
        x = -2
        y = 2
        z = 0.5
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("bo"
                           "dy.urdf")
        pyrosim.Send_Cube(name="BackLeg", pos=[0.5, 0, 0.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="BackLeg_Torso", parent="BackLeg", child="Torso", type="revolute", position="1.0 0 1.0")
        pyrosim.Send_Cube(name="Torso", pos=[0.5, 0, 0.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position="1.0 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        for currentRow in range(0, 3):
            for currentCol in range(0,2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentCol+3, weight=self.weights[currentRow][currentCol])

        pyrosim.End()

    def Mutate(self):
        randomRow =random.randint(0,2)
        randomColumn = random.randint(0,1)
        self.weights[randomRow][randomColumn] = random.random() * 2 - 1

