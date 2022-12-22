import math

n_instrucoes = int(input())
comp_A = input() 
comp_B = input()
new_info_A = comp_A.split(' - ')
new_info_B = comp_B.split(' - ')
nomeA = new_info_A[0]
nomeB = new_info_B[0]

def conta(n_instrucoes, info):
  info_int = int(info[1])
  computador = info[0]
  complexidade = info[3]
  
  if(complexidade == '2n^2'):
    return "%.2f"%((2*(n_instrucoes**2))/info_int)
  elif(complexidade == 'n.logn'):
    return "%.2f"%((n_instrucoes*math.log(n_instrucoes, 10))/info_int)
  elif(complexidade == '2^n'):
    return "%.2f"%((2**n_instrucoes)/info_int)
  elif(complexidade == 'n'):
    return "%.2f"%((n_instrucoes)/info_int)

velocidadeA = conta(n_instrucoes, new_info_A)
velocidadeB = conta(n_instrucoes, new_info_B)

print(f'Velocidade do {nomeA}: {velocidadeA} segundos')
print(f'Velocidade do {nomeB}: {velocidadeB} segundos')

if(float(velocidadeA) > float(velocidadeB)):
  print(f'O {new_info_B[0]} foi mais rápido!')
else:
  print(f'O {new_info_A[0]} foi mais rápido!')
