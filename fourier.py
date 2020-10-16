#!/usr/bin/python
#-*- coding: <encoding utf-8> -*-

# funcoes
def cria_malha(mtr, tam):
	for linhas in range(tam):
		mtr.append([])
		for colunas in range(tam):
			mtr[linhas] = mtr[linhas] + [0]
		mtr[linhas] = mtr[linhas] + ["GGG"]

def transcreve_malha(mlh1, mlh2, tam): #Trancreve mlh2 para mlh1
	for m in range(tam):
		for n in range(tam):
			mlh1[m][n] = mlh2[m][n]

# main

interv_temp = [0.01, 0.001, 0.0001]

for a in range(3):
	print(interv_temp[a])

ind = 1 # indice de interv_temp

alpha = 0.318 # propriedade do material

#montando uma matriz com o tamanho requerido

lado_fora = 3000
lado_dentro = 1000
interv_esp = 100
t_nos = lado_fora/interv_esp

matriz = []

cria_malha(matriz, t_nos)

print(matriz)
raw_input("Aperte uma tecla")

#condicoes iniciais 

no1 = (lado_fora - lado_dentro)/(2*interv_esp)
no2 = no1 + lado_dentro/interv_esp
for m in range(t_nos):
	for n in range(t_nos):
		if(n == t_nos - 1):
			matriz[m][n] = 300
		elif(n == 0 or m ==0 or m == t_nos-1):
			matriz[m][n] = 100
		elif((m>=no1-1 and m<=no2-1) and (n>=no1-1 and n<=no2-1)):
			if(m==no1-1):
				matriz[m][n] = 20
			elif(m==no2-1):
				matriz[m][n] = 15
			elif(n==no1-1):
				matriz[m][n] = 10
			elif(n==no2-1):
				matriz[m][n] = 30
			else:
				matriz[m][n] = ' '

print(matriz)

# Progresso temporal da matriz

matriz_futura = []

cria_malha(matriz_futura, t_nos)

transcreve_malha(matriz_futura, matriz, t_nos)

m, n = 0 ,0

deltaxy = interv_esp/1000.000

saida_laco = 1

tempo = 0

print(deltaxy*deltaxy)

raw_input("Pause!")
resol = 0.0001
while(saida_laco):
	for m in range(t_nos):
		for n in range(t_nos):
			if (m != 0 and n != 0 and m != t_nos-1 and n != t_nos-1 and ((m<no1-1 or m>no2-1) or (n<no1-1 or n>no2-1))): 
				temperatura_mn = (((matriz[m][n-1] + matriz[m][n+1] + matriz[m-1][n] + matriz[m+1][n] - (4*matriz[m][n]))/(deltaxy*deltaxy))*alpha*interv_temp[ind]) + matriz[m][n]
				matriz_futura[m][n] = temperatura_mn
	tempo = tempo + 1
	if(matriz_futura[1][1]-matriz[1][1]<resol):
		saida_laco = 0
	transcreve_malha(matriz, matriz_futura, t_nos)


print(matriz_futura)
print(tempo)

