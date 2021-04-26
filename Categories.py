import numpy as np
import pandas as pd

## import datset
dataset = pd.read_csv("Batchelor_Degree_Categories.csv")

##sort the dataset by the number of courses in each category
print(dataset.sort_values("Courses"))



