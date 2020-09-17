
import pandas
from pathlib import Path
import argparse
import json
from datetime import datetime
import typing as T
import matplotlib.pyplot as plt
import numpy as np

good_temp= []
bad_temp = []
filer = open('dataset.txt')
data = load_data('dataset.txt')
onestd = statistics.pstdev(data)


for k in data:
  if ((k - staticstics.mean(data))>=onestd*3):
    bad_temp.append(k)
  else:
    good_temp.append(k)
    
    
 
