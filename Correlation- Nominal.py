import pandas as pd
import numpy as np
import scipy.stats

df = pd.read_excel("Sport-Dataset.xlsx", sheet_name=0)  # reading file

# x = input('Enter item1: ')
# y = input('Enter item2: ')
list1 = list(df['League'])  # making list from columns
list2 = list(df['International Matches'])


def count_list(a):  # counting the occurrences of all items in the lists
    d = {}
    for it in a:
        if it in d:
            d[it] += 1
        else:
            d[it] = 1
    return d


dict_list1 = count_list(list1)
dict_list2 = count_list(list2)
print("List1 Dictionary = ", count_list(list1), "\nList2 Dictionary = ", count_list(list2))
print("-------------------------------")

keys_list1 = list(dict_list1.keys())  # making list from keys(distinct items)
keys_list2 = list(dict_list2.keys())
print("keys_list1 = ", keys_list1, "\nkey_list2 = ", keys_list2)
print("-------------------------------")

values_list1 = list(dict_list1.values())  # making list from values(number of each distinct items)
values_list2 = list(dict_list2.values())
print("values_list1 = ", values_list1, "\nvalue_list2 = ", values_list2)
print("-------------------------------")

d_value1 = len(keys_list1)  # number of distinct items
d_value2 = len(keys_list2)
n = len(list1)  # number of tuples

row = keys_list1 + ['sum 1']  # for naming columns and rows
col = keys_list2 + ['sum 2']

contingency_table = [[0] * (d_value2 + 1) for i in range(d_value1 + 1)]  # making an empty Contingency_Table
contingency_table[-1][-1] = n

print("Contingency Table (1):", "\n", pd.DataFrame(np.array(contingency_table), columns=col, index=row))
print("-------------------------------")

for i in range(d_value1):  # update Contingency_Table with sum of items
    contingency_table[i][-1] = values_list1[i]
for i in range(d_value2):
    contingency_table[-1][i] = values_list2[i]
print("Contingency Table (2):", "\n", pd.DataFrame(np.array(contingency_table), columns=col, index=row))
print("-------------------------------")

for k in range(d_value1):  # count occurrences of each list1 x list2
    for j in range(d_value2):
        for i in range(n):
            if keys_list1[k] == list1[i] and keys_list2[j] == list2[i]:
                contingency_table[k][j] += 1  # update Contingency_Table with sum of each list 1 x list2
print("Contingency Table (3):", "\n", pd.DataFrame(np.array(contingency_table), columns=col, index=row))
print("-------------------------------")

expected_table = [[0] * d_value2 for i in range(d_value1)]  # making an empty Expected_Table
X2 = 0

for i in range(d_value1):  # find elements of Expected_Table  and calculate X2
    for j in range(d_value2):
        expected_table[i][j] = (contingency_table[-1][j] * contingency_table[i][-1]) / n
        X2 += (pow((expected_table[i][j] - contingency_table[i][j]), 2)) / expected_table[i][j]

print("Expected Table:", "\n", pd.DataFrame(np.array(expected_table), columns=keys_list2, index=keys_list1))
print("-------------------------------")

print("X2 =", X2)

critical_value = scipy.stats.chi2.ppf(1 - .05, df=(d_value1 - 1) * (d_value2 - 1))  # find Chi-Square critical value
print("Critical Value X2 = ", critical_value)
print("-------------------------------")
if X2 <= critical_value:
    print('Independent (H0 is accepted)')
else:
    print('Dependent (H1 is accepted)')
