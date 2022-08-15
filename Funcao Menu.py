

def menu():

    texto = f'''
        ------------BANCO DO CELSO-------
    
        [1] SALDO
        [2] DEPOSITO
        [3] SAQUE
        [4] EMPRESTIMO
        [5] SAIR
    
        '''
    print(texto)

from datetime import datetime
from tkinter import *

import grid as grid
import texto as texto




janela = Tk()
janela.title(' MENU BANCO DO CELSO ')
janela.geometry('500x300')

janela2 = Tk()
janela2.title(' MENU BANCO DO CELSO ')
janela2.geometry('500x300')


menu_orientacao = Label(janela, text='Escolha do Menu:')
menu_orientacao.grid(column=10, row=0)
menu_orientacao.grid(padx= 10,pady=10)


opcao_orientacao = Label(janela, text= 'ESCOLHA AS OPCAOES A BAIXO')
opcao_orientacao.grid(column=10, row=3)
opcao_orientacao.grid(padx= 10,pady=3)


botao = Button(janela, text= 'SALDO',command='text')
botao.grid(column= 1, row=5)

botao_saldo = Label(janela2, text= 'MENU SALDO' )
botao_saldo.grid(column=10, row=0)
botao_saldo.grid(padx= 10,pady=10)
botao_saldo= Button(janela, text= 'SALDO,', command= datetime)

botao_a =Button(janela, text= 'Extrato',command='text')
botao_a.grid(column= 1, row=10)

botao_b =Button(janela, text= 'Emprestimo',command='text')
botao_b.grid(column= 1, row=15)

botao_c =Button(janela, text= 'SAQUE',command='text')
botao_c.grid(column= 1, row=20)

botao_d =Button(janela, text= 'SAIR',command='text')
botao_d.grid(column= 1, row=25)

texto_menu = Label(janela, text= ' ')
texto_menu.grid(column=10, row=70)
texto_menu.grid(padx= 10,pady=30)

janela = mainloop()
