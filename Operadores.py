# TRABALHANDO COM OPERADORES

# A = 5
# B = 15
# C = 20

# print("A == B AND B > C : ", A == B and B > C)
# print("A < B OR B > C : ", A < B or B > C)
# print("not A == B : ", not A == B)

idade = int(input("Digite a idade da pessoa: "))

if idade >= 18:
    print("Maior de idade")
elif idade >= 16:
    print("Infanto Juvenil")
else:
    print("Menor de idade")