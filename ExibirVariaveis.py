# DECLARANDO VARIÁVEIS

codigo = int(input("Digite o código do funcionário: "))
salario = float(input("Informe o salário: "))
nome = input("Digite o nome do funcionário: ")
situacao = True

# tipo = type (salario)
# print(salario)
# print(tipo)

# print("Código: " + str(codigo) + " Nome: " + nome + " Salário: " + str(salario))

print("Código: %d "% codigo)
print("Nome: %s "% nome)
print("Salário: %.2f"% salario)
print("Ativo: %r "% situacao)