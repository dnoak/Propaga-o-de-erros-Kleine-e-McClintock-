# Código em Python do método de propagação de erros
# de Kleine e McClintock
# Autor: Daniel Carvalho

import re
import sympy
import os
import platform

os.system('clear') if platform.system().lower()=='linux'else os.system('cls')

for i in range(0, 5):
    ex = i+1
    print('Exercício:', ex,'\n')

    exercicios = {
        1: {'variaveis': 'r1 = 20 +- 0.4; r2 = 300 +- 6',
            'equacoes': 'req = r1 + r2 ;req = 1/(1/r1 + 1/r2)'},
        2: {'variaveis': 'l = 1000 +- 2; a = 20+- 1; b=200 -+2; f=1000 +- 20; e = 210000 +- 21000',
            'equacoes': 'ep = f*l**3/(3*e*(b*a**3/12)); i = b*a**3/12'},
        3: {'variaveis': 'u = 220 +- 2.2; r = 50 +- 1; j = 4.4 +- 0.044',
            'equacoes': 'p = u**2/r ; p = u*j'},
        4: {'variaveis': 'd = 6 +- 0.012; h = 9 +- 0.018',
            'equacoes': 'v = 3.141592*d**2/4*h'},
        5: {'variaveis': 'r0 = 8 -+ 0.16; a = 0.0004 +- 0.00002; t0 = 20 +- 2; t = 40 +- 2',
            'equacoes': 'r = r0*(1+a*(t-t0))'}
        }

    variaveis = exercicios[ex]['variaveis'].upper().replace(' ', '').split(';')#input('Variáveis: ').upper()
    variaveis = [re.split(r'=|\+-|-\+', var) for var in variaveis ]

    for sym in variaveis:
        sym[0] = sympy.symbols(sym[0])

    equacoes = exercicios[ex]['equacoes'].upper().replace(' ', '').split(';') 
    equacoes = [eq.split('=') for eq in equacoes]

    for eq in equacoes:
        erro = 0
        for var in variaveis:
            diff = sympy.diff(eq[1], var[0])
            resdiff = diff.subs([(v[0], v[1]) for v in variaveis])
            print(f'd{eq[0]}/d{var[0]} ( {eq[1]} ) = {diff} = {resdiff}')
            erro += (resdiff.evalf() * float(var[2]))**2
        resultado = sympy.sympify(eq[1]).subs([(v[0], v[1]) for v in variaveis])
        print(f'{eq[0]} = {resultado.evalf():.4f} ± {erro**(1/2):.4f} ({100*erro**(1/2)/resultado.evalf():.4f}%)\n')
    print('-'*70, '\n')