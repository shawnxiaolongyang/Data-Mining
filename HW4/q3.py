rowdata = [['sunny','hot','high','weak','No'],
['sunny','hot','high','strong','No'],
['overcast','hot','high','weak','Yes'],
['rain','mild','high','weak','Yes'],
['rain','cool','normal','weak','Yes'],
['rain','cool','normal','strong','No'],
['overcast','cool','normal','strong','Yes'],
['sunny','mild','high','weak','No'],
['sunny','cool','normal','weak','Yes'],
['rain','mild','normal','weak','Yes'],
['sunny','mild','normal','strong','Yes'],
['overcast','mild','high','strong','Yes'],
['overcast','hot','normal','weak','Yes'],
['rain','mild','high','strong','No']]

sunny = [0,0] 
overcast = [0,0] 
rain = [0,0] 
hot = [0,0] 
mild = [0,0] 
cool = [0,0] 
high = [0,0] 
normal = [0,0] 
strong = [0,0] 
weak = [0,0]
length = 14

for i in range(14):
    if rowdata[i][0] == 'sunny':
        if rowdata[i][4] == 'Yes':
            sunny[0] += 1
        else:
            sunny[1] += 1
    elif rowdata[i][0] == 'overcast':
        if rowdata[i][4] == 'Yes':
            overcast[0] += 1
        else:
            overcast[1] += 1
    elif rowdata[i][0] == 'rain':
        if rowdata[i][4] == 'Yes':
            rain[0] += 1
        else:
            rain[1] += 1

for i in range(14):
    if rowdata[i][1] == 'hot':
        if rowdata[i][4] == 'Yes':
            hot[0] += 1
        else:
            hot[1] += 1
    elif rowdata[i][1] == 'mild':
        if rowdata[i][4] == 'Yes':
            mild[0] += 1
        else:
            mild[1] += 1
    elif rowdata[i][1] == 'cool':
        if rowdata[i][4] == 'Yes':
            cool[0] += 1
        else:
            cool[1] += 1

for i in range(14):
    if rowdata[i][2] == 'high':
        if rowdata[i][4] == 'Yes':
            high[0] += 1
        else:
            high[1] += 1
    elif rowdata[i][2] == 'normal':
        if rowdata[i][4] == 'Yes':
            normal[0] += 1
        else:
            normal[1] += 1

for i in range(14):
    if rowdata[i][3] == 'strong':
        if rowdata[i][4] == 'Yes':
            strong[0] += 1
        else:
            strong[1] += 1
    elif rowdata[i][3] == 'weak':
        if rowdata[i][4] == 'Yes':
            weak[0] += 1
        else:
            weak[1] += 1

yes = high[0] + normal[0]
no =  high[1] + normal[1]

import math

def expected_information(D):
    D_and_sum= sum(D)
    information = 0
    for i in D:
        if i == 0:
            information += 0
        else:
            information += (float(i)/D_and_sum)*math.log(float(i)/D_and_sum,2) 
    return -information 


Total_information = expected_information([yes,no])
print Total_information


def information_for_attributes(one):
    return float(sum(one))/length*expected_information(one) 

Gain_weather = Total_information - information_for_attributes(sunny) - information_for_attributes(overcast)- information_for_attributes(rain)
Gain_temperature = Total_information - information_for_attributes(hot) - information_for_attributes(mild)- information_for_attributes(cool)
Gain_humidity = Total_information - information_for_attributes(high) - information_for_attributes(normal)
Gain_wind = Total_information - information_for_attributes(weak) - information_for_attributes(strong)



print Gain_weather,Gain_temperature,Gain_humidity,Gain_wind
print expected_information(sunny),expected_information(overcast),expected_information(rain)
print (float(overcast[0])/sum(overcast))


sunny_and_hot = [0,0]
sunny_and_mild = [0,0]
sunny_and_cool = [0,0]
rain_and_hot = [0,0]
rain_and_mild = [0,0]
rain_and_cool = [0,0]
sunny_and_high = [0,0]
sunny_and_normal = [0,0]
rain_and_high = [0,0]
rain_and_normal = [0,0]
sunny_and_strong = [0,0]
sunny_and_weak = [0,0]
rain_and_strong = [0,0]
rain_and_weak = [0,0]


for i in range(14):
    if rowdata[i][0] == 'sunny':
        if rowdata[i][1] == 'hot':
            if rowdata[i][4] == 'Yes':
                sunny_and_hot[0] += 1
            else:
                sunny_and_hot[1] += 1
        elif rowdata[i][1] == 'mild':
            if rowdata[i][4] == 'Yes':
                sunny_and_mild[0] += 1
            else:
                sunny_and_mild[1] += 1
        elif rowdata[i][1] == 'cool':
            if rowdata[i][4] == 'Yes':
                sunny_and_cool[0] += 1
            else:
                sunny_and_cool[1] += 1
    elif rowdata[i][0] == 'rain':
        if rowdata[i][1] == 'hot':
            if rowdata[i][4] == 'Yes':
                rain_and_hot[0] += 1
            else:
                rain_and_hot[1] += 1
        elif rowdata[i][1] == 'mild':
            if rowdata[i][4] == 'Yes':
                rain_and_mild[0] += 1
            else:
                rain_and_mild[1] += 1
        elif rowdata[i][1] == 'cool':
            if rowdata[i][4] == 'Yes':
                rain_and_cool[0] += 1
            else:
                rain_and_cool[1] += 1

for i in range(14):
    if rowdata[i][0] == 'sunny':
        if rowdata[i][2] == 'high':
            if rowdata[i][4] == 'Yes':
                sunny_and_high[0] += 1
            else:
                sunny_and_high[1] += 1
        elif rowdata[i][2] == 'normal':
            if rowdata[i][4] == 'Yes':
                sunny_and_normal[0] += 1
            else:
                sunny_and_normal[1] += 1
    elif rowdata[i][0] == 'rain':
        if rowdata[i][2] == 'high':
            if rowdata[i][4] == 'Yes':
                rain_and_high[0] += 1
            else:
                rain_and_high[1] += 1
        elif rowdata[i][2] == 'normal':
            if rowdata[i][4] == 'Yes':
                rain_and_normal[0] += 1
            else:
                rain_and_normal[1] += 1


for i in range(14):
    if rowdata[i][0] == 'sunny':
        if rowdata[i][3] == 'strong':
            if rowdata[i][4] == 'Yes':
                sunny_and_strong[0] += 1
            else:
                sunny_and_strong[1] += 1
        elif rowdata[i][3] == 'weak':
            if rowdata[i][4] == 'Yes':
                sunny_and_weak[0] += 1
            else:
                sunny_and_weak[1] += 1
        
        
    elif rowdata[i][0] == 'rain':
        if rowdata[i][3] == 'strong':
            if rowdata[i][4] == 'Yes':
                rain_and_strong[0] += 1
            else:
                rain_and_strong[1] += 1
        elif rowdata[i][3] == 'weak':
            if rowdata[i][4] == 'Yes':
                rain_and_weak[0] += 1
            else:
                rain_and_weak[1] += 1

Gain_sunny_and_temperature =information_for_attributes(sunny) - information_for_attributes(sunny_and_hot) - information_for_attributes(sunny_and_mild)- information_for_attributes(sunny_and_cool)
Gain_sunny_and_humidity = information_for_attributes(sunny)- information_for_attributes(sunny_and_high) - information_for_attributes(sunny_and_normal)
Gain_sunny_and_wind = information_for_attributes(sunny) - information_for_attributes(sunny_and_weak) - information_for_attributes(sunny_and_strong)
Gain_rain_and_temperature =information_for_attributes(rain)- information_for_attributes(rain_and_hot) - information_for_attributes(rain_and_mild)- information_for_attributes(rain_and_cool)
Gain_rain_and_humidity =information_for_attributes(rain)- information_for_attributes(rain_and_high) - information_for_attributes(rain_and_normal)
Gain_rain_and_wind =information_for_attributes(rain) - information_for_attributes(rain_and_weak) - information_for_attributes(rain_and_strong)


print Gain_sunny_and_temperature,Gain_sunny_and_humidity,Gain_sunny_and_wind
print Gain_rain_and_temperature, Gain_rain_and_humidity, Gain_rain_and_wind
print (float(rain_and_strong[0])/sum(rain_and_strong)), (float(rain_and_weak[0])/sum(rain_and_weak))

sunny_and_high_and_hot =[0,0]
sunny_and_high_and_mild =[0,0]
sunny_and_high_and_cool =[0,0]
sunny_and_normal_and_hot =[0,0]
sunny_and_normal_and_mild =[0,0]
sunny_and_normal_and_cool =[0,0]

for i in range(14):
    if rowdata[i][0] == 'sunny':
        if rowdata[i][2] == 'high':
            if rowdata[i][1] == 'hot':
                if rowdata[i][4] == 'Yes':
                    sunny_and_high_and_hot[0] += 1
                else:
                    sunny_and_high_and_hot[1] += 1
            elif rowdata[i][1] == 'mild':
                if rowdata[i][4] == 'Yes':
                    sunny_and_high_and_mild[0] += 1
                else:
                    sunny_and_high_and_mild[1] += 1
            elif rowdata[i][1] == 'cool':
                if rowdata[i][4] == 'Yes':
                    sunny_and_high_and_cool[0] += 1
                else:
                    sunny_and_high_and_cool[1] += 1
        elif rowdata[i][2] == 'normal':
            if rowdata[i][1] == 'hot':
                if rowdata[i][4] == 'Yes':
                    sunny_and_normal_and_hot[0] += 1
                else:
                    sunny_and_normal_and_hot[1] += 1
            elif rowdata[i][1] == 'mild':
                if rowdata[i][4] == 'Yes':
                    sunny_and_normal_and_mild[0] += 1
                else:
                    sunny_and_normal_and_mild[1] += 1
            elif rowdata[i][1] == 'cool':
                if rowdata[i][4] == 'Yes':
                    sunny_and_normal_and_cool[0] += 1
                else:
                    sunny_and_normal_and_cool[1] += 1

Gain_sunny_and_high_and_temperature = information_for_attributes(sunny_and_high)-information_for_attributes(sunny_and_high_and_hot) - information_for_attributes(sunny_and_high_and_mild)- information_for_attributes(sunny_and_high_and_cool)
Gain_sunny_and_normal_and_temperature = information_for_attributes(sunny_and_normal)-information_for_attributes(sunny_and_normal_and_hot) - information_for_attributes(sunny_and_normal_and_mild)- information_for_attributes(sunny_and_normal_and_cool)


print Gain_sunny_and_high_and_temperature,Gain_sunny_and_normal_and_temperature
print (float(sunny_and_normal[0])/sum(sunny_and_normal)),(float(sunny_and_high[0])/sum(sunny_and_high))

def split_information(D):
    information = 0
    for i in D:
        information += float(i)/sum(D)*math.log(float(i)/sum(D),2) 
    return -information

Gain_ratio_weather = float(Gain_weather)/split_information([sum(sunny),sum(overcast),sum(rain)])
Gain_ratio_temperature = float(Gain_temperature)/split_information([sum(hot),sum(mild),sum(cool)])
Gain_ratio_humidity = float(Gain_humidity)/split_information([sum(high),sum(normal)])
Gain_ratio_wind = float(Gain_wind)/split_information([sum(weak),sum(strong)])

print Gain_ratio_weather,Gain_ratio_temperature, Gain_ratio_humidity,Gain_ratio_wind


