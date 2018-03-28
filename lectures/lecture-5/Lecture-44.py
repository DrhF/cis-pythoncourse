
# coding: utf-8

# # Pandas
# # Введение
# 
# #### Куксёнок Илья 
# #### НИЯУ МИФИ ИИКС

# ## Структуры данных в Pandas

# In[1]:


import numpy as np
import pandas as pd


# # Структуры данных python

# In[2]:


list = [i for i in range(3)]
print(list)


# In[3]:


list.append('seven')
print(list)


# In[4]:


list.pop()
print(list)


# In[5]:


list.insert(3, "tri")
print(list)


# ## Генераторы списков

# In[6]:


squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
squares_true_way = [i**2 for i in range(10)]
print(squares_true_way)


# In[7]:


combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# аналогично
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
             combs.append((x, y))
print(combs)


# ## Кортежи

# In[8]:


kortej = 12345, 54321, 'hello!'

toje_kortej = [i for i in range(4)], 12345, 54321, 'hello!'

print(kortej)
print(toje_kortej)


# In[9]:


toje_kortej[0].append("DOBAVIM_ELEMENT")
print(toje_kortej)


# In[10]:


madness = combs, kortej
print(madness)
combs.append(5)
print(combs)
print(madness)


# ## Множества

# In[11]:


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)           


# In[12]:


'orange' in basket


# In[13]:


a = set('abracadabra')
b = set('alacazam')
a - b


# ## Словарь

# In[14]:


tel = {'A': 1, 'B': 2, 'C': 3}


# In[15]:


tel.keys()


# In[16]:


tel.values()


# In[17]:


'D'in tel


# In[18]:


'A'in tel


# ## >>> s = pd.Series(data, index=index)

# In[19]:


s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
s


# In[20]:


d = {'a' : 0., 'b' : 1., 'c' : 2.}

pd.Series(d)


# In[21]:


pd.Series(d, index=['b', 'c', 'd', 'a'])


# In[22]:


s[0]


# In[23]:


s[:3]


# In[24]:


s[3:]


# In[25]:


s[s>0.1]


# ## Задача
# ### Создайте набор из NumPy массива и списка, добавьте по одному 
# ### элементу в каждый из них, посмотрите что получится. 
# 

# In[26]:


import random
a = np.random.random((2))
b = [random.random() for i in range(0,2)]
g = pd.Series([a,b], index=['one', 'two'])
g


# In[27]:


a = np.insert(a,2,5,axis = 0)
b.append(4)


# In[28]:


g


# In[29]:


g = pd.Series([a,b], index=['one', 'two'])


# In[30]:


g


# In[31]:


np.sin(g['one'])


# In[32]:


np.sin(g['two'])


# # DataFrame

# In[33]:


d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}


# In[34]:


df = pd.DataFrame(d)


# In[35]:


df


# ## Задача
# ### Создайте набор из NumPy массива и списка, добавьте по одному 
# ### элементу в каждый из них, посмотрите что получится. 
# ### Обратитесь к измененному элементу.

# # (ง ° ͜ ʖ °)ง

# In[36]:


df['one']['d']=4.0


# In[37]:


df


# In[38]:


data1 = {'A':np.random.random(3),'B':np.random.random(3),'C':np.random.random(3)}
df1 = pd.DataFrame(data1)
df1.assign(e=s[:3].values)


# In[39]:


df1['A'] = df1['B'] * df1['C']
df1['flag'] = df1['A'] > 0.1
df1


# In[40]:


df1.insert(2, 'copy_of_A', df1['A'][:2])


# In[41]:


df1


# In[43]:


json_df = pd.read_json('example.json')


# In[44]:


json_df


# In[45]:


np.sin(json_df['a'])


# ## Задача на дом
# ## Распарсить task-[1-2].json
# ### После распасрсивания первого произвести опреацию сложения столбцов
# ### Во втором случае вывести значения полей домашний/рабочий/мобильный телефон, а также город
