from simulation import SIMULATION
import sys



direcotOrGUI = sys.argv[1]
simulation = SIMULATION(direcotOrGUI)
simulation.Run()
simulation.Get_Fitness()
