import math
from math import sqrt
from math import ceil

a = list(input('Please enter a list of numbers'))

def sortalist(list):
	sorta = a.sort()
	new_list = a
	return new_list
sorted = sortalist(a)
	
def sumoflist(a):
	suma = sum(a)
	return suma
	
sumofdalist = sumoflist(a)
	
def list_squared(a):
	list_squared = [x**2 for x in a]
	return list_squared
	
def sum_list_square(a):
	sumah = sum(list_squared(a))
	return sumah

def mean(a):
 	meana = float(sum(a))/float(len(a))
 	return meana

def position_for_median(a):
## the goal of the median is to first sort the list
	posn= (float(len(a)+1))/(float(2))
	return posn

posna = int(position_for_median(a))
p_ = int(posna-0.5)
pplus = int(posna+0.5)
posna_1 = posna-1

pp = p_
ppp = pplus

def median_even(sorted):
  sumah =sorted[pp] +sorted[ppp]
  avge = float(sumah)/float(2)
  return avge
  
def median_odds(sorted):
	med_odd= sorted[posna_1]
	return med_odd
	
def median(sorted):
	if len(sorted)%2==0:
		return median_even(sorted)
	else:
		 return median_odds(sorted)
	  
def sdev_squared(a):
	sumoflist= sum(list_squared(a))
	listsquared = float(sumofdalist**2)/float(len(a))
	leba = len(a)-1
	ha=float(sumoflist)-float(listsquared)/float(leba)
	return ha
	
s_squared = sqrt(sdev_squared(a))
  
def sdev(a):
	res = round(s_squared,2)
	return res
	
def ranger(a):
	res = max(a)-min(a)
	return res
	
def midrange(a):
	midrange = float(min(a)+max(a))/float(2)
	return midrange

	


print'The sorted list is:{0}\n The sum of the list is:  {1}\n The list sqaured is {2}\n The mean of the list of numbers is: {3}\n The median of the list is :{4}\n The Standard deviation of the list is :{5}.\n The standard deviation sqaured of the list is: {6}\n The range is :{7}\n The midrange is:{8}.\n the sum of the list squared is : {9}'.format(sortalist(a),sumoflist(a),list_squared(a),mean(a),median(a),sdev(a),sdev_squared(a),ranger(a),midrange(a),sum_list_square(a))


inputa= input('Hey, input percentile')
	
def quartile_gen(sorted):
	quart = float(len(a)*inputa)/float(100)
	return quart	
	
result = quartile_gen(sorted)
 
def quartile_posn(a):
	if result != int(result):
		res = ceil(result)
	else:
		res = result+0.5
	return res
		
quart_pos = int(quartile_posn(sorted))
quart_pos_ = int(quart_pos-1.5)
quart_posn = int(quart_pos-0.5)

def quartile(sorted):
	if quart_pos == int(quart_pos):
		res = sorted[quart_pos]
	else:
		res = float(sorted[quart_pos_]+sorted[quart_posn])/float(2)
	return res	
	
print 'the first step is :{0}\n the quartile position is :{1} \n The number in the {2}th percentile is : {3}'.format(result,quart_pos,inputa,quartile(sorted))

z = input('hey, input x here for the z-score')

the_mean = mean(a)
def z_score(z):
	res = float(z-mean(a))/float(sdev(a))
	return res


		
##code in construction
