
# Required packages.
import os
import pandas as pd


DATA_DIR = "C:/Users/BGhor/OneDrive/OU Vault/Fun_Projects/FARS/FARS2020National"
FOLDERS_ALL = os.listdir(DATA_DIR)
print(FOLDERS_ALL)

FILES = os.listdir(os.path.join(DATA_DIR, FOLDERS_ALL[0]))
print(FILES)
data = pd.read_csv(os.path.join(DATA_DIR, FOLDERS_ALL[0], FILES[1]))
print(data.head().to_string)
print(data.columns)
