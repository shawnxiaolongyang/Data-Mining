#Question 2(a)
Jaccard=round(42,3)/(42+38+30)
print round(Jaccard,3)

#Question 2(b)
#Let the values Y and P be 1, and the value N 0
patient=[[1,1,1,1,0,0],[1,0,1,0,0,0],[1,1,0,1,0,0]]
print patient

def dissim(data):
    dissim=[[] for i in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data)):
            q=0;r=0;s=0
            if i>j:
                for k in range(len(data[i])):
                    if data[i][k]==1 and data[j][k]==1:
                        q+=1
                    elif data[i][k]==1 and data[j][k]==0:
                        s+=1
                    elif data[i][k]==0 and data[j][k]==1:
                        r+=1
                    
                dissim[i].append(float(r+s)/(q+r+s))
            if i==j:                
                dissim[i].append(0)
    return dissim
print "The dissim between patients is "+str(dissim(patient))

#Question 2(c)

M=[[1,0,0],[0,1,0],[0,0,1],[0,1,0]]

Cat_dis= dissim(M)

#Let the value excellent be 3, good 2, and fair 1
#For ordinal variables, Z(excellent)=(3-1)/(3-1)=0.5
#Z(good)=(2-1)/(3-1)=0.5,Z(fair)=(1-1)/(3-1)=0

Ord=[[1],[0],[1],[0.5]]

Ord_dis=[[] for i in range(len(Ord))]
for i in range(len(Ord)):
    for j in range(len(Ord)):
        if i==j:
            Ord_dis[i].append(0)
        if i>j:
            for k in range(len(Ord[i])):
                Ord_dis[i].append(((Ord[i][k]-Ord[j][k])**2)**0.5)
print Cat_dis
print Ord_dis

mix_dis=[[] for i in range(len(Cat_dis))]
for i in range(len(Cat_dis)):
    for j in range(len(Cat_dis[i])):
        mix_dis[i].append((Cat_dis[i][j]+Ord_dis[i][j])/2)

print mix_dis

#Question 2(d)
A=[4,4,2]
B=[-3,2,6]

def euclidean_dist(a,b):
    dist=0
    for i in range(len(a)):
        dist +=(a[i]-b[i])**2
        dist_sqrt= dist**0.5
    return round(dist_sqrt,3)

print "The Euclidean distance between A and B is "+str(euclidean_dist(A,B))

def manhattan_dist(a,b):
    dist=0
    for i in range(len(a)):
        dist += abs((a[i]-b[i]))
    return round(dist,3)

print "The Manhattan distance between A and B is "+str(manhattan_dist(A,B))      
            
def minkowski_dist(a,b):
    dist=0
    for i in range(len(a)):
        if dist<abs(a[i]-b[i]):
            dist=abs(a[i]-b[i])
    return round(dist,3)

print "The Minkowski distance between A and B is "+str(minkowski_dist(A,B))

#Question 2(e)

Alto=[0,0,12,34,14,21,13,5,0,30,41,23,3,2]

document= open("./home.txt","r")
doc1= document.read()

s=doc1.split("\n")
s.pop(0),s.pop(-1)
#print s

Geo_ID=[0]*len(s)
Place=[0]*len(s)
Char=[[] for i in range(len(s))]

for i in range(len(s)):
    Geo_ID[i]=s[i].split("\t")[0]
    Place[i]=s[i].split("\t")[1]
    for j in range(2, len(s[i].split("\t"))):
        Char[i].append(int(s[i].split("\t")[j]))

#print Char
def cos_sim(a,b):
    vector=0
    d1=0
    d2=0
    for i in range(len(a)):
        vector+=a[i]*b[i]
        d1 +=a[i]**2
        d2 +=b[i]**2
        
    d1_sqrt=d1**0.5
    d2_sqrt=d2**0.5
    return round(vector/((float(d1_sqrt))*(float(d2_sqrt))),3)
    
    
cos_m=[[] for i in range(len(Char))]

for i in range(len(Char)):
    cos_m[i].append(cos_sim(Alto,Char[i]))
    cos_m[i].append(Geo_ID[i])
    cos_m[i].append(Place[i])
    

import numpy as np

def column_sort(data,i):
    table=np.array(data).tolist()
    table.sort(key=lambda x:x[i])
    return np.array(table)


new_table=column_sort(cos_m,0)

#print new_table

for i in range(1,6):
    print new_table[-i]
    






