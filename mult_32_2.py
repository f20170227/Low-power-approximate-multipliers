## 32 bit multiplier scheme 2
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from pandas import Series
import random

get_bin = lambda x, n: format(x, 'b').zfill(n)
x=list(range(10000))
x1=list(range(6))
yans=list(range(10000))
yans1=list(range(10000))
res = [] 
res1 = []
mean_error_distance = 0
mean_relative_error_distance = 0
normalized_error_distance = 0
normailzed_relative_error_distance = 0
acceptance_prob = 0
for c in range(10000): 
	res.append(random.randint(1, 4294967295)) 

for d in range(10000): 
	res1.append(random.randint(1, 4294967295)) 

for g in range (6):
	mean_error_distance_1 = 0
	mean_relative_error_distance_1 = 0
	normalized_error_distance_1 = 0
	normailzed_relative_error_distance_1 = 0
	prob = 0
	for f in range (10000):
		a=res[f]
		b=res1[f]	
		y=a*b
		abin = get_bin(a,32)
		bbin = get_bin(b,32)
		if abin[0]=='1':
			num=8
		elif bbin[0]=='1':
			num=8
		elif abin[1]=='1':

			num=8
		elif bbin[1]=='1':
			num=8
		elif abin[2]=='1':
			num=7
		elif bbin[2]=='1':
			num=7
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
			num=7
		elif bbin[6]=='1':
			num=7
		elif abin[7]=='1':
			num=7
		elif bbin[7]=='1':
			num=7
		elif abin[8]=='1':
			num=7
		elif bbin[8]=='1':
			num=7
		elif abin[9]=='1':
			num=7
		elif bbin[9]=='1':
			num=7


		else:
			num=6
		i=0
		while (abin[i]=='0'):
			i=i+1

		j=0
		while (bbin[j]=='0'):
			j=j+1
		k=i
		l=j
		sum1=32-k-num
		sum2=32-l-num
		if (sum1<0):
			sum1=0
		if (sum2<0):
			sum2=0
		sum3=(sum1+sum2)*-1
		if (k+num>32):
			k = 32-num
		if (l+num>32):
			l = 32-num
		amul=abin[k:k+num]
		bmul=bbin[l:l+num]
		q=int(amul,2)
		w=int(bmul,2)
		e=q*w
		yapp = get_bin(e,64)
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
mean_error_distance = mean_error_distance/10000
mean_relative_error_distance = mean_relative_error_distance/10000
normalized_error_distance = mean_error_distance/max1
normailzed_relative_error_distance = mean_relative_error_distance/max2
acceptance_prob = prob/10000
acceptance_prob = 1-acceptance_prob
print ("*******************************")
print ("MEAN ERROR DISTANCE : ", mean_error_distance)
print ("mean_relative_error_distance : ", mean_relative_error_distance)
print ("normalized_error_distance : ", normalized_error_distance)
print ("normailzed_relative_error_distance : ", normailzed_relative_error_distance)
print ("acceptance_probability at 1% : ", acceptance_prob)

plt.title ('32 BIT MULTIPLIER SCHEME 2')
plt.xlabel('Random Numbers Generated')
plt.ylabel('Relative Error(%)')	
plt.show()


