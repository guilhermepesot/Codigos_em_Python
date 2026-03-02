Nome_func = input("Escreva o nome do funcionário: ")
salario_base = int(input("Escreva o salário base: "))
bonus = int(input("Escreva a porcentagem do bônus: "))
acrecimo = (salario_base * bonus)/100
salario_final = salario_base + acrecimo
if(salario_base < 0 or bonus < 0 ):
    print("Invalido")
else:
    print("O salário final de {}, é de R${:.2f}".format(Nome_func,salario_final))
 
