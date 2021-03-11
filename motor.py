import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c
import pathlib

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.motorValues = numpy.zeros(c.numSteps)
        self.values = numpy.linspace(-numpy.pi, numpy.pi, c.numSteps)
        self.frequency = c.backLegFrequency
        self.amplitude = c.backLegAmplitude
        self.offset = c.backLegPhaseOffset

        if self.jointName == "Torso_FrontLeg":
            self.frequency *= 2

        for i in range(c.numSteps):
            self.motorValues[i] = (self.amplitude * numpy.sin(self.frequency * self.values[i] + self.offset))

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[t],
            maxForce = c.forceAmount)

    def Save_Values(self):
        numpy.save(r'C:\Users\Administrator\Documents\LUDObots\data\motorValues.npy', self.motorValues)