import copy
from solution import SOLUTION
import constants as c
import os
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        # self.parent = SOLUTION()
        self.nextAvailableID = 0
        self.parents = {}
        for x in range(c.populationSize):
            self.parents[x] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        os.system("rm brain*.nndf")
        os.system("rm fitness*.nndf")

    def Evolve(self):
        # self.parent.Evaluate("DIRECT")
        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            if currentGeneration == 0:
                self.Evolve_For_One_Generation("GUI")
            else:
                self.Evolve_For_One_Generation("DIRECT")

        # for x in range (c.populationSize):
        #     print("\nThe parent fitness is " + str(self.parents[x].fitness) + " while the child fitness is " + str(self.children[x].fitness) + "\n")


    def Evolve_For_One_Generation(self, directOrGUI):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)

        self.Select()
        for x in range (c.populationSize):
            print("\nThe parent fitness is " + str(self.parents[x].fitness) + " while the child fitness is " + str(self.children[x].fitness) + "\n")

    def Spawn(self):
        self.children = {}
        for x in range (c.populationSize):
            self.children[x] = copy.deepcopy(self.parents[x])
            self.children[x].myID = self.nextAvailableID
            self.nextAvailableID += 1

    def Mutate(self):
        for x in range (c.populationSize):
            self.children[x].Mutate()

    def Select(self):
        for x in range (c.populationSize):
            if self.parents[x].fitness > self.children[x].fitness:
                self.parents[x] = self.children[x]

    def Show_Best(self):
        best = 0
        for x in range (c.populationSize):
            print("Fitness for parent " + str(x) + " is " + str(self.parents[x].fitness))

            if self.parents[best].fitness > self.parents[x].fitness:
                best = x
                print("Fitness for best changed and is now " + str(self.parents[best].fitness))

        input("Press Enter to continue...")
        self.parents[best].Start_Simulation("GUI")

        # self.parent = SOLUTION(self.nextAvailableID)
        #
        # for x in range (c.populationSize):
        #     if x == 0:
        #         self.parent.fitness = self.parents[x].fitness
        #         print("The parent fitness value is " + str(self.parent.fitness) + " while the fitness value for " + str(
        #             x) + " is " +
        #               str(self.parents[x].fitness))
        #
        #     if self.parent.fitness > self.parents[x].fitness:
        #         self.parent.fitness = self.parents[x].fitness
        #         print("The parent fitness value is " + str(self.parent.fitness) + " while the fitness value for " + str(x) + " is " +
        #             str(self.parents[x].fitness))
        #
        #
        # print("The parent fitness value is " + str(self.parent.fitness))
        # input("Press Enter to continue...")
        # self.parent.Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for x in range (c.populationSize):
            solutions[x].Start_Simulation("DIRECT")

        for x in range (c.populationSize):
            solutions[x].Wait_For_Simulation_To_End()
