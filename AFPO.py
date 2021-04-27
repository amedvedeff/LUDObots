import copy
from solution import SOLUTION
import constants as c
import os
import random
class AFPO:
    def __init__(self):
        self.nextAvailableID = 0
        self.population = {}
        for x in range(c.populationSize):
            self.population[x] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        os.system("rm tmp*.txt")

    def Expand_Population_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Add_Random_Individuals_To_Population()

        # input("Press Enter to continue...")

    def Contract_Population_For_One_Generation(self):
        # compare two individuals randomly
        while len(self.population) != c.populationSize:
            randNum1 = random.randint(0, (len(self.population) - 3))
            randNum2 = random.randint(0, (len(self.population) - 3))

            if(self.isYounger(randNum1, randNum2) and self.isFitter(randNum1, randNum2)):
                del self.population[randNum2]
                self.Population_Reorder(randNum2)
                print("Element number " + str(randNum2) + " was removed. There are now " + str(len(self.population)) + " elements remaining.")
                self.Show_Population()
                input("Press Enter to continue...")
            if (self.isYounger(randNum2, randNum1) and self.isFitter(randNum2, randNum1)):
                del self.population[randNum1]
                self.Population_Reorder(randNum1)
                print("Element number " + str(randNum1) + " was removed. There are now " + str(len(self.population)) + " elements remaining.")
                self.Show_Population()
                input("Press Enter to continue...")

    def Evolve(self):
        for currentGeneration in range(c.numberOfGenerations):
            self.Expand_Population_For_One_Generation()
            self.Evaluate(self.population)

            input("Beginning contraction!!! Press Enter to continue...")
            self.Show_Population()
            input("Press Enter to continue...")

            self.Contract_Population_For_One_Generation()
            print("There are " + str(len(self.population)) + "elements remaining in population!")
            input("Beginning incrementation of age!!! Press Enter to continue...")
            self.Increment_Age_Of_Population()
            print("End of one generation!")


    def Evolve_For_One_Generation(self, directOrGUI):
        pass
        # self.Spawn()
        # self.Mutate()
        # self.Evaluate(self.children)
        #
        # self.Select()
        # for x in range (c.populationSize):
        #     print("\nThe parent fitness is " + str(self.population[x].fitness) + " while the child fitness is " + str(self.children[x].fitness) + "\n")

    def Spawn(self):
        for x in range (c.populationSize):
            self.population[c.populationSize + x] = copy.deepcopy(self.population[x])
            self.population[c.populationSize + x].myID = self.nextAvailableID
            self.nextAvailableID += 1

    def Mutate(self):
        for x in range (c.populationSize):
            self.population[c.populationSize + x].Mutate()

    def Select(self):
        pass
        # for x in range (c.populationSize):
        #     if self.population[x].fitness > self.children[x].fitness:
        #         self.population[x] = self.children[x]

    def Show_Best(self):
        best = 0
        for x in range (c.populationSize):
            print("Fitness for parent " + str(x) + " is " + str(self.population[x].fitness))

            if self.population[best].fitness > self.population[x].fitness:
                best = x
                print("Fitness for best changed and is now " + str(self.population[best].fitness))

        input("Press Enter to continue...")
        self.population[best].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for x in range (len(self.population)):
            solutions[x].Start_Simulation("DIRECT")

        for x in range (len(self.population)):
            solutions[x].Wait_For_Simulation_To_End()



    def isYounger(self, solution1, solution2):
        if self.population[solution1].myAge > self.population[solution2].myAge:
            return False
        if self.population[solution1].myAge <= self.population[solution2].myAge:
            return True


    def isFitter(self, solution1, solution2):
        if self.population[solution1].fitness >= self.population[solution2].fitness:
            return False
        if self.population[solution1].fitness < self.population[solution2].fitness:
            return True

    def Increment_Age_Of_Population(self):
        for x in range(len(self.population)):
            self.population[x].myAge += 1

    def Add_Random_Individuals_To_Population(self):
        for x in range (c.numberOfIndividualsAddedEachGeneration):
            self.population[(2 * c.populationSize) + x] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Population_Reorder(self, randNum):
        if randNum == len(self.population):
            randNum = randNum
        else:
            while randNum < len(self.population) - 1:
                self.population[randNum] = self.population[randNum+1]
                randNum += 1

            del self.population[randNum]

    def Show_Population(self):
        for x in range(len(self.population)):
            print("The fitness of the element at " + str(x) + " is " + str(self.population[x].fitness) + ". There are " + str(len(self.population)) + "remaining.")