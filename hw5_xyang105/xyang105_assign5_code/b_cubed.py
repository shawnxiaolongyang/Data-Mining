
# coding: utf-8

# In[36]:

def norm(data):
    data1 = [[0,0,0]for i in range(len(data))]
    d0 = []
    d1 = []
    d2 = []
    for i in range(len(data)):
        d0.append(data[i][0])
        d1.append(data[i][1])
        d2.append(data[i][2])
    for i in range(len(data)):
        data1[i][0] = round(float((data[i][0]-min(d0)))/(max(d0)-min(d0)),4)
        data1[i][1] = round(float((data[i][1]-min(d1)))/(max(d1)-min(d1)),4)
        data1[i][2] = d2[i]
    return data1


# In[24]:

f = open("../xyang105_assign5_result/truth.txt", "r")


# In[25]:

all_text = f.read()


# In[26]:

c = all_text.split("\n")


# In[27]:

c.pop(0),c.pop(0),c.pop(-1)


# In[29]:

data = [[0,0,0] for i in range(len(c))]
for i in range(len(c)):
    data[i][0] = float(c[i].strip(' ').split(',')[0])
    data[i][1] = float(c[i].strip(' ').split(',')[1])
    data[i][2] = float(c[i].strip(' ').split(',')[2])
    


# In[37]:

data1 = norm(data)


# In[80]:

def b_cube(filename):
    step1_text = filename.read()
    d = step1_text.split("\n")
    d.pop(0),d.pop(0),d.pop(-1)
    dat = [[0,0,0] for i in range(len(d))]
    for i in range(len(d)):
        dat[i][0] = float(d[i].strip(' ').split(',')[0])
        dat[i][1] = float(d[i].strip(' ').split(',')[1])
        dat[i][2] = float(d[i].strip(' ').split(',')[2])
    data2 = [[0,0,0,0] for i in range(len(data))]
    for ii in range(len(dat)):
        for iii in range(len(data1)):
            if dat[ii][0] == data1[iii][0]:
                if dat[ii][1] == data1[iii][1]:
                    data2[ii][0] = dat[ii][0]
                    data2[ii][1] = dat[ii][1]
                    data2[ii][2] = dat[ii][2]
                    data2[ii][3] = data1[iii][2]
    TP = [[0,0,0,0]for i in range(4)]
    P = [0,0,0,0]
    T = [0,0,0,0]
    for n in range(4):
        for i in data2:
            for m in range(4):
                if i[2] ==n+1:
                    if i[3] ==m+1:
                        TP[n][m] += 1

        for i in data2:
            if i[2] ==n+1:
                P[n] += 1

        for i in data2:
            if i[3] ==n+1:
                T[n] += 1
    return TP,P,T
    


# ## For step1

# In[81]:

f1 = open("../xyang105_assign5_result/step1.txt", "r")


# In[82]:

TP,P,T = b_cube(f1)


# In[83]:

print TP,P,T


# In[107]:

Precision = ((float(352)**2/868+float(518)**2/518+float(4270)**2/4999+float(3326)**2/3326))/sum([352,518,4270,3326])


# In[108]:

Recall = (float(352)**2/1073+float(518)**2/1034+float(4270)**2/4270+float(3326)**2/3334)/sum([352,518,4270,3326])


# In[109]:

print Precision


# In[110]:

print Recall


# ## For step2a

# In[87]:

f2a = open("../xyang105_assign5_result/step2a.txt", "r")


# In[88]:

TP,P,T = b_cube(f2a)


# In[89]:

print TP,P,T


# In[112]:

Precision = (float(1029)**2/1029+float(4270)**2/5343+float(3334)**2/3339)/sum([1029,4270,3334])


# In[127]:

Recall = (float(1029)**2/1034+float(4270)**2/4270+float(3334)**2/3334)/sum([1029,4270,3334])


# In[114]:

print Precision


# In[128]:

print Recall


# ## For step2b

# In[121]:

f2b = open("../xyang105_assign5_result/step2b.txt", "r")


# In[122]:

TP,P,T = b_cube(f2b)


# In[123]:

print TP,P,T


# In[126]:

Precision = (float(1073)**2/5299+float(4270)**2/4270)/sum([1073,4270])


# In[129]:

Recall = (float(1073**2)/1073+float(4270)**2/4270)/sum([1073,4270])


# In[130]:

print Precision


# In[131]:

print Recall


# In[ ]:



