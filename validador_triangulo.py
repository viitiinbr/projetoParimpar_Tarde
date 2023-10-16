# Validador de Triângulo
# Validador de Triângulo
n1 = float(input('digite um comprimento\n'))
n2 = float(input('digite um outro comprimento\n'))
n3 = float(input('digite um outro comprimento\n'))

if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print(f'{n1},{n2} e {n3} formam um triangulo')
else:
    print(f'{n1},{n2} e {n3} não formam um triangulo')