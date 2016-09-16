#Question 1(a)

table_1=[0,1,2,4,5,5,7,10,10,12,13,17,39]



def mean(data):
    mean1 =sum(data)/len(data)
    return mean1


print "The mean of dataset" +str(round(mean(table_1),3))

def square(i):
    i = i*i
    return i

def variance(data):
    var=0
    for i in data:
        var=var+square(i-mean(data))
    var=var/len(data)
    return var

print round(variance(table_1),3)

std_dev=variance(table_1)**0.5
print "The standard deviation is "+str(round(std_dev,3))

#Question 1(b)

table2=sorted(table_1)
print table2

def first_quartile(data):
    if (len(data))%4==0 or (len(data)-1)%4==0:
        return (data[len(data)/4-1]+data[len(data)/4])*0.5
    else:
        return data[len(data)/4]

print "The first quartile of data is "+str(first_quartile(table2))

def third_quartile(data):
    if (len(data))%4==0:
        return (data[len(data)/4*3-1]+data[len(data)/4*3])*0.5
    elif (len(data)-1)%4==0:
        return (data[(len(data)-1)/4*3]+data[(len(data)-1)/4*3+1])*0.5
    elif (len(data)-2)%4==0:
        return data[(len(data)-2)/4*3+1]
    else:
        return data[(len(data)-3)/4*3+2]

table3=[1,2,3,4]
    
print "The third quartile of data is "+str(third_quartile(table2))

Interquartile = third_quartile(table_1)-first_quartile(table_1)
print "The interquartile of data is "+str(round(Interquartile,3))

#Question 1(c)


def modality(data):
    mod2 = [0]*len(data)
    for i in range(len(data)):
        mod2[i] = data.count(data[i])
    for i in range(len(data)):
        if mod2[i] == max(mod2):
            
            print "the mode is "+str(data[i])

modality(table_1)
    
#Question 1(d)
file1=open("./data.freeway.txt","r")
text=file1.read()
#print text

s=text.split("\n")
s.pop(0),s.pop(-1)
#print s

Timestamp=[0]*len(s)
Speed=[0]*len(s)
Occupancy=[0]*len(s)

for i in range(len(s)):
    Speed[i]=float(s[i].split("\t")[1])

def median(data):
    if (len(data)+1)%2==0:
        return data[(len(data)+1)/2]
    else:
        return ((data[len(data)/2]+data[len(data)/2+1])/2)

Speed_1=sorted(Speed)
Quarter1=first_quartile(Speed_1)
Quarter3=third_quartile(Speed_1)
Mean=mean(Speed_1)
Median=median(Speed_1)



print "The first quartile of data is "+str(round(Quarter1,3))
print "The third quartile of data is "+str(round(Quarter3,3))
print "The mean of data is "+str(round(Mean,3))
print "The median of data is "+str(round(Median,3))
modality(Speed_1)

#Question 1(e)
#The distribution has a positive skewness because the mean is larger than the median.

#Question 3(a)
sample=[[1,2,3,4,5],[27,51,52,33,45],[19000,64000,100000,55000,45000]]

def normalize(data):
    x=[0]*len(data)
    for i in range(len(data)):
        x[i] = round(float((data[i]-min(data)))/(max(data)-min(data)),3)
    return x

sample[1]=normalize(sample[1])
sample[2]=normalize(sample[2])

print "normalized age is "+str(sample[1])
print "normalized salary is "+str(sample[2])

#Question 3(b)

def std_norm(data,y):
    m = mean(data)
    standard_dev = variance(data)**0.5
    z = [0]*len(data)
    for i in range(len(data)):
        z[i] = (data[i] - m)/standard_dev
    y = (y - m)/standard_dev
    return z, round(y,3)

std_speed, Speed_55 = std_norm(Speed,55)

print "The mean of speed is "+str(round(mean(Speed),3))
print "The mean of speed after normalization "+str(round(mean(std_speed),3))
print "The variance before normalization "+ str(round(variance(Speed),3))
print "The variance after normalization "+ str(variance(std_speed))
print "The correspoding speed after normalization is "+ str(round(Speed_55,3))



    
