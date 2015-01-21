#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Dongutsi'
import csv

#tenta criar o arquivo CSV
try:
    saida = csv.writer(file('teste.csv', 'w'))
except:
    #se não for possível a criação do aquivo, mostra  a msg e sai do programa
    print 'Nao foi possivel criar o arquivo...'
    exit()

#dados que serão gravados, a ordem tem que estar de acordo com o banco ou planilha
#cada par de (), representa um registro, no caso serão gravados dois registros
seraGravado = (
    ('Carlos','Gomes da Silva', 30, '10/05/1984'),
    ('Fabio','Viudes', 20, '02/04/1994')
    )

#tenta salvar o arquivo
try:
    saida.writerows(seraGravado)
    print 'Dados gravados com sucesso!'
except:
    print 'Erro ao gerar o arquivo\nVerifique suas permissoes...'