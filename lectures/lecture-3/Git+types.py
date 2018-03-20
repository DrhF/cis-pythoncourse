
# coding: utf-8

# # Git 
# # структурыданных 
# 
# #### Куксёнок Илья 
# #### НИЯУ МИФИ ИИКС

# # Git
# ## основные моменты

# # крутые чуваки сидят тут:
# 
# ## https://github.com/
# 
# ![right](https://assets-cdn.github.com/images/modules/logos_page/Octocat.png)

# ![center](https://git-scm.com/figures/18333fig0106-tn.png)

# # 1) Вы вносите изменения в файлы в своём рабочем каталоге.
# # 2) Подготавливаете файлы, добавляя их слепки в область подготовленных файлов.
# # 3) Делаете коммит, который берёт подготовленные файлы из индекса и помещает их в каталог Git'а на постоянное хранение.

# ## Локальные настройки
# ### git config --global user.name "User Name"
# 
# ### git config --global user.mail "USER@MAIL.COM";

# ## клонирование репозитория
# 
# ### git clone https://github.com/NVIDIA/nvidia-docker.git 

# ## Создание своего репозитория
# 
# ### git init
# 

# 
# ## Добавление файлов в проект
# 
# ### git add .
# 
# ### git add some.py
# 
# ### git add *.py
# 

# ## Первый коммит
# 
# ###  git status
# 
# ### git commit -m 'initial commit'
# 
# ### git pull
# 
# ### git push
# 

# ## А что если в репозитории есть мусор?
# 
# 
# ### notepad (vim, vin, nano, etc) .gitignore

# ## Подробнее про сей файл
# 
#  Пустые строки, а также строки, начинающиеся с #, игнорируются.
#  
#  Можно заканчивать шаблон символом слэша (/) для указания каталога.
#  
#  Можно инвертировать шаблон, использовав восклицательный знак (!) в качестве первого символа.

# In[ ]:


# комментарий — эта строка игнорируется
# не обрабатывать файлы, имя которых заканчивается на .a
*.a
# НО отслеживать файл lib.a, несмотря на то, что мы игнорируем все .a файлы с помощью предыдущего правила
get_ipython().system('lib.a')
# игнорировать только файл TODO находящийся в корневом каталоге, не относится к файлам вида subdir/TODO
TODO()
# игнорировать все файлы в каталоге build/
build/
# игнорировать doc/notes.txt, но не doc/server/arch.txt
doc/*.txt
# игнорировать все .txt файлы в каталоге doc/
doc/**/*.txt


# ## Удаление файлов
# 
# ### git rm readme.txt
# 
# ### git rm log/\*.log
# 
# ### git mv file_from file_to

# ## Просмотр истории
# 
# ### git log 
# 
# ### git log -p -2

# In[ ]:


## Фиксим косяки!

$ git commit -m 'initial commit'
$ git add forgotten_file
$ git commit --amend


# ## Tags
# 
# ### git tag -a v1.0 -m 'my version 1.0'

# ![center](https://git-scm.com/figures/18333fig0301-tn.png)

# ![center](https://git-scm.com/figures/18333fig0303-tn.png)

# ## Ветки
# 
# ### Создадим вкетку
# 
# ### git branch testing

# ![center](https://git-scm.com/figures/18333fig0305-tn.png)

# ### Перейдем в вкетку
# 
# ### git checkout testing
# 
# ![center](https://git-scm.com/figures/18333fig0306-tn.png)

# ![center](https://git-scm.com/figures/18333fig0307-tn.png)

# ![center](https://git-scm.com/figures/18333fig0308-tn.png)

# ![center](https://git-scm.com/figures/18333fig0309-tn.png)

# ## слияние веток
# 
# ### git checkout master
# 
# ### git merge hotfix
# 

# ![center](https://git-scm.com/figures/18333fig0313-tn.png)

# ![center](https://git-scm.com/figures/18333fig0314-tn.png)

# ![center](https://git-scm.com/figures/18333fig0317-tn.png)

# ## удаление веток
# 
# ### git branch -d 
# 
# #### если ну ооочень хочется удалить ветку
# 
# ### git branch -D develop

# ## Структуры данных
# 
# ### Списки
# ### Кортежи
# ### Словари 
# ### Множества

# ## типы в Python
# ![center](http://s00.yaplakal.com/pics/pics_original/1/6/8/603861.jpg)
# 

# ## Динамическая типизация

# In[83]:


a = 5
b = str(a) + "five"
print(b)


# ## Ссылочные типы

# In[85]:


a = "seven"
a = b
b = 7
print(a)


# ## Типы. Они есть.
# 

# In[17]:


a = 4
b = 2
print(a/b) #float
print(int(a/b)) #integer
print (a + b) #integer
print(3/2) # float


# In[18]:


complex(a,b) 


# ## Булевы типы
# 

# In[24]:


print(2+2 == 4) 
print(2+2 is 42)


# # Списки

# In[42]:


list = [i for i in range(3)]
print(list)


# In[54]:


list.append('seven')
print(list)


# In[53]:


list.pop()
print(list)


# In[51]:


list.insert(3, "tri")
print(list)


# ## Генераторы списков

# In[57]:


squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
squares_true_way = [i**2 for i in range(10)]
print(squares_true_way)


# In[77]:


combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# аналогично
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
             combs.append((x, y))
print(combs)


# ## Кортежи

# In[67]:


kortej = 12345, 54321, 'hello!'

toje_kortej = [i for i in range(4)], 12345, 54321, 'hello!'

print(kortej)
print(toje_kortej)


# In[70]:


toje_kortej[0].append("DOBAVIM_ELEMENT")
print(toje_kortej)


# In[79]:


madness = combs, kortej
print(madness)
combs.append(5)
print(combs)
print(madness)


# ## Множества

# In[86]:


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)           


# In[87]:


'orange' in basket


# In[89]:


a = set('abracadabra')
b = set('alacazam')
a - b


# ## Словарь

# In[91]:


tel = {'Snejanna': 8910432098, 'Madlen': 8980443139, 'Georgiy': '02'}


# In[93]:


tel.keys()


# In[94]:


tel.values()


# In[96]:


tel['Georgiy']


# In[110]:


## Найдите ошибку ))
if 'Viktorya' in tel is False:
    print('uvi')
else:
    print(tel['Viktorya'])


