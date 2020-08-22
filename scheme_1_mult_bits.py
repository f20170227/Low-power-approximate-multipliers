##### 128 ###########


import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from pandas import Series
import random
num = 8

err = [0, 0, 0, 0, 0,0]
err1 = [0, 0, 0, 0, 0,0]
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
	res.append(random.randint(1, 340282366920938463463374607431768211455)) 

for d in range(100000): 
	res1.append(random.randint(1, 340282366920938463463374607431768211455)) 

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
		abin = get_bin(a,128)
		bbin = get_bin(b,128)
		i=0
		while (abin[i]=='0'):
			i=i+1

		j=0
		while (bbin[j]=='0'):
			j=j+1
		k=i
		l=j
		sum1=128-k-num
		sum2=128-l-num
		if (sum1<0):
			sum1=0
		if (sum2<0):
			sum2=0
		sum3=(sum1+sum2)*-1
		amul=abin[k:k+num]
		bmul=bbin[l:l+num]
		q=int(amul,2)
		w=int(bmul,2)
		e=q*w
		yapp = get_bin(e,256)
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
	

mean_error_distance = mean_error_distance/100000
mean_relative_error_distance = mean_relative_error_distance/100000
err[5] = mean_relative_error_distance 
normalized_error_distance = mean_error_distance/max1
normailzed_relative_error_distance = mean_relative_error_distance/max2
acceptance_prob = prob/100000
acceptance_prob = 1-acceptance_prob
err1[5] = acceptance_prob
print ("*******************************")
print ("MEAN ERROR DISTANCE : ", mean_error_distance)
print ("mean_relative_error_distance : ", mean_relative_error_distance)
print ("normalized_error_distance : ", normalized_error_distance)
print ("normailzed_relative_error_distance : ", normailzed_relative_error_distance)
print ("acceptance_probability at 1% : ", acceptance_prob)






##### 64 ###########


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
		mean_error_distance = (y-w) + mean_error_distance
		mean_relative_error_distance = mean_relative_error_distance + ans
		max1 = max(yans1)
		max2 = max(yans)
		if (ans>1):
			prob = prob + 1
	

mean_error_distance = mean_error_distance/100000
mean_relative_error_distance = mean_relative_error_distance/100000
err[4] = mean_relative_error_distance 
normalized_error_distance = mean_error_distance/max1
normailzed_relative_error_distance = mean_relative_error_distance/max2
acceptance_prob = prob/100000
acceptance_prob = 1-acceptance_prob
err1[4] = acceptance_prob
print ("*******************************")
print ("MEAN ERROR DISTANCE : ", mean_error_distance)
print ("mean_relative_error_distance : ", mean_relative_error_distance)
print ("normalized_error_distance : ", normalized_error_distance)
print ("normailzed_relative_error_distance : ", normailzed_relative_error_distance)
print ("acceptance_probability at 1% : ", acceptance_prob)






##### 32 ###########


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
	res.append(random.randint(1, 4294967295)) 

for d in range(100000): 
	res1.append(random.randint(1, 4294967295)) 

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
		abin = get_bin(a,32)
		bbin = get_bin(b,32)
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
	

mean_error_distance = mean_error_distance/100000
mean_relative_error_distance = mean_relative_error_distance/100000
err[3] = mean_relative_error_distance 
normalized_error_distance = mean_error_distance/max1
normailzed_relative_error_distance = mean_relative_error_distance/max2
acceptance_prob = prob/100000
acceptance_prob = 1-acceptance_prob
err1[3] = acceptance_prob
print ("*******************************")
print ("MEAN ERROR DISTANCE : ", mean_error_distance)
print ("mean_relative_error_distance : ", mean_relative_error_distance)
print ("normalized_error_distance : ", normalized_error_distance)
print ("normailzed_relative_error_distance : ", normailzed_relative_error_distance)
print ("acceptance_probability at 1% : ", acceptance_prob)





#########   16 bit ######

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
	
mean_error_distance = mean_error_distance/100000
mean_relative_error_distance = mean_relative_error_distance/100000
err[2] = mean_relative_error_distance 
normalized_error_distance = mean_error_distance/max1
normailzed_relative_error_distance = mean_relative_error_distance/max2
acceptance_prob = prob/100000
acceptance_prob = 1-acceptance_prob
err1[2] = acceptance_prob
print ("*******************************")
print ("MEAN ERROR DISTANCE : ", mean_error_distance)
print ("mean_relative_error_distance : ", mean_relative_error_distance)
print ("normalized_error_distance : ", normalized_error_distance)
print ("normailzed_relative_error_distance : ", normailzed_relative_error_distance)
print ("acceptance_probability at 1% : ", acceptance_prob)





#########   8 bit ######

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
	res.append(random.randint(1, 255)) 

for d in range(100000): 
	res1.append(random.randint(1, 255)) 

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
		abin = get_bin(a,8)
		bbin = get_bin(b,8)
		i=0
		while (abin[i]=='0'):
			i=i+1

		j=0
		while (bbin[j]=='0'):
			j=j+1
		k=i
		l=j
		sum1=8-k-num
		sum2=8-l-num
		if (sum1<0):
			sum1=0
		if (sum2<0):
			sum2=0
		sum3=(sum1+sum2)*-1
		amul=abin[k:k+num]
		bmul=bbin[l:l+num]
		q=int(amul,2)
		w=int(bmul,2)
		e=q*w
		yapp = get_bin(e,16)
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
	

mean_error_distance = mean_error_distance/100000
mean_relative_error_distance = mean_relative_error_distance/100000
err[1] = mean_relative_error_distance 
#normalized_error_distance = mean_error_distance/max1
#normailzed_relative_error_distance = mean_relative_error_distance/max2
acceptance_prob = prob/100000
acceptance_prob = 1-acceptance_prob
err1[1] = acceptance_prob
print ("*******************************")
print ("MEAN ERROR DISTANCE : ", mean_error_distance)
print ("mean_relative_error_distance : ", mean_relative_error_distance)
print ("normalized_error_distance : ", normalized_error_distance)
print ("normailzed_relative_error_distance : ", normailzed_relative_error_distance)
print ("acceptance_probability at 1% : ", acceptance_prob)






#########   4 bit ######

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
	res.append(random.randint(1, 15)) 

for d in range(100000): 
	res1.append(random.randint(1, 15)) 

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
		abin = get_bin(a,4)
		bbin = get_bin(b,4)
		i=0
		while (abin[i]=='0'):
			i=i+1

		j=0
		while (bbin[j]=='0'):
			j=j+1
		k=i
		l=j
		sum1=4-k-num
		sum2=4-l-num
		if (sum1<0):
			sum1=0
		if (sum2<0):
			sum2=0
		sum3=(sum1+sum2)*-1
		amul=abin[k:k+num]
		bmul=bbin[l:l+num]
		q=int(amul,2)
		w=int(bmul,2)
		e=q*w
		yapp = get_bin(e,8)
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
	

mean_error_distance = mean_error_distance/100000
mean_relative_error_distance = mean_relative_error_distance/100000
err[0] = mean_relative_error_distance 
#normalized_error_distance = mean_error_distance/max1
#normailzed_relative_error_distance = mean_relative_error_distance/max2
acceptance_prob = prob/100000
acceptance_prob = 1-acceptance_prob
err1[0] = acceptance_prob
print ("*******************************")
print ("MEAN ERROR DISTANCE : ", mean_error_distance)
print ("mean_relative_error_distance : ", mean_relative_error_distance)
print ("normalized_error_distance : ", normalized_error_distance)
print ("normailzed_relative_error_distance : ", normailzed_relative_error_distance)
print ("acceptance_probability at 1% : ", acceptance_prob)




p = (0,1,2,3,4,5,6)
l = (4,8,16,32,64,128)
plt.plot (x1,err)
plt.title ('RELATIVE ERROR VS. LENGTH OF MULTIPLIER')
plt.xticks(p,l)
plt.ylabel('Relative Error')
plt.xlabel('Length Of Multiplier (Latency Parameter = 8)')
plt.show()


plt.plot (x1,err1)
plt.title ('ACCEPTANCE PROBABILITY VS. LENGTH OF MULTIPLIER')
plt.xticks(p,l)
plt.ylabel('Acceptance Probability (1% Relative Error)')
plt.xlabel('Length Of Multiplier (Latency Parameter = 8)')
plt.show()

