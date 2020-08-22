## 64 bit multiplier scheme 1
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from pandas import Series
import random

get_bin = lambda x, n: format(x, 'b').zfill(n)
x=list(range(100000))
x1=list(range(6))
yans=list(range(100000))
yans1=list(range(100000))
res = [] 
res1 = []
num1 = [7, 8, 9, 10, 11, 12]
mean_error_distance = [0, 0, 0, 0, 0, 0]
mean_relative_error_distance = [0., 0., 0., 0., 0., 0.]
normalized_error_distance = [0., 0., 0., 0., 0., 0.]
normailzed_relative_error_distance = [0., 0., 0., 0., 0., 0.]
acceptance_prob = [0., 0., 0., 0., 0., 0.]
for c in range(100000): 
	res.append(random.randint(1, 18446744073709551615)) 

for d in range(100000): 
	res1.append(random.randint(1, 18446744073709551615)) 

for g in range (6):
	mean_error_distance_1 = 0
	mean_relative_error_distance_1 = 0
	normalized_error_distance_1 = 0
	normailzed_relative_error_distance_1 = 0
	prob = 0
	for f in range (100000):
		a=res[f]
		b=res1[f]	
		y=a*b
		abin = get_bin(a,64)
		bbin = get_bin(b,64)
		num = num1[g]
		i=0
		while (abin[i]=='0'):
			i=i+1

		j=0
		while (bbin[j]=='0'):
			j=j+1
		k=i
		l=j
		sum1=64-k-num
		sum2=64-l-num
		if (sum1<0):
			sum1=0
		if (sum2<0):
			sum2=0
		sum3=(sum1+sum2)*-1
		sum3=(sum1+sum2)*-1
		if (k+num>64):
			k = 64-num
		if (l+num>64):
			l = 64-num
		amul=abin[k:k+num]
		bmul=bbin[l:l+num]
		q=int(amul,2)
		w=int(bmul,2)
		e=q*w
		yapp = get_bin(e,128)
		yapp = [int(x) for x in yapp]
		yapp = np.roll(yapp,sum3)
		yapp = ' '.join(str(e) for e in yapp)
		yapp = str.replace(yapp," ","")
		w=int(yapp,2)
		ans=((y-w)/y)*100
		yans[f]=ans
		yans1[f] = (y-w)
		mean_error_distance[g] = (y-w) + mean_error_distance[g]
		mean_relative_error_distance[g] = mean_relative_error_distance[g] + ans
		max1 = max(yans1)
		max2 = max(yans)
		if (ans>1):
			prob = prob + 1
		
	
	mean_error_distance[g] = mean_error_distance[g]/100000
	mean_relative_error_distance[g] = mean_relative_error_distance[g]/100000
	normalized_error_distance[g] = mean_error_distance[g]/max1
	normailzed_relative_error_distance[g] = mean_relative_error_distance[g]/max2
	acceptance_prob[g] = prob/100000
	acceptance_prob[g] = 1-acceptance_prob[g]
	print ("*******************************")
	print ("latency parameter: ",num1[g])
	print ("mean_error_distance : ", mean_error_distance[g])
	print ("mean_relative_error_distance : ", mean_relative_error_distance[g])
	print ("normalized_error_distance : ", normalized_error_distance[g])
	print ("normailzed_relative_error_distance : ", normailzed_relative_error_distance[g])
	print ("acceptance_probability at 1% : ", acceptance_prob[g])
	plt.plot(x,yans)
	plt.title ('RELATIVE ERROR(%) 64 BIT MULTIPLIER SCHEME 1')
	plt.xlabel('Random Numbers Generated')
	plt.ylabel('Relative Error(%)')
	
plt.show()
p = (0,1,2,3,4,5)
l = (7,8,9,10,11,12)
plt.plot (x1,mean_error_distance)
plt.title ('64 BIT MULTIPLIER SCHEME 1')
plt.xticks(p,l)
plt.xlabel('Latency Parameter')
plt.ylabel('Mean Error Distance')
plt.show()
plt.plot (x1,mean_relative_error_distance)
plt.title ('64 BIT MULTIPLIER SCHEME 1')
plt.xticks(p,l)
plt.xlabel('Latency Parameter')
plt.ylabel('Mean Relative Error Distance')
plt.show()
plt.plot (x1,normalized_error_distance)
plt.title ('64 BIT MULTIPLIER SCHEME 1')
plt.xticks(p,l)
plt.xlabel('Latency Parameter')
plt.ylabel('Normalized Error Distance ')
plt.show()
plt.plot (x1,normailzed_relative_error_distance)
plt.title ('64 BIT MULTIPLIER SCHEME 1')
plt.xticks(p,l)
plt.xlabel('Latency Parameter')
plt.ylabel('Normailzed Relative Error Distance')
plt.show()
plt.plot (x1,acceptance_prob)
plt.title ('64 BIT MULTIPLIER SCHEME 1')
plt.xticks(p,l)
plt.xlabel('Latency Parameter')
plt.ylabel('Acceptance Probability(1% Relative Error)')
plt.show()

