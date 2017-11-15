#Напишите функцию суммирования двух целых чисел без использования «+» и других арифметических операторов.
a=bin(int(input('Введите число а: ')))
b=bin(int(input('Введите число b: ')))
a=a[2:]
b=b[2:]
buf='0'
rez=''

if len(a)>len(b):
	max=a
	min=b

else:
	max=b
	min=a
min="0"*(len(max)-len(min))+min
i=-1
j=-len(max)
#print ('max =',max, 'min = ',min)
for sym in max:
	#print ('i=',i,'max=',max[i],'min=',min[i],'buf=',buf,'rez=',rez)
	if buf=='1':
		if max[i]==min[i]=='1':
			buf='1'
			rez='1'+rez
		elif max[i]==min[i]=='0':
			buf='0'
			rez='1'+rez
		else:
			buf='1'
			rez='0'+rez
	else:
		if max[i]==min[i]=='1':
			buf='1'
			rez='0'+rez
		elif max[i]==min[i]=='0':
			buf='0'
			rez='0'+rez
		else:
			buf='0'
			rez='1'+rez
	i-=1
			
if buf=='1':
	rez='1'+rez

	
#rez='2b'+rez.reverse()

print(rez, int(rez,2))
#print (int(join(rez)))