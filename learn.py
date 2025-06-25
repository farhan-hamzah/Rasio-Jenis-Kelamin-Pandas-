#Menentukan penumpang yang selamat
import pandas as pd
data = pd.read_csv('kapal_titanic.csv')
selamat = (data['survived'] == 1).sum()
tidakSelamat = (data['survived'] == 0).sum()
print(selamat)


