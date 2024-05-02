n=int(input("Поиск простых чисел до "))
a=[2]
for i in range(3, n+1, 2):
	k=0
	q=int(n**0.5)
	for j in a:
		if j>q:
			break
		if i%j==0:
			k=1
			break
	if k==0:
		a.append(i)
print("ОБЩИЕ КОЛИЧЕСТВО ЧИСЕЛ: "+ str(len(a)))
print(a)