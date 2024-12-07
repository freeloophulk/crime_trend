import os
import glob 
import pandas as pd
import matplotlib as plt
import numpy as np
os.chdir("/Users/alicexu/Desktop/HIT140 csv subfile/")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
combined_csv.to_csv("combine_xlsx.csv",index= False)

