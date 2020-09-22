def matriz(a,b):
	m=[]
	for i in range(a+1):
		linha=[]
		for j in range(b+1):
			c=0
			linha.append (c)
		m.append(linha)
	return m

def melhor(principe,princesa):
	m, n = len(principe), len(princesa)
	c = matriz(m,n)
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if principe[i - 1] == princesa[j - 1]:
				c[i][j] = c[i - 1][j - 1] + 1
			else:
				c[i][j] = max(c[i][j - 1], c[i - 1][j])
	return c[m][n]

casos= int(input()) + 1
dic={}
for i in range(1, casos):
	input()  
	principe = input().split()
	princesa = input().split()
	resultado=melhor(principe,princesa)
	dic[i]= resultado
for case, resultado in dic.items():
     print(f"Case {case}: {resultado}")
