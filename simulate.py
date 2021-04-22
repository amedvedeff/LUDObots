from simulation import SIMULATION
import sys



direcotOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(direcotOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness(solutionID)
