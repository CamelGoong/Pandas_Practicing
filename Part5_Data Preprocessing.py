#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns

#  타이타닉 데이터셋 불러오기
df = sns.load_dataset("titanic")
df.head()


# In[3]:


df.info()


# In[4]:


# deck 열의 NaN 갯수 계산
nan_deck = df['deck'].value_counts(dropna = False)
print(nan_deck)


# In[7]:


print(df.head().isnull().sum(axis = 0))


# 누락 데이터 제거

# In[14]:


# for 반복문으로 각 열의 NaN 갯수 계산하기
missing_df = df.isnull()
for col in missing_df.columns:
    missing_count = missing_df[col].value_counts()
    try:
        print(col, ': ', missing_count[True])
    except:
        print(col, ': ', 0)


# In[17]:


# thresh 옵션을 적용하여 deck열 제거
df_thresh = df.dropna(axis = 1, thresh = 500)


# In[18]:


print(df_thresh.columns)


# In[19]:


# age열의 데이터가 NaN인 모든 행을 삭제
df_age = df.dropna(subset = ['age'], how = 'any', axis = 0)


# In[20]:


print(len(df_age))


# 누락 데이터 치환

# In[27]:


# age가 NaN인 데이터들을 나이 평균으로 치환해주고자 함.
print(df['age'].head(10))
mean_age = df['age'].mean()


# In[28]:


df['age'].fillna(mean_age)


# In[29]:


# 최빈값으로 치환하기
print(df['embark_town'][825:830])


# In[33]:


most_freq = df['embark_town'].value_counts(dropna = True).idxmax()
most_freq


# In[36]:


df['embark_town'].fillna(most_freq, inplace = True)


# In[37]:


print(df['embark_town'][825:830])


# In[38]:


# 바로 앞에 있는 행의 값으로 치환하기
import seaborn as sns
df = sns.load_dataset("titanic")


# In[42]:


print(df['embark_town'][825:830])
df['embark_town'].fillna(method = 'ffill', inplace = True)
print("\n수정후")
print(df['embark_town'][825:830])


# 중복 데이터 처리

# In[47]:


# 중복데이터 확인
import pandas as pd
df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
                'c2':[1,1,1,2,2],
                'c3':[1,1,2,2,2]})
print(df)


# In[49]:


df_dup = df.duplicated()
df_dup


# In[50]:


# 중복데이터 제거
df2 = df.drop_duplicates()
print(df2)


# In[53]:


df3 = df.drop_duplicates(subset = ["c2", "c3"])
print(df3)


# 데이터 표준화

# In[65]:


# 3-1 단위 환산
import pandas as pd
df = pd.read_csv('./auto-mpg.csv', header = None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']
df.head()


# In[66]:


# mpg -> kpl
mpg_to_kpl = 1.60934/3.78541


# In[67]:


df['kpl'] = df['mpg'] * mpg_to_kpl


# In[68]:


df['kpl'] = df['kpl'].round(2)


# In[69]:


print(df.head())


# In[70]:


# 3-2 자료형 변환
print(df.dtypes)


# In[71]:


# horsepower열의 고유값 확인
df['horsepower'].unique()


# In[74]:


# 누락데이터(?) 삭제
import numpy as np
df['horsepower'].replace("?", np.nan, inplace = True)
df.dropna(subset = ['horsepower'], axis = 0, inplace = True) # horsepower열에서 누락된 데이터가 있으면 바로 삭제
df['horsepower'] = df['horsepower'].astype('float')

print(df['horsepower'].dtypes)


# In[75]:


print(df['origin'].unique)


# In[77]:


print(df['origin'].dtypes)
df['origin'].replace({1:"USA", 2:"EU", 3:"JPN"}, inplace = True)
print(df['origin'].dtypes)


# In[79]:


# origin을 object ->  category형으로 변환
df['origin'] = df['origin'].astype("category")
print(df['origin'].dtypes)


# In[83]:


# model year: 정수형 -> 범주형으로 변환
print(df['model year'].head(3))
print(df['model year'].dtypes)
df['model year'] = df['model year'].astype("category")
print(df['model year'].dtypes)


# In[ ]:




