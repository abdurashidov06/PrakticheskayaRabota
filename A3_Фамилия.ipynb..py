# ATTS 03-24 R ABDURASHIDOV ABDULAZIZ
# Практическая работа A3: «паспорт» учебного набора данных Wine (вино)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine


wine = load_wine(as_frame=True)
df = wine.frame
print('Размер исходной таблицы (строки, столбцы):', df.shape)


df_raw = df.copy()


df_raw.insert(0, 'sample_id', range(1, len(df_raw) + 1))


df_raw['class_name'] = df_raw['target'].map({0: 'сорт_0', 1: 'сорт_1', 2: 'сорт_2'})

df_raw.loc[[5, 40, 100], 'magnesium'] = np.nan
df_raw.loc[60, 'ash'] = 0
df_raw.loc[20, 'alcohol'] = 999


df_raw = pd.concat([df_raw, df_raw.iloc[[10, 50]]], ignore_index=True)

df_raw.to_csv('wine_raw.csv', index=False)
df_raw = pd.read_csv('wine_raw.csv')



print('Размер таблицы (строки, столбцы):', df_raw.shape)
print('Типы столбцов:')
print(df_raw.dtypes)
print('Число пропусков по столбцам:')
print(df_raw.isna().sum())
print('Число полных дубликатов:', df_raw.duplicated().sum())
print('Число проб в каждом сорте:')
print(df_raw['target'].value_counts())



print('Строки с пропусками:')
print(df_raw[df_raw.isna().any(axis=1)])
print('Строки, где зола равна 0 (невозможное значение):')
print(df_raw[df_raw['ash'] == 0])
print('Дубликаты (показаны обе копии):')
print(df_raw[df_raw.duplicated(keep=False)])
print('Три самых больших значения спирта (поиск выброса):')
print(df_raw.sort_values('alcohol', ascending=False).head(3))



y = df_raw['target']

X = df_raw.drop(columns=['target', 'class_name', 'sample_id'])
print('Размер X и y:', X.shape, y.shape)




print('Сопоставление class_name и target (утечка данных):')
print(pd.crosstab(df_raw['class_name'], df_raw['target']))



df_clean = df_raw.copy()
df_clean = df_clean.drop_duplicates()
df_clean.loc[df_clean['alcohol'] > 100, 'alcohol'] = np.nan
df_clean.loc[df_clean['ash'] == 0, 'ash'] = np.nan


print('до очистки   :', df_raw['alcohol'].agg(['min', 'max', 'mean', 'median']).round(2).to_dict())
print('после очистки:', df_clean['alcohol'].agg(['min', 'max', 'mean', 'median']).round(2).to_dict())



df_clean['alcohol'].hist(bins=15, color='green')
plt.title('Распределение содержания спирта')
plt.xlabel('спирт, %'); plt.ylabel('число проб')
plt.savefig('hist_alcohol.png', dpi=150, bbox_inches='tight')
plt.close()


for cls, color in zip([0, 1, 2], ['green', 'orange', 'red']):

    df_clean[df_clean['target'] == cls]['alcohol'].hist(bins=10, alpha=0.5, color=color, label=f'сорт {cls}')
plt.legend(); plt.xlabel('спирт, %'); plt.ylabel('число проб')
plt.title('Спирт по сортам вина')
plt.savefig('hist_by_class.png', dpi=150, bbox_inches='tight')
plt.close()



fig, axes = plt.subplots(1, 3, figsize=(12, 3))
for ax, b in zip(axes, [3, 15, 60]):
    df_clean['alcohol'].hist(bins=b, color='green', ax=ax)
    ax.set_title(f'столбцов: {b}')
plt.tight_layout()
plt.savefig('hist_bins.png', dpi=150, bbox_inches='tight')
plt.close()

print('Готово: графики сохранены в файлы hist_alcohol.png, hist_by_class.png, hist_bins.png')