import os

from AFPO import AFPO

afpo = AFPO()
afpo.Evolve()
afpo.Show_Best()

# for i in range(5):
#     os.system("python generate.py")
#     os.system("python simulate.py")