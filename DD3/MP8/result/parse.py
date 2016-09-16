
# coding: utf-8

# In[8]:

import xyang105_FP_growth as FP_growth


# In[9]:

routings = [['45.0', '40.0', '41.0'],
 ['71.0', '74.0', '73.0'],
 ['115.0', '98.0', '71.0', '132.0', '114.0', '126.0'],
 ['126.0', '124.0'],
 ['134.0', '71.0', '130.0', '132.0', '126.0', '133.0']]                                 
min_sup = 2                            
front__tab = {}        

treegene = FP_growth.Tree_generation(routings=routings, min_sup=min_sup, front__tab=front__tab)    
FP_growth.tree_analysis(Tree=treegene.tree, min_sup=min_sup, front__tab=front__tab)    


# In[10]:

import xlrd


# In[11]:

data = xlrd.open_workbook('topic-0.xlsx')
table = data.sheets()[0]
a = [[] for i in range(len(table.col_values(1)))]

for i in range(len(table.col_values(1))):
    for ii in range(len(table.row_values(1))):
        if table.row_values(i)[ii] != '':
            a[i].append(str(table.row_values(i)[ii]))


# In[12]:

a[0:5]


# In[13]:

def fp_finder(csv_path, min_sup):
    data = xlrd.open_workbook(csv_path)
    table = data.sheets()[0]
    a = [[] for i in range(len(table.col_values(1)))]

    for i in range(len(table.col_values(1))):
        for ii in range(len(table.row_values(1))):
            if table.row_values(i)[ii] != '':
                a[i].append(str(table.row_values(i)[ii]))
    routings = a                         
    front__tab = {}        

    treegene = FP_growth.Tree_generation(routings=routings, min_sup=min_sup, front__tab=front__tab)    
    FP_growth.tree_analysis(Tree=treegene.tree, min_sup=min_sup, front__tab=front__tab)


# In[14]:

fp_finder('topic-0.xlsx',50)


# In[ ]:



