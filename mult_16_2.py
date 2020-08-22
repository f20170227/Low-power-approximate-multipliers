## 16 bit multiplier scheme 2
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
mean_error_distance = 0
mean_relative_error_distance = 0
normalized_error_distance = 0
normailzed_relative_error_distance = 0
acceptance_prob = 0
for c in range(100000): 
	res.append(random.randint(1, 65535)) 

for d in range(100000): 
	res1.append(random.randint(1, 65535)) 

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
		abin = get_bin(a,16)
		bbin = get_bin(b,16)
		if abin[0]=='1':
			num=8
		elif bbin[0]=='1':
			num=8
		elif abin[1]=='1':

			num=8
		elif bbin[1]=='1':
			num=8
		elif abin[2]=='1':
			num=8
		elif bbin[2]=='1':
			num=8
		elif abin[3]=='1':
			num=7
		elif bbin[3]=='1':
			num=7
		elif abin[4]=='1':
			num=7
		elif bbin[4]=='1':
			num=7
		elif abin[5]=='1':
			num=7
		elif bbin[5]=='1':
			num=7
		elif abin[6]=='1':
			num=6
		elif bbin[6]=='1':
			num=6
	

		else:
			num=5
		i=0
		while (abin[i]=='0'):
			i=i+1

		j=0
		while (bbin[j]=='0'):
			j=j+1
		k=i
		l=j
		sum1=16-k-num
		sum2=16-l-num
		if (sum1<0):
			sum1=0
		if (sum2<0):
			sum2=0
		sum3=(sum1+sum2)*-1
		if (k+num>16):
			k = 16-num
		if (l+num>16):
			l = 16-num
		amul=abin[k:k+num]
		bmul=bbin[l:l+num]
		q=int(amul,2)
		w=int(bmul,2)
		e=q*w
		yapp = get_bin(e,32)
		yapp = [int(x) for x in yapp]
		yapp = np.roll(yapp,sum3)
		yapp = ' '.join(str(e) for e in yapp)
		yapp = str.replace(yapp," ","")
		w=int(yapp,2)
		ans=((y-w)/y)*100
		yans[f]=ans
		yans1[f] = (y-w)
		mean_error_distance = (y-w) + mean_error_distance
		mean_relative_error_distance = mean_relative_error_distance + ans
		max1 = max(yans1)
		max2 = max(yans)
		if (ans>1):
			prob = prob + 1
	
plt.plot(x,yans)
mean_error_distance = mean_error_distance/100000
mean_relative_error_distance = mean_relative_error_distance/100000
normalized_error_distance = mean_error_distance/max1
normailzed_relative_error_distance = mean_relative_error_distance/max2
acceptance_prob = prob/100000
acceptance_prob = 1-acceptance_prob
print ("*******************************")
print ("MEAN ERROR DISTANCE : ", mean_error_distance)
print ("mean_relative_error_distance : ", mean_relative_error_distance)
print ("normalized_error_distance : ", normalized_error_distance)
print ("normailzed_relative_error_distance : ", normailzed_relative_error_distance)
print ("acceptance_probability at 1% : ", acceptance_prob)

plt.title ('16 BIT MULTIPLIER SCHEME 2')
plt.xlabel('Random Numbers Generated')
plt.ylabel('Relative Error(%)')	
plt.show()


