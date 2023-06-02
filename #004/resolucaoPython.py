array = []
inserirValor = True
print("Crie o array")
while(inserirValor):
    array.append(int(input("")))
    inserirValor = 'S' == (input("Continuar a inserir valores: (S)"))
def inteiroFaltante(array):
 menor = array[0];
 for i in array:
    if(i < menor and i > 0):
        menor = i+1
 if(menor < 0):
    menor = 0
 return menor

print(inteiroFaltante(array))

