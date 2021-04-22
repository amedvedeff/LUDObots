from world import WORLD
from robot import ROBOT

import time
import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import numpy
import constants as c
import math
import random
import pathlib



class SIMULATION:

    def __init__(self, directOrGUI, solutionID):
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        elif directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)

        self.directOrGUI = directOrGUI
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def Run(self):
        backLegSensorValues = numpy.zeros(c.numSteps)
        frontLegSensorValues = numpy.zeros(c.numSteps)
        frontLegTargetAngles = c.frontLegAmplitude * numpy.sin(c.frontLegFrequency * numpy.linspace(-numpy.pi, numpy.pi,
        																						   c.numSteps) +
        													  									c.frontLegPhaseOffset)

        backLegTargetAngles = c.backLegAmplitude * numpy.sin(c.backLegFrequency * numpy.linspace(-numpy.pi, numpy.pi,
        																						 c.numSteps) +
        												 									c.backLegPhaseOffset)

        for x in range (0, c.numSteps):
            p.stepSimulation()
            self.robot.Sense(x)
            self.robot.Think()
            self.robot.Act(x)
            if self.directOrGUI == "GUI":
                time.sleep(c.sleepAmount)

    def Get_Fitness(self, solutionID):
        self.robot.Get_Fitness(solutionID)

    def __del__(self):
        p.disconnect()
