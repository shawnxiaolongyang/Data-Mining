
# coding: utf-8

# ## Problem1

# In[76]:

data1 = [0,1,2,4,5,5,7,10,10,12,13,17,39]


# ### 1.a

# In[77]:

def mean(data):
    mean1 = sum(data)/len(data)
    return round(mean1,3)


# In[78]:

mean(data1)


# In[79]:

def variance(data):
    variance1 = 0
    for i in data:
        variance1 = variance1 + (i-mean(data))**2
    variance1 = variance1/len(data)
    return round(variance1,3)


# In[80]:

variance1 = variance(data1)


# In[81]:

std_dev1 = variance1**0.5


# In[82]:

"%.3f" % std_dev1


# ------------------------------

# ### 1.b

# In[83]:

data1b = sorted(data1)


# In[84]:

data1b


# #### the 1st quatile

# In[85]:

def first_quartile(data):
    if (len(data) + 1) % 4 == 0:
        return data[(len(data) + 1) / 4 - 1]
    else:
        yushu = (len(data) + 1) % 4
        weishu = (len(data) + 1) / 4
        return (data[weishu-1]*(1-float(yushu)/4) + data[weishu]*(float(yushu)/4))


# In[86]:

"%.3f" % first_quartile(data1b) 


# #### the 3rd quatile

# In[87]:

def third_quartile(data):
    if (len(data) + 1)*3 % 4 == 0:
        return data[(len(data) + 1)*3 / 4 - 1]
    else:
        yushu = (len(data) + 1)*3 % 4
        weishu = (len(data) + 1)*3 / 4
        return (data[weishu-1]*(1-float(yushu)/4) + data[weishu]*(float(yushu)/4))


# In[88]:

"%.3f" % third_quartile(data1b)


# In[89]:

interquartile = third_quartile(data1b) - first_quartile(data1b)


# In[90]:

"%.3f" % interquartile


# ------------------------------

# ### 1.c

# In[91]:

def mode(data):
    a = []
    a1 = []
    for i in data:
        if i not in a:
            a.append(i)
    b = [0]*len(a)
    for i in range(len(a)):
        for ii in data:
            if a[i] == ii:
                b[i] += 1
    for i in range(len(b)):
        if b[i] == max(b):
            a1.append(a[i])
    return a1


# In[92]:

mode(data1)


# ------------------------------

# ### 1.d

# In[93]:

f = open("./data.freeway.txt", "r")


# In[94]:

all_text = f.read()


# In[95]:

all_text


# In[96]:

c = all_text.split("\n")


# In[97]:

c.pop(0), c.pop(-1)


# In[98]:

Timestamp =[0]*len(c)
Speed = [0]*len(c)
Occupancy = [0]*len(c)
for i in range(len(c)):
    Timestamp[i] = c[i].split("\t")[0]
    Speed[i] = float(c[i].split("\t")[1])
    Occupancy[i] = float(c[i].split("\t")[2])


# In[99]:

def median(data):
    if (len(data)+1)%2 ==0:
        return data[(len(data)+1)/2]
    else:
        return ((data[len(data)/2]+data[len(data)/2+1])/2)
    


# In[100]:

Speed1 = sorted(Speed)
Q1= first_quartile(Speed1)
Q3 = third_quartile(Speed1)
Mean = mean(Speed1)
Median = median(Speed1)
Mode = mode(Speed1)


# In[101]:

"%.3f" % Q1


# In[102]:

"%.3f" % Q3


# In[103]:

"%.3f" % Median


# In[104]:

"%.3f" % Mean


# In[105]:

Mode


# ------------------------------

# ### 1.e

# ***Since the mean is larger than the median, the distribution has a positive skewness.***

# ------------------------------------------------------------
# ------------------------------------------------------------

# ### Probelm 2

# #### 2.a

# *** Since J=q/(q+r+s) ***

# In[106]:

J = round((42),3)/(42+30+38)


# In[107]:

"%.3f" % J


# ------------------------------

# #### 2.b

# *** Suppose Jack, Jim and Mary are the 1st, 2nd and 3rd in the following column ***
# 
# let Y and P be 1, N be 0

# In[108]:

disease = [0]*3
disease[0] = [1,1,1,1,0,0]
disease[1] = [1,0,1,0,0,0]
disease[2] = [1,1,0,1,0,0]


# In[109]:

disease


# For asymmetric data, we use the (r+s)/(q+r+s) to evaluate dissimilarity
# 
# since r+s = whole-q-t, and q+r+s = whole-t
# 

# In[110]:

def dissimilarity(data):
    dissimilarity = [[] for i in range(len(data))]

    for i in range(len(data)):
        for ii in range(len(data)):
            if i > ii :
                q = 0
                t = 0
                for iii in range(len(data[i])):
                    if data[i][iii]==1 and data[ii][iii]==1:
                        q += 1
                    if data[i][iii]==0 and data[ii][iii]==0:
                        t += 1
                dissimilarity[i].append(float((len(data[0])-q-t))/(len(data[0])-t))
            if i == ii:
                dissimilarity[i].append(0)
                
    return dissimilarity


# In[111]:

dissimilarity(disease)


#  We can find the ***1st*** and ***3rd*** patient have the lest disimilarity 0.25
#  
#  So we can determine they have the same disease

# ------------------------------

# #### 2.c
# For category data, we take 3 more features in the data matrix

# In[112]:

matrix = [[1,0,0],
         [0,1,0],
         [0,0,1],
         [0,1,0]]


# In[113]:

bi_dis = dissimilarity(matrix)


# *** Suppose excellent is 3, good is 2, fair is 1***
# 
# For ordinal variables, use Z = (ri-1)/(M-1), which means:
# excellemt = (3-1)/(3-1) = 1
# 
# good = (2-1)/(3-1) = 0.5
# 
# fair = (1-1)/(3-1) = 0

# In[114]:

nu_matrix = [[1],
            [0],
            [1],
            [0.5]]


# In[115]:

nu_dis = [[] for i in range(len(nu_matrix))]
for i in range(len(nu_matrix)):
    for ii in range(len(nu_matrix)):
        if i > ii :
            for iii in range(len(nu_matrix[i])):
                nu_dis[i].append(((nu_matrix[i][iii]-nu_matrix[ii][iii])**2)**0.5)
        if i == ii:
            nu_dis[i].append(0)


# In[116]:

bi_dis,nu_dis


# *** suppose the weights of each feature is 0.5 ***

# In[117]:

mixed_dis = [[] for i in range(len(nu_dis))]
for i in range(len(nu_dis)):
    for ii in range(len(nu_dis[i])):
        mixed_dis[i].append(bi_dis[i][ii]*0.5 + nu_dis[i][ii]*0.5)


# In[118]:

mixed_dis


# ------------------------------

# #### 2.d

# In[119]:

def eucl_dist(a,b):
    distance = 0
    for i in range(len(a)):
        distance += (a[i]-b[i])**2
    return round(float(distance)**0.5,3)
    


# In[120]:

def manh_dist(a,b):
    distance = 0
    for i in range(len(a)):
        distance += abs((a[i]-b[i]))
    return round(distance,3)


# In[121]:

def mink_dist(a,b):
    distance = 0 
    for i in range(len(a)):
        if distance < abs((a[i]-b[i])):
            distance = abs((a[i]-b[i]))
    return round(distance,3)


# In[122]:

A = [4,4,2]
B = [-3,2,6]
print "the Euclidean distance is "
print eucl_dist(A,B)
print "the Manhattan distance is "
print manh_dist(A,B)
print "the Minkowski distance is "
print mink_dist(A,B)


# ------------------------------

# #### 2.e

# In[123]:

def cos_sim(a,b):
    vector = 0
    A_len = 0
    B_len = 0
    for i in range(len(a)):
        vector += a[i]*b[i]
        A_len += a[i]**2
        B_len += b[i]**2
    return round(vector/((float(A_len)**0.5)*(float(B_len)**0.5)),3)


# In[124]:

f2 = open("./home.txt", "r")


# In[125]:

text = f2.read()


# In[126]:

text


# In[127]:

line = text.split("\n")


# In[128]:

line.pop(0),line.pop(-1)


# In[129]:

Geo_ID = [0]*len(line)
Place = [0]*len(line)
area = [[] for i in range(len(line))]

for i in range(len(line)):
    Geo_ID[i] = line[i].split("\t")[0]
    Place[i] =  line[i].split("\t")[1]
    for ii in range(2,len(line[i].split("\t"))):
        area[i].append(int(line[i].split("\t")[ii]))


# In[130]:

Alto = [0,0,12,34,14,21,13,5,0,30,41,23,3,2]


# In[131]:

cos_ans = [[] for i in range(len(area))]
for i in range(len(area)):
    cos_ans[i].append(cos_sim(Alto,area[i]))
    cos_ans[i].append(Geo_ID[i])
    cos_ans[i].append(Place[i])


# In[132]:

import numpy as np
def sort_by_col(data,icol):
    data1 = np.array(data).tolist()
    data1.sort(key=lambda x:x[icol])
    return np.array(data1)


# In[133]:

ans = sort_by_col(cos_ans, 0)


# In[134]:

for i in range(1,6):
    print ans[-i]


# ------------------------------------------------------------
# ------------------------------------------------------------

# ### Problem 3

# #### 3.a

# In[374]:

empl = [[1,2,3,4,5],
        [27,51,52,33,45],
        [19000,64000,100000,55000,45000]]


# zi=(xi−min(x))/(max(x)−min(x))

# In[376]:

def norm(data):
    data1 = [0]*len(data)
    for i in range(len(data)):
        data1[i] = round(float((data[i]-min(data)))/(max(data)-min(data)),3)
    return data1


# In[378]:

empl[1] = norm(empl[1])
empl[2] = norm(empl[2])


# In[379]:

empl


# ------------------------------

# #### 3.b
# σ = (sum(X-mean)^2/n)^0.5
# 
# z = (x−μ)/ σ

# In[139]:

def std_norm(data,test):
    m = mean(data)
    pstd = variance(data)**0.5
    z = [0]*len(data)
    for i in range(len(data)):
        z[i] = (data[i] - m)/pstd
    test = (test - m)/pstd
    return z, round(test,3)


# In[140]:

std_speed, speed_55 = std_norm(Speed,55)


# In[141]:

mean(Speed),mean(std_speed)


# In[142]:

variance(Speed),variance(std_speed)


# In[108]:

round(speed55,3)


# ------------------------------------------------------------
# ------------------------------------------------------------

# ### Problem 4

# #### 4.I.a

# In[204]:

data = [[2.5,0.5,2.2,1.9,3.1,2.3,2,1.0,1.5,1.1],[2.4,0.7,2.9,2.2,3.0,2.7,1.6,1.1,1.6,0.9]]


# In[205]:

A = data[0]
B = data[1]


# In[206]:

A_mean = mean(data[0])
B_mean = mean(data[1])
A_std = variance(data[0])**0.5
B_std = variance(data[1])**0.5  


# In[207]:

AB = 0
for i in range(len(A)):
    AB += A[i] * B[i]
    


# In[209]:

coefficient = (AB-len(A)*A_mean*B_mean)/(len(A)*A_std*B_std)


# In[211]:

round(coefficient,3)


# We can find the x-axis's data is highly related to the y-axis's data

# #### 4.I.b

# If a data has a high variance in signal while low variance in noises, we need consider use the PCA.
# 
# Since the correlation is close to 1, which means x-axis's data is highly related to the y-axis's data, if we use the x-y basis, there would be high redundancy. 
# 
# If we chose to use PCA, it would change the aspect and show the most difference in noise.  
# 
# In this case, we should use PCA to do the job.

# #### 4.I.c

# In[213]:

covariance = AB/len(A)-A_mean*B_mean


# In[215]:

round(covariance,3)


# Since the Co-variance is higher than 0, 
# 
# data in X-axis rise with Y-axis.

# ------------------------------

# #### 4.II

# In[331]:

a = [[1,-1,0,0],[1,0,0,-1]]

m = len(a)
n = len(a[0])
for i in range(m):
    for ii in range(n):
        a[i][ii] = a[i][ii] - mean(a[i])


# In[344]:

def transpose(data):
    data = [[row[col] for row in data] for col in range(len(data[0]))]
    return data


# In[345]:

def dot_mult(A, B):
    ans = [[0] * len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for ii in range(len(B[0])):
            for iii in range(len(B)):
                ans[i][ii] += A[i][iii] * B[iii][ii]
    return ans


# In[346]:

def cov(data):
    n = len(data[0])
    m = len(data)
    cov = [[0]*m for i in range(m)]
    for i in range(m):
        for ii in range(m):
            cov[i][ii] = dot_mult(data,transpose(data))[i][ii]/n 
    return cov


# In[335]:

cov_a = cov(a)


# In[336]:

cov_a


# In[337]:

from sympy import *
def eigenvlaues(data):
    dat = data
    x = Symbol('x')   
    for i in range(len(dat)):
        dat[i][i] -= x
    a = Matrix(dat)
    print a.det()    
    return solve(a.det(),x)


# In[338]:

e_value = eigenvlaues(cov_a)


# In[339]:

e_value


# When e_value is 0.25, it would be cov_a minus e_value in the diagnol
# 
# [[0.25,0.25],[0.25,0.25]]

# this means the eigenvector is [1,-1]

# When e_value is 0.75, it would be cov_a minus e_value in the diagnol
# [[-0.25,0.25],[0.25,-0.25]]

# this means the eigenvector is [1,1]

# In[340]:

P = [[1,-1],[1,1]]


# In[341]:

Y = dot_mult(P,a)


# In[342]:

Y


# In[349]:

cov_y = cov(Y)


# In[350]:

cov_y


# Now the Y become a diagonal matrix

# since 1.5>0.5, the *** frist principle vector *** is the 2nd row
# 
# if we make it norminalization

# In[405]:

P1 = [round((1**2+1**2)**0.5/2,3),round((1**2+1**2)**0.5/2,3)]


# In[406]:

P1


# #### 4.II.b

# The coordinate should be P[1]*a in 1-d space

# In[407]:

a_1d = [0]*4
for ii in range(4):
    a_1d[ii] = P1[0]*a[0][ii] + P1[0]*a[1][ii]


# In[408]:

a_1d


# #### 4.II.C

# we need to use transposed P[1]*a_1d to recover

# In[409]:

P_tran = [[0.707],[0.707]]


# In[413]:

a_recover = [[0]*4 for i in range(2)]
for i in range(2):
    for ii in range(4):
        a_recover[i][ii] = round(P_tran[i][0]*a_1d[ii],2)


# In[414]:

a_recover


# In[412]:

a


# After compare, we can find half of the data(2 of 4) can be recoverd.

# In[ ]:



