# Разработайте алгоритм, обнаруживающий в массиве все пары целых чисел,
# сумма которых равна заданному значению.
#lst = [8,6,4,1,6,9,6,4,1,6,3,9,5,4,1,6,7]
lst=[1,2,3,4,5,6]
n = int(input('ВВедите число: '))

j = 1
for elem in lst:
	for elem2 in lst[j:]:
		if (elem+elem2)==n:
			print (elem, elem2)
	j+=1
			
	
