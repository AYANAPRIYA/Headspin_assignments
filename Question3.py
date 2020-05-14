n= int(input())                     #takes the input, the length of series
def SumOfSeries(number):
	odd_number = []
	for i in range(n):
		if i % 2 ==1:
			odd_number.append(i)            #create the list of oddnumbers till n
	if n < 3:
		result = 1                                      #return 1 if n is less than 3               
	else:
		for i in range(1, (len(odd_number))):
			result = 1
			result = result + (odd_number[i]**2)/(odd_number[i]**3)         #returns the sum of series
	return(print(result))
SumOfSeries(n)
