a=int(input('Введите число а: '))
b=int(input('Введите число b: '))

def sloz (a,b):
	if b == 0: return a
	sum = a ^ b
	carry = (a & b) << 1
	return sloz(sum,carry)
	
print (sloz(a,b))