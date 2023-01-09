import math
import os
os.system('cls')

confirm = ''

while confirm != 'Sim':
    area = input('Você deseja calcular a área de qual figura?')
    if area == 'Triângulo':
        b = int(input('Forneça o valor da base: '))
        h = int(input('Forneça o valor da altura: '))
        res = (b*h)/2
        print('O resultado da área do triângulo é: '+ str(res))
    elif area == 'Quadrado':
        l = int(input('Forneça o lado do quadrado: '))
        res = l*l
        print('O resultado da área do quadrado é: '+ str(res))
    elif area == 'Círculo':
        quest = input('Você deseja fornecer o raio ou o diâmetro?')
        if quest == 'Raio':
            r = int(input('Forneça o valor do raio: '))
            res = r*r*math.pi
            print('O resultado da área do círculo é: '+ str(res))
        elif quest == 'Diâmetro':
            d = int(input('Forneça o valor do diâmetro: '))
            r = d/2
            res = r*r*math.pi
            print('O resultado da área do círculo é: '+ str(res))
    confirm = input('Você deseja sair do programa? ')
    os.system('cls')