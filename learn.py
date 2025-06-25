# Mencari rata-rata umur dalam sebuah kelas
import pandas as pd
data = pd.read_csv('kapal_titanic.csv')
kelas = int(input())
jumKelas = data[data['pclass'] == kelas]
age = jumKelas['age'].mean()
print(age)
