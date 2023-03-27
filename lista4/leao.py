salarioSport = input().split()
salarioNovo = input().split()

def mergeSort(data):
  tam_data = len(data)

  if tam_data < 2:
    return
  
  meio = tam_data // 2 

  left_data = data[:meio]
  right_data = data[meio:]

  mergeSort(left_data)
  mergeSort(right_data)

  left_index = 0
  right_index = 0
  data_index = 0

  while left_index < len(left_data) and right_index < len(right_data):

    if int(left_data[left_index]) < int(right_data[right_index]):
      data[data_index] = int(left_data[left_index])
      left_index += 1

    else:
      data[data_index] = int(right_data[right_index])
      right_index += 1
    data_index += 1

  while left_index < len(left_data):
    data[data_index] = int(left_data[left_index])
    left_index += 1
    data_index += 1

  while right_index < len(right_data):
    data[data_index] = int(right_data[right_index])
    right_index += 1
    data_index += 1

def getMediana(data):

    if(len(data) % 2 == 0):
      par = len(data) // 2
      mediana = ((data[par-1] )+ data[par])/2
      return mediana
    
    else:
      index = (len(data) / 2) + 0.5
      mediana = data[int(index)]
      return mediana

arraySalarios = salarioNovo + salarioSport

mergeSort(arraySalarios)
mediana = getMediana(arraySalarios)

print(f'O salário sugerido por Juba na primeira negociação será de {mediana:.2f} mil reais.')