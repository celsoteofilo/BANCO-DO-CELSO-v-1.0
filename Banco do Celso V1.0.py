from tkinter import *

import grid as grid
import texto as texto

saldo = 0
escolha = 0


janela = Tk()
janela.title(' MENU BANCO DO CELSO ')
janela.geometry('300x300')


menu_orientacao = Label(janela, text='Escolha do Menu:')
menu_orientacao.grid(column=10, row=0)
menu_orientacao.grid(padx= 10,pady=10)


opcao_orientacao = Label(janela, text= 'ESCOLHA AS OPCAOES A BAIXO')
opcao_orientacao.grid(column=10, row=3)
opcao_orientacao.grid(padx= 10,pady=3)

botao = Button(janela, text= 'SALDO',command='text')
botao.grid(column= 10, row=40)



texto_menu = Label(janela, text= ' ')
texto_menu.grid(column=10, row=70)
texto_menu.grid(padx= 10,pady=30)



print('\033[32m ---------BEM VINDOS AO BANCO DO CELSO ----------\033[m')

while escolha == 1 or 2 or 3 or 4 or 5:



    texto = f'''
    ------------BANCO DO CELSO-------

    [1] SALDO
    [2] DEPOSITO
    [3] SAQUE
    [4] EMPRESTIMO
    [5] SAIR

    '''
    print(texto)
    texto_menu['text'] = texto

    janela = mainloop()
    escolha = int(input(' ESCOLHA A OPCAO A  CIMA DE [1 A 4 E PRESS ENTER ] : '))



    # -------------------------------------------------------------------------------------------
    if escolha == 1:
        print(f' Voce esta no menu SALDO  : \n SEU SALDO E DE R$: \033[33m{saldo:.2f}\033[m')


    # -------------------------------------------------------------------------------------------
    if escolha == 2:

        print('\033[33mVOCE ESTA NO MENU DE DEPOSITO\033[m')
        deposito = float(input('QUAL VALOR GOSTARIA DE DEPOSITAR HOJE R$: '))

        if deposito != 0:
            saldo = deposito + saldo
        print(f'SEU NOVO SALDO : \033[32m{saldo:.2f}\033[m')
    # -------------------------------------------------------------------------------------------
    if escolha == 3:

        print('VOCE ESTA NO MENU DE SAQUE:  ')
        saque = float(input('QUAL VALOR GOSTARIA  DE SACAR HOJE : '))

        if saque != 0:
            saldo = saldo - saque
        print(f'SEU NOVO SALDO : \033[31m{saldo:.2f}\033[m')

        if saldo < 0:
            print('SEU SALDO ESTA NEGATIVO !!!  --TEMOS EMPRESTIMO a 5% de juros  (opcao 5)')
        else:
            print(' ')
    # -------------------------------------------------------------------------------------------
    if escolha == 4:

        print(' ----- \033[32m EMPRESTIMO ------ \033')

        emprestimo = float(input('QUAL E  O VALOR DE EMPRESTIMO: '))
        salarioAtual = float(input('QUAL E O SEU SALARIO ATUAL : '))
        parcelas = int(input('QUAL E O NUMERO DE PARCELAS:  '))

        autorizado = salarioAtual * 10 / 100
        print(f'AUTORIZADO O VALOR DE R$: {autorizado:.2f}')

        autorizarparcela = autorizado / parcelas

        if autorizado > autorizarparcela:
            print(f'Valor das parcelas {parcelas} de R$: {autorizarparcela:.2f}')
            print('EMPRESTIMO APROVADO!!!')
            emprestimo = int(input('QUAL E O VALOR DE EMPRESTIMO: '))


        else:

            print('Seu salario esta Utrapassando o limite !!! ')
    # --------------------------------------------------------------------------------------------
    if escolha == 5:
        break
# -------------------------------------------------------------------------------------------

print('CONTA ENCERRADA !!! Volte sempre !!! ')
