#Напишите функцию суммирования двух целых чисел без использования «+» и других арифметических операторов.
a=bin(int(input('Введите число а: ')))
b=bin(int(input('Введите число b: ')))
a=a[2:]
b=b[2:]
buf=0
rez=''
i=-len(a)
if len(a)>len(b):
	max=a
	min=b
else:
	max=b
	min=b
	
for j in max:
	if buf=='1':
		if max[i]==min[i]=='1':
			buf='1'
			rez.append('1')
		elif max[i]==min[i]=='0':
			buf='0'
			rez.append('1')
		else:
			buf='1'
			rez.append('0')
	else:
		if max[i]==min[i]=='1':
			buf='1'
			rez.append('0')
		elif max[i]==min[i]=='0':
			buf='0'
			rez.append('0')
		else:
			buf='0'
			rez.append('1')
			
if buf=='1':
	rez.append('1')
	
#rez='2b'+rez.reverse()
rez.reverse()
print(rez)
#print (int(join(rez)))