import os
import glob
import pandas as pd

os.chdir("/Users/Kishor_J/Downloads/EnergyUse/")
extension = 'csv'

all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

fout=open("TotalEnergyUse(15-12-2020To12-06-2021).csv","a")

for file in all_filenames:
    for line in open(file):
        fout.write(line)