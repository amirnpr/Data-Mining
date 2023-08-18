import pandas as pd
from math import sqrt
import matplotlib.pyplot as plt

df = pd.read_excel("Sport-Dataset.xlsx", sheet_name=0)  # reading file

# x = input('Enter item1: ')
# y = input('Enter item2: ')
list1 = list(df['Relegated'])  # making list from columns
list2 = list(df['Twitter Followers'])

n = len(list1)
k2 = 0
sum_A = 0
sum_B = 0
mean_A = 0
mean_B = 0
deviation_A = 0
deviation_B = 0
inner_product = 0
Correlation = 0

for j in range(n):  # calculate mean
    mean_A += list1[j] / n
    mean_B += list2[j] / n

print("mean A = ", round(mean_A, 3), "\nmean B = ", round(mean_B, 3))
print("-------------------------------")

for i in range(n):  # calculate  Standard Deviation
    deviation_A += pow(list1[i] - mean_A, 2) / n
    deviation_B += pow(list2[i] - mean_B, 2) / n
deviation_A = sqrt(deviation_A)
deviation_B = sqrt(deviation_B)
print("Deviation A = ", round(deviation_A, 3), "\nDeviation B = ", round(deviation_B, 3))
print("-------------------------------")

for i in range(n):  # calculate Inner Product
    inner_product += list1[i] * list2[i]

print("inner product A&B = ", round(inner_product, 3))
print("-------------------------------")

Correlation = (inner_product - (n * mean_A * mean_B)) / ((n - 1) * deviation_A * deviation_B)
print("Correlation A&B = ", round(Correlation, 3))
print("-------------------------------")


Covariance = 0
E = 0
for i in range(n):
    E += list1[i] * list2[i] / n
Covariance = E - mean_A * mean_B
print("Covariance A&B = ", round(Covariance, 3))

Correlation_coefficient = Covariance / (deviation_A * deviation_B)
print("Correlation coefficient A&B = ", round(Correlation_coefficient, 3))

plt.scatter(list1, list2, c="blue")  # Scatter Plot
plt.xlabel("Relegated")
plt.ylabel("Twitter Followers")
plt.show()