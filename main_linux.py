import random
import os

def cargar():
    with open('./data/palabras.txt', 'r', encoding='utf-8') as f:
        palabras = [line.strip('\n') for line in f.readlines()]

        palabra = random.choice(palabras)

        new_sentence = palabra.maketrans('áéíóú', 'aeiou') # Quitar las tildes
        escogida = palabra.translate(new_sentence)
        escogida = list(escogida)
        print(escogida)

        #letras = {i:(1 if i not in escogida else letras[i] + 1) for i in escogida} # intento de dictionary comprenhension
        letras = {}
        for i in escogida:
            if i in letras:
                letras[i] += 1
            else:
                letras[i] = 1
        print(letras) 
        tamanio = len(letras)
        vacio = ['_']*len(escogida)
        contador = 0
        victoria = tamanio
        if tamanio < 5:
            tamanio = 5
        repetidas = []
        repetida = False

        while True:
            os.system('clear')
            if repetida:
                print('Esa ya la escribiste 7-7')
                repetida = False
            print('Adivina adivinador, Cuál es la palabra?')
            print(vacio)
            intentos = tamanio - contador
            if intentos > 1:
                print(f'Tienes {intentos} intentos =D')
            elif intentos == 1:
                print(f'Tienes {intentos} intento O.o')
            else:
                print('Ya no te quedan intentos T-T')
                print(f'La palabra era {palabra}')
                break
            letter = input('Inserta una letra: ')
            if letter in repetidas:
                repetida = True
            else:
                repetidas.append(letter)
                assert letter.isalpha(), 'Solo puedes ingresar letras del alfabeto español'
                
                if letter in escogida:
                    for i in range(len(escogida)):
                        if escogida[i] == letter:
                            vacio[i] = letter
                    victoria -= 1
                else:
                    print('Intenta con otra.')
                    contador += 1 
                if victoria == 0:
                    print('Ganaste =3')
                    print(f'La palabra es {palabra}')
                    break

def run():
    cargar()

if __name__ == '__main__':
    run()