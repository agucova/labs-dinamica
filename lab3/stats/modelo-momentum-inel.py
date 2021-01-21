import pandas as pd
import numpy as np

datos = pd.read_csv("inel.csv")
experimentales = datos["Delta Energía (J)"]
psinf = datos["pdenergia3"]
pfinal = datos["pfinal"]

print(experimentales)
print(psinf)
print(pfinal)

corr_matrix = np.corrcoef(experimentales, psinf)
corr = corr_matrix[0, 1]
r_sq = corr ** 2
n = 6
k = 3
r_sqa = 1 - ((1 - r_sq) * (n - 1) / (n - k - 1))

print("*Modelo sin fricción*")
print("R^2:", r_sq)
print("R^2 ajustado: ", r_sqa)

corr_matrix = np.corrcoef(experimentales, pfinal)
corr = corr_matrix[0, 1]
r_sq = corr ** 2
n = 6
k = 4
r_sqa = 1 - ((1 - r_sq) * (n - 1) / (n - k - 1))

print("*Modelo con fricción*")
print("R^2:", r_sq)
print("R^2 ajustado: ", r_sqa)
