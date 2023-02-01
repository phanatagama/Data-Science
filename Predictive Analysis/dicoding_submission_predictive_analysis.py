# -*- coding: utf-8 -*-
"""dicoding-submission Predictive Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pNYsBLYAta1DX7_AtcbFHNyk4P_D3bHi

# **Saham ACE Predictive Analytics**

Download dataset from kaggle
"""

!pip install kaggle
from google.colab import files
files.upload()
!mkdir ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d muamkh/ihsgstockdata
!unzip ihsgstockdata.zip

"""**Import required library**"""

# Commented out IPython magic to ensure Python compatibility.
import seaborn as sns 
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
# %matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('/content/daily/ACES.csv')
df['timestamp'] = pd.to_datetime(df['timestamp']) 
df = df.set_index('timestamp')
print(f"Jumlah Baris = {df.shape[0]}")
df.head()

plt.figure(figsize=(15,5))
sns.set_style('darkgrid')
plt.plot(df.index, df['close'])
plt.title("Harga Saham\nPT. ACE Hardware Indonesia", fontsize=25)
plt.show()

"""## Exploratory Data Analysis
**Deskripsi Variabel**
* Timestamp : Tanggal pencatatan data
* Open : harga ketika dibuka yang dihitung perhari
* Close : harga ketika ditutup yang dihitung perhari
* Low : harga terendah perhari
* High : harga tertinggi perhari
* Volume : volume transaksi perhari
"""

df.info()

"""Fungsi describe() memberikan informasi statistik pada masing-masing kolom, antara lain:

*   Count  adalah jumlah sampel pada data.
*   Mean adalah nilai rata-rata.
*   Std adalah standar deviasi.
*   Min yaitu nilai minimum setiap kolom. 
*   25% adalah kuartil pertama. Kuartil adalah nilai yang menandai batas interval dalam empat bagian sebaran yang sama. 
*   50% adalah kuartil kedua, atau biasa juga disebut median (nilai tengah).
*   75% adalah kuartil ketiga.
*   Max adalah nilai maksimum.
"""

df.drop(['volume'],axis=1,inplace=True)
df.describe()

df.isnull().sum()

"""Dari hasil analisa diatas, tidak terdapat Missing Value pada setiap variabel"""

plt.subplots(figsize=(10,7))
sns.boxplot(data=df).set_title("ACE")
plt.show()

"""Jika dilihat dari plot diatas tidak terdapat Outlier pada setiap variabel yang dipilih

### Univariate Analysis

Karena tidak terdapat Categorical Features, maka kita dapat langsung menganalisis Numerical Features pada dataset dengan menampilkan plot dan grafik histogramnya
"""

df.hist(bins=50, figsize=(20,15))
plt.show()

"""Dari hasil histogram diatas dapat disimpulkan bahwasannya hampir semua variabel Distribusi nilainya miring ke kanan (right-skewed). Hal ini akan berimplikasi pada model nantinya.

### Multivariate Analysis
"""

sns.pairplot(df, diag_kind = 'kde')
plt.show()

"""Korelasi yang terjadi kebanyakan bernilai positif karena kebanyakan grafik pada sumbu y dan x mengalami peningkatan yang cukup signifikan membentuk sebuah garis"""

plt.figure(figsize=(10, 8))
correlation_matrix = df.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix ", size=20)
plt.show()

"""terlihat bahwa pada matriks korelasi diatas dapat disimpulkan bahwasannya semua variabel memiliki keterikatan dan korelasi yang kuat antar variabel lainnya, dimana nilai korelasi antar variabel bernilai 1.

## Data Preparation

### Train Test Split
Membagi data latih dan data test
"""

X = df.drop("close",axis=1)
y = df.close

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 2023,shuffle=False)
print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

"""Melakukan standarisasi/normalisasi data """

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

"""## Model Development

**K-Nearest Neighbor**
"""

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
 
knn = KNeighborsRegressor(n_neighbors=8)
knn.fit(X_train, y_train)

"""**Random Forest**



"""

from sklearn.ensemble import RandomForestRegressor
 
RF = RandomForestRegressor(n_estimators=64, max_depth=16, random_state=2023, n_jobs=-1)
RF.fit(X_train, y_train)

"""**Boosting Algorithm**"""

from sklearn.ensemble import AdaBoostRegressor
 
boosting = AdaBoostRegressor(learning_rate=0.05, random_state=2023)                             
boosting.fit(X_train, y_train)

"""**Linear Regression**"""

from sklearn.linear_model import LinearRegression
LR = LinearRegression()
LR.fit(X_train, y_train)

"""## Evaluasi Model

Mengukur nilai MSE
"""

mse = pd.DataFrame(columns=['train', 'test'], index=['KNN','RF','Boosting','LR'])
 
# Buat dictionary untuk setiap algoritma yang digunakan
model_dict = {'KNN': knn, 'RF': RF, 'Boosting': boosting, 'LR': LR}
 
# Hitung Mean Squared Error masing-masing algoritma pada data train dan test
for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e3 
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e3
 
# Panggil mse
mse

fig, ax = plt.subplots()
mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

"""Dari gambar di atas, terlihat bahwa, model Linear Regression (LR) memberikan nilai eror yang paling kecil. Sedangkan model dengan algoritma Boosting memiliki eror yang paling besar. Model inilah yang akan kita pilih sebagai model terbaik untuk melakukan prediksi.

### Menghitung akurasi model
"""

knn_accuracy = knn.score(X_test, y_test)*100
rf_accuracy = RF.score(X_test, y_test)*100
boosting_accuracy = boosting.score(X_test, y_test)*100
lr_accuracy = LR.score(X_test, y_test)*100

list_evaluasi = [[knn_accuracy],
            [rf_accuracy],
            [boosting_accuracy],
            [lr_accuracy],]
evaluasi = pd.DataFrame(list_evaluasi,
                        columns=['Accuracy (%)'],
                        index=['K-Nearest Neighbor', 'Random Forest', 'Boosting', 'Linear Regression'])
evaluasi

"""## Predict"""

prediksi = X_test.copy()
pred_dict = {'y_true':y_test}
for name, model in model_dict.items():
    pred_dict['prediksi_'+name] = model.predict(prediksi).round(1)
 
pd.DataFrame(pred_dict)

plt.figure(figsize=(15,5))
sns.set_style('darkgrid')
plt.plot(y_test.index, LR.predict(X_test), label='Pred')
plt.plot(y_test.index, y_test, label='Real')
plt.legend(loc='upper right')
plt.ylabel('Price', fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.title("Harga Saham\nPT. ACE Hardware Indonesia", fontsize=25)
plt.show()