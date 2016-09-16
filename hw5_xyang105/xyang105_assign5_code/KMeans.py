
# coding: utf-8

# In[937]:

def norm(data):
    data1 = [[0,0]for i in range(len(data))]
    d0 = []
    d1 = []
    for i in range(len(data)):
        d0.append(data[i][0])
        d1.append(data[i][1])
    for i in range(len(data)):
        data1[i][0] = round(float((data[i][0]-min(d0)))/(max(d0)-min(d0)),4)
        data1[i][1] = round(float((data[i][1]-min(d1)))/(max(d1)-min(d1)),4)
    return data1


# In[938]:

def eucl_dist(a,b):
    distance = 0
    for i in range(len(a)):
        distance += (a[i]-b[i])**2
    return round(float(distance)**0.5,3)


# In[939]:

def find_center(cluster):
    C_x = 0
    C_y = 0
    for i in cluster:
        C_x += i[0]
        C_y += i[1]
    center = [round(float(C_x)/len(cluster),4), round(float(C_y)/len(cluster),4)]
    return center


# In[940]:

from random import randint as ri


# In[941]:

def random_value(data,center):
    value = ri(0,len(data)-1)
    random_value = data[value]
    center.append(random_value)
    data.pop(value)
    return data,center


# In[942]:

def SSE(C,center,k):
    error = 0
    for i in range(k):
        for D in C[k-i-1]:
            error += (eucl_dist(center[i],D))**2
    return error         


# In[943]:

def rand_value(center):
    value = data[ri(0,len(data)-1)]
    q = 0
    for iii in center:
        if eucl_dist(value,iii) > 0.2:
            q += 0
        else:
            q += 1
    if q == 0:
        return value
    else:
        return None


# In[944]:

def cluster(data,k,center,error):
    C = [[]for i in range(k)]       
    value = [[0]*k for i in range(len(data))]
    
    for i in range(len(data)):
        for ii in range(k):
            
            value[i][ii] =  eucl_dist(data[i],center[ii])
    for i in range(len(data)):
        for ii in range(k):
            if eucl_dist(data[i],center[ii]) == max(value[i]):
                t = 0
                if ii > 0:
                    for iii in range(ii):
                        if data[i] not in C[iii]:
                            t += 0
                        else:
                            t += 1
                if t == 0:
                    C[ii].append(data[i])
    n = 0
    center2 = [[0,0]for i in range(k)]
    
    if error !=0:
        for i in range(k):
            for ii in range(i+1,k):
                
                if center[ii] == center[i]:
                    for iii in range(100):
                        value = rand_value(center)
                        if value:
                            center[ii] = value
                            break
                    print "replace one point"
            
            if center[i] ==[0,0]:
                center[i] = data[ri(0,len(data)-1)]
                print "add one new point"
            
            if len(C[k-i-1])==0:
                center[i] = find_center(data)            
            else:
                center2[i] = find_center(C[k-i-1])
                
        print center,error,center2,SSE(C,center2,k)
                
                
        if SSE(C,center2,k)<error:
            center = center2
        else:
            n = 1          
    error = SSE(C,center,k)
    return center,C,error,n


# In[945]:

def resul(C,k):
    results = []
    for i in range(k):
        a = []
        for ii in range(len(C[i])):
            a=C[i][ii]
            a.append(i)
            results.append(a)
    return results


# In[946]:

def iteration(data,k):
    data1 = []
    for i in data:
        data1.append(i)
    center = []
    if k<= 2:
        for i in range(k):
            data1,center = random_value(data1,center)
    if k ==3:
        center = [[0.2,0.2],[0.2,1],[0.9,0.2]]
    if k ==4:
        center = [[0.2,0.2],[0.2,0.9],[0.9,0.2],[0.5,0.65]]
    if k ==5:
        center = [[0.2,0.2],[0.1,0.9],[0.3,0.9],[0.9,0.2],[0.5,0.6]]
    
    n = 0
    results = []
    error = 0
    for i in range(200):
        print i
        if i == 199:
            center,C,error,n = cluster(data,k,center,error)
            results = resul(C,k)
            return results,error
        elif n == 0:
            center,C,error,n = cluster(data,k,center,error)
            print "go on"
        else:
            center,C,error,n = cluster(data,k,center,error)
            print "find optimization"
            results = resul(C,k)
            return results,error
            break


# In[947]:

data = [[1,1],[1,2],[2,1],[2,2]]
results0,error0 = iteration(data,2)
data = [[1,1],[1,2],[2,1],[2,2]]
results1,error1 = iteration(data,2)
if error0 < error1:
    results = results0
else:
    results = results1


# In[948]:

results


# In[949]:

f = open(".data/data.txt", "r")


# In[950]:

all_text = f.read()


# In[951]:

c = all_text.split("\n")


# In[952]:

c.pop(0),c.pop(-1)


# In[953]:

data = [[0,0] for i in range(len(c))]
for i in range(len(c)):
    data[i][0] = float(c[i].strip(' ').split(',')[0])
    data[i][1] = float(c[i].strip(' ').split(',')[1])


# In[954]:

def double_evaluate(data,k):
    data1 = norm(data)
    results0,error0 = iteration(data1,k)
    data2 = norm(data)
    results1,error1 = iteration(data2,k)
    if error0 < error1:
        results = results0
    else:
        results = results1
    return results


# In[955]:

results = [[]for i in range(5)]


# In[956]:

results[3] = double_evaluate(data,4)


# In[957]:

results[2] = double_evaluate(data,3)


# In[958]:

results[4] = double_evaluate(data,5)


# In[959]:

results[1] = double_evaluate(data,2)


# In[960]:

import itertools 


# In[961]:

file = open('../xyang105_assign5_result/step1.txt', 'w')
string = str(len(data))+"\n"
for i in results[3]:
    for ii in range(len(i)):
        if ii != 2:
            string += str(i[ii]) + ','
        if ii ==2 :
            a = i[ii]+1
            string += str(a) + ','
    string += '\n'
file.write(string)
file.close()


# In[962]:

file = open('../xyang105_assign5_result/step2a.txt', 'w')
string = str(len(data))+"\n"
for i in results[2]:
    for ii in range(len(i)):
        if ii != 2:
            string += str(i[ii]) + ','
        if ii ==2 :
            a = i[ii]+1
            string += str(a) + ','
    string += '\n'
file.write(string)
file.close()


# In[963]:

file = open('../xyang105_assign5_result/step2b.txt', 'w')
string = str(len(data))+"\n"
for i in results[4]:
    for ii in range(len(i)):
        if ii != 2:
            string += str(i[ii]) + ','
        if ii ==2 :
            a = i[ii]+1
            string += str(a) + ','
    string += '\n'
file.write(string)
file.close()


# In[969]:

f.close()


# In[ ]:



