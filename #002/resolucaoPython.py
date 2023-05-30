array = []
arrayr = []
inserirValor = True
print("Crie o array")
while(inserirValor):
    array.append(int(input("")))
    inserirValor = 'S' == (input("Continuar a inserir valores: (S)"))

for i in range(len(array)):
    arrayr.append(1)
    for j in range(len(array)):
     if(i!= j):
      arrayr[i]*=array[j]
    print
arrayrstr = ','.join(map(str,arrayr))
print("[",arrayrstr,"]")
    