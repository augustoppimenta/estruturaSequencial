# -*- coding:UTF-8 -*-


altura = input("Digite sua altura: ")
sexo = raw_input("Digite seu sexo use M - Masculino ou F - Feminino: ")
str(sexo)

if sexo == "F" or sexo == "Feminino":
    peso_ideal = (62.1 * altura) - 44.7
    print "O seu peso ideal é de:", peso_ideal, "kg"
elif sexo == "M" or sexo == "Masculino":
    peso_ideal = (72.7 * altura) - 58
    print "O seu peso ideal é de:", peso_ideal, "kg"
else:
    print "Ops! Esse sexo não existe"
