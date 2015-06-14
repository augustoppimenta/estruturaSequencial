#! usr/bin/env python
# -*- coding: utf-8 -*-

area_a_ser_pintada = input("Quantos metros quadrados serão pintados: ")

litros_necessarios = area_a_ser_pintada / 3.0
print "Litros Necessários", litros_necessarios
numero_de_latas = litros_necessarios/18.0
print "Número de latas", numero_de_latas

resto = numero_de_latas % 1
print "Resto", resto


if resto != 0:
    numero = int(numero_de_latas)
    numero = numero + 1
    print "Para pintar a área de", area_a_ser_pintada, "m², você precisará adiquirir", numero, "lata(s)"
    valor = 80 * numero
    print "O valor total é R$", valor


else:
    print "PARA pintar a área de", area_a_ser_pintada, "m², você precisará adiquirir", int(numero_de_latas), "lata(s)"
    valor = 80 * numero_de_latas
    print "O valor total é R$", valor
