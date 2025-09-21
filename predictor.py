#%%
# Core data + math
import pandas as pd
import numpy as np

# Machine learning
from sklearn.model_selection import train_test_split, TimeSeriesSplit, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Visualization
import matplotlib.pyplot as plt
#%%

#%%
df = pd.read_csv("epl_final.csv")
print(df.head())
#%%

#%%
print("Random Home Teams:")
print(df["HomeTeam"].sample(10))  # 10 random rows
#%%
