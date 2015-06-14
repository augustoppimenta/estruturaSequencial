#! usr/bin/env python
# -*- coding: utf-8 -*-

peso_de_peixes = input("Informe o peso de peixes pescados hoje: ")

multa = 4
peso_de_peixes_maximo = 50
valor_ultrapassado = 0
valor_multa = 0

if peso_de_peixes > peso_de_peixes_maximo:
    valor_ultrapassado = peso_de_peixes - peso_de_peixes_maximo
    valor_multa = valor_ultrapassado * multa
    print "Você ultrapassou", valor_ultrapassado, "kg. Sua multa será de R$ ", valor_multa
else:
    print "Você ultrapassou", valor_ultrapassado, "kg do seu limite diário, logo sua multa é de R$", \
    valor_multa
