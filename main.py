import os
# Tabuada
def start():
    while True:
        try:
            cont = 0
            numero = int(input(f"{os.linesep}Digite um Numero para saber sua tabuada:{os.linesep} "))
            print(f'Excelente,aqui esta a tabuada do numero {numero} !{os.linesep} ')
            print(f'Qualquer numero dividido por 0 o resultado é zero{os.linesep} ')
            tab = (numero * 10) + 1
            for tabuada in range(numero, tab, numero):
                cont += 1
                print(numero, ' x ', cont, ' = ', tabuada)
        except:
            print(f'Utilize apenas numeros inteiros!{os.linesep} ')
if __name__ == '__main__':
         start()